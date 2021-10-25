###Synopsis

`#include <stdio.h>`

`int fwscanf(FILE *stream, const char *format, ...);`
`int swscanf(const char *restrict format, ...);`
`int wscanf(const char *restrict s, const char *restrict format, ...);`

###Description

The functions read formatted input from the given stream.

The `fwscanf()` function reads from the named input stream. The `wscanf()` function reads from the standard input stream `stdin`. The `swscanf()` function reads from the wide-character string <u>ws</u>. 
Each function reads wide characters, interprets them according to a format, and stores the results in its arguments. Each expects, as arguments, a control wide-character string <u>format</u> described below, and a set of pointer arguments indicating where the converted input should be stored. The result is undefined if there are insufficient arguments for the <u>format</u>. If the <u>format</u> is exhausted while arguments remain, the excess arguments is evaluated but otherwise ignored.

Conversions can be applied to the nth argument after the <u>format</u> in the argument list, rather than to the next unused argument. In this case, the conversion specifier wide character `%` (see below) is replaced by the sequence "%n$", where `n` is a decimal integer in the range `[1,{NL_ARGMAX}]`. This feature provides for the definition of <u>format</u> wide-character strings that select arguments in an order appropriate to specific languages. In <u>format</u> wide-character strings containing the "%n$" form of conversion specifications, the numbered arguments in the argument list can be referenced from the <u>format</u> wide character string more than once.

The <u>format</u> can contain either form of a conversion specification-that is, `%` or "%n$"-but the two forms cannot be mixed within a single <u>format</u> wide-character string. The only exception to this is that %% or %* can be mixed with the "%n$" form. When numbered argument specifications are used, specifying the `Nth` argument requires that all the leading arguments, from the first to the `(N-1)`th, are pointers.

The `fwscanf()` function in all its forms allows detection of a language-dependent radix character in the input character string. The radix character is defined in the current locale (category `LC_NUMERIC`). In the POSIX locale, or in a locale where the radix character is not defined, the radix character defaults to a <period> ( '.' ).

The <u>format</u> is a wide-character string, composed of zero or more directives. Each directive is composed of one of the following: one or more white-space characters ( <space>, <tab>, <newline>, <vertical-tab>, or <form-feed>); an ordinary wide character (neither '%' nor a white-space character); or a conversion specification. Each conversion specification is introduced by the character '%' or the character sequence "%n$", after which the following appear in sequence:

 * An optional assignment-suppressing character '*'.

 * An optional non-zero decimal integer that specifies the maximum field width.

 * An optional assignment-allocation character 'm'.

 * An optional length modifier that specifies the size of the receiving object.

 * A conversion specifier wide character that specifies the type of conversion to be applied. The valid conversion specifiers are described below.

The `fwscanf()` functions executes each directive of the <u>format</u> in turn. If a directive fails, as detailed below, the function returns. Failures are described as input failures (due to the unavailability of input wide characters) or matching failures (due to inappropriate input).

A directive composed of one or more white-space wide characters is executed by reading input until no more valid input can be read, or up to the first wide character which is not a white-space character, which remains unread.

A directive that is an ordinary wide character is executed as follows: the next wide character is read from the input and compared with the wide character that comprises the directive; if the comparison shows that they are not equivalent, the directive fails, and the differing and subsequent wide characters remain unread. Similarly, if end-of-file, an encoding error, or a read error prevents a wide character from being read, the directive fails.

A directive that is a conversion specification defines a set of matching input sequences, as described below for each conversion character. A conversion specification is executed in the following steps.

Input white-space wide characters (as specified by  `iswspace()`) are skipped, unless the conversion specification includes `a [`, `c` or `n` conversion specifier.

