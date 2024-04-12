# sqrt

## Synopsis

`#include <math.h>`

`double sqrt(double x);`

`float sqrtf(float x);`

`long double sqrtl(long double x);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the square root of their argument _x_,
An application wishing to check for error situations should set errno to zero and call
`feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID` | `FE_DIVBYZERO` | `FE_OVERFLOW` | `FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the square root of _x_.
For finite values of `x < -0`, a domain error shall occur, and
either a `NaN` (if supported), or an implementation-defined value shall be returned.
If
_x_ is `NaN`, a `NaN` shall be returned.
If _x_ is `±0` or `+Inf`, _x_ shall be returned.
If _x_ is `-Inf`, a domain `error` shall occur, and a `NaN` shall be returned.

## Errors

These functions shall fail if:

`Domain Error` - the finite value of `x` is `< -0`, or _x_ is `-Inf`.
If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `EDO`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the invalid floating-point exception
shall be raised.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
