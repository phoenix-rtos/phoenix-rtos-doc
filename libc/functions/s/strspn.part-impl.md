# Synopsis

`#include <string.h>`

`size_t strspn(const char *s1, const char *s2);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strspn()` function shall compute the length (in bytes) of the maximum initial segment of the string pointed to by
_s1_ which consists entirely of bytes from the string pointed to by _s2_.

## Return value

The `strspn()` function shall return the computed length; no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
