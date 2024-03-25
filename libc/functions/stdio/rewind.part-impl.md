# rewind

## Synopsis

`#include <stdio.h>`

`void rewind(FILE *stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`rewind()` - reset the file position indicator in a stream

The call:

`rewind(stream)`

shall be equivalent to:

`(void) fseek(stream, 0L, SEEK_SET)`

Except that `rewind()` shall also clear the error indicator.

Since `rewind()` does not return a value, an application wishing to detect errors should clear `errno`, then call
`rewind()`, and if `errno` is non-zero, assume an error has occurred.

## Return value

The `rewind()` function shall not return a value.

## Errors

Refer to `fseek()` except `EINVAL` which does not apply.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
