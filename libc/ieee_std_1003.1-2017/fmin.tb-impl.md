###Synopsis

`#include <math.h>`

`double fmin(double x, double y);`
`float fminf(float x, float y);`
`long double fminl(long double x, long double y);`

###Description

These functions determine the minimum numeric value of their arguments. 
`NaN` arguments are treated as missing data: if one argument is a `NaN` and the other numeric, then these functions choose the numeric value.

Arguments:
<u>x</u> - the first argument.
<u>y</u> - the second argument.


###Return value

Upon successful completion, these functions return the minimum numeric value of their arguments.

If just one argument is a `NaN`, the other argument is returned.

If <u>x</u> and <u>y</u> are `NaN`, a `NaN` is returned. 

###Errors

No errors are defined.

###Implementation tasks

 * Implement the `fmin()` function.
 * Implement the `fminf()` function.
 * Implement the `fminl()` function.
