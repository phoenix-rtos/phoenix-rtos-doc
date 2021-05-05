###Synopsis

`#include <math.h>`

`double cos(double x);`
`float cosf(float x);`
`long double cosl(long double x);`

###Description

The functions calculate the cosine of an angle of <u>x</u> radians.

Arguments:
<u>x</u> - the angle, which cosine is to be calculated.

###Return value

On success, these functions return the cosine of <u>x</u>.

If <u>x</u> is a `NaN`, a `NaN` is returned.

If <u>x</u> is positive infinity or negative infinity, a domain error occurs, and a `NaN` is returned.

###Errors

[`EDOM`] -Domain Error - the <u>x</u> argument is `Inf`.

If the integer expression (`math_errhandling & MATH_ERRNO`) is non-zero, then `errno` is set to [`EDOM`], else the invalid floating-point exception is raised.

On error, the expressions (`math_errhandling & MATH_ERRNO`) and (`math_errhandling & MATH_ERREXCEPT`) are independent of each other, but at least one of them must be non-zero.
###Implementation tasks

* Implement error handling,
* Implement the functions: `cosf()` and `cosl()`.

### Examples:
1. Cosine of a `45`-degree angle
`double radians = 45 * M_PI / 180;
double result;
...
result = cos(radians);`

2. Cosine of a `45`-degree angle - another way
`double radians = M_PI / 4;
double result;
...
result = cos(radians);`
