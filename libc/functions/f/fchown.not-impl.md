# Synopsis

`#include <unistd.h>`

`int fchown(int fildes, uid_t owner, gid_t group);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fchown()` function shall be equivalent to `chown()` except that the file
whose _owner_ and _group_ are changed is specified by the file descriptor _fildes_.

## Return value

Upon successful completion, `fchown()` shall return 0. Otherwise, it shall return -1 and set `errno` to indicate the
error.

## Errors

The `fchown()` function shall fail if:

* `EBADF` - The _fildes_ argument is not an open file descriptor.

* `EPERM` - The effective user ID does not match the owner of the file or the process does not have appropriate
 privileges and `_POSIX_CHOWN_RESTRICTED` indicates that such privilege is required.

* `EROFS` - The file referred to by _fildes_ resides on a read-only file system.

The `fchown()` function may fail if:

* `EINVAL` - The owner or group ID is not a value supported by the implementation. The _fildes_ argument refers to a
 pipe or socket or a `fattach()`-ed STREAM and the implementation disallows execution of `fchown()` on a pipe.

* `EIO` - A physical I/O error has occurred.

* `EINTR` - The `fchown()` function was interrupted by a signal which was caught.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
