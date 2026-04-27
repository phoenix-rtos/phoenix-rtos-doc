# Management

Processes are created by forking. The current process splits into parent and child. There are two forking functions
used for process creation in Phoenix-RTOS - each of them should be used depending on the platform and MMU presence.
The differences between these functions and circumstances of their usage are discussed in this chapter.

## Creating new process using `fork()`

The well-known method of creating new process in general purpose operating systems (e.g. UN*X) is a forking.
The explanation of this method is quite simple. In the certain point of time a thread within a process calls `fork()`
system call which creates a new process (child process) based on linear address space and operating system resources
used by process calling `fork()` (parent process) and launches the thread within a child process. From this point of
time processes are separated, and they operate on their own address spaces. It means that all modifications of process
memory are visible only within them.

<!-- REVIEW: consider condensing the fork/COW example (lines ~13-17) - five sentences for a simple concept -->
For example, let's consider process A forking into processes A and B.
After forking, one of the threads of process A modifies variable located at address `addr` and stores their value 1
and thread of process B modifies the same variable at address `addr` and stores there 2. The modification is specific
for the forked processes, and operating system assures that process A sees the variable located at `addr`
as 1 and process B sees it as 2.

This requires MMU hardware. On processors lacked of MMU the `fork()` method is unavailable, and it is replaced by `vfork()`.

## Creating new process using `vfork()`

`vfork()` optimizes the fork-then-exec pattern. A traditional `fork()` requires duplicating all the memory of the parent
process in the child which leads to significant overhead. The goal of the `vfork()` function was to reduce this
overhead by preventing unnecessary memory copying when new process is created. `fork()` before `exec()` wastes effort:
child memory is copied only to be discarded when `exec()` loads a new program.

In UN*X operating system history "The Mach VM system" added Copy On Write (COW), which made the `fork()` much cheaper,
and in BSD 4.4, `vfork()` was made synonymous to `fork()`.

`vfork()` also enables POSIX-compatible process creation on non-MMU architectures.

<!-- REVIEW: POSIX history paragraph (vfork removed in POSIX.1-2008) may be excessive detail -->
Some consider the semantics of `vfork()` to be an architectural blemish and POSIX.1-2008 removed `vfork()` from the
standard and replaced it with `posix_spawn()`. The POSIX rationale for the `posix_spawn()` function notes that that
function, which provides functionality equivalent to `fork()`+`exec()`, is designed to be implementable on
systems that lack an MMU.

### Kernel Stack Management During vfork

When `vfork()` is called, the parent process is fully suspended until the child calls `exec()` or `_exit()`. The kernel
achieves this by saving and restoring the parent's kernel stack:

1. **Parent suspension**: The parent's kernel stack is saved into a dynamically allocated buffer (`parentkstack`). The
   parent thread is blocked and cannot run until the child completes.

2. **Child execution**: The child runs in the parent's address space (no copy-on-write). The child must not modify the
   parent's stack or return from the function that called `vfork()`.

3. **Child exit or exec**: When the child calls `exec()` or `_exit()`, the kernel restores the parent's kernel stack
   from `parentkstack` and resumes the parent. An additional `execkstack` buffer handles the transition when the child
   calls `exec()`.

```{note}
`vfork()` is a full synchronization primitive - the parent is unconditionally blocked, not merely
deprioritized. On non-MMU architectures this is the primary process creation mechanism.
```

## Process termination

Process can be terminated abnormally - as the consequence of receiving signal or normally after executing `exit()`
function. When process exits all of its threads are terminated, all memory objects are unmapped and all resource handles
are freed/closed. The parent process receives `SIGCHLD` signal notifying it about the child termination. `SIGCHLD`
signal plays another important role in process termination sequence. It allows to safe remove the remaining child
process resources which are not able to be removed during the process runtime (e.g. last thread kernel stack).

## Signal Subsystem

Phoenix-RTOS implements a POSIX-compatible signal subsystem. The kernel provides five signal-related syscalls:

| Syscall | Purpose |
|---------|---------|
| `signalHandle(signal, handler)` | Register a signal handler function for a specific signal number |
| `signalPost(pid, tid, signal)` | Send a signal to a process or a specific thread within a process |
| `signalMask(how, mask, old)` | Modify the calling thread's signal mask (block/unblock signals) |
| `signalSuspend(mask)` | Suspend the thread until a signal matching the given mask is delivered |
| `sigreturn()` | Return from signal handler context (called by the signal trampoline) |

Additionally, `tkill(pid, tid, signal)` sends a signal to a specific thread identified by TID, bypassing the
kernel's default thread selection for process-directed signals.

### Signal Delivery

When a signal is posted to a process, the kernel selects a thread within that process to handle it. The signal is
marked as pending until the target thread is scheduled and the signal is not blocked by the thread's signal mask.
When the thread runs, the kernel diverts execution to the registered handler. After the handler returns, `sigreturn()`
restores the original execution context.

## Process Groups and Sessions

Process groups and sessions provide job control capabilities. The kernel implements four syscalls:

| Syscall | Purpose |
|---------|---------|
| `setpgid(pid, pgid)` | Set the process group ID of a process |
| `getpgid(pid)` | Get the process group ID of a process |
| `setpgrp()` | Set the calling process's group to its own PID (equivalent to `setpgid(0, 0)`) |
| `setsid()` | Create a new session with the calling process as session leader |

These syscalls are routed through the POSIX compatibility layer (`posix_setpgid()`, `posix_getpgid()`,
`posix_setsid()`).

## Program execution

To execute a new program the binary object representing it should be mapped into the process linear address space and
control have to be passed to the program entry point. This is the responsibility of `exec()` family functions.

On non-MMU architectures, there is one important step performed after a binary object is mapped and before control is
passed to the program entry point. This step is the program relocation which recalculates some program structures
(e.g. `GOT`) used for accessing variables during the runtime. The relocation depends on the current memory location of
program.

## Thread management

While process represents a memory space and operating system resources devoted for particular executed program the
thread represents the program instruction stream executed concurrently to other threads in the process context
(using defined linear address space and associated operating system resources). To manage threads `beginthread()`,
`endthread()` functions should be used.

`beginthread()` function starts a new thread using function address and stack allocated by a calling thread. The kernel
stacks for all of desired thread execution modes are allocated. `endthread()` function terminates calling thread and
releases allocated kernel stacks.

### Thread Run States

Each thread is in one of three run states:

| State | Value | Description |
|-------|-------|-------------|
| `READY` | 0 | Thread is eligible for scheduling and may be running or waiting in the ready queue |
| `SLEEP` | 1 | Thread is blocked waiting on a synchronization object (mutex, condvar, semaphore, or message) |
| `GHOST` | 2 | Thread has terminated but its resources have not yet been cleaned up by the reaper |

### Termination Flags

In addition to run states, two flags control thread termination:

| Flag | Value | Description |
|------|-------|-------------|
| `THREAD_END` | 1 | Cooperative termination request - thread should exit at its next safe point |
| `THREAD_END_NOW` | 2 | Immediate termination request - thread is forcibly stopped |

These are flags, not states - a thread can be in `READY` state with `THREAD_END` set, meaning it will terminate
the next time it is scheduled. The reaper thread handles final resource cleanup for `GHOST` threads.

### Kernel Stack Architecture

Each thread has a dedicated kernel stack with a size defined per architecture (`SIZE_KSTACK`). During system bootstrap
a separate initial stack (`SIZE_INITIAL_KSTACK`) is used before the thread subsystem is initialized. Stack canaries
are placed at the bottom of each kernel stack (`threads_canaryInit()`) to detect stack overflow.
