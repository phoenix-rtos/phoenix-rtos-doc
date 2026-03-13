# Partitioning

Partitioning is a mechanism that enables spatial and temporal isolation of groups of processes running on
Phoenix-RTOS. A partition defines a set of resources — memory regions, scheduling windows, and communication
permissions — that are shared by the processes assigned to it. Partitioning enforces boundaries between
independent software components, allowing them to coexist on a single system without interfering with each
other.

## Concepts

### Partition

A partition is a named resource container configured at boot time via the bootloader (`plo`). Each partition
specifies:

- **Allocation maps** — memory maps from which the partition's processes may allocate memory (currently only
  used on NOMMU targets).
- **Access maps** — memory maps that the partition's processes are allowed to access (currently only
  used on NOMMU targets, relevant on MPU-equipped targets).
- **Scheduling windows** — time slots during which the partition's threads are eligible to run.
- **Memory limit** — an upper bound on the total amount of physical memory the partition may consume.
- **Flags** — behavioral modifiers (e.g. global IPC and spawn permissions).

Every program loaded via the `app` bootloader command is associated with exactly one partition. If the
partition is not specified explicitly, a default partition is created automatically for that program.

```{note}
When `app` is used without the optional partition argument, `plo` creates a new partition for that
program. For backward compatibility that partition is assigned to the background scheduling window (ID 0),
has global IPC enabled, and grants spawn-all permission. Its access maps are all imaps and dmaps and its
only allocation map is its first dmap.
```


### Scheduling windows

The Phoenix-RTOS scheduler extends its priority-based round-robin algorithm with a time-partitioned
scheduling layer. Time is divided into a repeating cycle of *scheduling windows*. Each window has a fixed
duration (in microseconds) and is assigned an identifier. The cycle repeats continuously; when the last
window in the cycle completes, the scheduler wraps around and starts from the first window again.

There is always a special **background window** (window 0) that is implicitly present. Threads belonging to
processes without explicit partition assignment, as well as kernel threads, execute in the background window.
The background window is always eligible to run — its threads may be scheduled during any window in the cycle.
Threads from background window are executed according to assigned priorities, but before threads from currently
running window with the same priority. The background window is introduced for event-driven threads. These
threads are typically responsible for handling asynchronous events and system tasks that must remain responsive
regardless of the current partition window. As a result, background threads can preempt partition-specific threads
of the same priority and are always eligible to run, ensuring timely processing of critical events.

This means threads from background window have the ability to run in any window.
Partition-specific threads only run during their assigned windows.

Multiple partitions may share the whole set of scheduling windows. In that case, their threads are placed in the same
ready queues and compete for CPU time using the standard priority-based round-robin policy within that
window. Sharing set of scheduling windows only partially is an invalid configuration.

When a scheduling window expires, the scheduler transitions to the next window. If a partition's thread was
running when its window ended, the thread is preempted and will not run again until its window comes back
around in the next cycle.

### Memory limits

Each partition tracks its physical memory consumption. When a process belonging to a partition attempts to
allocate memory (via `mmap` or internal kernel allocations), the kernel checks whether the allocation would
exceed the partition's configured memory limit. If it would, the allocation fails with an out-of-memory
error.

Memory freed by the partition's processes is credited back to the partition's usage counter.

Memory limits do not include memory for internal kernel objects. Separate kernel-memory limit is planned in the future.

```{note}
On NOMMU targets memory consumption is not yet implemented. If target is MPU-equipped, memory access is constrained
to the specific memory maps listed as the partition's access maps. Regardless of MPU, the allocation is restricted to
partition's allocation maps.
```


### IPC isolation

By default, processes in different partitions are not allowed to exchange messages. If a process attempts to
send a message (`msgSend`) to a port owned by a process in a different partition, the operation fails with
`-EACCES`. The same restriction applies to `msgRecv` on ports owned by processes in other partitions.

This isolation can be relaxed using the **`-m` flag** (global IPC). When a partition is created with the
`-m` flag, its processes are allowed to communicate with processes in any partition. Communication is
permitted if either the sender's or the receiver's partition has the `-m` flag set.

Kernel threads are not subject to IPC restrictions.

### Process spawning restrictions

