###Synopsis

`#include <stdio.h>`
`#include <wchar.h>`

`int fwprintf(FILE *restrict stream, const wchar_t *restrict format, ...);`
`int swprintf(wchar_t *restrict ws, size_t n,
       const wchar_t *restrict format, ...);`
`int wprintf(const wchar_t *restrict format, ...);`

###Description

The functions print formatted wide-character output.

Arguments:
<u>stream</u> - the output stream,
<u>format</u> - a character string defining output format.

<u>ws</u> - a character table, to which the resulting formatted wide character string is put,
<u>n</u> - the size of the buffer,

The `fwprintf()` function places output on the named output <u>stream</u>. 

The `swprintf()` function places output followed by the null byte, '\0', in consecutive bytes starting at *<u>ws</u>.  No more than <u>n</u> wide characters are written, including a terminating null wide character, which is always added (unless <u>n</u> is zero).

The `wprintf()` function places output on the standard output stream `stdout`. 

Each of these functions converts, formats, and prints its arguments under control of the <u>format</u> wide-character string. The <u>format</u>. The <u>format</u> is composed of zero or more directives: ordinary wide-characters, which are simply copied to the output stream, and conversion specifications, each of which results in the fetching of zero or more arguments. The results are undefined if there are insufficient arguments for the <u>format</u>. If the <u>format</u> is exhausted while arguments remain, the excess arguments are evaluated but are otherwise ignored.

Conversions can be applied to the nth argument after the format in the argument list, rather than to the next unused argument. In this case, the conversion specifier wide-character `%` (see below) is replaced by the sequence `"%n$"`, where `n` is a decimal integer in the range `[1,{NL_ARGMAX}]`, giving the position of the argument in the argument list. This feature provides for the definition of <u>format</u> wide-character strings that select arguments in an order appropriate to specific languages.

The <u>format</u> can contain either numbered argument conversion specifications (that is, `"%n$"` and `"*m$"`), or unnumbered argument conversion specifications (that is, `%` and `*` ), but not both. The only exception to this is that `%%` can be mixed with the `"%n$"` form. The results of mixing numbered and unnumbered argument specifications in a <u>format</u> wide-character string are undefined. When numbered argument specifications are used, specifying the `Nth` argument requires that all the leading arguments, from the first to the `(N-1)`th, are specified in the <u>format</u> wide-character string.

In <u>format</u> strings containing the `"%n$"` form of conversion specification, numbered arguments in the argument list can be referenced from the <u>format</u> wide-character string as many times as required.

In <u>format</u> strings containing the `%` form of conversion specification, each conversion specification uses the first unused argument in the argument list.

All forms of the `fwprintf()` functions allow for the insertion of a locale-dependent radix character in the output string. The radix character is defined in the current locale (category `LC_NUMERIC`). In the POSIX locale, or in a locale where the radix character is not defined, the radix character defaults to a <period> ( `'.'` ). 

Each conversion specification is introduced by the `'%'` character or by the wide-character sequence `"%n$"`, after which the following appear in sequence:

 * Zero or more flags (in any order), which modify the meaning of the conversion specification.

 * An optional minimum field width. If the converted value has fewer wide characters than the field width, it is padded with <space> characters by default on the left; it is padded on the right if the left-adjustment flag ( `'-'` ), described below, is given to the field width. The field width takes the form of an <asterisk> ( `'*'` ), described below, or a decimal integer.

 * An optional precision that gives the minimum number of digits to appear for the `d`, `i`, `o`, `u`, `x`, and `X` conversion specifiers; the number of digits to appear after the radix character for the `a`, `A`, `e`, `E`, `f`, and `F` conversion specifiers; the maximum number of significant digits for the `g` and `G` conversion specifiers; or the maximum number of bytes to be printed from a string in the `s` and `S` conversion specifiers. The precision takes the form of a <period> ( `'.'` ) followed either by an <asterisk> ( `'*'` ), described below, or an optional decimal digit string, where a null digit string is treated as zero. If a precision appears with any other conversion specifier, the behaviour is undefined.

 * An optional length modifier that specifies the size of the argument.

 * A conversion specifier wide character that indicates the type of conversion to be applied.

