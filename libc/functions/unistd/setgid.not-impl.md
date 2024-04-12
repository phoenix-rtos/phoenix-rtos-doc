# setgid

## Synopsis

`#include <unistd.h>`

`int setgid(gid_t gid);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If the process has appropriate privileges, `setgid()` shall set the real group ID, effective group ID, and the saved
set-group-ID of the calling process to _gid_.

If the process does not have appropriate privileges, but _gid_ is equal to the real group ID or the saved set-group-ID,
`setgid()` shall set the effective group ID to _gid_; the real group ID and saved set-group-ID shall remain
unchanged.

The `setgid()` function shall not affect the supplementary group list in any way.

Any supplementary group IDs of the calling process shall remain unchanged.

## Return value

Upon successful completion, 0 is returned. Otherwise, `-1` shall be returned and `errno` set to indicate the error.

## Errors

The `setgid()` function shall fail if:

* `EINVAL` - The value of the _gid_ argument is invalid and is not supported by the implementation.

* `EPERM` - The process does not have appropriate privileges and _gid_ does not match the real group ID or the saved
set-group-ID.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
