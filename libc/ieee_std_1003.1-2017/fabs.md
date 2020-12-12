###Synopsis

`#include <math.h>`

`double fabs(double x);`
`float fabsf(float x);`
`long double fabsl(long double x);`

###Description

The  functions compute the absolute value of their argument <u>x</u>,| <u>x</u>|.

Arguments:

<u>x</u> - the value of which the absolute value is computed.

###Return value

Upon successful completion, these functions return the absolute value of <u>x</u>.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0`, `0` is returned.

If <u>x</u> is `Inf`, +`Inf` is returned.

###Errors

No errors are defined.

###Implementation tasks

 * Implement the functions