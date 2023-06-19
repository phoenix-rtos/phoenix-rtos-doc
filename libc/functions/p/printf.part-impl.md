# Synopsis

`#include <stdio.h>`

`int dprintf(int _fildes_, const char *restrict format, ...);`

`int fprintf(FILE *restrict stream, const char *restrict format, ...);`

`int printf(const char *restrict format, ...);`

`int snprintf(char *restrict s, size_t n,`

`const char *restrict format, ...);`

`int sprintf(char *restrict s, const char *restrict format, ...);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fprintf()` function shall place output on the named output stream. The `printf()` function shall place output on
the standard output stream stdout. The `sprintf()` function shall place output followed by the null byte, `\0`, in
consecutive bytes starting at *s; it is the user's responsibility to ensure that enough space is available.

 The `dprintf()` function shall be equivalent to the `fprintf()` function, except that `dprintf()` shall write output
 to the file associated with the file descriptor specified by the _fildes_ argument rather than place output on a
 stream.

The `snprintf()` function shall be equivalent to `sprintf()`, with the addition of the `n` argument which states the
size of the buffer referred to by s. If `n` is zero, nothing shall be written and `s` may be a null pointer. Otherwise,
output bytes beyond the `n-1st` shall be discarded instead of being written to the array, and a `null` byte is written
at the end of the bytes actually written into the array.

If copying takes place between objects that overlap as a result of a call to `sprintf()` or `snprintf()`, the results
are undefined.

Each of these functions converts, formats, and prints its arguments under control of the _format_. The _format_ is a
character string, beginning and ending in its initial shift state, if any. The _format_ is composed of zero or more
directives: ordinary characters, which are simply copied to the output stream, and conversion specifications, each of
which shall result in the fetching of zero or more arguments. The results are undefined if there are insufficient
arguments for the _format_. If the _format_ is exhausted while arguments remain, the excess arguments shall be evaluated
but are otherwise ignored.

 Conversions can be applied to the `nth` argument after the _format_ in the argument list, rather than to the next
 unused argument. In this case, the conversion specifier character `%` (see below) is replaced by the sequence `%n$`,
 where `n` is a decimal integer in the range `[1,NL_ARGMA]`, giving the position of the argument in the argument list.
 This feature provides for the definition of format strings that select arguments in an order appropriate to specific
 languages.

The format can contain either numbered argument conversion specifications (that is, `%n$` and `*m$`), or unnumbered
argument conversion specifications (that is, `%` and `*`), but not both. The only exception to this is that `%%` can
be mixed with the `%n$` form. The results of mixing numbered and unnumbered argument specifications in a format string
are undefined. When numbered argument specifications are used, specifying the `Nth` argument requires that all the
leading arguments, from the first to the `(N-1)th`, are specified in the format string.

In format strings containing the `%n$` form of conversion specification, numbered arguments in the argument list can be
referenced from the format string as many times as required.

In format strings containing the `%` form of conversion specification, each conversion specification uses the first
unused argument in the argument list.

 All forms of the `fprintf()` functions allow for the insertion of a language-dependent `radix` character in the output
 string. The `radix` character is defined in the current locale (category `LC_NUMERIC`). In the POSIX locale, or in a
 locale where the `radix` character is not defined, the `radix` character shall default to a `<period>` (`.`).

Each conversion specification is introduced by the `%` character or by the character sequence `%n$`, after which
the following appear in sequence:

* Zero or more flags (in any order), which modify the meaning of the conversion specification.

* An optional minimum field width. If the converted value has fewer bytes than the field width, it shall be padded with
 `<space>` characters by default on the left; it shall be padded on the right if the left-adjustment flag (`-`),
 described below, is given to the field width. The field width takes the form of a `<asterisk>` (`*`), described
 below, or a decimal integer.

An optional precision that gives the minimum number of digits to appear for the `d`, `i`, `o`, `u`, `x`, and `X`
conversion specifiers; the number of digits to appear after the `radix` character for the `a`, `A`, `e`, `E`, `f`, and
`F` conversion specifiers; the maximum number of significant digits for the `g` and `G` conversion specifiers; or the
maximum number of bytes to be printed from a string in the `s` and `S` conversion specifiers. The precision takes
the form of a `<period>` (`.`) followed either by a `<asterisk>` (`*`), described below, or an optional decimal
digit string, where a `null` digit string is treated as zero. If a precision appears with any other conversion
specifier, the behavior is undefined.

An optional length modifier that specifies the size of the argument.

A conversion specifier character that indicates the type of conversion to be applied.

