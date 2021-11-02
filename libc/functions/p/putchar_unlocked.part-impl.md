# Synopsis 
`#include <stdio.h>`</br>
` int getc_unlocked(FILE *stream);`</br>
` int getchar_unlocked(void);`</br>
` int putc_unlocked(int c, FILE *stream);`</br>
` int putchar_unlocked(int c); `</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


Versions of the functions `getc()`, `getchar()`, `putc()`, and `putchar()` respectively named `getc_unlocked()`, `getchar_unlocked()`,
`putc_unlocked()`, and `putchar_unlocked()` shall be provided which are functionally equivalent to the original versions,
with the exception that they are not required to be implemented in a fully thread-safe manner. They shall be thread-safe when used
within a scope protected by `flockfile()` (or `ftrylockfile()`) and `funlockfile()`.

These functions can safely be used in a multi-threaded program if and only if they are called while the invoking thread owns the `( FILE *)` object, as is the case after a successful call to the `flockfile()`
or `ftrylockfile()` functions.

If `getc_unlocked()` or `putc_unlocked()` are implemented as macros they may evaluate stream more than once, so
the stream argument should never be an expression with side-effects.


## Return value


See `getc()`, `getchar()`, `putc()`, and `putchar()`.


## Errors


See `getc()`, `getchar()`, `putc()`, and `putchar()`.




## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
