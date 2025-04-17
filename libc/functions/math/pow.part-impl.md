# pow

## Synopsis

`#include <math.h>`

`double pow(double x, double y);`

`float powf(float x, float y);`

`long double powl(long double x, long double y);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the value of `x` raised to the power `y`. If `x` is negative, the application shall ensure
that `y` is an integer value.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)`
before calling these functions. On return, if `errno` is non-zero or
`fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

## Return value

Upon successful completion, these functions shall return the value of _x_ raised to the power _y_.

For finite values of `x < 0`, and finite non-integer values of `y`, a domain error shall occur and either a `NaN`
(if representable), or an implementation-defined value shall be returned.

If the correct value would cause overflow, a range error shall occur and `pow()`, `powf()`, and `powl()` shall return
`±HUGE_VAL`, `±HUGE_VALF`, and `±HUGE_VALL`, respectively, with the same sign as the correct value of the function.

If the correct value would cause underflow, and is not representable, a range error may occur, and `pow()`,
`powf()`, and `powl()` shall return `0.0`, or (if IEC 60559 Floating-Point is not supported) an
implementation-defined value no greater in magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively.

For `y < 0`, if _x_ is zero, a pole error may occur and `pow()`, `powf()`, and `powl()` shall return `±HUGE_VAL`,
`±HUGE_VALF`, and `±HUGE_VALL`, respectively.  On systems that support the IEC 60559 Floating-Point option, if _x_ is
`±0`, a pole error shall occur and `pow()`, `powf()`, and `powl()` shall return `±HUGE_VAL`, `±HUGE_VALF`, and
`±HUGE_VALL`, respectively if _y_ is an odd integer, or `HUGE_VAL`, `HUGE_VALF`, and `HUGE_VALL`, respectively if _y_
is not an odd integer.

If_x_or_y_ is a `NaN`, a `NaN` shall be returned (unless specified elsewhere in this description).

* For any value of _y_ (including `NaN`), if _x_ is `+1`, `1.0` shall be returned.
* For any value of _x_ (including `NaN`), if _y_ is `±0`, `1.0` shall be returned.
* For any odd integer value of `y > 0`, if _x_ is `±0`, `±0` shall be returned.
* For `y > 0` and not an odd integer, if_x_ is `±0`, `+0` shall be returned.

If x is `-1`, and _y_ is `±Inf`, `1.0` shall be returned.

* For `|x| < 1`, if _y_ is `-Inf`, `+Inf` shall be returned.
* For `|x| > 1`, if _y_ is `-Inf`, `+0` shall be returned.
* For `|x| < 1`, if _y_ is `+Inf`, `+0` shall be returned.
* For `|x| > 1`, if _y_ is `+Inf`, `+Inf` shall be returned.
* For _y_ an odd integer `< 0`, if _x_ is `-Inf`, `-0` shall be returned.
* For `y < 0` and not an odd integer, if _x_ is `-Inf`, `+0` shall be returned.
* For _y_ an odd integer `> 0`, if _x_ is `-Inf`, `-Inf` shall be returned.
* For `y > 0` and not an odd integer, if _x_ is `-Inf`, `+Inf` shall be returned.
* For `y < 0`, if _x_ is `+Inf`, `+0` shall be returned.
* For `y > 0`, if _x_ is `+Inf`, `+Inf` shall be returned.

If the correct value would cause underflow, and is representable, a range error may occur, and the correct value shall
be returned.

## Errors

These functions shall fail if:

* `Domain Error` - The value of _x_ is negative and _y_ is a finite non-integer.
 If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to [`EDOM`]. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the invalid floating-point exception
shall be raised.

* `Pole Error` - The value of _x_ is zero and _y_ is negative.
 If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to [`ERANGE`]. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the divide-by-zero floating-point
exception shall be raised.

* `Range Error` - The result overflows.
 If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to [`ERANGE`]. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the overflow floating-point exception
shall be raised.

These functions may fail if:

* `Pole Error` - The value of _x_ is zero and _y_ is negative.
 If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to [`ERANGE`]. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the divide-by-zero floating-point
exception shall be raised.

* `Range Error` - The result underflows.
 If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to [`ERANGE`]. If
the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the underflow floating-point exception
shall be raised.

## Tests

Untested

## Known bugs

None
