# Synopsis

`#include <string.h>`

`void *memccpy(void *restrict s1, const void *restrict s2, int c, size_t n)`;

## Status

Not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `memccpy()` function shall copy bytes from memory area _s2_ into _s1_, stopping after the first occurrence of byte
_c_ (converted to a `unsigned char`) is copied, or after _n_ bytes are copied, whichever comes first. If copying takes
place between objects that overlap, the behavior is undefined.

## Return value

The `memccpy()` function shall return a pointer to the byte after the copy of _c_ in _s1_, or a `null` pointer if _c_
was not found in the first _n_ bytes of _s2_.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
