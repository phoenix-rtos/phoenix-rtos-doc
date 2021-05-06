# Synopsis

`#include <math.h>`

`long double acoshl(long double x);`

## Status

To be implemented

## Description

The function shall compute the inverse hyperbolic cosine of the argument x.

Arguments:
<u>x</u> - value whose arc cosine is computed, in the interval [-1,+1].
If the argument is out of this interval, a domain error occurs.

An application wishing to check for error situations should set <i>errno</i> to zero and call <i>feclearexcept</i>(FE_ALL_EXCEPT) before calling this function. On return, if <i>errno</i> is non-zero or <i>fetestexcept</i>(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW) is non-zero, an error has occurred.

## Return value

Upon successful completion, the function shall return the inverse hyperbolic cosine of its argument.

For finite values of x < 1, a domain error shall occur, and either a NaN (if supported), or an implementation-defined value shall be returned.

If x is NaN, a NaN shall be returned.

If x is +1, +0 shall be returned.

If x is +Inf, +Inf shall be returned.

If x is -Inf, a domain error shall occur, and a NaN shall be returned. 

## Errors

[EDOM] - (Domain Error) the x argument is finite and less than +1.0, or is -Inf.

If the integer expression (<i>math_errhandling</i> & MATH_ERRNO) is non-zero, then <i>errno</i> shall be set to [EDOM].

If the integer expression (<i>math_errhandling</i> & MATH_ERREXCEPT) is non-zero, then the invalid floating-point exception shall be raised.

## Comments

On error, the expressions (<i>math_errhandling</i> & MATH_ERRNO) and (<i>math_errhandling</i> & MATH_ERREXCEPT) are independent of each other, but at least one of them must be non-zero.
