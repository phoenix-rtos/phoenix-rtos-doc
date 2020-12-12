###Synopsis

`#include <complex.h>`

`double cacosh(double complex z);`
`float cacoshf(float complex z);`
`long double cacoshl(long double complex z);`

###Description

The functions compute a complex arc hyperbolic cosine value.

Arguments
<u>z</u> - a complex number.
 
These functions compute the complex  arc hyperbolic cosine of <u>z</u>, with branch cut at values less than `1` along the real axis.

###Return value

These functions return the complex arc hyperbolic cosine of <u>z</u>, in the range of a half-strip [0,&#x03C0] of non-negative values along the real axis and in the interval [-i<span>&#960;</span>, +i<span>&#960;</span>] along the imaginary axis.

###Errors

No errors are defined.