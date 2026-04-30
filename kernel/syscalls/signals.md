# Signal syscalls

Signal syscalls register a process-level handler, post pending signals, manage the calling thread signal mask, and
return from signal handler context.
The implementation is in `phoenix-rtos-kernel/syscalls.c`, `phoenix-rtos-kernel/proc/threads.c`, and
`phoenix-rtos-kernel/posix/posix.c`.

## Syscall entry points

| Handler | Arguments | Source behavior |
| --- | --- | --- |
| `syscalls_signalHandle()` | `handler`, `mask`, `mmask` | Updates the process signal mask bits selected by `mmask` and stores the process handler. |
| `syscalls_signalPost()` | `pid`, `tid`, `signal` | Finds the target process, optionally finds a thread, validates ownership, and calls `threads_sigpost()`. |
| `syscalls_signalMask()` | `mask`, `mmask` | Updates the calling thread mask bits selected by `mmask` and returns the previous thread mask. |
| `syscalls_signalSuspend()` | `mask` | Atomically installs a temporary mask and sleeps until a signal path wakes the thread. |
| `syscalls_sigreturn()` | `oldmask`, `ctx` | Restores the saved signal mask and validates that return context is not supervisor mode. |
| `syscalls_sys_tkill()` | `pid`, `tid`, `sig` | Delegates POSIX-compatible targeting rules to `posix_tkill()`. |

## Pending signal storage

The process structure stores `sigmask`, `sigpend`, and a `sighandler` pointer.
Each thread stores its own `sigmask` and `sigpend`.
A process-directed signal sets the process pending bit, while a thread-directed signal sets the target thread pending
bit.

`threads_sigpost()` handles special signals before queueing:

| Signal value | Behavior |
| --- | --- |
| `signal_kill` | Kills the process. |
| `signal_cancel` | Destroys the target thread. |
| `signal_segv` and `signal_illegal` | Kill the process when no process handler is installed. |
| `0` | Returns success without setting a pending bit. |

For process-directed signals, `threads_sigpost()` walks the process thread list and interrupts the first thread that
has the signal unmasked and is marked as interruptible.
If the process has no threads, the function returns `-ESRCH`.

## Delivery

The scheduler checks signals on the return-to-user path and during `signalSuspend()`.
The pending set is computed as `(thread->sigpend | process->sigpend) & ~thread->sigmask`.
When a process handler is installed and a pending bit exists, the HAL selects the signal number with
`hal_cpuGetLastBit()` and builds handler context with `hal_cpuPushSignal()`.
After the context is built, the delivered bit is cleared from both the thread and process pending sets.

`threads_setupUserReturn()` installs the signal handler context after syscall handling and jumps to the process handler.
`threads_sigsuspend()` temporarily replaces the thread mask, checks pending signals before sleeping, sleeps on an
interruptible queue, checks again after wakeup, restores the old mask when no handler runs, and returns `-EINTR`.

## Thread-specific kill

`syscalls_sys_tkill()` reads `pid`, `tid`, and `sig`, then calls `posix_tkill()`.
`posix_tkill()` applies these source-defined rules:

| Condition | Return or action |
| --- | --- |
| `sig < 0` or `sig > NSIG` | Returns `-EINVAL`. |
| `pid == 0` | Returns `-ENOSYS`. |
| `pid == -1` | Returns `-ESRCH`. |
| `pid > 0` | Sends the signal to one process through `posix_killOne(pid, tid, sig)`. |
| `pid < 0` | Sends the signal to the process group `-pid` through `posix_killGroup()`. |

A nonnegative `tid` in `syscalls_signalPost()` must name a thread that belongs to the selected process.
