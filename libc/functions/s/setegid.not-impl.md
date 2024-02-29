# setegid

## Synopsis

`#include <unistd.h>`

`int setegid(gid_t gid);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If _gid_ is equal to the real group ID or the saved set-group-ID, or if the process has appropriate privileges,
`setegid()` shall set the effective group ID of the calling process to _gid_; the real group ID, saved set-group-ID, and
any supplementary group IDs shall remain unchanged.

The `setegid()` function shall not affect the supplementary group list in any way.

## Return value

Upon successful completion, 0 shall be returned; otherwise, -1 shall be returned and `errno` set to indicate the error.

## Errors

The `setegid()` function shall fail if:

* `EINVAL` - The value of the _gid_ argument is invalid and is not supported by the implementation.

* `EPERM` - The process does not have appropriate privileges and _gid_ does not match the real group ID or the saved
set-group-ID.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
