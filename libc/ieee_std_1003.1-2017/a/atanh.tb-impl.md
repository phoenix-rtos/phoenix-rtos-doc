###Synopsis

`#include <math.h>`

`double atanh(double x);`
`float atanhf(float x);`
`long double atanhl(long double x);`

###Description

The functions compute the inverse hyperbolic tangent of their argument <u>x</u>.

Arguments
<u>x</u> - the argument of `atanh`

###Return value

Upon successful completion, these functions shall return the inverse hyperbolic tangent of their argument.

###Errors

`[EDOM]`(`Domain Error`) - The x argument is finite and not in the range [`-1`,`1`] or is `Inf`.
    If the integer expression (`math_errhandling` & `MATH_ERRNO`) is non-zero, then `errno` shall be set to `[EDOM]`. If the integer expression (`math_errhandling` & `MATH_ERREXCEPT`) is non-zero, then the invalid floating-point exception is raised.

`[ERANGE]`(`Pole Error`) - The x argument is `1`.
    If the integer expression (`math_errhandling` & `MATH_ERRNO`) is non-zero, then `errno` shall be set to `[ERANGE]`. If the integer expression (`math_errhandling` & `MATH_ERREXCEPT`) is non-zero, then the divide-by-zero floating-point exception is raised.

`[ERANGE]`(`Range Error`) - The value of <u>x</u> is subnormal. 
 
If the integer expression (`math_errhandling` & `MATH_ERRNO`) is non-zero, then `errno` is set to `[ERANGE]`. If the integer expression (`math_errhandling` & `MATH_ERREXCEPT`) is non-zero, then the underflow floating-point exception is raised.

On error, the expressions (`math_errhandling` & `MATH_ERRNO`) and (`math_errhandling` & `MATH_ERREXCEPT`) are independent of each other, but at least one of them is non-zero.
