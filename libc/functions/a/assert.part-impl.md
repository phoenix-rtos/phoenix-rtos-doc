# assert

## Synopsis

`#include <assert.h>`</br>

`void assert(scalar expression);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to insert program diagnostics. The `assert()` macro shall insert diagnostics into programs, it shall
expand to a `void` expression. When it is executed, if _expression_ (which shall have a scalar type) is false (that is,
compares equal to `0`), `assert()` shall write information about the particular call that failed on stderr
and shall call `abort()`.

The information written about the call that failed shall include the text of the argument, the name of the source file,
the source file line number, and the name of the enclosing function, the latter are, respectively, the values of the
preprocessing macros `__FILE__` and `__LINE__` and of the identifier `__func__`.

Forcing a definition of the name `NDEBUG`,
either from the compiler command line or with the preprocessor control statement `#define NDEBUG` ahead of the
`#include <assert.h>` statement, shall stop assertions from being compiled into the program.

## Return value

The `assert()` macro shall not return a value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
