###Synopsis

`#include <math.h>`

`double copysign(double x, double y);`
`float copysignf(float x, float y);`
`long double copysignl(long double x, long double y);`

###Description

The functions compute the value with the magnitude of <u>x</u> and the sign of <u>y</u>.

Arguments
<u>x</u> - a number whose magnitude is taken into account.
<u>y</u> - a number whose sign is taken into account.
 
###Return value

These functions return the value with the magnitude of <u>x</u>. The value has the sign of <u>y</u>.

###Errors

No errors are defined.

###Implementation tasks

* Implement the functions: `copysign()`, `copysignf()` and `copysignl()`.