A field width, or precision, or both, may be indicated by a `<asterisk>` (`*`). In this case an argument of type int
supplies the field width or precision. Applications shall ensure that arguments specifying field width, or precision,
or both appear in that order before the argument, if any, to be converted. A negative field width is taken as a `-`
flag followed by a positive field width. A negative precision is taken as if the precision were omitted. In format
strings containing the `%n$` form of a conversion specification, a field width or precision may be indicated by the
sequence `*m$`, where `m` is a decimal integer in the range `[1,NL_ARGMA]` giving the position in the argument list
(after the format argument) of an integer argument containing the field width or precision, for example:

    `printf("%1$d:%2$.*3$d:%4$.*3$d\n", hour, min, precision, sec);`

The flag characters and their meanings are:

* __`'`__ \(The `<apostrophe>`\)
The integer portion of the result of a decimal conversion (`%i`, `%d`, `%u`, `%f`, `%F`, `%g`, or `%G`) shall be
formatted with thousands' grouping characters. For other conversions the behavior is undefined. The non-monetary
grouping character is used.

* __`-`__ -
The result of the conversion shall be left-justified within the field. The conversion is right-justified if this flag is
not specified.

* __`+`__ -
The result of a signed conversion shall always begin with a sign (`+` or `-`). The conversion shall begin with a sign
only when a negative value is converted if this flag is not specified.

* __`<space>`__
If the first character of a signed conversion is not a sign or if a signed conversion results in no characters, a
`<space>` shall be prefixed to the result. This means that if the `<space>` and `+` flags both appear, the `<space>`
flag shall be ignored.

* __`#`__
Specifies that the value is to be converted to an alternative form. For `o` conversion, it shall increase the precision,
if and only if necessary, to force the first digit of the result to be a zero (if the value and precision are both `0`,
a single `0` is printed). For `x` or `X` conversion specifiers, a non-zero result shall have `0x` (or `0X`) prefixed to
it. For `a`, `A`, `e`, `E`, `f`, `F`, `g`, and `G` conversion specifiers, the result shall always contain a `radix`
character, even if no digits follow the `radix` character. Without this flag, a `radix` character appears in the result
of these conversions only if a digit follows it. For `g` and `G` conversion specifiers, trailing zeros shall not be
removed from the result as they normally are. For other conversion specifiers, the behavior is undefined.

* __`0`__
For `d`, `i`, `o`, `u`, `x`, `X`, `a`, `A`, `e`, `E`, `f`, `F`, `g`, and `G` conversion specifiers, leading zeros
(following any indication of sign or base) are used to pad to the field width rather than performing space padding,
except when converting an infinity or `NaN`. If the `0` and `-` flags both appear, the `0` flag is ignored. For `d`,
`i`, `o`, `u`, `x`, and `X` conversion specifiers, if a precision is specified, the `0` flag shall be ignored.
If the `0` and `<apostrophe>` flags both appear, the grouping characters are inserted before zero padding. For other
conversions, the behavior is undefined.

The length modifiers and their meanings are:

* `hh` -
Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a signed char or unsigned
char argument (the argument will have been promoted according to the integer promotions, but its value shall be
converted to signed char or unsigned char before printing); or that a following `n` conversion specifier applies
to a pointer to a signed char argument.

* `h` -
Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a short or unsigned short
argument (the argument will have been promoted according to the integer promotions, but its value shall be converted
to short or unsigned short before printing); or that a following `n` conversion specifier applies to a pointer to a
short argument.

* `l (ell)` -
Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a long or unsigned long
argument; that a following `n` conversion specifier applies to a pointer to a long argument; that a following `c`
conversion specifier applies to a `wint_t` argument; that a following `s` conversion specifier applies to a pointer
to a `wchar_t` argument; or has no effect on a following `a`, `A`, `e`, `E`, `f`, `F`, `g`, or `G` conversion specifier.

* `ll (ell-ell)` -
Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `long long` or `unsigned
long long` argument; or that a following `n` conversion specifier applies to a pointer to a `long long` argument.

* `j` -
Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `intmax_t` or `uintmax_t`
argument; or that a following `n` conversion specifier applies to a pointer to a `intmax_t` argument.

* `z` -
Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `size_t` or the
corresponding signed integer type argument; or that a following `n` conversion specifier applies to a pointer to a
signed integer type corresponding to a `size_t` argument.

* `t` -
Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `ptrdiff_t` or the
corresponding unsigned type argument; or that a following `n` conversion specifier applies to a pointer to a
`ptrdiff_t` argument.

* `L` -
Specifies that a following `a`, `A`, `e`, `E`, `f`, `F`, `g`, or `G` conversion specifier applies to a long double
argument.

If a length modifier appears with any conversion specifier other than as specified above, the behavior is undefined.

The conversion specifiers and their meanings are:

* `d`, `i` -
The int argument shall be converted to a signed decimal in the style `[-]dddd`. The precision specifies the minimum
number of digits to appear; if the value being converted can be represented in fewer digits, it shall be expanded with
leading zeros. The default precision is `1`. The result of converting zero with an explicit precision of zero shall be
no characters.

