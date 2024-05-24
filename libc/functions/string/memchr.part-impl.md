# memchr

## Synopsis

`#include <string.h>`

`void *memchr(const void *s, int c, size_t n);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `memchr()` function shall locate the first occurrence of _c_ (converted to an unsigned char) in the initial _n_
bytes (each interpreted as unsigned char) pointed to by s.

Implementations shall behave as if they read the memory byte by byte from the beginning of the bytes pointed to by s
and stop at the first occurrence of _c_ (if it is found in the initial n bytes).

## Return value

The `memchr()` function shall return a pointer to the located byte, or a `null` pointer if the byte is not found.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
