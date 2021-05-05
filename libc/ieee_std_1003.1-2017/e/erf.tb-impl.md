###Synopsis

`#include <math.h>`

`double erf(double x);`
`float erff(float x);`
`long double erfl(long double x);`

###Description

These functions compute the error function of their argument <u>x</u>, defined as:

${2 over sqrt pi} int from 0 to x e"^" " "{- t"^" 2" "} dt$    
    
Arguments:
    
<u>x</u> - the argument for which the error function is calculated,
    
An application wishing to check for error situations should set `errno` to zero and call `feclearexcept`(`FE_ALL_EXCEPT`) before calling these functions. On return, if `errno` is non-zero or `fetestexcept`(`FE_INVALID` | `FE_DIVBYZERO` | `FE_OVERFLOW` | `FE_UNDERFLOW`) is non-zero, an error has occurred.

###Return value

On success the functions return the value of the error function.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0`, `0` is returned.

If <u>x</u> is `Inf`, `1` is returned. 

If the correct value would cause underflow, a range error occurs, and `erf()`, `erff()`, and `erfl()` return `DBL_MIN-1`, `FLT_MIN-1`, and `LDBL_MIN-1`, respectively.

###Errors

[`ERANGE`] The result underflows.

If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` is set to [`ERANGE`]. If the integer expression (`math_errhandling & MATH_ERREXCEPT`) is non-zero, then the underflow floating-point exception is raised.

###Implementation tasks

* Implement the `erf()` function.
* Implement the `erff()` function.
* Implement the `erfl()` function.
