# strncat

## Synopsis

`#include <string.h>`

`char *strncat(char *restrict s1, const char *restrict s2, size_t n);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strncat()` function shall append not more than _n_ bytes (a `NULL` character and bytes that follow it are not
appended) from the array pointed to by _s2_ to the end of the string pointed to by _s1_. The initial byte of _s2_
overwrites the `NULL` character at the end of _s1_. A terminating `NULL` character is always appended to the result. If
copying takes place between objects that overlap, the behavior is undefined.

## Return value

The `strncat()` function shall return _s1_; no return value shall be reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
