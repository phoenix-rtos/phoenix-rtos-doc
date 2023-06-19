# Synopsis

`#include <stdlib.h>`

`unsigned long strtoul(const char *restrict str, char **restrict endptr, int base);`

`unsigned long long strtoull(const char *restrict str, char **restrict endptr, int base);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall convert the initial portion of the string pointed to by _str_ to a type `unsigned long` and
`unsigned long long` representation, respectively. First, they decompose the input string into three parts:

* An initial, possibly empty, sequence of white-space characters (as specified by `isspace()`)

* A subject sequence interpreted as an integer represented in some `radix` determined by the value of _base_

* A final string of one or more unrecognized characters, including the terminating `NUL` character of the input string

Then they shall attempt to convert the subject sequence to an unsigned integer, and return the result.

If the value of _base_ is 0, the expected form of the subject sequence is that of a decimal constant, octal constant, or
hexadecimal constant, any of which may be preceded by a `+` or `-` sign. A decimal constant begins with a
non-zero digit, and consists of a sequence of decimal digits. An octal constant consists of the prefix `0` optionally
followed by a sequence of the digits `0` to `7` only. A hexadecimal constant consists of the prefix `0x` or `0X`
followed by a sequence of the decimal digits and letters `a` (or `A`) to `f` (or `F`) with
values `10` to `15` respectively.

If the value of _base_ is between `2` and `36`, the expected form of the subject sequence is a sequence of letters and
digits representing an integer with the radix specified by _base_, optionally preceded by a `+` or `-` sign. The letters
from `a` (or `A`) to `z` (or `Z`) inclusive are ascribed the values `10` to `35`; only letters whose ascribed values are
less than that of _base_ are permitted. If the value of _base_ is `16`, the characters `0x` or `0X` may optionally
precede the sequence of letters and digits, following the sign if present.

The subject sequence is defined as the longest initial subsequence of the input string, starting with the first
non-white-space character that is of the expected form. The subject sequence shall contain no characters if the input
string is empty or consists entirely of white-space characters, or if the first non-white-space character is other than
a sign or a permissible letter or digit.

If the subject sequence has the expected form and the value of _base_ is `0`, the sequence of characters starting with
the first digit shall be interpreted as an integer constant. If the subject sequence has the expected form and the value
of _base_ is between `2` and `36`, it shall be used as the base for conversion, ascribing to each letter its value as
given above. If the subject sequence begins with a `<hyphen-minus>`, the value resulting from the conversion shall be
negated. A pointer to the final string shall be stored in the object pointed to by _endptr_, provided that _endptr_ is
not a `null` pointer.

In other than the C or POSIX locale, additional
locale-specific subject sequence forms may be accepted.
If the subject sequence is empty or does not have the expected form, no conversion shall be performed; the value of
 _str_ shall be stored in the object pointed to by _endptr_, provided that _endptr_ is not a `null` pointer.

These functions shall not change the setting of `errno` if successful.

Since `0`, ``ULONG_MAX`, and`ULLONG_MAX` are returned on error and are also valid returns on success, an application
wishing to check for error situations should set `errno` to 0, then call `strtoul()` or
`strtoull()`, then check`errno`.

## Return value

Upon successful completion, these functions shall return the converted value, if any. If no conversion could be
performed, `0` shall be returned and `errno` may be set to `EINVAL`.

If the value of _base_ is not supported, 0 shall be returned and `errno` shall be set to `EINVAL`.

If the correct value is outside the range of representable values, `ULONG_MAX` or `ULLONG_MAX` shall be returned and
`errno` set to `ERANG`.

## Errors

These functions shall fail if:

* `EINVAL` -  
The value of _base_ is not supported.

* `ERANGE` - The value to be returned is not representable.

These functions may fail if:

* `EINVAL` - No conversion could be performed.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
