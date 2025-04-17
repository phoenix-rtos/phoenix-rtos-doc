# exp

## Synopsis

`#include <math.h>`

`double exp(double x);`

`float expf(float x);`

`long double expl(long double x);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the base `e` exponential of _x_.

An application wishing to check for error situations should set `errno` to zero and call
`feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the exponential value of _x_.

* If the correct value would cause overflow, a range error shall occur and `exp()`, `expf()`, and `expl()` shall return
the value of the macro `HUGE_VAL`, `HUGE_VALF`, and `HUGE_VALL`, respectively.

* If the correct value would cause underflow, and is not representable, a range error may occur, and `exp()`,
`expf()`, and `expl()` shall return `0.0`, or (if the IEC 60559 Floating-Point option is not supported) an
implementation-defined value no greater in magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

* If _x_ is `NaN`, a `NaN` shall be returned.
* If _x_ is `±0`, `1` shall be returned.
* If _x_ is `-Inf`, `+0` shall be returned.
* If _x_ is `+Inf`, _x_ shall be returned.
* If the correct value would cause underflow, and is representable, a range error may occur, and the correct value shall
be returned.

## Errors

These functions shall fail if:

* Range Error - The result overflows.

 If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the overflow floating-point exception
shall be raised.

These functions may fail if:

* Range Error - The result underflows.

 If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the underflow floating-point exception
shall be raised.

## Tests

Untested

## Known bugs

None
