###Synopsis

`#include <math.h>`

`long double asinl(long double x);`

###Description

The function returns the principal value of the arc sine of x, expressed in radians.

Arguments:
<u>x</u> - value whose arc sine is computed, in the interval [-1,+1].

###Return value
Upon successful completion, the function shall return the arc sine of x, in the range [-<span>&#960;</span>/2,<span>&#960;</span>/2] radians.

For finite values of <u>x</u>  not in the range [-1,1], a domain error shall occur, and either a NaN (if supported) or  an implementation-defined value shall be returned.

If <u>x</u> is NaN, a NaN shall be returned.

If <u>x</u> is 0, <u>x</u> shall be returned.

If <u>x</u> is Inf, a domain error shall occur, and a NaN shall be returned.

If <u>x</u> is subnormal, a range error may occur and <u>x</u> should be returned.

If <u>x</u> is not returned, asinl() shall return an implementation-defined value no greater in magnitude than DBL_MIN respectively.

###Errors
[EDOM] (Domain Error) -     The <u>x</u> argument is finite and is not in the range [-1,1] or is Inf. 

If the integer expression (math_errhandling & MATH_ERRNO) is non-zero, then errno shall be set to [EDOM]. If the integer expression (math_errhandling & MATH_ERREXCEPT) is non-zero, then the invalid floating-point exception shall be raised.

[ERANGE] (Range Error) - The value of <u>x</u> is subnormal.

If the integer expression (math_errhandling & MATH_ERRNO) is non-zero, then errno shall be set to [ERANGE]. If the integer expression (math_errhandling & MATH_ERREXCEPT) is non-zero, then the underflow floating-point exception shall be raised.
