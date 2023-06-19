<!-- Documentation template to fill -->
<!-- #MUST_BE: make good synopsis -->
# Synopsis

`#include <stdarg.h>`
`#include <stdio.h>`

`int vfscanf(FILE *restrict stream, const char *restrict format, va_list arg);`

`int vscanf(const char *restrict format, va_list arg);`

`int vsscanf(const char *restrict s, const char *restrict format, va_list arg);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1, 2017

## Description

The `vscanf()`, `vfscanf()`, and `vsscanf()` functions shall be equivalent to the `scanf()`, `fscanf()`, and `sscanf()`
functions, respectively, except that instead of being called with a variable number of arguments, they are called with
an argument list as defined in the `<stdarg.h>` header. These functions shall not invoke the `va_end` macro. As these
functions invoke the `va_arg` macro, the value of _ap_ after the return is unspecified.

## Return value

Refer to [fscanf](../f/fscanf.part-impl.md).

## Errors

Refer to [fscanf](../f/fscanf.part-impl.md).

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
