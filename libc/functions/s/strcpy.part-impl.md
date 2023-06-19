# Synopsis

`#include <string.h>`

`char *stpcpy(char *restrict s1, const char *restrict s2);`

`char *strcpy(char *restrict s1, const char *restrict s2);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `stpcpy()` and `strcpy()` functions shall copy the
string pointed to by _s2_ (including the terminating `NUL` character) into the array pointed to by _s1_.
If copying takes place between objects that overlap, the behavior is undefined.

## Return value

The
`stpcpy()` function shall return a pointer to the terminating `NUL` character copied into the _s1_ buffer.
The `strcpy()` function shall return _s1_.
No return values are reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
