# puts

## Synopsis

`#include <stdio.h>`

`int puts(const char *s);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `puts()` function shall write the string pointed to by _s_, followed by a `<newline>`, to the standard output stream
stdout. The terminating `null` byte shall not be written.

The
last data modification and last file status change timestamps of the file shall be marked for update between the
successful execution of `puts()` and the next successful completion of a call to `fflush()` or `fclose()` on the same
stream or a call to `exit()` or `abort()`.

## Return value

Upon successful completion, `puts()` shall return a non-negative number. Otherwise, it shall return `EOF`, shall set an
error indicator for the stream,  and `errno` shall be set to indicate the error.

## Errors

Refer to `fputc()`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
