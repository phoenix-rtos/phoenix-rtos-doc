###Synopsis

`#include <math.h>`

`double fdim(double x, double y);`
`float fdimf(float x, float y);`
`long double fdiml(long double x, long double y);`

###Description

The functions compute positive difference between two floating-point numbers.

Arguments:

<u>x</u> - the first floating point number.
<u>y</u> - the second floating point number.

The functions determine the positive difference between their arguments. If <u>x</u> is greater than <u>y</u>, <u>x</u> - <u>y</u> is returned. If <u>x</u> is less than or equal to <u>y</u>, `+0` is returned.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or `fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.
 
###Return value

Upon successful completion, these functions return the positive difference value.

If <u>x</u> - <u>y</u> is positive and overflows, a range error occurs and `fdim()`, `fdimf()`, and `fdiml()` return the value of the macro `HUGE_VAL`, `HUGE_VALF`, and `HUGE_VALL`, respectively.

If the correct value would cause underflow, a range error may occur, and `fdim()`, `fdimf()`, and `fdiml()` return the correct value.
If <u>x</u> or <u>y</u> is `NaN`, a `NaN` is returned.

###Errors

[`ERANGE`] - The result overflows or the result underflows.

If the integer expression (`math_errhandling & MATH_ERRNO`) is non-zero, then `errno` is set to [`ERANGE`]. If the integer expression (`math_errhandling & MATH_ERREXCEPT`) is non-zero, then the overflow (underflow) floating-point exception is raised.

On error, the expressions (`math_errhandling & MATH_ERRNO`) and (`math_errhandling & MATH_ERREXCEPT`) are independent of each other, but at least one of them must be non-zero.

###Implementation tasks

 * Implement the `fdim()` function.
 * Implement the `fdimf()` function.
 * Implement the `fdiml()` function.