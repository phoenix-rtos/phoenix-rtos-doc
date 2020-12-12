###Synopsis

`#include <math.h>`

`double cbrt(double x);`
`float  cbrtf(float  x);`
`long double  cbrtl(long double x);`

###Description

The functions compute the  the real cube root of their argument <u>x</u>.

Arguments
<u>x</u> - a number.
 
###Return value

On success these functions return the real cube root of their argument <u>x</u>.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0` or `Inf`, <u>x</u> is returned.

###Errors

No errors are defined.

###Implementation tasks
* Implement cbrt()function.
* Implement cbrtf()function.
* Implement cbrtl()function.