* `o` -
The unsigned argument shall be converted to unsigned octal format in the style `dddd`. The precision specifies the
minimum number of digits to appear; if the value being converted can be represented in fewer digits, it shall be
expanded with leading zeros. The default precision is `1`. The result of converting zero with an explicit precision
of zero shall be no characters.

* `u` -
The unsigned argument shall be converted to unsigned decimal format in the style `dddd`. The precision specifies the
minimum number of digits to appear; if the value being converted can be represented in fewer digits, it shall be
expanded with leading zeros. The default precision is `1`. The result of converting zero with an explicit precision of
zero shall be no characters.

* `x` -
The unsigned argument shall be converted to unsigned hexadecimal format in the style `dddd`; the letters `abcdef` are
used. The precision specifies the minimum number of digits to appear; if the value being converted can be represented
in fewer digits, it shall be expanded with leading zeros. The default precision is `1`. The result of converting zero
with an explicit precision of zero shall be no characters.

* `X` -
Equivalent to the x conversion specifier, except that letters `ABCDEF` are used instead of `abcdef`.

* `f`, `F` -
The double argument shall be converted to decimal notation in the style `[-]ddd.ddd`, where the number of digits after
the `radix` character is equal to the precision specification. If the precision is missing, it shall be taken as `6`; if
the precision is explicitly zero and no `#` flag is present, no `radix` character shall appear. If a `radix` character
appears, at least one digit appears before it. The low-order digit shall be rounded in an implementation-defined manner.
A double argument representing an infinity shall be converted in one of the styles `[-]inf` or `[-]infinity`; which
style is implementation-defined. A double argument representing a `NaN` shall be converted in one of the styles
`[-]nan(n-char-sequence)` or `[-]nan`; which style, and the meaning of any n-char-sequence, is implementation-defined.
The `F` conversion specifier produces `INF`, `INFINITY`, or `NAN` instead of `inf`, `infinity`, or `nan`, respectively.

* `e, E` -
The double argument shall be converted in the style `[-]d.ddde±dd`, where there is one digit before the `radix`
character (which is non-zero if the argument is non-zero) and the number of digits after it is equal to the precision;
if the precision is missing, it shall be taken as `6`; if the precision is zero and no '#' flag is present, no `radix`
character shall appear. The low-order digit shall be rounded in an implementation-defined manner. The `E` conversion
specifier shall produce a number with `E` instead of `e` introducing the exponent. The exponent shall always contain
at least two digits. If the value is zero, the exponent shall be zero.
A double argument representing an infinity or `NaN` shall be converted in the style of a `f` or `F` conversion
specifier.

* `g`, `G`
The double argument representing a floating-point number shall be converted in the style `f` or `e` (or in the style `F`
or `E` in the case of a `G` conversion specifier), depending on the value converted and the precision. Let `P` equal the
precision if non-zero, `6` if the precision is omitted, or `1` if the precision is zero. Then, if a conversion with
style `E` would have an exponent of `X`:
\- If `P > X>=-4`, the conversion shall be with style `f` (or `F`) and precision `P-(X+1)`.
\- Otherwise, the conversion shall be with style `e` (or `E`) and precision `P-1`.
Finally, unless the `#` flag is used, any trailing zeros shall be removed from the fractional portion of the result and
the decimal-point character shall be removed if there is no fractional portion remaining.
A double argument representing an infinity or `NaN` shall be converted in the style of a `f` or `F` conversion
specifier.

* `a`, `A` -
A double argument representing a floating-point number shall be converted in the style `[-]0xh.hhhhp±d`, where there is
one hexadecimal digit (which shall be non-zero if the argument is a normalized floating-point number and is otherwise
unspecified) before the decimal-point character and the number of hexadecimal digits after it is equal to the precision;
if the precision is missing and `FLT_RADIX` is a power of `2`, then the precision shall be sufficient for an exact
representation of the value; if the precision is missing and `FLT_RADIX` is not a power of `2`, then the precision shall
be sufficient to distinguish values of type double, except that trailing zeros may be omitted; if the precision is zero
and the `#` flag is not specified, no decimal-point character shall appear. The letters `abcdef` shall be used for a
conversion and the letters `ABCDEF` for A conversion. The `A` conversion specifier produces a number with `X` and `P`
instead of `x` and `p`. The exponent shall always contain at least one digit, and only as many more digits as necessary
to represent the decimal exponent of `2`. If the value is zero, the exponent shall be zero.
A double argument representing an infinity or `NaN` shall be converted in the style
of a `f` or `F` conversion specifier.

* `c` -
The int argument shall be converted to a `unsigned char`, and the resulting byte shall be written.
If a `l (ell)` qualifier is present, the `wint_t` argument shall be converted as if by a `ls` conversion specification
with no precision and an argument that points to a two-element array of type `wchar_t,` the first element of which
contains the `wint_t` argument to the `ls` conversion specification and the second element contains a `null` wide
character.

