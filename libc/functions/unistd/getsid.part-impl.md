# getsid

## Synopsis

`#include <unistd.h>`

`pid_t getsid(pid_t pid);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getsid()` function shall obtain the process group ID of the process that is the session leader of the process
specified by _pid_. If _pid_ is `(pid_t)0`, it specifies the calling process.

## Return value

Upon successful completion, `getsid()` shall return the process group ID of the session leader of the specified process.
Otherwise, it shall return `-1` and set `errno` to indicate the error.

## Errors

The `getsid()` function shall fail if:

* `EPERM` - The process specified by _pid_ is not in the same session as the calling process, and the implementation
 does not allow access to the process group ID of the session leader of that process from the calling process.

* `ESRCH` - There is no process with a process ID equal to _pid_.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
