# fsync

## Synopsis

`#include <unistd.h>`

`int fsync(int fildes);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fsync()` function shall request that all data for the open file descriptor named by _fildes_ is to be transferred
to the storage device associated with the file described by _fildes_. The nature of the transfer is
implementation-defined.

The `fsync()` function shall not return until the system has completed that action or until an error is detected.

If `_POSIX_SYNCHRONIZED_IO` is defined, the `fsync()` function shall force all currently queued I/O operations
associated with the file indicated by file descriptor _fildes_ to the synchronized I/O completion state. All I/O
operations shall be completed as defined for synchronized I/O file integrity completion.

## Return value

Upon successful completion, `fsync()` shall return `0`. Otherwise, `-1` shall be returned and `errno` set to indicate
the error. If the `fsync()` function fails, outstanding I/O operations are not guaranteed to have been completed.

## Errors

The `fsync()` function shall fail if:

* `EBADF` - The _fildes_ argument is not a valid descriptor.
* `EINTR` - The `fsync()` function was interrupted by a signal.
* `EINVAL` - The _fildes_ argument does not refer to a file on which this operation is possible.
* `EIO` - An I/O error occurred while reading from or writing to the file system.

In the event that any of the queued I/O operations fail, `fsync()` shall return the error conditions defined for
`read()` and `write()`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
