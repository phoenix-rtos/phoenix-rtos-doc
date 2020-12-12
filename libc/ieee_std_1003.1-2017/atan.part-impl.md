###Synopsis

`#include <math.h>`

`double atan(double x);`
`float atanf(float x);`
`long double atanl(long double x);`

###Description

These functions return the principal value of the `arc tan` of <u>x</u>, expressed in radians.

Arguments
<u>x</u> - the value for which `arc tan` is computed.

###Return value

Upon successful completion, the function returns the arc tangent of <u>x</u> in the range [-<span>&#960;</span>/2,<span>&#960;</span>/2] radians. 

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0`, <u>x</u> is returned.

If <u>x</u> is `Inf`, <span>&#960;</span>/2 is returned.

If <u>x</u> is subnormal, a range error occurs and <u>x</u> is returned. 

###Errors

`[ERANGE]` (Range Error) - the value of <u>x</u> is subnormal.

If the integer expression (`math_errhandling & MATH_ERRNO`) is non-zero, then `errno` is set to `[ERANGE]`. If the integer expression (`math_errhandling & MATH_ERREXCEPT`) is non-zero, then the underflow floating-point exception is raised. 

On error, the expressions (`math_errhandling & MATH_ERRNO`) and (`math_errhandling & MATH_ERREXCEPT`) are independent of each other, but at least one of them must be non-zero.

###Implementation tasks

* implement ERANGE error detection,
* implement NaN, Inf and subnormal argument handling,
* implement  underflow floating-point exception raising. 

* implement atanf(),
* implement atanl(),

###Tests

======

###EXAMPLES
None.