An item is read from the input, unless the conversion specification includes an `n` conversion specifier wide character. An input item is defined as the longest sequence of input wide characters (up to any specified maximum field width, which is an initial subsequence of a matching sequence. The first wide character, if any, after the input item remains unread. If the length of the input item is zero, the execution of the conversion specification fails; this condition is a matching failure, unless end-of-file, an encoding error, or a read error prevented input from the stream, in which case it is an input failure.

Except in the case of a `%` conversion specifier, the input item (or, in the case of a `%n` conversion specification, the count of input wide characters) is converted to a type appropriate to the conversion character. If the input item is not a matching sequence, the execution of the conversion specification fails; this condition is a matching failure. Unless assignment suppression was indicated by a '*', the result of the conversion is placed in the object pointed to by the first argument following the <u>format</u> argument that has not already received a conversion result if the conversion specification is introduced by `%`, or in the `n`th argument if introduced by the wide-character sequence "%n$". If this object does not have an appropriate type, or if the result of the conversion cannot be represented in the space provided, the behaviour is undefined.

The `%c`, `%s`, and `%[` conversion specifiers accept an optional assignment-allocation character 'm', which causes a memory buffer to be allocated to hold the wide character string converted including a terminating null wide character. In such a case, the argument corresponding to the conversion specifier should be a reference to a pointer variable that receives a pointer to the allocated buffer. The system allocates a buffer as if `malloc()` had been called. The application is responsible for freeing the memory after usage. If there is insufficient memory to allocate a buffer, the function sets `errno` to [`ENOMEM`] and a conversion error results. If the function returns `EOF`, any memory successfully allocated for parameters using assignment-allocation character 'm' by this call is freed before the function returns.

The length modifiers and their meanings are:

 * `hh` - Specifies that a following `d`, `i`, `o`, `u`, `x`, `X`, or `n` conversion specifier applies to an argument with type pointer to `signed char` or `unsigned char`.
 * `h` -  Specifies that a following `d`, `i`, `o`, `u`, `x`, `X`, or `n` conversion specifier applies to an argument with type pointer to `short` or `unsigned short`.
 * `l` (ell) - Specifies that a following `d`, `i`, `o`, `u`, `x`, `X`, or `n` conversion specifier applies to an argument with type pointer to `long` or `unsigned long`; that a following `a`, `A`, `e`, `E`, `f`, `F`, `g`, or `G` conversion specifier applies to an argument with type pointer to double; or that a following c, s, or [ conversion specifier applies to an argument with type pointer to wchar_t. [CX] [Option Start]  If the 'm' assignment-allocation character is specified, the conversion applies to an argument with the type pointer to a pointer to wchar_t. [Option End]
 * `ll` (ell-ell) - Specifies that a following `d`, `i`, `o`, `u`, `x`, `X`, or `n` conversion specifier applies to an argument with type pointer to `long long` or `unsigned long long`.
 * `j` - Specifies that a following `d`, `i`, `o`, `u`, `x`, `X`, or `n` conversion specifier applies to an argument with type pointer to `intmax_t` or `uintmax_t`.
 * `z` - Specifies that a following `d`, `i`, `o`, `u`, `x`, `X`, or `n` conversion specifier applies to an argument with type pointer to `size_t` or the corresponding `signed` integer type.
 * `t` - Specifies that a following `d`, `i`, `o`, `u`, `x`, `X`, or `n` conversion specifier applies to an argument with type pointer to `ptrdiff_t` or the corresponding `unsigned` type.
 * `L` - Specifies that a following `a`, `A`, `e`, `E`, `f`, `F`, `g`, or `G` conversion specifier applies to an argument with type pointer to `long double`.

If a length modifier appears with any conversion specifier other than as specified above, the behavior is undefined.

The following conversion specifier wide characters are valid:

 * `d` - Matches an optionally signed decimal integer, whose format is the same as expected for the subject sequence of `wcstol()` with the value `10` for the base argument. In the absence of a size modifier, the application ensures that the corresponding argument is a pointer to `int`.

 * `i` - Matches an optionally signed integer, whose format is the same as expected for the subject sequence of `wcstol()` with `0` for the base argument. In the absence of a size modifier, the application ensures that the corresponding argument is a pointer to `int`.
 
 * `o` - Matches an optionally signed octal integer, whose format is the same as expected for the subject sequence of `wcstoul()` with the value `8` for the base argument. In the absence of a size modifier, the application ensures that the corresponding argument is a pointer to `unsigned`.
 
 * `u` - Matches an optionally signed decimal integer, whose format is the same as expected for the subject sequence of `wcstoul()` with the value `10` for the base argument. In the absence of a size modifier, the application ensures that the corresponding argument is a pointer to `unsigned`.
 
 * `x` - Matches an optionally signed hexadecimal integer, whose format is the same as expected for the subject sequence of `wsctoul()` with the value `16` for the base argument. In the absence of a size modifier, the application ensures that the corresponding argument is a pointer to `unsigned`.
 
 * `a`, `e`, `f`, `g` - Matches an optionally signed floating-point number, infinity, or `NaN`, whose format is the same as expected for the subject sequence of `wcstod()`. In the absence of a size modifier, the application ensures that the corresponding argument is a pointer to `float`.

    If the `fwprintf()` family of functions generates character string representations for infinity and `NaN` (a symbolic entity encoded in floating-point format) to support, the `fwscanf()` family of functions recognizes them as input.
 
 * `s` - Matches a sequence of wide characters that are not white-space characters. characters from the input field are converted as if by repeated calls to the `wcrtomb()` function, with the conversion state described by an `mbstate_t` object initialized to zero before the first wide character is converted. If the 'm' assignment-allocation character is not specified, the application ensures that the corresponding argument is a pointer to a character array large enough to accept the sequence and the terminating null character, which is added automatically. Otherwise, the application ensures that the corresponding argument is a pointer to a pointer to a `wchar_t`.

If the `l`(`ell`) qualifier is present and the 'm' assignment-allocation character is not specified, the application ensures that the corresponding argument is a pointer to an array of `wchar_t` large enough to accept the sequence and the terminating null wide character, which are added automatically. If the `l` (`ell`) qualifier is present and the 'm' assignment-allocation character is present, the application ensures that the corresponding argument is a pointer to a pointer to a `wchar_t`. 
 
 * `[` - Matches a non-empty sequence of wide characters from a set of expected wide characters (the `scanset`).  If no `l` (`ell`) qualifier is present, wide characters from the input field are converted as if by repeated calls to the `wcrtomb()` function, with the conversion state described by an `mbstate_t` object initialized to zero before the first wide character is converted. If the 'm' assignment-allocation character is not specified, the application ensures that the corresponding argument is a pointer to a character array large enough to accept the sequence and the terminating null character, which is added automatically. Otherwise, the application ensures that the corresponding argument is a pointer to a pointer to a `wchar_t`.
    
    If an `l` (`ell`) qualifier is present and the 'm' assignment-allocation character is not specified, the application ensures that the corresponding argument is a pointer to an array of `wchar_t` large enough to accept the sequence and the terminating null wide character. If an `l` (`ell`) qualifier is present and the 'm' assignment-allocation character is specified, the application ensures that the corresponding argument is a pointer to a pointer to a `wchar_t`. 

    Otherwise, the application ensures that the corresponding argument is a pointer to a pointer to a `wchar_t`.

    The conversion specification includes all subsequent wide characters in the <u>format</u> wide character string up to and including the matching <right-square-bracket> ( ']' ). The wide characters between the square brackets (the `scanlist`) comprise the scanset, unless the byte after the <left-square-bracket> is a <circumflex> ( '^' ), in which case the scanset contains all wide characters that do not appear in the scanlist between the <circumflex> and the <right-square-bracket>. If the conversion specification begins with "[]" or "[^]", the <right-square-bracket> is included in the scanlist and the next <right-square-bracket> is the matching <right-square-bracket> that ends the conversion specification; otherwise, the first <right-square-bracket> is the one that ends the conversion specification. If a '-' is in the scanlist and is not the first wide character, nor the second where the first character is a '^', nor the last wide character.
 
 * `c` - Matches a sequence of wide characters of the number specified by the field width (`1` if no field width is present in the conversion specification).
 
    If no `l` (`ell`) length modifier is present, characters from the input field are converted as if by repeated calls to the `wcrtomb()` function, with the conversion state described by an `mbstate_t` object initialized to zero before the first wide character is converted. No null character is added. If the 'm' assignment-allocation character is not specified, the application ensures that the corresponding argument is a pointer to the initial element of a character array large enough to accept the sequence. Otherwise, the application ensures that the corresponding argument is a pointer to a pointer to a `char`. 
 
    No null wide character is added. If an `l` (`ell`) length modifier is present and the 'm' assignment-allocation character is not specified, the application ensures that the corresponding argument is a pointer to the initial element of an array of `wchar_t` large enough to accept the sequence. If an `l` (`ell`) qualifier is present and the 'm' assignment-allocation character is specified, the application ensures that the corresponding argument is a pointer to a pointer to a `wchar_t`.
    
 * `p` - Matches an implementation-defined set of sequences, which is the same as the set of sequences that is produced by the `%p` conversion specification of the corresponding `fwprintf()` functions. The application ensures that the corresponding argument is a pointer to a pointer to `void`. If the input item is a value converted earlier during the same program execution, the pointer that results shall compare equal to that value; otherwise, the behaviour of the `%p` conversion specification is undefined.
 
 * `n` - No input is consumed. The application ensures that the corresponding argument is a pointer to the integer into which is written the number of wide characters read from the input so far by this call to the `fwscanf()` functions. Execution of a `%n` conversion specification does not increment the assignment count returned at the completion of execution of the function. No argument is converted, but one is consumed. If the conversion specification includes an assignment-suppressing wide character or a field width, the behaviour is undefined.
 
 * `C` - Equivalent to `lc`.
 
 * `S` - Equivalent to `ls`.
 
 * `%` - Matches a single '%' wide character; no conversion or assignment occurs. The complete conversion specification is `%%`.

If a conversion specification is invalid, the behavior is undefined.

The conversion specifiers `A`, `E`, `F`, `G`, and `X` are also valid and are equivalent to `a`, `e`, `f`, `g`, and `x`, respectively.

If end-of-file is encountered during input, conversion is terminated. If end-of-file occurs before any wide characters matching the current conversion specification (except for `%n` ) have been read (other than leading white-space characters, where permitted), execution of the current conversion specification terminates with an input failure. Otherwise, unless execution of the current conversion specification is terminated with a matching failure, execution of the following conversion specification (if any) is terminated with an input failure.

Reaching the end of the wide character string in `wscanf()` is equivalent to encountering end-of-file for `fwscanf()`.

If conversion terminates on a conflicting input, the offending input is left unread in the input. Any trailing white space (including <newline> characters) is left unread unless matched by a conversion specification. The success of literal matches and suppressed assignments is only directly determinable via the `%n` conversion specification.

The `fwscanf()` and `wscanf()` functions may mark the last data access timestamp of the file associated with stream for update. The last data access timestamp is marked for update by the first successful execution of `fgetwc()`, `fgetws()`, `fwscanf()`, `getwc()`, `getwchar()`, `vfwscanf()`, `vwscanf()`, or `wscanf()` using stream that returns data not supplied by a prior call to `ungetwc()`.

###Return value

Upon successful completion, these functions return the number of successfully matched and assigned input items; this number can be zero in the event of an early matching failure. If the input ends before the first conversion (if any) has completed, and without a matching failure having occurred, `EOF` is returned. If an error occurs before the first conversion (if any) has completed, and without a matching failure having occurred, `EOF` is returned and `errno` is set to indicate the error. If a read error occurs, the error indicator for the stream is set.

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the `fgetc()` operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for reading. 
[`EINTR`]  The read operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`]    A physical I/O error has occurred, or the process is in a background process group attempting to read from its controlling terminal, and either the calling thread is blocking `SIGTTIN` or the process is ignoring `SIGTTIN` or the process group of the process is orphaned.
[`EOVERFLOW`]  The file is a regular file and an attempt was made to read at or beyond the offset maximum associated with the corresponding stream. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device.
[`EILSEQ`] Input byte sequence does not form a valid character.
[`EINVAL`] There are insufficient arguments. 

###Implementation tasks

* Implement wide character handling.
* Implement fwscanf().
* Implement swscanf().
* Implement wscanf().