A field width, or precision, or both, may be indicated by an <asterisk> ( `'*'` ). In this case an argument of type `int` supplies the field width or precision. Applications ensure that arguments specifying field width, or precision, or both appear in that order before the argument, if any, to be converted. A negative field width is taken as a `'-'` flag followed by a positive field width. A negative precision is taken as if the precision were omitted. In <u>format</u> strings containing the `"%n$"` form of a conversion specification, a field width or precision may be indicated by the sequence `"*m$"`, where `m` is a decimal integer in the range `[1,{NL_ARGMAX}]` giving the position in the argument list (after the <u>format</u> argument) of an integer argument containing the field width or precision, for example:

`wprintf(L"%1$d:%2$.*3$d:%4$.*3$d\n", hour, min, precision, sec);`

The flag wide characters and their meanings are:

 * `'` (The apostrophe) The integer portion of the result of a decimal conversion ( `%i`, `%d`, `%u`, `%f`, `%F`, `%g`, or `%G` ) are formatted with thousands' grouping wide characters. For other conversions the behaviour is undefined. The numeric grouping wide character is used.
 
 * `-` The result of the conversion is left-justified within the field. The conversion is right-justified if this flag is not specified.

 * `+` The result of a signed conversion always begins with a sign ( `'+'` or `'-'` ). The conversion begins with a sign only when a negative value is converted if this flag is not specified.
 
 * ` ` (space) If the first character of a signed conversion is not a sign or if a signed conversion results in no characters, a <space> is prefixed to the result. This means that if the <space> and `'+'` flags both appear, the <space> flag are ignored.
 
 * `#` Specifies that the value is to be converted to an alternative form. For `o` conversion, it increases the precision, if and only if necessary, to force the first digit of the result to be a zero (if the value and precision are both `0`, a single `0` is printed). For `x` or `X` conversion specifiers, a non-zero result has `0x` (or `0X`) prefixed to it. For `a`, `A`, `e`, `E`, `f`, `F`, `g`, and `G` conversion specifiers, the result always contains a radix character, even if no digits follow the radix character. Without this flag, a radix character appears in the result of these conversions only if a digit follows it. For `g` and `G` conversion specifiers, trailing zeros are not 
 removed from the result as they normally are. For other conversion specifiers, the behavior is undefined.

 * `0` For `d`, `i`, `o`, `u`, `x`, `X`, `a`, `A`, `e`, `E`, `f`, `F`, `g`, and `G` conversion specifiers, leading zeros (following any indication of sign or base) are used to pad to the field width rather than performing space padding, except when converting an infinity or `NaN`. If the `'0'` and `'-'` flags both appear, the `'0'` flag is ignored. For `d`, `i`, `o`, `u`, `x`, and `X` conversion specifiers, if a precision is specified, the `'0'` flag is ignored. If the `'0'` and <apostrophe> flags both appear, the grouping wide characters are inserted before zero padding. For other conversions, the behaviour is undefined.

