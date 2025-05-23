# atan2

## Synopsis

```c
#include <math.h>

double atan2(double y, double x);

float atan2f(float y, float x);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the principal value of the arc tangent of _y_/_x_, using the signs of both arguments to
determine the quadrant of the return value.

An application wishing to check for error situations should set `errno` to zero and call
`feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the arc tangent of _y_/_x_ in the range `[-PI,PI]` radians.

* If _y_ is `±0` and _x_ is < `0`, `±` shall be returned.

* If _y_ is `±0` and _x_ is > `0`, `±0` shall be returned.

* If _y_ is < `0` and _x_ is `±0`, `-/2` shall be returned.

* If _y_ is > `0` and _x_ is `±0`, `/2` shall be returned.

* If _x_ is `0`, a pole error shall not occur.

* If either _x_ or _y_ is `NaN`, a `NaN` shall be returned.

* If the correct value would cause underflow, a range error may occur, and `atan()`, `atan2f()`, and `atan2l()` shall
return an implementation-defined value no greater in magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

* If the `IEC 60559` Floating-Point option is supported, _y_/_x_ should be returned.

* If _y_ is `±0` and _x_ is `-0`, `±` shall be returned.

* If _y_ is `±0` and _x_ is `+0`, `±0` shall be returned.

* For finite values of ± _y_ > `0`, if _x_ is `-Inf`, `±` shall be returned.

* For finite values of ± _y_ > `0`, if _x_ is `+Inf`, `±0` shall be returned.

* For finite values of _x_, if _y_ is `±Inf`, `±/2` shall be returned.

* If _y_ is `±Inf` and _x_ is `-Inf`, `±3/4` shall be returned.

* If _y_ is `±Inf` and _x_ is `+Inf`, `±/4` shall be returned.

* If both arguments are `0`, a domain error shall not occur.

## Errors

These functions may fail if:

* Range Error

  The result underflow's:

  If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `ERANGE`.
  If the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the underflow
  floating-point exception shall be raised.

## Tests

Untested

## Known bugs

None
