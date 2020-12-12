###Synopsis

`#include <math.h>`

`double asinh(double x);` 
`float asinhf(float x);`
`long double asinhl(long double x);`

###Description

The functions return the inverse hyperbolic sine of their argument <u>x</u>.

Arguments:
<u>x</u> - value whose inverse hyperbolic sine is computed.

###Return value
Upon successful completion, the function return the inverse hyperbolic sine of their argument.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0` or `Inf`, <u>x</u> is returned.

If <u>x</u> is subnormal, a range error occurs and <u>x</u> is returned.

###Errors

`[ERANGE]` (Range Error) - The value of <u>x</u> is subnormal.

If the integer expression (`math_errhandling & MATH_ERRNO`) is non-zero, then `errno` is set to   `[ERANGE]`. If the integer expression (`math_errhandling & MATH_ERREXCEPT`) is non-zero, then the underflow floating-point exception is raised.
On error, the expressions (`math_errhandling & MATH_ERRNO`) and (`math_errhandling & MATH_ERREXCEPT`) are independent of each other, but at least one of them must be non-zero.

###Comments

An application wishing to check for error situations sets `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)` before calling this function. On return, if `errno` is non-zero or `fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.