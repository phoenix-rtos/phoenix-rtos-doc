###Synopsis

`#include <complex.h>`

`double complex catanh(double complex z);`
`float complex catanhf(float complex z);`
`long double complex catanhl(long double complex z);`

###Description

The functions compute the complex arc hyperbolic tangent of <u>z</u>, with branch cuts outside the interval `[-1, +1]` along the real axis.

Arguments
<u>z</u> - a complex number.
 
###Return value

These functions return the complex arc hyperbolic tangent value, in the range of a strip mathematically unbounded along the real axis and in the interval [-`i`<span>&#960;</span>/2, +`i`<span>&#960;</span>/2] along the imaginary axis.

###Errors

No errors are defined.