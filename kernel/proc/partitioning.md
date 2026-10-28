# Partitioning

Partitioning is a mechanism that enables spatial and temporal isolation of groups of processes running in the system. A partition defines a set of resources — memory regions, scheduling windows, and communication
permissions — that are shared by the processes assigned to it. Partitioning enforces boundaries between
independent software components, allowing them to coexist on a single system without interfering with each
other.

A partition should not be able to influence execution of another partition, apart from IPC using defined shared ports, shared memory mapped objects from these shared ports, and execution time of syscalls that require global resources.

Currently, there are no limits regarding information disclosure across partitions, meaning all partitions can query data about state of all processes, global maps etc. running in the system (e.g. via the `sysinfo`/`meminfo` interfaces). Active control over foreign processes and threads is however blocked (see
[Process and thread control isolation](#process-and-thread-control-isolation)).

## Concepts

### Partition

A partition is a named resource container configured at boot time via the bootloader (`plo`). Each partition
specifies:

- **Access maps** — memory maps that the partition's processes are allowed to access. On NOMMU targets these
  maps are programmed into the MPU on every context switch. On MMU targets they restrict `MAP_PHYSMEM`
  mappings.
- **Scheduling window** — time slots during which the partition's threads are eligible to run.
- **Memory limit** — an upper bound on the total amount of physical memory the partition may consume.
- **Minimum priority** — the highest-criticality (numerically lowest) scheduler priority the partition's threads
  may use.
- **Flags** — controls access to certain system functionality, including interrupt handlers, PlatformCtl calls, global UTC time changes and Perf subsystem syscalls.

```{note}
Currently, the number of partitions is limited to 32 (including the default partition). A single partition may
declare at most 16 access maps.
```

Every program loaded via the `app` bootloader command is associated with exactly one partition. If the
partition is not specified explicitly, it is assigned to special, default partition.

```{note}
When `app` is used without the optional partition argument, `plo` assigns it to a special, default partition.
For backward compatibility that partition is assigned to the kernel scheduling window (ID 0), has no memory limit,
no priority limit and all access flags set. On NOMMU, each app in default partition gets its own, separate access
maps via MPU configuration, derived from its own `imaps`/`dmaps`. On MMU default partition apps have access to all
physical maps. In both cases default partition apps allocate memory only from the first map listed in their `dmaps`.
```

### Scheduling windows

The Phoenix-RTOS scheduler extends its priority-based round-robin algorithm with a time-partitioned
scheduling layer. Time is divided into a repeating cycle of slots, separate for each CPU. Each slot has a fixed
duration (in microseconds) and is assigned a particular **scheduling window**. The cycle repeats continuously; when the last
window in the cycle completes, the scheduler wraps around and starts from the first window again. Single window can be assigned to multiple slots.

Each partition is assigned to a single scheduling window, multiple partitions may share the same window.
In that case, their threads are placed in the same ready queues and compete for CPU time using the standard priority-based round-robin policy within that window.

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

Each window has its own set of priority-indexed ready queues and its own tree of sleeping threads. When selecting
the next thread, the scheduler scans priorities from the highest criticality and, for a given priority, checks
the ready queue of the current window first, then the background window, and finally the kernel window. The next
timer wakeup is computed from both the end of the current slot and the earliest wakeup of sleeping threads in the
windows eligible to run, so a partition cannot influence the moment the timer interrupt is programmed for another
partition.

```{note}
On some targets, due to hal limitations, scheduling slots will be aligned to SYSTICK_INTERVAL, which usually is 1ms.
```

```{note}
The scheduler configuration given with the `sched` command must contain exactly one cycle description per CPU
present in the system.
```

If the `sched` command is not used at all, `plo` provides a default configuration with no partition windows —
all threads run in the kernel window (0) and no time partitioning is performed. This default cycle is shared by
all CPUs.

#### Priority limits

Each partition defines a minimum allowed priority. Phoenix-RTOS priorities range from -32 to 31, where a lower
value means higher criticality. Creating a thread with a priority below the partition's limit fails with `-EINVAL`
and changing the priority of an existing thread below the limit fails with `-EPERM`. This allows guaranteeing
precedence to critical event-driven threads (e.g. in the background window) over threads of other partitions.

The limit applies to the base priority only — a thread may temporarily exceed it through priority inheritance on
kernel locks.

#### Kernel locks owned by another partition

If a thread waits for a kernel lock owned by a thread from a different scheduling window, the owner is
temporarily moved to the kernel window (0) ready queues. The owner executes its critical section in the current
slot (with priority inherited from the waiter, according to the lock attributes) and returns to its partition's
window right after releasing the lock, followed by a reschedule. As a result, the time a partition can be blocked
on a lock held by another partition is bounded by the length of the critical section and does not include
waiting for the next slot of the owner's window.

### Memory isolation

#### NOMMU targets (MPU)

On NOMMU targets the MPU is fully reprogrammed on every context switch. For each partition (and for each
program in the default partition) `plo` precomputes a separate table of MPU region register values while
parsing the configuration script. Thanks to this, a configuration that cannot be represented with the available
number of MPU regions is detected at boot time, before the kernel is started, not at runtime.

#### MMU targets

On MMU targets spatial separation is provided by virtual memory. `MAP_PHYSMEM` mappings are possible only to
partition's accessible maps and to physical memory outside of any defined maps.

#### Physical maps and allocation pools

Physical memory is divided into several independent physical maps, corresponding to the maps declared in the `plo`
script, each with its own allocation pool. The `dmaps` argument of the `app` command defines the ordered list of
physical maps the process allocates its memory from — allocation attempts follow the list order and the first map with
enough free memory is used. Child processes created with `(v)fork`/`spawn` inherit the list from their parent.

Processes in the default partition allocate memory only from the first map listed in `dmaps`; the remaining maps
are only accessible (e.g. via manual `MAP_PHYSMEM` mappings).

Assigning disjoint allocation maps to partitions limits memory contention and sharing of allocator locks between
partitions.

#### Object mappings

Mappings backed by an object (file-backed `mmap`) require that the calling process is allowed to send messages to the port owning that object. Otherwise `mmap` fails with `-EACCES`. Anonymous shared objects (created with `MAP_CONTIGUOUS`) are bound to the partition that created them and cannot be mapped by other partitions.

### Memory limits

Each partition tracks its physical memory consumption. When a process belonging to a partition attempts to
allocate memory (via `mmap` or internal kernel allocations done on behalf of the process within its memory map),
the kernel checks whether the allocation would exceed the partition's configured memory limit. If it would, the
allocation fails with `-ENOMEM`.

Memory freed by the partition's processes is credited back to the partition's usage counter.

Memory limits do not include memory for internal kernel objects. Separate kernel-memory limit is planned in the future.

### IPC isolation

Processes in different partitions are not allowed to exchange messages over regular (dynamically created)
ports. If a process attempts to send a message (`msgSend`) to a port owned by a process in a different
partition, the operation fails with `-EACCES`. The same restriction applies to `msgRecv` on ports owned by
processes in other partitions.

Kernel threads are not subject to IPC restrictions.

#### Named ports

The Inter-Partition communication can only occur on dedicated named ports that are configurable to work between selected partitions.

Named ports are declared in the `plo` script (see the `port` command) and are created by the kernel during
boot, before any user process is started. They have no owning process — access is governed solely by two
partition lists:

- **receive list** — partitions whose processes may call `msgRecv` on the port,
- **send list** — partitions whose processes may call `msgSend` to the port.

A process obtains the port identifier of a named port with the `sys_namedResource` syscall:

```c
int sys_namedResource(const char *name, size_t len, u32 *portId);
```

The call returns `-EINVAL` if no port of that name is declared and `-EACCES` if the calling partition is
listed in neither of the two lists.

```{note}
The kernel log port (`/dev/kmsg` served by `usrv`) is a predefined named port called `usrv`. Its receive list is
empty (only the kernel receives on it) and its send list allows all partitions.
```

#### Name resolution isolation

The kernel name cache (used by `portRegister`, `portUnregister` and `lookup`) is partition-scoped. Entries
registered by a process are visible only to processes of the same partition, including the root entry `/`.
Different partitions may therefore register the same path name, each resolving to its own server. This allows
each partition to have its own, independent filesystem tree.

```{note}
To share a filesystem, partitions can decide to use a shared port as filesystem port and each sharing partition need to register that port (e.g. as root fs `/`), or bind within other filesystem.
```

### Process and thread control isolation

- **Process spawning** — a process belonging to a partition can only spawn new processes within the same
  partition by default. An attempt to spawn a process in a different partition results in an `-EACCES` error.
- **Thread control** — syscalls operating on a given thread or process reject objects belonging to another
  partition with `-ESRCH`, as if the object did not exist.
- **Signals** — sending a signal to a process or thread of another partition fails with `-ESRCH`.
- **Unix sockets** — a unix socket is bound to the partition that created it; processes of other partitions
  cannot access it.

### Restricted syscalls

The following syscalls are gated by partition flags and return `-EPERM` if the corresponding flag is not set:

| Syscall                                                      | Required flag |
|--------------------------------------------------------------|---------------|
| `interrupt`                                                  | `i`           |
| `platformctl`                                                | `c`           |
| `settime`                                                    | `t`           |
| `perf_start`, `perf_read`, `perf_stop`, `perf_finish`        | `p`           |

All user programs execute in unprivileged mode. Interrupt handlers are executed in privileged mode, hence
installing them is restricted to partitions with the `i` flag.

## Configuration

Partitioning is configured entirely through the Phoenix-RTOS loader (`plo`) command-line interface before
the kernel is started. The configuration involves four steps:

1. Define scheduling windows using the `sched` command.
2. Define partitions using the `part` command.
3. Load applications into partitions using the `app` command.
4. Define named ports with access restrictions using the `port` command.

### Step 1: Define scheduling windows

```text
- sched <windowsCnt> <CPU0 [bgId];id:duration;...> [CPU1 [bgId];id:duration;...] ...
```

The `sched` command defines the scheduling cycle by specifying the microseconds duration and window of each slot.
Windows are numbered sequentially starting from 1 (window 0 is the implicit kernel window). `windowsCnt` is the
number of windows excluding the kernel window; no window ID used later may exceed it.

One cycle description must be given per CPU. The optional `bgId` at the beginning of a cycle description selects
the background window for that CPU; if omitted, only the kernel window acts as a background window.

**Example:**

```text
- sched 4 1;2:10000;3:20000;4:10000
```

This declares four scheduling windows (1-4) and the following cycle:

| Slot | Window ID | Duration    |
|------|-----------|-------------|
| bg   | 1         | -           |
| 1    | 2         | 10 000 µs   |
| 2    | 3         | 20 000 µs   |
| 3    | 4         | 10 000 µs   |

The total cycle length is 40 000 µs (40 ms). The cycle repeats: `window 2 -> window 3 -> window 4 -> window 2 -> ...`.
Window 1 is the background window, meaning its threads may run during any slot.

### Step 2: Define partitions

```text
- part <name> <accessmaps> <schedwindow> <memlimit> <minPriority> [-flags]
```

Parameters:

- **`name`** — a unique name for the partition.
- **`accessmaps`** — semicolon-separated list of map names that this partition's processes may access
  (enforced by MPU on supported targets, at most 16 entries).
- **`schedwindow`** — scheduling window ID (as defined by `sched`) assigned to this partition.
- **`memlimit`** — maximum amount of memory that the partition may use. Set to `0` for unlimited.
- **`minPriority`** — minimum allowed thread priority (-32 to 31, lower value means higher criticality). Set to
  `-32` for no limit.
- **`flags`** — access flags to:
  - **`i`** — interrupt handlers,
  - **`c`** — PlatformCtl calls,
  - **`t`** — global UTC time changes,
  - **`p`** — Perf subsystem syscalls.

**Example:**

```text
- part safety sram1;sram2;flash1 3 0x80000 0
- part mission sram2;flash2 2 0x100000 -16
- part drivers sram1;dev 1 0 -32 -ic
```

This defines three partitions:

- **`safety`**: can access `sram1`, `sram2`, and `flash1`, runs in scheduling
  window 3, has a memory limit of 512 KB (0x80000), its threads may not use priorities below 0.
- **`mission`**: can access `sram2` and `flash2`, runs in scheduling window 2,
  has a memory limit of 1 MB (0x100000), its threads may not use priorities below -16.
- **`drivers`**: can access `sram1` and `dev`, runs in scheduling window 1,
  has no memory limit nor priority limit and can install interrupt handlers or use platformCtl system calls.

### Step 3: Load applications into partitions

```text
app <dev> [-x] <name> <imaps> <dmaps> [<partition>]
```

The `app` command has an optional last argument specifying the partition name. **`dmaps`** defines list of maps that this process and subprocesses will allocate memory from, in the order given.

If omitted, a default partition is automatically assigned for the application with settings to behave
just like without partitioning support. For backwards compatibility, in this case only first **`dmap`** is used for allocation, while remaining maps listed are only accessible (e.g. via manual MAP_PHYSMEM mappings).

**Example:**

```text
- app flash0 -x dummyfs sram1 sram1 safety
- app flash0 -x executor sram2 sram2 mission
- app flash0 -x sensor_driver sram1 sram1 drivers
```

This loads `dummyfs` into the `safety` partition, `executor` into the `mission` partition, and `sensor_driver` into the `drivers` partition.

### Step 4: Define named ports

```text
- port <name> <recvPart1;recvPart2...> <sendPart1;sendPart2...>
```

Parameters:

- **`name`** — a unique name of the port, used later by `sys_namedResource`.
- **`recvParts`** — semicolon-separated list of partition names allowed to receive messages on the port.
- **`sendParts`** — semicolon-separated list of partition names allowed to send messages to the port.

**Example:**

```text
- port sensors drivers safety;mission
```

This creates a `sensors` port on which only the `drivers` partition may receive, while the `safety` and
`mission` partitions may send requests to it.

## Complete configuration example

Example of `plo` script fragment demonstrates a complete partitioning setup:

```yaml
- sched 3 1;2:10000;3:20000

- part safety sram1;sram2;flash1 3 0x80000 0
- part mission sram2;flash2 2 0x100000 -16
- part drivers sram1;dev 1 0 -32 -ic

- app flash0 -x dummyfs sram1 sram1 safety
- app flash0 -x executor sram2 sram2 mission
- app flash0 -x sensor_driver sram1 sram1 drivers

- port sensors drivers safety;mission

```

The cycle alternates between window 2 (`mission`, 10 ms) and window 3 (`safety`, 20 ms), while window 1
(`drivers`) is the background window and may run in any slot. The `sensors` named port lets both application
partitions talk to the driver partition.

## Known limitations

- Memory limits do not cover memory used by internal kernel objects.
- There are no restrictions on information disclosure (`sysinfo`, `meminfo`).
- A partition may influence another partition through the execution time of syscalls that use global kernel
  resources, and through shared hardware resources (CPU caches, memory bus).
- On some targets scheduling slots are aligned to `SYSTICK_INTERVAL`.
- At most 32 partitions and 16 access maps per partition.
- Inter-partition communication uses the existing, synchronous IPC methods only.
