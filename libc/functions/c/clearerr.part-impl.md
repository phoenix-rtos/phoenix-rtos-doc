# Synopsis

`#include <stdio.h>`</br>

`void clearerr(FILE *stream);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to clear indicators on a stream. The `clearerr()` function shall clear the end-of-file and error
indicators for the stream to which _stream_ points.
The `clearerr()` function shall not change the setting of `errno` if stream is valid.

## Return value

The `clearerr()` function shall not return a value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
