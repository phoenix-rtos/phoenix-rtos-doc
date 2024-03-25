# feof

## Synopsis

`#include <stdio.h>`

`int feof(FILE *stream);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `feof()` function shall test the end-of-file indicator for the stream pointed to by _stream_.

The `feof()` function shall not change the setting of errno if stream is valid.

## Return value

The `feof()` function shall return non-zero if and only if the end-of-file indicator is set for stream.

## Errors

No errors are defined.

## Tests

Tested in [test-libc](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc).

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
