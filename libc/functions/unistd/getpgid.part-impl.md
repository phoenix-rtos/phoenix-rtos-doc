# getpgid

## Synopsis

`#include <unistd.h>`

`pid_t getpgid(pid_t pid);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getpgid()` function shall return the process group ID of the process whose process ID is equal to _pid_. If _pid_
is equal to `0`, `getpgid()` shall return the process group ID of the calling process.

## Return value

Upon successful completion, `getpgid()` shall return a process group ID. Otherwise, it shall return `(pid_t)-1` and set
`errno` to indicate the error.

## Errors

The `getpgid()` function shall fail if:

* `EPERM` - The process whose process ID is equal to _pid_ is not in the same session as the calling process, and the
 implementation does not allow access to the process group ID of that process from the calling process.

* `ESRCH` - There is no process with a process ID equal to _pid_.

The `getpgid()` function may fail if:

* `EINVAL` - The value of the _pid_ argument is invalid.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
