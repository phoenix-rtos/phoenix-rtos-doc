# Synopsis

`#include <ctype.h>`

`int isblank(int c);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `isblank()` function shall test whether _c_ is a character of class _blank_ in the current locale.

The _c_ argument is a type `int`, the value of which the application shall ensure is a character representable as an
`unsigned char` or equal to the value of the macro `EOF`. If the argument has any other value, the behavior is
undefined.

## Return value

The `isblank()` function shall return non-zero if _c_ is a `<blank>`, otherwise shall return `0`.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
