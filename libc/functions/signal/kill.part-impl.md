# kill

## Synopsis

`#include <signal.h>`

`int kill(pid_t pid, int sig);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `kill()` function shall send a signal to a process or a group of processes specified by _pid_. The signal to be sent
is specified by _sig_ and is either one from the list given in `<signal.h>` or 0. If _sig_ is `0` (the `null` signal),
error checking is performed, but no signal is actually sent. The `null` signal can be used to check the validity of
_pid_.

For a process to have permission to send a signal to a process designated by _pid_, unless the sending process has
appropriate privileges, the real or effective user ID of the sending process shall match the real or saved set-user-ID
of the receiving process.

If _pid_ is greater than `0`, _sig_ shall be sent to the process whose process ID is equal to _pid_.

If _pid_ is `0`, _sig_ shall be sent to all processes (excluding an unspecified set of system processes) whose process
group ID is equal to the process group ID of the sender, and for which the process has permission to send a signal.

If _pid_ is `-1`, _sig_ shall be sent to all processes (excluding an unspecified set of system processes) for which the
process has permission to send that signal.

If _pid_ is negative, but not `-1`, _sig_ shall be sent to all processes (excluding an unspecified set of system
processes) whose process group ID is equal to the absolute value of _pid_, and for which the process has permission
to send a signal.

If the value of _pid_ causes _sig_ to be generated for the sending process, and if _sig_ is not blocked for the calling
thread and if no other thread has _sig_ unblocked or is waiting in a `sigwait()` function for _sig_, either _sig_ or at
least one pending unblocked signal shall be delivered to the sending thread before `kill()` returns.

The user ID tests described above shall not be applied when sending `SIGCONT` to a process that is a member of the same
session as the sending process.

An implementation that provides extended security controls may impose further implementation-defined restrictions on the
sending of signals, including the `null` signal. In particular, the system may deny the existence of some or all of the
processes specified by _pid_.

The `kill()` function is successful if the process has permission to send _sig_ to any of the processes specified by
_pid_. If `kill()` fails, no signal shall be sent.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and errno set to indicate the
error.

## Errors

The `kill()` function shall fail if:

* `EINVAL` - The value of the _sig_ argument is an invalid or unsupported signal number.

* `EPERM` - The process does not have permission to send the signal to any receiving process.

* `ESRCH` - No process or process group can be found corresponding to that specified by _pid_.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
