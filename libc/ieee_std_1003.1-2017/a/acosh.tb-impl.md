# Synopsis

`#include <math.h>`

`double acosh(double x);`

`float acoshf(float x);`

`long double acoshl(long double x);`

## Status

To be implemented

## Description

The function computes the inverse hyperbolic cosine of its argument <u>x</u>.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept` (`FE_ALL_EXCEPT`) before calling this function. On return, if `errno` is non-zero or `fetestexcept` (`FE_INVALID` | `FE_DIVBYZERO` | `FE_OVERFLOW` | `FE_UNDERFLOW`) is non-zero, an error has occurred.

Arguments:
<u>x</u> - an argument for which inverse hyperbolic cosine is computed.

## Return value

Upon successful completion, this function returns the inverse hyperbolic cosine of its argument.

For finite values of <u>x</u>  < `1`, a domain error occurs and `NaN` is returned.
If <u>x</u>  is `NaN`, a `NaN` is returned.
If <u>x</u>  is +`1`, +`0` is returned.
If <u>x</u>  is +`Inf`, +`Inf` is returned.
If <u>x</u> is -`Inf`, a domain error occurs, and a `NaN` is returned. 

## Errors

[`EDOM`] (Domain Error) - The <u>x</u> argument is finite and less than +`1.0` or is -`Inf`.

If the integer expression (`math_errhandling` & `MATH_ERRNO`) is non-zero, then `errno` is set to [`EDOM`].

If the integer expression (`math_errhandling` & `MATH_ERREXCEPT`) is non-zero, then the invalid floating-point exception is raised.

## Comments

On error, the expressions (`math_errhandling` & `MATH_ERRNO`) and (`math_errhandling` & `MATH_ERREXCEPT`) are independent of each other, but at least one of them must be non-zero.
