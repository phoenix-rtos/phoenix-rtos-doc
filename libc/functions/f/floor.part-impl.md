###Synopsis

`#include <math.h>`

`double floor(double x);`
`float floorf(float x);`
`long double floorl(long double x);`

###Description

Rounds <u>x</u> downward, returning the largest integral value that is not greater than <u>x</u>.

Arguments:
<u>x</u> - the value of which the largest integral value is computed.

The return value should be tested before assigning it to an integer type to avoid the undefined results of an integer overflow.

###Return value

Upon successful completion, these functions return the largest integral value not greater than <u>x</u>, expressed as a `double`, `float`, or `long double`, as appropriate for the return type of the function.
The result has the same sign as <u>x</u>.
 
If <u>x</u> is`NaN`, a `NaN` is returned.

If <u>x</u> is `0` or   `Inf`, <u>x</u> is returned. 

###Errors

No errors are defined.

###Implementation tasks

 * Implement the `floorf()` function.
 * Implement the `floorl()` function.
