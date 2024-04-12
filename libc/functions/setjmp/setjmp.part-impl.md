# setjmp

## Synopsis

`#include <setjmp.h>`

`int setjmp(jmp_buf env);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

A call to `setjmp()` shall save the calling environment in its _env_ argument for later use by `longjmp()`.
It is unspecified whether `setjmp()` is a macro or a function. If a macro definition is suppressed in order to access an
actual function, or a program defines an external identifier with the name `setjmp`, the behavior is undefined.
An application shall ensure that an invocation of `setjmp()` appears in one of the following contexts only:

* The entire controlling expression of a selection or iteration statement

* One operand of a relational or equality operator with the other operand an integral constant expression, with the
resulting expression being the entire controlling expression of a selection or iteration statement

* The operand of a unary `!` operator with the resulting expression being the entire controlling expression of a
selection or iteration

* The entire expression of an expression statement (possibly cast to `void`)

If the invocation appears in any other context, the behavior is undefined.

## Return value

If the return is from a direct invocation, `setjmp()` shall return `0`. If the return is from a call to `longjmp()`,
`setjmp()` shall return a non-zero value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
