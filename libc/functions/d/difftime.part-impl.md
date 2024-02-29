# difftime

## Synopsis

`#include <time.h>`</br>

`double difftime(time_t time1, time_t time0);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `difftime()` function shall compute the difference between two calendar times
(as returned by `time()`): _time1_ - _time0_.

## Return value

The `difftime()` function shall return the difference expressed in seconds as a type double.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
