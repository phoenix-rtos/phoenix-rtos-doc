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

- **Access maps** — memory maps that the partition's processes are allowed to access (currently only
  used on NOMMU targets, relevant on MPU-equipped targets).
- **Scheduling window** — time slots during which the partition's threads are eligible to run.
- **Memory limit** — an upper bound on the total amount of physical memory the partition may consume (currently only on MMU targets).

Every program loaded via the `app` bootloader command is associated with exactly one partition. If the
partition is not specified explicitly, it is assigned to special, default partition.

```{note}
When `app` is used without the optional partition argument, `plo` assignes it to a special, default partition. For backward compatibility that partition is assigned to the kernel scheduling window (ID 0). On NOMMU, each app in default partition gets its own, separate access maps via MPU configuration.
```


### Scheduling windows

The Phoenix-RTOS scheduler extends its priority-based round-robin algorithm with a time-partitioned
scheduling layer. Time is divided into a repeating cycle of slots, separate for each CPU. Each slot has a fixed
duration (in microseconds) and is assigned a particular **scheduling window**. The cycle repeats continuously; when the last
window in the cycle completes, the scheduler wraps around and starts from the first window again. Single window can be assigned
to multiple slots.

Each partition is assigned to a single scheduling window, multiple partitions may share the same window.
In that case, their threads are placed in the same ready queues and compete for CPU time using the standard priority-based round-robin policy
within that window.

There is also possibility of configuring a special **background window** for each CPU separately. The background window is always eligible to run — its threads may be scheduled during any slot in the cycle.
Threads from background window are executed according to assigned priorities, but after threads from currently
running window with the same priority. The background window is introduced for event-driven threads. These
threads are typically responsible for handling asynchronous events and system tasks that must remain responsive
regardless of the current scheduler slot. As a result, background threads can preempt partition-specific threads
of lower priority and are always eligible to run, ensuring timely processing of critical events.

This means threads from background window have the ability to run in any slot on given CPU.
Partition-specific threads only run during their assigned windows slots.

There is also a special kernel window (0). It acts as second, implicit background window on each CPU. Kernel threads and threads belonging to processes in default partition execute in the kernel window. Other partitions can also be assigned to this special window.

When a scheduler slot expires, the scheduler transitions to the next slot. If a partition's thread was
running when its window's slot ended, the thread is preempted and will not run again until any of its window's slot is scheduled again.

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

Kernel threads are not subject to IPC restrictions.

In the future, dedicated named ports should be configurable to work between selected partitions.

### Process spawning restrictions

A process belonging to a partition can only spawn new processes within the same partition by default. An
attempt to spawn a process in a different partition results in an `-EACCES` error.


## Configuration

Partitioning is configured entirely through the Phoenix-RTOS loader (`plo`) command-line interface before
the kernel is started. The configuration involves three steps:

```{note}
Cleaner configuration is on the way, with nested yaml objects, which ultimately will be parsed to this PLO-script config.
```

1. Define scheduling windows using the `sched` command.
2. Define partitions using the `part` command.
3. Load applications into partitions using the `app` command.

### Step 1: Define scheduling windows

```text
- sched <windowsCnt> <CPU0 [bgId];id:duration;...> [CPU1 [bgId];id:duration;...] ...
```

The `sched` command defines the scheduling cycle by specifying the microseconds duration and window of each slot.
Windows are numbered sequentially starting from 1 (window 0 is the implicit kernel window). The
slots are separated by semicolons.

**Example:**

```text
- sched 4 1;2:10000;3:20000;4:10000
```

This creates three scheduling windows:

| Window ID | Duration    |
|-----------|-------------|
| 1         | -           |
| 2         | 10 000 µs   |
| 3         | 20 000 µs   |
| 4         | 10 000 µs   |

The total cycle length is 40 000 µs (40 ms). The cycle repeats: `window 2 -> window 3 -> window 4 -> window 2 -> ...`.
Window 1 is a background window.

### Step 2: Define partitions

```text
- part <name> <accessmaps> <schedwindow> <memlimit>
```

Parameters:

- **`name`** — a unique name for the partition.
- **`accessmaps`** — semicolon-separated list of map names that this partition's processes may access
  (enforced by MPU on supported targets).
- **`schedwindow`** — scheduling window ID (as defined by `sched`) assigned to this partition.
- **`memlimit`** — maximum amount of memory that the partition may use. Set to `0` for unlimited.

**Example:**

```text
- part safety -m sram1;sram2;flash1 1 0x80000
- part mission sram2;flash2 2 0x100000
- part drivers sram1;dev 0 0
```

This defines two partitions:

- **`safety`**: can access `sram1`, `sram2`, and `flash1`, runs in scheduling
  window 1, has a memory limit of 512 KB (0x80000).
- **`mission`**: can access `sram2` and `flash2`, runs in scheduling window 2,
  has a memory limit of 1 MB (0x100000).
- **`drivers`**: can access `sram1` and `dev`, runs in background scheduling window (0),
  has no memory limit.

```{warning}
Multiple maps and memory limits are used together only for illustration purposes.
Currently multimap management is only supported by NOMMU targets and memory limits only work on targets with MMU.
```

### Step 3: Load applications into partitions

```text
app <dev> [-x] <name> <imaps> <dmaps> [<partition>]
```

The `app` command has an optional last argument specifying the partition name. If omitted,
a default partition is automatically assigned for the application with settings to behave
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
- sched 4 1;2:10000;3:20000

- part safety -m sram1;sram2;flash1 3 0x80000
- part mission sram2;flash2 2 0x100000
- part drivers sram1;dev 1 0

- app flash0 -x dummyfs sram1 sram1 safety
- app flash0 -x executor sram2 sram2 mission
- app flash0 -x sensor_driver sram1 sram1 drivers

```
