# Synopsis 
`#include <unistd.h>`</br>

` pid_t setsid(void);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `setsid()` function shall create a new session, if the calling process is not a process group leader. Upon return the
calling process shall be the session leader of this new session, shall be the process group leader of a new process group, and
shall have no controlling terminal. The process group ID of the calling process shall be set equal to the process ID of the calling
process. The calling process shall be the only process in the new process group and the only process in the new session.


## Return value


Upon successful completion, `setsid()` shall return the value of the new process group ID of the calling process.
Otherwise, it shall return `-1` and set `errno` to indicate the error.


## Errors


The `setsid()` function shall fail if:


 * `EPERM` - The calling process is already a process group leader, or the process group ID of a process other than the calling process
matches the process ID of the calling process.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
