###Synopsis

`#include <math.h>`

`double ceil(double x);`
`float ceilf(float x);`
`long double ceill(long double x);`

###Description

Rounds <u>x</u> upward, returning the smallest integral value that is not less than <u>x</u>.

Arguments:
<u>x</u> - a value to be rounded.

The result has the same sign as <u>x</u>.

If <u>x</u> is `NaN`, a `NaN` is returned.

If <u>x</u> is `0` or `Inf`, <u>x</u> is returned. 

###Return value
The rounded <u>x</u> value.

###Errors
These functions raise the inexact floating-point exception if the result differs in value from the argument.
No errors are defined.

###Implementation tasks

* `NaN`, `Inf` and `0` <u>x</u> value handling.
* Negative values of argument handling.
* The return value is tested before assigning it to an integer type to avoid the undefined results of an integer overflow.
* These functions raise the inexact floating-point exception if the result differs in value from the argument.
* Implement `ceilf()` function.
* Implement `ceill()` function.
###Tests

======

###EXAMPLES
None.