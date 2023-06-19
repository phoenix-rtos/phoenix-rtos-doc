# Synopsis

`#include <math.h>`

`double ldexp(double x, int exp);`

`float ldexpf(float x, int exp);`

`long double ldexpl(long double x, int exp);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the quantity `x * 2^exp`.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if errno is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return _x_ multiplied by `2`, raised to the power _exp_.

If these functions caused overflow, a range error shall occur and `ldexp()`, `ldexpf()`, and `ldexpl()` shall
return `±HUGE_VAL`, `±HUGE_VALF`, and `±HUGE_VALL` (according to the sign of _x_), respectively.

If the correct value would cause underflow, and is not representable, a range error may occur, and `ldexp()`,
`ldexpf()`, and `ldexpl()` shall return `0.0`, or (if IEC 60559 Floating-Point is not supported) an
implementation-defined value no greater in magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

* If _x_ is `NaN`, a `NaN` shall be returned.
* If _x_ is `±0` or `±Inf`, _x_ shall be returned.
* If _exp_ is `0`, _x_ shall be returned.
* If the correct value would cause underflow, and is representable, a range error may occur, and the correct value
 shall be returned.

## Errors

These functions shall fail if:

* `Range Error` - The result overflows.
If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the overflow floating-point
exception shall be raised.

These functions may fail if:

* `Range Error` - The result underflows.
If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then errno shall be set to `ERANGE`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the underflow floating-point exception
shall be raised.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
