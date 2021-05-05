###Synopsis

`#include <math.h>`

`double fmax(double x, double y);`
`float fmaxf(float x, float y);`
`long double fmaxl(long double x, long double y);`

###Description

These functions  determine the maximum numeric value of their arguments.

Arguments:
<u>x</u> - the first argument of the function.
<u>y</u> - the second argument of the function.

`NaN` arguments is treated as missing data: if one argument is a `NaN` and the other numeric, then these functions  choose the numeric value. 

###Return value

Upon successful completion, these functions  return the maximum numeric value of their arguments.

If just one argument is a `NaN`, the other argument is returned.

If <u>x</u> and <u>y</u> are `NaN`, a `NaN` is returned. 

###Errors

No errors are defined.
    
###Implementation tasks

 * Implement the `fmax()` function.
 * Implement the `fmaxf()` function.
 * Implement the `fmaxl()` function.
