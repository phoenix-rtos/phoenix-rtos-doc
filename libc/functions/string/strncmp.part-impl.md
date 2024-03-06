# strncmp

## Synopsis

`#include <string.h>`

`int strncmp(const char *s1, const char *s2, size_t n);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strncmp()` function shall compare not more than _n_ bytes (bytes that follow a `NULL` character are not compared)
from the array pointed to by _s1_ to the array pointed to by _s2_.
The sign of a non-zero return value is determined by the sign of the difference between the values of the first pair of
bytes (both interpreted as type `unsigned char`) that differ in the strings being compared.

## Return value

Upon successful completion, `strncmp()` shall return an integer greater than, equal to, or less than `0`, if the
possibly null-terminated array pointed to by _s1_ is greater than, equal to, or less than the possibly null-terminated
array pointed to by _s2_ respectively.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
