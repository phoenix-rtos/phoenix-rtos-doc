###Synopsis

`#include <math.h>`

`long double acosl(long double x);`

###Description

Shall compute the principal value of the arc cosine of the argument x, expressed in radians.

Arguments:
<u>x</u> - value whose arc cosine is computed, in the interval [-1,+1].
If the argument is out of this interval, a domain error occurs.

An application wishing to check for error situations should set <i>errno</i> to zero and call <i>feclearexcept</i>(FE_ALL_EXCEPT) before calling this function. On return, if <i>errno</i> is non-zero or <i>fetestexcept</i>(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW) is non-zero, an error has occurred.

###Return value
The principal value of the arc cosine of x, expressed in radians.

For finite values of x not in the range [-1,1], a domain error shall occur, and either a NaN (if supported), or an implementation-defined value shall be returned.

If x is NaN, a NaN shall be returned.

If x is +1, +0 shall be returned.

If x is Inf, a domain error shall occur, and a NaN shall be returned. 

###Errors

Domain Error - the <i>x</i> argument is finite and is not in the range [-1,1], or is Inf.

If the integer expression (<i>math_errhandling</i> & MATH_ERRNO) is non-zero, then <i>errno</i> shall be set to [EDOM] (domain error). If the integer expression (<i>math_errhandling</i> & MATH_ERREXCEPT) is non-zero, then the invalid floating-point exception shall be raised.

On error, the expressions (<i>math_errhandling</i> & MATH_ERRNO) and (<i>math_errhandling </i>& MATH_ERREXCEPT) are independent of each other, but at least one of them must be non-zero.