The length modifiers and their meanings are:

  * `hh` Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `signed char` or `unsigned char` argument (the argument will have been promoted according to the integer promotions, but its value is converted to `signed char` or `unsigned char` before printing); or that a following `n` conversion specifier applies to a pointer to a `signed char` argument.
 
  * `h`  Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `short` or `unsigned short` argument (the argument will have been promoted according to the integer promotions, but its value is converted to `short` or `unsigned short` before printing); or that a following `n` conversion specifier applies to a pointer to a `short` argument.

  * `l` (`ell`) Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `long` or `unsigned long` argument; that a following `n` conversion specifier applies to a pointer to a `long` argument; that a following `c` conversion specifier applies to a `wint_t` argument; that a following s conversion specifier applies to a pointer to a `wchar_t` argument; or has no effect on a following `a`, `A`, `e`, `E`, `f`, `F`, `g`, or `G` conversion specifier.

  * `ll` (`ell`-`ell`) Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `long long` or `unsigned long long` argument; or that a following `n` conversion specifier applies to a pointer to a `long long` argument.

  * `j` Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to an `intmax_t` or `uintmax_t` argument; or that a following `n` conversion specifier applies to a pointer to an `intmax_t` argument.

  * `z` Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `size_t` or the corresponding `signed integer` type argument; or that a following `n` conversion specifier applies to a pointer to a `signed integer` type corresponding to a `size_t` argument.

  * `t` Specifies that a following `d`, `i`, `o`, `u`, `x`, or `X` conversion specifier applies to a `ptrdiff_t` or the corresponding `unsigned` type argument; or that a following `n` conversion specifier applies to a pointer to a `ptrdiff_t` argument.

  * `L` Specifies that a following `a`, `A`, `e`, `E`, `f`, `F`, `g`, or `G` conversion specifier applies to a `long double` argument.

If a length modifier appears with any conversion specifier other than as specified above, the behavior is undefined.

