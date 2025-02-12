# atan

## Synopsis

`#include <math.h>`

`double atan(double x);`

`float atanf(float x);`

`long double atanl(long double x);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the principal value of the arc tangent of their argument _x_.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the arc tangent of _x_ in the range `[-PI/2,PI/2]` radians.

* If _x_ is `NaN`, a `NaN` shall be returned.

* If _x_ is `±0`, _x_ shall be returned.

* If _x_ is `±Inf`, `±/2` shall be returned.

* If _x_ is subnormal, a range error may occur and _x_ should be returned.

* If _x_ is not returned, `atan()`, `atanf()`, and `atanl()` shall return an implementation-defined value no greater in
magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

## Errors

These functions may fail if:

* Range Error

  The value of _x_ is subnormal.

  If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`. If the
  integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the underflow floating-point
  exception shall be raised.

## Tests

Untested

## Known bugs

None
