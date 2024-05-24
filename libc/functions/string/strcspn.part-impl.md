# strcspn

## Synopsis

`#include <string.h>`

`size_t strcspn(const char *s1, const char *s2);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strcspn()` function shall compute the length (in bytes) of the maximum initial segment of the string pointed to by
_s1_ which consists entirely of bytes not from the string pointed to by _s2_.

## Return value

The `strcspn()` function shall return the length of the computed segment of the string pointed to by _s1_; no return
value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