The conversion specifiers and their meanings are:

 * `d`, `i` The `int` argument is converted to a `signed` decimal in the style `"[-]dddd"`. The precision specifies the minimum number of digits to appear; if the value being converted can be represented in fewer digits, it is expanded with leading zeros. The default precision is `1`. The result of converting zero with an explicit precision of zero is no wide characters.

 * `o` The `unsigned` argument is converted to `unsigned` octal <u>format</u> in the style `"dddd"`. The precision specifies the minimum number of digits to appear; if the value being converted can be represented in fewer digits, it is expanded with leading zeros. The default precision is `1`. The result of converting zero with an explicit precision of zero is no wide characters.

 * `u` The `unsigned` argument is converted to `unsigned` decimal <u>format</u> in the style `"dddd"`. The precision specifies the minimum number of digits to appear; if the value being converted can be represented in fewer digits, it is expanded with leading zeros. The default precision is `1`. The result of converting zero with an explicit precision of zero is no wide characters.

 * `x` The `unsigned` argument is converted to `unsigned` hexadecimal <u>format</u> in the style `"dddd"`; the letters `"abcdef"` are used. The precision specifies the minimum number of digits to appear; if the value being converted can be represented in fewer digits, it is expanded with leading zeros. The default precision is `1`. The result of converting zero with an explicit precision of zero are no wide characters.

 * `X` Equivalent to the `x` conversion specifier, except that letters `"ABCDEF"` are used instead of `"abcdef"`.
 
 * `f`, `F` The `double` argument is converted to decimal notation in the style `"[-]ddd.ddd"`, where the number of digits after the radix character is equal to the precision specification. If the precision is missing, it is taken as `6`; if the precision is explicitly zero and no `'#'` flag is present, no radix character appears. If a radix character appears, at least one digit appears before it. The low-order digit is rounded.
      A `double` argument representing an infinity is converted in one of the styles `"[-]inf"` or `"[-]infinity"`; which style is implementation-defined. A `double` argument representing a `NaN` is converted in one of the styles `"[-]nan(n-char-sequence)"` or `"[-]nan"`; which style, and the meaning of any `n-char`-sequence, is implementation-defined. The F conversion specifier produces `"INF"`, `"INFINITY"`, or `"NAN"` instead of `"inf"`, `"infinity"`, or `"nan"`, respectively.

 * `e`, `E`  The `double` argument is converted in the style `"[-]d.dddedd"`, where there is one digit before the radix character (which is non-zero if the argument is non-zero) and the number of digits after it is equal to the precision; if the precision is missing, it is taken as `6`; if the precision is zero and no `'#'` flag is present, no radix character appears. The low-order digit is rounded. The E conversion specifier produces a number with 'E' instead of 'e' introducing the exponent. The exponent always contains at least two digits. If the value is zero, the exponent is zero.
           A `double` argument representing an infinity or `NaN` is converted in the style of an `f` or `F` conversion specifier.
 
 * `g`, `G`  The `double` argument representing a floating-point number is converted in the style `f` or `e` (or in the style `F` or `E` in the case of a `G` conversion specifier), depending on the value converted and the precision. Let `P` equal the precision if non-zero, `6` if the precision is omitted, or `1` if the precision is zero. Then, if a conversion with style `E` would have an exponent of `X`:

    * If `P > X>=-4`, the conversion is with style `f` (or `F` ) and precision `P -( X+1)`.

    * Otherwise, the conversion is with style `e` (or `E` ) and precision `P -1`.

    Finally, unless the `'#'` flag is used, any trailing zeros are removed from the fractional portion of the result and the decimal-point character is removed if there is no fractional portion remaining.

    A `double` argument representing an infinity or `NaN` is converted in the style of an `f` or `F` conversion specifier.

 * `a`, `A`  A `double` argument representing a floating-point number is converted in the style `"[-]0xh.hhhhpd"`, where there is one hexadecimal digit (which is non-zero if the argument is a normalized floating-point number and is otherwise unspecified) before the decimal-point wide character and the number of hexadecimal digits after it is equal to the precision; if the precision is missing and `FLT_RADIX` is a power of `2`, then the precision is sufficient for an exact representation of the value; if the precision is missing and `FLT_RADIX` is not a power of `2`, then the precision is sufficient to distinguish values of type `double`, except that trailing zeros may be omitted; if the precision is zero and the `'#'` flag is not specified, no decimal-point character shall appear. The letters `"abcdef"` are used for `a` conversion and the letters `"ABCDEF"` for `A` conversion. The `A` conversion specifier produces a number with `'X'` and `'P'` instead of `'x'` and `'p'`. The exponent always contains at least one digit, and only as many more digits as necessary to represent the decimal exponent of `2`. If the value is zero, the exponent is zero.

    A `double` argument representing an infinity or `NaN` is converted in the style of an `f` or `F` conversion specifier.

 * `c` If no `l` (`ell`) qualifier is present, the `int` argument is converted to a wide character as if by calling the `btowc()` function and the resulting wide character is written. Otherwise, the `wint_t` argument is converted to `wchar_t`, and written.

 * `s`  If no `l` (`ell`) qualifier is present, the application ensures that the argument is a pointer to a character array containing a character sequence beginning in the initial shift state. Characters from the array are converted as if by repeated calls to the `mbrtowc()` function, with the conversion state described by an `mbstate_t` object initialized to zero before the first character is converted, and written up to (but not including) the terminating null wide character.  If the precision is specified, no more than that many wide characters are written. If the precision is not specified or is greater than the size of the array, the application ensures that the array contains a null wide character.

      If an `l` (`ell`) qualifier is present, the argument is a pointer to an array of type `wchar_t`. Wide characters from the array are written up to (but not including) a terminating null wide character. If no precision is specified, or is greater than the size of the array, the application ensures that the array contains a null wide character. If a precision is specified, no more than that many wide characters are written.

 * `p`  The application ensures that the argument is a pointer to `void`. The value of the pointer is converted to a sequence of printable characters.

 * `n`  The application ensures that the argument is a pointer to an `integer` into which is written the number of wide characters written to the output so far by this call to one of the `fwprintf()` functions. No argument is converted, but one is consumed.

 * `C`  Equivalent to `lc`.

 * `S`  Equivalent to `ls`.
 
 * `%`  Output a `'%'` wide character; no argument is converted. The complete conversion specification is `%%`.

If a conversion specification does not match one of the above forms, the behaviour is undefined.

