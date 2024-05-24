# memset

## Synopsis

`#include <string.h>`

`void *memset(void *s, int c, size_t n);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `memset()` function shall copy _c_ (converted to an unsigned char) into each of the first _n_ bytes of the object
pointed to by _s_.

## Return value

The `memset()` function shall return _s_; no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
