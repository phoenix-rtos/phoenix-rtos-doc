# log10

## Synopsis

`#include <math.h>`

`double log10(double x);`

`float log10f(float x);`

`long double log10l(long double x);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the base 10 logarithms of their argument _x_, `log10(x)`.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the base 10 logarithms of _x_.

* If _x_ is `±0`, a pole error shall occur and `log10()`, `log10f()`, and `log10l()` shall return `-HUGE_VAL`,
`-HUGE_VALF`, and `-HUGE_VALL`, respectively.

For finite values of _x_ that are less than `0`, or if _x_ is `-Inf`, a domain error shall occur, and either a
`NaN` (if supported), or an implementation-defined value shall be returned.

* If _x_ is `NaN`, a `NaN` shall be returned.
* If _x_ is `1`, `+0` shall be returned.
* If _x_ is `+Inf`, `+Inf` shall be returned.

## Errors

These functions shall fail if:

* `Domain Error` - The finite value of _x_ is negative, or _x_ is -Inf.
If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `EDOM`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the invalid floating-point exception
shall be raised.

* `Pole Error` - The value of _x_ is zero.
If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the divide-by-zero floating-point
exception shall be raised.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
