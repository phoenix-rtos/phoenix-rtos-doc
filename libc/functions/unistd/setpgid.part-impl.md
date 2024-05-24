# setpgid

## Synopsis

`#include <unistd.h>`

`int setpgid(pid_t pid, pid_t pgid);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `setpgid()` function shall either join an existing process group or create a new process group within the session of
the calling process.
The process group ID of a session leader shall not change.
Upon successful completion, the process group ID of the process with a process ID that matches _pid_ shall be set to
_pgid_.
As a special case, if _pid_ is 1, the process ID of the calling process shall be used. Also, if _pgid_ is `0`, the
process ID of the indicated process shall be used.

## Return value

Upon successful completion, `setpgid()` shall return `0`; otherwise, `-1` shall be returned and `errno` shall be set to
indicate the error.

## Errors

The `setpgid()` function shall fail if:

* `EACCES` - The value of the _pid_ argument matches the process ID of a child process of the calling process and the
child process has successfully executed one of the exec functions.

* `EINVAL` - The value of the _pgid_ argument is less than `0`, or is not a value supported by the implementation.

* `EPERM` - The process indicated by the _pid_ argument is a session leader.

* `EPERM` - The value of the _pid_ argument matches the process ID of a child process of the calling process and the
child process is not in the same session as the calling process.

* `EPERM` - The value of the _pgid_ argument is valid but does not match the process ID of the process indicated by the
_pid_ argument and there is no process with a process group ID that matches the value of the _pgid_ argument in the
same session as the calling process.

* `ESRCH` - The value of the _pid_ argument does not match the process ID of the calling process or of a child process
of the calling process.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