In no case a nonexistent or small field width causes truncation of a field; if the result of a conversion is wider than the field width, the field is expanded to contain the conversion result. Characters generated by `fwprintf()` and `wprintf()` are printed as if `fputwc()` had been called.

For `a` and `A` conversions, if `FLT_RADIX` is not a power of `2` and the result is not exactly representable in the given precision, the result should be one of the two adjacent numbers in hexadecimal floating style with the given precision, with the extra stipulation that the error should have a correct sign for the current rounding direction.

For the `e`, `E`, `f`, `F`, `g`, and `G` conversion specifiers, if the number of significant decimal digits is at most `DECIMAL_DIG`, then the result is correctly rounded. If the number of significant decimal digits is more than `DECIMAL_DIG` but the source value is exactly representable with `DECIMAL_DIG` digits, then the result is an exact representation with trailing zeros. Otherwise, the source value is bounded by two adjacent decimal strings `L` < `U`, both having `DECIMAL_DIG` significant digits; the value of the resultant decimal string `D` should satisfy `L <= D <= U`, with the extra stipulation that the error should have a correct sign for the current rounding direction.

The last data modification and last file status change timestamps of the file is marked for update between the call to a successful execution of `fwprintf()` or `wprintf()` and the next successful completion of a call to `fflush()` or `fclose()` on the same stream or a call to `exit()` or `abort()`.

###Return value

On success the functions return the number of wide characters transmitted, excluding the terminating null wide character in the case of `swprintf()`, or a negative value if an output error was encountered, and set `errno` to indicate the error. 

On output error these functions return `-1` and set `errno` to indicate the error. 

If <u>n</u> or more wide characters were requested to be written, `swprintf()` returns a negative value, and sets `errno` to indicate the error.

###Errors

The conditions under which `dprintf()`, `fprintf()`, and `printf()` fail are as follows:

[`EAGAIN`] - The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation.
[`EBADF`] - The file descriptor underlying stream is not a valid file descriptor open for writing.
[`EFBIG`] - An attempt was made to write to a file that exceeds the maximum file size or 
          - An attempt was made to write to a file that exceeds the file size limit of the process or 
          - The file is a regular file and an attempt was made to write at or beyond the offset maximum. 
[`EINTR`] - The write operation was terminated due to the receipt of a signal, and no data was transferred.
[`EINVAL`] -  There are insufficient arguments for the format. 
[`EIO`] - A physical I/O error has occurred, or the process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. This error may also be returned under implementation-defined conditions. 
[`ENOSPC`] - There was no free space remaining on the device containing the file. 
[`EPIPE`] - An attempt is made to write to a pipe or FIFO that is not open for reading by any process. A `SIGPIPE` signal shall also be sent to the thread. 
[`ENOMEM`] - Insufficient storage space is available. 
[`ENXIO`] - A request was made of a nonexistent device, or the request was outside the capabilities of the device. 

[`EILSEQ`] - A wide-character code that does not correspond to a valid character has been detected.
[`EOVERFLOW`] - The value to be returned or the value of <u>n</u> is greater than {`INT_MAX`} or the number of bytes needed to hold the output excluding the terminating null is greater than {`INT_MAX`}. 
[`ENOMEM`] - Insufficient storage space is available.


###Examples

To print the language-independent date and time format, the following statement could be used:

   ` wprintf(format, weekday, month, day, hour, min); `

For American usage, format could be a pointer to the wide-character string:

   ` L"%s, %s %d, %d:%.2d\n" `

producing the message:

 ` Sunday, July 3, 10:02`

whereas for German usage, format could be a pointer to the wide-character string:

   ` L"%1$s, %3$d. %2$s, %4$d:%5$.2d\n" `

producing the message:

 ` Sonntag, 3. Juli, 10:02`

###Implementation tasks

* implement wide characters,
* implement `fwprintf()`,
* implement `wprintf()`,
* implement `swprintf()`,