A process belonging to a partition can only spawn new processes within the same partition by default. An
attempt to spawn a process in a different partition results in an `-EACCES` error.

An exception exists for partitions with the **`-s`** flag: processes in such partitions may
spawn into other partitions. This flag is used by default partitions auto-created by `app` when no explicit
partition is provided (backwards-compatible behavior).


## Configuration

Partitioning is configured entirely through the Phoenix-RTOS loader (`plo`) command-line interface before
the kernel is started. The configuration involves three steps:

1. Define scheduling windows using the `sched` command.
2. Define partitions using the `part` command.
3. Load applications into partitions using the `app` command.

### Step 1: Define scheduling windows

```text
- sched <duration1;duration2;...>
```

The `sched` command defines the scheduling cycle by specifying the duration of each window in microseconds.
Windows are numbered sequentially starting from 1 (window 0 is the implicit background window). The
durations are separated by semicolons.

**Example:**

```text
- sched 10000;20000;10000
```

This creates three scheduling windows:

| Window ID | Duration     |
|-----------|-------------|
| 1         | 10 000 µs   |
| 2         | 20 000 µs   |
| 3         | 10 000 µs   |

The total cycle length is 40 000 µs (40 ms). The cycle repeats: `window 1 -> window 2 -> window 3 -> window 1 -> ...`

### Step 2: Define partitions

```text
- part <name> [-ms] <allocmaps> <accessmaps> <schedwindows> <memlimit>
```

Parameters:

- **`name`** — a unique name for the partition.
- **`-sm`** — *(optional flags)*
- **`allocmaps`** — semicolon-separated list of map names from which this partition may allocate memory.
- **`accessmaps`** — semicolon-separated list of map names that this partition's processes may access
  (enforced by MPU on supported targets).
- **`schedwindows`** — semicolon-separated list of scheduling window IDs (as defined by `sched`) assigned to
  this partition.
- **`memlimit`** — maximum amount of memory that the partition may use. Set to `0` for unlimited.

**Example:**

```text
- part safety -m sram1 sram1;sram2;flash1 1 0x80000
- part mission sram2 sram2;flash2 2;3 0x100000
- part drivers sram1 sram1;dev 0 0
```

This defines two partitions:

- **`safety`**: allocates from `sram1`, can access `sram1`, `sram2`, and `flash1`, runs in scheduling
  window 1, has a memory limit of 512 KB (0x80000), and IPC is restricted to within the partition.
- **`mission`**: allocates from `sram2`, can access `sram2` and `flash2`, runs in scheduling windows 2 and
  3, has a memory limit of 1 MB (0x100000), and IPC is restricted to within the partition.
- **`drivers`**: allocates from `sram1`, can access `sram1` and `dev`, runs in background scheduling window (0),
  has no memory limit, and has global IPC enabled.

```{warning}
Multiple maps and memory limits are used together only for illustration purposes.
Currently multimap management is only supported by NOMMU targets and memory limits only work on targets with MMU.
```

```{note}
If two partitions share at least one scheduling window ID, they must share all of their window IDs (that is,
their `schedwindows` sets must be identical). Partially overlapping window assignments are not allowed and
will result in a configuration error.
```

### Step 3: Load applications into partitions

```text
app <dev> [-x] <name> <imaps> <dmaps> [<partition>]
```

The `app` command has an optional last argument specifying the partition name. If omitted,
a partition is created automatically for the application with settings to behave
just like without partitioning support.

**Example:**

```text
- app flash0 -x dummyfs sram1 sram1 safety
- app flash0 -x executor sram2 sram2 mission
- app flash0 -x sensor_driver sram1 sram1 drivers
```

This loads `dummyfs` into the `safety` partition, `executor` into the `mission` partition, and `sensor_driver` into the `drivers` partition.

## Complete configuration example

Example of `plo` script fragment demonstrates a complete partitioning setup:

```yaml
- sched 10000;20000;10000


- part safety -m sram1 sram1;sram2;flash1 1 0x80000
- part mission sram2 sram2;flash2 2;3 0x100000
- part drivers sram1 sram1;dev 0 0


- app flash0 -x dummyfs sram1 sram1 safety
- app flash0 -x executor sram2 sram2 mission
- app flash0 -x sensor_driver sram1 sram1 drivers

```
