# Synopsis

`#include <stdio.h>`

`void perror(const char *s);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `perror()` function shall map the error number accessed through the symbol `errno` to a language-dependent error
message, which shall be written to the standard error stream as follows:

* First (if _s_ is not a `null` pointer and the character pointed to by _s_ is not the `null` byte), the string pointed
to by _s_ followed by a `<colon>` and a `<space>`.

* Then an error message string followed by a `<newline>`.

The contents of the error message strings shall be the same as those returned by `strerror()` with argument `errno`.
The
`perror()` function shall mark for update the last data modification and last file status change timestamps of the file
associated with the standard error stream at some time between its successful completion and `exit()`, `abort()`, or the
completion of `fflush()` or `fclose()` on stderr.

The `perror()` function shall not change the orientation of the standard error stream.

On error, `perror()` shall set the error indicator for the stream to which stderr points, and shall set `errno` to
indicate the error.

Since no value is returned, an application wishing to check for error situations should call `clearerr(stderr)` before
calling `perror()`, then if `ferror(stderr)` returns non-zero, the value of `errno` indicates which error occurred.

## Return value

The `perror()` function shall not return a value.

## Errors

Refer to `fputc()`

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
