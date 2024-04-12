# wcstombs

## Synopsis

`#include <stdlib.h>`

`size_t wcstombs(char *str, const wchar_t *pwcs, size_t n);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

`wcstombs()` - convert a wide-character string to a character string

The `wcstombs()` function shall convert the sequence of wide-character codes that are in the array pointed to by _pwcs_
into a sequence of characters that begins in the initial shift state and store these characters into the array pointed
to by _s_, stopping if a character would exceed the limit of _n_ total bytes or if a null byte is stored.
Each wide-character code shall be converted as if by a call to `wctomb()`, except that the shift state of `wctomb()`
shall not be affected.

The behavior of this function shall be affected by the `LC_CTYPE` category of the current locale.

No more than _n_ bytes shall be modified in the array pointed to by _s_. If copying takes place between objects that
overlap, the behavior is undefined. If _s_ is a `null` pointer, `wcstombs()` shall return the length required to
convert the entire array regardless of the value of _n_, but no values are stored.

## Return value

If a wide-character code is encountered that does not correspond to a valid character (of one or more bytes each),
`wcstombs()` shall return `(size_t)-1`. Otherwise, `wcstombs()` shall return the number of bytes stored in the
character array, not including any terminating `null` byte. The array shall not be `null`-terminated if the value
returned is _n_.

## Errors

The `wcstombs()` function shall fail if:

* `EILSEQ` - a wide-character code does not correspond to a valid character.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
