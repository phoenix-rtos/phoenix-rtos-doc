###Synopsis

`#include <math.h>`

`double expm1(double x);`
`float expm1f(float x);`
`long double expm1l(long double x);`

###Description

The  functions compute the base-`e` exponential function of <u>x</u> minus `1.0`, which is `e` raised to the power <u>x</u> minus `1.0`: `e`<sup><u>x</u></sup> -`1.0`.

Arguments:

<u>x</u> - the value of which the 'e'<sup><u>x</u></sup>-'1' is computed.

An application wishing to check for error situations sets `errno` to zero and calls `feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or `fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.

###Return value

Upon successful completion, these functions return `e`<sup><u>x</u></sup>-'1.0'.

If the correct value causes overflow, a range error occurs and `expm1()`, `expm1f()`, and `expm1l()` return the value of the macro `HUGE_VAL`, `HUGE_VALF`, and `HUGE_VALL`, respectively.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0`, `0` is returned.

If <u>x</u> is -`Inf`, `-1` is returned.

If <u>x</u> is +`Inf`, <u>x</u> is returned.

If <u>x</u> is subnormal, a range error may occur and <u>x</u> is returned.

If <u>x</u> is not returned, `expm1()`, `expm1f()`, and `expm1l()` return an implementation-defined value no greater in magnitude than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN`, respectively. 

###Errors

[`ERANGE`] - the result overflows (overflow floating-point exception is raised) or the value of <u>x</u> is subnormal. 
            
On error, the expressions (`math_errhandling & MATH_ERRNO`) and (`math_errhandling & MATH_ERREXCEPT`) are independent of each other, but at least one of them must be non-zero.            