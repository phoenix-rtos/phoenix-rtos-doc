# strncpy

## Synopsis

`#include <string.h>`

`char *stpncpy(char *restrict s1, const char *restrict s2, size_t n);`

`char *strncpy(char *restrict s1, const char *restrict s2, size_t n);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`stpncpy()` and `strncpy()` functions shall copy not more than _n_ bytes (bytes that follow a `NULL` character are not
copied) from the array pointed to by _s2_ to the array pointed to by _s1_.

If the array pointed to by _s2_ is a string that is shorter than _n_ bytes, `NULL` characters shall be appended to the
copy in the array pointed to by _s1_, until _n_ bytes in all are written.

If copying takes place between objects that overlap, the behavior is undefined.

## Return value

If a `NULL` character is written to the destination, the `stpncpy()` function shall return the address of the first such
`NULL` character. Otherwise, it shall return `&s1[n]`.

The `strncpy()` function shall return _s1_.

No return values are reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
