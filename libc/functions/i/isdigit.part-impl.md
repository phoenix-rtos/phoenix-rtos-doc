# Synopsis

`#include <ctype.h>`

`int isdigit(int c);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `isdigit()` function shall test whether _c_ is a character of class _digit_ in the current locale.

The _c_ argument is an `int`, the value of which the application shall ensure is a character representable as an
`unsigned char` or equal to the value of the macro `EOF`. If the argument has any other value, the behavior is
undefined.

## Return value

The `isdigit()` function shall return non-zero if _c_ is decimal digit, otherwise shall return `0`.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
