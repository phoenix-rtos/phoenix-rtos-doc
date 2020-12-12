###Synopsis

`#include <math.h>`

`double asin(double x);`
`float asinf(float x);`
`long double asinl(long double x);`

###Description

The functions return the principal value of the arc sine of <u>x</u>, expressed in radians.

Arguments:
<u>x</u> - value whose arc sine is computed, in the interval [`-1`,`+1`].

###Return value
Upon successful completion, the functions return the arc sine of <u>x</u>, in the range [-<span>&#960;</span>/2,<span>&#960;</span>/2] radians.

For finite values of <u>x</u>  not in the range [`-1`,`1`], a domain error occurs and a `NaN` is returned.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0`, <u>x</u> is returned.

If <u>x</u> is `Inf`, a domain error occurs, and a `NaN` is returned.

If <u>x</u> is subnormal, a range error occurs and <u>x</u> is returned.

###Errors
`[EDOM]` (Domain Error) -     The <u>x</u> argument is finite and is not in the range [`-1,1`] or is `Inf`. 
            If the integer expression (`math_errhandling` & `MATH_ERRNO`) is non-zero, then `errno` is set to [`EDOM`]. If the integer expression (`math_errhandling` & `MATH_ERREXCEPT`) is non-zero, then the invalid floating-point exception is raised.

`[ERANGE]` (Range Error) - The value of <u>x</u> is subnormal.
            If the integer expression (`math_errhandling` & `MATH_ERRNO`) is non-zero, then `errno` is set to [`ERANGE`]. If the integer expression (`math_errhandling` & `MATH_ERREXCEPT`) is non-zero, then the underflow floating-point exception is raised.
