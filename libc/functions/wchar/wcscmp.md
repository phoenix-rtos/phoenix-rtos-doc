# wcscmp

## Synopsis

`#include <wchar.h>`

`int wcscmp(const wchar_t *ws1, const wchar_t *ws2);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `wcscmp()` function shall compare the wide-character string pointed to by _`ws1`_ to the wide-character string
pointed to by _`ws2`_.

The sign of a non-zero return value shall be determined by the sign of the difference between the values of the first
pair of wide-character codes that differ in the objects being compared.

## Return value

Upon completion, `wcscmp()` shall return an integer greater than, equal to, or less than 0, if the wide-character string
pointed to by _`ws1`_ is greater than, equal to, or less than the wide-character string pointed to by _`ws2`_,
respectively.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
