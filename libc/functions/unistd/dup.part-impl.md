# dup

## Synopsis

`#include <unistd.h>`

`int dup(int fildes);`

`int dup2(int fildes, int fildes2);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `dup()` function provides an alternative interface to the service provided by `fcntl()` using the `F_DUPFD` command.
The call `dup(fildes)` shall be equivalent
to:

`fcntl(fildes, F_DUPFD, 0);`

The `dup2()` function shall cause the file descriptor _fildes2_ to refer to the same open file description as the file
descriptor _fildes_ and to share any locks, and shall return _fildes2_. If _fildes2_ is already a valid open file
descriptor, it shall be closed first, unless _fildes_ is equal to _fildes2_ in which case `dup2()` shall return
_fildes2_ without closing it. If the close operation fails to close _fildes2_, `dup2()` shall return ``-1`` without
changing the open file description to which _fildes2_ refers. If _fildes_ is not a valid file descriptor, `dup2()`
shall return `-1` and shall not close _fildes2_. If _fildes2_ is less than `0` or greater than or equal to `OPEN_MAX`,
`dup2()` shall return `-1` with errno set to `EBADF`.

Upon successful completion, if _fildes_ is not equal to _fildes2_, the `FD_CLOEXEC` flag associated with _fildes2_
shall be cleared. If _fildes_ is equal to _fildes2_, the `FD_CLOEXEC` flag associated with _fildes2_ shall not be
changed.
If _fildes_ refers to a typed memory object, the result of the `dup2()` function is unspecified.

## Return value

Upon successful completion a non-negative integer, namely the file descriptor, shall be returned; otherwise, `-1` shall
be returned and errno set to indicate the error.

## Errors

The `dup()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid open file descriptor.

* `EMFILE` - All file descriptors available to the process are currently open.

The `dup2()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid open file descriptor or the argument _fildes2_ is negative or greater
 than or equal to `OPEN_MAX`.

* `EINTR` - The `dup2()` function was interrupted by a signal.

The `dup2()` function may fail if:

* `EIO` - An I/O error occurred while attempting to close _fildes2_.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
