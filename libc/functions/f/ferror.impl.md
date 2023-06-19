# Synopsis

`#include <stdio.h>`

`int ferror(FILE *stream);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `ferror()` function shall test the error indicator for the stream pointed to by _stream_.

The `ferror()` function shall not change the setting of errno if stream is valid.

## Return value

The `ferror()` function shall return non-zero if and only if the error indicator is set for stream.

## Errors

No errors are defined.

## Tests

Tested in [test-libc](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc).

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