* `s` -
The argument shall be a pointer to an array of `char`. Bytes from the array shall be written up to (but not including)
any terminating `null` byte. If the precision is specified, no more than that many bytes shall be written. If the
precision is not specified or is greater than the size of the array, the application shall ensure that the array
contains a `null` byte.
If a `l (ell)` qualifier is present, the argument shall be a pointer to an array of type `wchar_t`. Wide characters
from the array shall be converted to characters (each as if by a call to the `wcrtomb()` function, with the conversion
state described by a `mbstate_t` object initialized to zero before the first wide character is converted) up to and
including a terminating `null` wide character. The resulting characters shall be written up to (but not including) the
terminating `null` character (byte). If no precision is specified, the application shall ensure that the array contains
a `null` wide character. If a precision is specified, no more than that many characters (bytes) shall be written
(including shift sequences, if any), and the array shall contain a `null` wide character if, to equal the character
sequence length given by the precision, the function would need to access a wide character one past the end of the
array. In no case shall a partial character be written.

* `p` -
The argument shall be a pointer to `void`. The value of the pointer is converted to a sequence of printable characters,
in an implementation-defined manner.

* `n` -
The argument shall be a pointer to an integer into which is written the number of bytes written to the output so far by
this call to one of the `fprintf()` functions. No argument is converted.

* `C` -
Equivalent to `lc`.

* `S` -
Equivalent to `ls`.

* `%` -
Print a `%` character; no argument is converted. The complete conversion specification shall be `%%`.

If a conversion specification does not match one of the above forms, the behavior is undefined. If any argument is not
the correct type for the corresponding conversion specification, the behavior is undefined.

In no case shall a nonexistent or small field width cause truncation of a field; if the result of a conversion is wider
than the field width, the field shall be expanded to contain the conversion result. Characters generated by `fprintf()`
and `printf()` are printed as if `fputc()` had been called.

For the `a` and `A` conversion specifiers, if `FLT_RADIX` is a power of `2`, the value shall be correctly rounded to a
hexadecimal floating number with the given precision.

For `a` and `A` conversions, if `FLT_RADIX` is not a power of `2` and the result is not exactly representable in the
given precision, the result should be one of the two adjacent numbers in hexadecimal floating style with the given
precision, with the extra stipulation that the error should have a correct sign for the current rounding direction.

For the `e`, `E`, `f`, `F`, `g`, and `G` conversion specifiers, if the number of significant decimal digits is at most
`DECIMAL_DIG,` then the result should be correctly rounded. If the number of significant decimal digits is more than
`DECIMAL_DIG`, but the source value is exactly representable with `DECIMAL_DIG` digits, then the result should be an
exact representation with trailing zeros. Otherwise, the source value is bounded by two adjacent decimal strings
`L < U`, both having `DECIMAL_DIG` significant digits; the value of the resultant decimal string `D` should satisfy
`L <= D <= U`, with the extra stipulation that the error should have a correct sign for the current rounding direction.

 The last data modification and last file status change timestamps of the file shall be marked for update:

* Between the call to a successful execution of `fprintf()` or `printf()` and the next successful completion of a call
to `fflush()` or `fclose()` on the same stream or a call to `exit()` or `abort()`

* Upon successful completion of a call to `dprintf()`

## Return value

Upon successful completion, the `dprintf()`, `fprintf()`, and `printf()` functions shall return the number of bytes
transmitted.

Upon successful completion, the `sprintf()` function shall return the number of bytes written to _s_, excluding the
terminating `null` byte.

Upon successful completion, the `snprintf()` function shall return the number of bytes that would be written to _s_
had `n` been sufficiently large excluding the terminating `null` byte.

If an output error was encountered, these functions shall return a negative value and set `errno` to indicate the
error.

If the value of `n` is zero on a call to `snprintf()`, nothing shall be written, the number of bytes that would have
been written had `n` been sufficiently large excluding the terminating `null` shall be returned, and _s_ may be a
`null` pointer.

## Errors

For the conditions under which `dprintf()`, `fprintf()`, and `printf()` fail and may fail, refer to `fputc()` or
`fputwc()`.

In addition, all forms of `fprintf()` shall fail if:

* [`EILSEQ`] - A wide-character code that does not correspond to a valid character has been detected.

* [`EOVERFLOW`] - The value to be returned is greater than `INT_MA`.

The `dprintf()` function may fail if:

* [`EBADF`] - The _fildes_ argument is not a valid file descriptor.

The `dprintf()`, `fprintf()`, and `printf()` functions may fail if:

* [`ENOMEM`] - Insufficient storage space is available.

The `snprintf()` function shall fail if:

* [`EOVERFLOW`] - The value of `n` is greater than `INT_MA`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
