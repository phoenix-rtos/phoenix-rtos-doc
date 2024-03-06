# tanh

`#include <math.h>`

`double tanh(double x);`

`float tanhf(float x);`

`long double tanhl(long double x);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the hyperbolic tangent of their argument _x_.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the hyperbolic tangent of _x_.

If _x_ is `NaN`, a `NaN` shall be returned.

If _x_ is `±0`, _x_ shall be returned.

If _x_ is `±Inf`, `±1` shall be returned.

If _x_ is subnormal, a range error may occur and _x_ should be returned.

If _x_ is not returned, `tanh()`, `tanhf()`, and `tanhl()` shall return an implementation-defined value no greater in
magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

## Errors

These functions may fail if:

- `ERANGE` - The value of _x_ is subnormal.

If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then errno shall be set to `ERANGE`.
If the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the underflow floating-point
exception shall be raised.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
