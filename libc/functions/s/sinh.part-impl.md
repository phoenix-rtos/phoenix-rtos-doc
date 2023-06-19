# Synopsis

`#include <math.h>`

`double sinh(double x);`

`float sinhf(float x);`

`long double sinhl(long double x);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the hyperbolic sine of their argument _x_.
An application wishing to check for error situations should set `errno` to zero and call
`feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID` | `FE_DIVBYZERO` | `FE_OVERFLOW` | `FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the hyperbolic sine of _x_.
If the result caused an overflow, a range error shall occur and `±HUGE_VAL`, `±HUGE_VALF`, and `±HUGE_VALL`
(with the same sign as x) shall be returned as appropriate for the type of the function.
  If
_x_ is `NaN`, a `NaN` shall be returned.
If _x_ is `±0` or `±Inf`, _x_ shall be returned.
If _x_ is subnormal, a range error may occur
  and _x_ should be returned.
  If
_x_ is not returned, `sinh()`, `sinhf()`, and `sinhl()` shall return an implementation-defined value no greater
in magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

## Errors

These functions shall fail if:

* `Range Error` - The result would cause an overflow.

If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then errno shall be set to `ERANG`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the overflow floating-point exception
shall be raised.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
