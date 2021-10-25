###Synopsis

`#include <math.h>`

`double exp2(double x);`
`float exp2f(float x);`
`long double exp2l(long double x);`

###Description

The  functions compute the base-`2` exponential function of <u>x</u>, which is `e` raised to the power <u>x</u>: `e`^<u>x</u>.

Arguments:

<u>x</u> - the value of which base-`2` exponential function is computed.

An application wishing to check for error situations sets `errno` to zero and calls `feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or `fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

###Return value

Upon successful completion, these functions return `2`<sup><u>x</u></sup>.

If the correct value causes overflow, a range error occurs and `exp2()`, `exp2f()`, and `exp2l()` return the value of the macro `HUGE_VAL`, `HUGE_VALF`, and `HUGE_VALL`, respectively.

If the correct value causes underflow, and is not representable, a range error occurs, and `exp2()`, `exp2f()`, and `exp2l()` return `0.0`.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0`, `1` is returned.

If <u>x</u> is -`Inf`, `+0` is returned.

If <u>x</u> is +`Inf`, <u>x</u> is returned.

If the correct value causes underflow, and is representable, a range error occurs and the correct value is returned. 

###Errors

[`ERANGE`] - the result overflows (overflow floating-point exception is raised) or
            the result underflows (underflow floating-point exception is raised)
            
On error, the expressions (`math_errhandling & MATH_ERRNO`) and (`math_errhandling & MATH_ERREXCEPT`) are independent of each other, but at least one of them must be non-zero.            