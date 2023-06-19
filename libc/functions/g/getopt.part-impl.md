# Synopsis

`#include <unistd.h>`

`int getopt(int argc, char * const argv[], const char *optstring);`

`extern char *optarg;`

`extern int opterr, optind, optopt;`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getopt()` function is a command-line parser that shall follow Utility Syntax Guidelines `3`, `4`, `5`, `6`, `7`,
`9`, and `10` in `XBD Utility Syntax Guidelines`.

The parameters _argc_ and _argv_ are the argument count and argument array as passed to `main()`. The argument
_optstring_ is a string of recognized option characters; if a character is followed by a `<colon>`, the option
takes an argument. All option characters allowed by `Utility Syntax Guideline 3` are allowed in _optstring_. The
implementation may accept other characters as an extension.

The variable _optind_ is the index of the next element of the `argv[]` vector to be processed. It shall be initialized
to `1` by the system, and `getopt()` shall update it when it finishes with each element of `argv[]`. If the application
sets optind to zero before calling `getopt()`, the behavior is unspecified. When an element of `argv[]` contains
multiple option characters, it is unspecified how `getopt()` determines which options have already been processed.

The `getopt()` function shall return the next option character (if one is found) from argv that matches a character in
optstring, if there is one that matches. If the option takes an argument, `getopt()` shall set the variable _optarg_
to point to the option-argument as follows:

 1. If the option was the last character in the string pointed to by an element of `argv`, then _optarg_ shall contain
 the next element of `argv`, and _optind_ shall be incremented by `2`. If the resulting value of _optind_ is greater
 than `argc`, this indicates a missing option-argument, and `getopt()` shall return an error indication.

 2. Otherwise, _optarg_ shall point to the string following the option character in that element of argv, and _optind_
 shall be incremented by `1`.

If, when `getopt()` is called:

- `argv[optind] is a null pointer`

- `*argv[optind] is not the character -`

- `argv[optind] points to the string "-"`

`getopt()` shall return `-1` without changing _optind_. If:

- `argv[optind] points to the string "--"`

`getopt()` shall return `-1` after incrementing optind.

If `getopt()` encounters an option character that is not contained in _optstring_, it shall return the `<question-mark>`
( `'?'` ) character. If it detects a missing option-argument, it shall return the `<colon>` character ( `':'` ) if the
first character of _optstring_ was a `<colon>`, or a `<question-mark>` character ( `'?'` ) otherwise. In either case,
`getopt()` shall set the variable _optopt_ to the option character that caused the error. If the application has not set
the variable opterr to `0` and the first character of _optstring_ is not a `<colon>`, `getopt()` shall also print a
diagnostic message to `stderr` in the format specified for the `getopts` utility, unless the `stderr` stream has wide
orientation, in which case the behavior is undefined

## Return value

The `getopt()` function shall return the next option character specified on the command line.

A `<colon>` ( `':'` ) shall be returned if getopt() detects a missing argument and the first character of optstring was
a `<colon>` ( `':'` ).

A `<question-mark>` ( `'?'` ) shall be returned if `getopt()` encounters an option character not in _optstring_ or
detects a missing argument and the first character of _optstring_ was not a `<colon>` ( `':'` ).

Otherwise, `getopt()` shall return `-1` when all command line options are parsed.

## Errors

If the application has not set the variable _opterr_ to `0`, the first character of optstring is not a `<colon>`, and a
write error occurs while `getopt()` is printing a diagnostic message to `stderr`, then the error indicator for `stderr`
shall be set; but `getopt()` shall still succeed and the value of `errno` after `getopt()` is unspecified.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
