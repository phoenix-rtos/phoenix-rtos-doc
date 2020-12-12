###Synopsis

`#include <math.h>`

`double frexp(double num, int* exp);`
`float frexpf(float num, int *exp);`
`long double frexpl(long double num, int *exp);`

###Description

The function breaks the floating point number <u>num</u> into its binary significant

* (a floating point with an absolute value between `0.5`(included) and `1.0`(excluded))
* an integral power of `2`.
 
Arguments:

<u>num</u> - a floating point number to be broken,
<u>exp</u> - an integer exponent. 

###Return value

For finite arguments, these functions return the value `x`, such that `x` has a magnitude in the interval `[,1)` or `0`, and <u>num</u> equals `x` times `2` raised to the power `*exp`.

If <u>num</u> is `NaN`, a `NaN` is returned, and the value of *<u>exp</u> is unspecified.

If <u>num</u> is `0`, `0` is returned, and the value of *<u>exp</u> is `0`.

If <u>num</u> is `Inf`, <u>num</u> is returned, and the value of *<u>exp</u> is unspecified. 

###Errors

No errors are defined.

###Implementation tasks

* `frexp()`: remove strange constant: `1022`.
* `normalizeSub()`: remove strange constants from the code.
* Implement `frexpf()`.
* Implement `frexpl()`.
