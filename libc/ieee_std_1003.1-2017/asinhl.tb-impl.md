###Synopsis

`#include <math.h>`

`long double asinhl(long double x);`

###Description

The function returns the inverse hyperbolic sine of its argument x.

Arguments:
<u>x</u> - value whose inverse hyperbolic sine shall be computed.

###Return value
Upon successful completion, this function shall return the inverse hyperbolic sine of its argument.

If <u>x</u> is NaN, a NaN shall be returned.

If <u>x</u> is 0 or Inf, <u>x</u> shall be returned.

If <u>x</u> is subnormal, a range error may occur and <u>x</u> should be returned.

If <u>x</u> is not returned, asinhl() shall return an implementation-defined value no greater in magnitude than DBL_MIN.

###Errors

[ERANGE] (Range Error) - The value of <u>x</u> is subnormal.

If the integer expression (math_errhandling & MATH_ERRNO) is non-zero, then errno shall be set to [ERANGE]. If the integer expression (math_errhandling & MATH_ERREXCEPT) is non-zero, then the underflow floating-point exception shall be raised.
On error, the expressions (math_errhandling & MATH_ERRNO) and (math_errhandling & MATH_ERREXCEPT) are independent of each other, but at least one of them must be non-zero.

###Comments

An application wishing to check for error situations should set errno to zero and call feclearexcept(FE_ALL_EXCEPT) before calling this function. On return, if errno is non-zero or fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW) is non-zero, an error has occurred.