# fileno

## Synopsis

`#include <stdio.h>`

`int fileno(FILE *stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fileno()` function maps a stream pointer to a file descriptor associated with the stream pointed to by _stream_.

## Return value

Upon successful completion, `fileno()` shall return the integer value of the file descriptor associated with _stream_.
Otherwise, the value `-1` shall be returned and `errno` set to indicate the error.

## Errors

The `fileno()` function shall fail if:

* `EBADF` - The stream is not associated with a file.

The `fileno()` function may fail if:

* `EBADF` - The file descriptor underlying stream is not a valid file descriptor.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
