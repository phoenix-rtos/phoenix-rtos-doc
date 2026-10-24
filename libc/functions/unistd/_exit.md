# _exit

## Synopsis

```c
#include <stdlib.h>

void _Exit(int status);

#include <unistd.h>

void _exit(int status);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `_Exit()` and `_exit()` functions terminate the calling process.

The value of status may be `0`, `EXIT_SUCCESS`, `EXIT_FAILURE`, or any other value, though only the least significant 8
bits (that is, `status & 0xff`) are available from `wait()` and `waitpid()`; the full value is available from `waitid()`
and in the `siginfo_t` passed to a signal handler for `SIGCHLD`.

The functions do not call functions registered with `atexit()` nor any registered signal handlers. Open streams are not
flushed, but opened file descriptors are closed. Finally, the calling process is terminated with the consequences
described below.

### Consequences of Process Termination

All the file descriptors, directory streams, conversion descriptors, and message catalog descriptors open in the
calling process are closed.

If the parent process of the calling process has set the action for the `SIGCHLD` signal to `SIG_IGN`:

* The process' status information, if any, is discarded.

* The lifetime of the calling process ends immediately and a `SIGCHLD` signal is sent to the parent process.

* If a thread in the parent process of the calling process is blocked in `wait()`, `waitpid()`, or `waitid()`, and the
parent process has no remaining child processes in the set of waited-for children, the `wait()`, `waitid()`, or
`waitpid()` function fails and sets errno to `[ECHILD]`.

Otherwise:

* Status information is generated.

* The calling process is transformed into a zombie process. Its status information is made available to the parent
process until the process' lifetime ends.

* The process' lifetime ends once its parent obtains the process' status information via a currently-blocked or future
call to `wait()`, `waitid()` (without `WNOWAIT`), or `waitpid()`.

* If one or more threads in the parent process of the calling process is blocked in a call to `wait()`, `waitid()`, or
`waitpid()` awaiting termination of the process, one (or, if any are calling `waitid()` with `WNOWAIT`, possibly more)
of these threads obtains the process' status information as specified in Status Information and becomes unblocked.

* A `SIGCHLD` is sent to the parent process.

Termination of a process does not directly terminate its children. The sending of a `SIGHUP` signal as described below
indirectly terminates children in some circumstances.

If the process is a controlling process, the controlling terminal associated with the session is disassociated from the
session, allowing it to be acquired by a new controlling process.

The parent process ID of all the existing child processes and zombie processes of the calling process are set to the
process ID of a `init` system process. That is, these processes are inherited by a `init` process.

Memory mappings that were created in the process are unmapped before the process is destroyed.

Threads terminated by a call to `_Exit()` do not invoke their cancellation cleanup handlers or per-thread data
destructors.

If the calling process is a trace controller process, any trace streams that were created by the calling process are
shut down as described by the `posix_trace_shutdown()` function, and mapping of trace event names to trace event type
identifiers of any process built for these trace streams may be deallocated.

## Return value

The functions can never return.

## Errors

No errors are defined.

## POSIX deviations

When a controlling process terminates, the `SIGHUP` signal is not sent to the foreground process group of its
controlling terminal. In Phoenix-RTOS, terminals are handled by drivers running as user-space servers, and the kernel
doesn't keep a reference to the controlling terminal of a session. Sending the signal would require the kernel to track
the terminal of every session and to notify its server on the termination of every session leader, which adds
inter-process communication to the process termination path of a microkernel designed for resource-constrained edge and
IoT devices. The terminal server checks whether the session leader still exists when it handles the next request for the
terminal, and releases the terminal of a terminated session, so the terminal can be acquired by a new controlling
process. The processes of the former foreground process group are not signaled and keep running.
