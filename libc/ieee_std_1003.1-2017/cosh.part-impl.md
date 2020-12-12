###Synopsis

`#include <math.h>`

`double cosh(double x);`
`float coshf(float x);`
`long double coshl(long double x);`

###Description

Calculates the hyperbolic cosine of <u>x</u>.

###Return value

On success the function returns the hyperbolic cosine of <u>x</u>.

If the correct value would cause overflow, a range error occurs and `cosh()`, `coshf()`, and `coshl()` return the value of the macro `HUGE_VAL`, `HUGE_VALF`, and `HUGE_VALL`, respectively.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0`, the value `1.0` is returned.

If <u>x</u> is `Inf`, `+Inf` is returned.

###Errors

`[ERANGE]` - the result causes overflow.

If the integer expression (`math_errhandling & MATH_ERRNO`) is non-zero, then `errno` is set to `[ERANGE]`. 
If the integer expression (`math_errhandling & MATH_ERREXCEPT`) is non-zero, then the overflow floating-point exception is raised.

###Implementation tasks

* Implement the functions: cosh(), coshf() and coshl() with error handling described above