# fchdir

## Synopsis

`#include <unistd.h>`

`int fchdir(int fildes);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fchdir()` function shall be equivalent to `chdir()` except that the directory that is to be the new current working
directory is specified by the file descriptor _fildes_.

A conforming application can obtain a file descriptor for a file of type directory using `open()`, provided that the
file status flags and access modes do not contain `O_WRONLY` or `O_RDWR`.

## Return value

Upon successful completion, `fchdir()` shall return 0. Otherwise, it shall return -1 and set `errno` to indicate the
error. On failure the current working directory shall remain unchanged.

## Errors

The `fchdir()` function shall fail if:

* `EACCES` - Search permission is denied for the directory referenced by _fildes_.

* `EBADF` - The _fildes_ argument is not an open file descriptor.

* `ENOTDIR` - The open file descriptor _fildes_ does not refer to a directory.

The `fchdir()` may fail if:

* `EINTR` - A signal was caught during the execution of `fchdir()`.

* `EIO` - An I/O error occurred while reading from or writing to the file system.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
