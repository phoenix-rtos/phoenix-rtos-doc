# strtod

## Synopsis

```c
#include <stdlib.h>

double strtod(const char *restrict nptr, char **restrict endptr);

float strtof(const char *restrict nptr, char **restrict endptr);

long double strtold(const char *restrict nptr, char **restrict endptr);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall convert the initial portion of the string pointed to by _nptr_ to `double`, `float`, and
`long double` representation, respectively. First, they decompose the input string into three parts:

* An initial, possibly empty, sequence of white-space characters (as specified by `isspace()`)

* A subject sequence interpreted as a floating-point constant or representing infinity or `NaN`

* A final string of one or more unrecognized characters, including the terminating `NULL` character of the input string

Then they shall attempt to convert the subject sequence to a floating-point number, and return the result.

The expected form of the subject sequence is an optional `+` or `-` sign, then one of the following:

* A non-empty sequence of decimal digits optionally containing a `radix` character; then an optional exponent part
consisting of the character `e` or the character `E`, optionally followed by a `+` or `-` character, and then
 followed by one or more decimal digits

* A `0x` or `0X`, then a non-empty sequence of hexadecimal digits optionally containing a radix character; then an
optional binary exponent part consisting of the character `p` or the character `P`, optionally followed by a `+` or `-`
character, and then followed by one or more decimal digits

* One of `INF` or `INFINITY`, ignoring case

* One of `NaN` or `NaN(n-char-sequenceopt)`, ignoring case in the `NaN` part, where:

```c
n-char-sequence:
    digit
    nondigit
    n-char-sequence digit
    n-char-sequence nondigit
```

The subject sequence is defined as the longest initial subsequence of the input string, starting with the first
non-white-space character, that is of the expected form. The subject sequence contains no characters if the input string
is not of the expected form.

If the subject sequence has the expected form for a floating-point number, the sequence of characters starting with the
first digit or the decimal-point character (whichever occurs first) shall be interpreted as a floating constant of the C
language, except that the `radix` character shall be used in place of a period, and that if neither an exponent part nor
a `radix` character appears in a decimal floating-point number, or if a binary exponent part does not appear in a
hexadecimal floating-point number, an exponent part of the appropriate type with value zero is assumed to follow the
last digit in the string. If the subject sequence begins with a `<hyphen-minus>`, the sequence shall be interpreted as
negated. A character sequence `INF` or `INFINITY` shall be interpreted as an infinity, if representable in the return
type, else as if it were a floating constant that is too large for the range of the return type. A character sequence
`NaN` or `NaN(n-char-sequenceopt)` shall be interpreted as a quiet `NaN`, if supported in the return type, else as if it
were a subject sequence part that does not have the expected form; the meaning of the n-char sequences is
implementation-defined. A pointer to the final string is stored in the object pointed to by _endptr_, provided that
_endptr_ is not a `null` pointer.

If the subject sequence has the hexadecimal form and `FLT_RADIX` is a power of 2, the value resulting from the
conversion is correctly rounded.

The
`radix` character is defined in the current locale (category `LC_NUMERIC`). In the POSIX locale, or in a locale where
the `radix` character is not defined, the `radix` character shall default to a `<period>` (`.`).

In other than the C or POSIX locale, additional
locale-specific subject sequence forms may be accepted.

If the subject sequence is empty or does not have the expected form, no conversion shall be performed; the value of nptr
is stored in the object pointed to by _endptr_, provided that _endptr_ is not a `null` pointer.

These functions shall not change the setting of `errno` if successful.
Since `0` is returned on error and is also a valid return on success, an application wishing to check for error
situations should set `errno` to `0`, then call `strtod()`, `strtof()`, or `strtold()`, then check `errno`.

## Return value

Upon successful completion, these functions shall return the converted value. If no conversion could be performed, `0`
shall be returned, and `errno` may be set to `EINVAL`.

If the correct value is outside the range of representable values, `±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` shall be
returned (according to the sign of the value), and errno shall be set to `ERANGE`.

If the correct value would cause an underflow, a value whose magnitude is no greater than the smallest normalized
positive number in the return type shall be returned and `errno` set to `ERANGE`.

## Errors

These functions shall fail if:

* `ERANGE` - The value to be returned would cause overflow or underflow.

These functions may fail if:

* `EINVAL` - No conversion could be performed.

## Tests

Untested

## Known bugs

None
