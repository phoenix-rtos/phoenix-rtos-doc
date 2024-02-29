# sigsetjmp

## Synopsis

`#include <setjmp.h>`

` int sigsetjmp(sigjmp_buf env, int savemask); `

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigsetjmp()` function shall be equivalent to the `setjmp()` function,
except as follows:

* References to `setjmp()` are equivalent to `sigsetjmp()`.

* References to `longjmp()` are equivalent to `siglongjmp()`.

* If the value of the `savemask` argument is not 0, `sigsetjmp()` shall also save the current signal mask of the calling

* Thread as part of the calling environment.

## Return value

If the return is from a successful direct invocation, `sigsetjmp()` shall return 0. If the return is from a call to
`siglongjmp()`, `sigsetjmp()` shall return a non-zero value.

## Errors

No errors are defined.

The following sections are informative.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
