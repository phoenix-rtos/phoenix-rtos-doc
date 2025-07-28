# cosh

## Synopsis

```c
#include <math.h>

double cosh(double x);

float coshf(float x);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the hyperbolic cosine of their argument _x_.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the hyperbolic cosine of _x_.

* If the correct value would cause overflow, a range error shall occur and `cosh()`, `coshf()`, and `coshl()` shall
return the value of the macro `HUGE_VAL`, and `HUGE_VALF` respectively.

* If _x_ is `NaN`, a `NaN` shall be returned.

* If _x_ is `±0`, the value `1.0` shall be returned.

* If _x_ is `±Inf`, `+Inf` shall be returned.

## Errors

These functions shall fail if:

* Range Error
  The result would cause an overflow.

  If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`. If the
  integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the overflow floating-point exception shall
  be raised.

## Tests

Untested

## Known bugs

None
