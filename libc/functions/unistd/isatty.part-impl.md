# isatty

## Synopsis

`#include <unistd.h>`

`int isatty(int fildes);`

`int isatty(int fildes);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `isatty()` function shall test whether _fildes_, an open file descriptor, is associated with a terminal
device.

## Return value

The `isatty()` function shall return `1` if _fildes_ is associated with a terminal; otherwise, it shall return `0` and
may set errno to indicate the error.

## Errors

The `isatty()` function may fail if:

* `EBADF` - The _fildes_ argument is not a valid open file descriptor.

* `ENOTTY` - The file associated with the _fildes_ argument is not a terminal.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
