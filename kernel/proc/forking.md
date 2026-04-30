# Management

Phoenix-RTOS creates processes with `fork()` or `vfork()`.
The selected mechanism depends on the target architecture and MMU availability.

## Create a process with `fork()`

The `fork()` syscall creates a child process from the current process.
The child receives a process image derived from the parent linear address space and operating system resources.
After `fork()`, parent and child modifications remain private to each process.

This mechanism requires MMU hardware.
On processors without an MMU, Phoenix-RTOS uses `vfork()`.

## Create a process with `vfork()`

`vfork()` optimizes the fork-then-exec pattern. A traditional `fork()` requires duplicating all the memory of the parent
process in the child which leads to significant overhead. The goal of the `vfork()` function was to reduce this
overhead by preventing unnecessary memory copying when new process is created. `fork()` before `exec()` wastes effort:
child memory is copied only to be discarded when `exec()` loads a new program.

`vfork()` also enables POSIX-compatible process creation on non-MMU architectures.

### Kernel stack management during vfork

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
`vfork()` is a full synchronization primitive.
The parent is blocked until the child calls `exec()` or `_exit()`.
On non-MMU architectures this is the primary process creation mechanism.
```

## Process termination

Process can be terminated abnormally - as the consequence of receiving signal or normally after executing `exit()`
function. When process exits all of its threads are terminated, all memory objects are unmapped and all resource handles
are freed/closed. The parent process receives `SIGCHLD` signal notifying it about the child termination. `SIGCHLD`
signal plays another important role in process termination sequence. It allows to safe remove the remaining child
process resources which are not able to be removed during the process runtime (e.g. last thread kernel stack).

## Signal subsystem

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

### Signal delivery

When a signal is posted to a process, the kernel selects a thread within that process to handle it. The signal is
marked as pending until the target thread is scheduled and the signal is not blocked by the thread's signal mask.
When the thread runs, the kernel diverts execution to the registered handler. After the handler returns, `sigreturn()`
restores the original execution context.

## Process groups and sessions

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

To execute a new program, the `exec()` family maps the binary object into the process linear address space and passes
control to the program entry point.

On non-MMU architectures, the kernel relocates the program after mapping the binary object and before passing control to
the program entry point.
Relocation recalculates program structures, such as `GOT`, that are used for variable access during runtime.
The relocation depends on the current program memory location.

## Thread management

A process represents memory space and operating system resources for an executed program.
A thread represents an instruction stream that runs concurrently with other threads in the process context.
The `beginthread()` and `endthread()` functions manage threads.

`beginthread()` starts a thread from a function address and a stack allocated by the calling thread.
The kernel allocates stacks for the required thread execution modes.
`endthread()` terminates the calling thread and releases allocated kernel stacks.

### Thread run states

Each thread is in one of three run states:

| State | Value | Description |
|-------|-------|-------------|
| `READY` | 0 | Thread is eligible for scheduling and is running or waiting in the ready queue |
| `SLEEP` | 1 | Thread is blocked waiting on a synchronization object (mutex, condvar, semaphore, or message) |
| `GHOST` | 2 | Thread has terminated but its resources have not yet been cleaned up by the reaper |

### Termination flags

In addition to run states, two flags control thread termination:

| Flag | Value | Description |
|------|-------|-------------|
| `THREAD_END` | 1 | Cooperative termination request. The thread exits at its next safe point. |
| `THREAD_END_NOW` | 2 | Immediate termination request. The thread is forcibly stopped. |

These are flags, not states.
A thread can be in `READY` state with `THREAD_END` set, which means it terminates the next time it is scheduled.
The reaper thread handles final resource cleanup for `GHOST` threads.

### Kernel stack architecture

Each thread has a dedicated kernel stack with a size defined per architecture (`SIZE_KSTACK`). During system bootstrap
a separate initial stack (`SIZE_INITIAL_KSTACK`) is used before the thread subsystem is initialized. Stack canaries
are placed at the bottom of each kernel stack (`threads_canaryInit()`) to detect stack overflow.
