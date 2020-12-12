###Synopsis

`#include <math.h>`

`double atan2(double y, double x);`
`float atan2f(float y, float x);`
`long double atan2l(long double y, long double x);`

###Description

The function computes the principal value of the arc tangent of <u>y</u>/<u>x</u> ,  using the signs of both arguments to determine the quadrant of the return value.

Arguments
<u>y</u> - first argument of `atan2` (the ordinate of the point)
<u>x</u> - second argument of `atan2` (the abscissa of the point)

###Return value

Upon successful completion, the functions returns the arc tangent of <u>y</u>/<u>x</u> in the range [-<span>&#960;</span>, <span>&#960;</span>] radians.

If <u>y</u> is `0` and <u>x</u> is < `0`, <span>&#960;</span> is returned.

If <u>y</u> is `0` and <u>x</u> is > `0`, `0` is returned.

If <u>y</u> is < `0` and <u>x</u> is `0`, -<span>&#960;</span>/2 is returned.

If <u>y</u> is > `0` and <u>x</u> is `0`, <span>&#960;</span>/2 is returned.

If <u>x</u> is `0`, a pole error does not occur.

If either <u>x</u> or <u>y</u> is `NaN`, a `NaN` is returned.

If the IEC 60559 Floating-Point option is supported, <u>y</u>/ <u>x</u> is returned. 

If <u>y</u> is `0` and <u>x</u> is `-0`, <span>&#960;</span> is returned.

If <u>y</u> is `0` and <u>x</u> is `+0`, `0` is returned.

For finite values of  <u>y</u> > `0`, if <u>x</u> is -`Inf`, <span>&#960;</span> is returned.

For finite values of  <u>y</u> > `0`, if <u>x</u> is +`Inf`, `0` is returned.

For finite values of <u>x</u>, if <u>y</u> is Inf, <span>&#960;</span>/2 is returned.

If <u>y</u> is `Inf` and <u>x</u> is -`Inf`, 3<span>&#960;</span>/4 is returned.

If <u>y</u> is `Inf` and <u>x</u> is +`Inf`, <span>&#960;</span>/4 is returned.

If both arguments are `0`, the domain error does not occur. 

###Errors

`[ERANGE]` The result underflows.

If the integer expression (`math_errhandling` & `MATH_ERRNO`) is non-zero, then `errno` is set to `[ERANGE]`. If the integer expression (`math_errhandling` & `MATH_ERREXCEPT`) is non-zero, then the underflow floating-point exception is raised.

On error, the expressions (`math_errhandling` & `MATH_ERRNO`) and (`math_errhandling` & `MATH_ERREXCEPT`) are independent of each other, but at least one of them is non-zero.

###Implementation tasks

* Error detection compatible with a description above.
* Implement atan2f().
* Implement atan2l().

###Tests

======

###EXAMPLES
None.
