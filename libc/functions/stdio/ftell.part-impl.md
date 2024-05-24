# ftell

## Synopsis

`#include <stdio.h>`

`long ftell(FILE *stream);`

`off_t ftello(FILE *stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to return a file offset in a stream. The `ftell()` function shall obtain the current value of the
file-position indicator for the stream pointed to by _stream_.

The `ftell()` function shall not change the setting of errno if successful.

The `ftello()` function shall be equivalent to `ftell()`, except that the return value is of type `off_t` and the
`ftello()` function may change the setting of `errno` if successful.

## Return value

Upon successful completion, `ftell()` and `ftello()` shall return the current value of the file-position indicator for
the stream measured in bytes from the beginning of the file.

Otherwise, `ftell()` and `ftello()` shall return `-1`, and set `errno` to indicate the error.

## Errors

The `ftell()` and `ftello()` functions
shall fail if:

* `EBADF` - The file descriptor underlying stream is not an open file descriptor.

* `EOVERFLOW` - For `ftell()`, the current file offset cannot be represented correctly in an object of type long.

* `EOVERFLOW` - For `ftello()`, the current file offset cannot be represented correctly in an object of type `off_t`.

* `ESPIPE` - The file descriptor underlying stream is associated with a pipe, FIFO, or socket.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
