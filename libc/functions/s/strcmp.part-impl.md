# Synopsis

`#include <string.h>`

`int strcmp(const char *s1, const char *s2);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strcmp()` function shall compare the string pointed to by _s1_ to the string pointed to by _s2_.
The sign of a non-zero return value shall be determined by the sign of the difference between the values of the first
pair of bytes (both interpreted as type unsigned char) that differ in the strings being compared.

## Return value

Upon completion, `strcmp()` shall return an integer greater than, equal to, or less than `0`, if the string pointed
to by _s1_ is greater than, equal to, or less than the string pointed to by _s2_, respectively.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
