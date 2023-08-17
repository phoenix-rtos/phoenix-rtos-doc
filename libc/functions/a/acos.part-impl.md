# Synopsis

`#include <math.h>`</br>

`double acos(double x);`</br>

`float acosf(float x);`</br>

`long double acosl(long double x);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the principal value of the arc cosine of their argument _x_. The value of _x_ should
be in the range `[-1,1]`.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the arc cosine of _x_, in the range `[0, pi]` radians.

For finite values of _x_ not in the range `[-1,1]`, a domain error shall occur, and either a `NaN` (if supported) or
an implementation-defined value shall be returned.

* If _x_ is `NaN`, a `NaN` shall be returned.

* If _x_ is `+1`, `+0` shall be returned.

* If _x_ is `±Inf`, a domain error shall occur, and a `NaN` shall be returned.

## Errors

These functions shall fail if:

Domain Error
The _x_ argument is finite and is not in the range `[-1,1]`, or is `±Inf`.
If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `EDOM`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the invalid floating-point
exception shall be raised.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
