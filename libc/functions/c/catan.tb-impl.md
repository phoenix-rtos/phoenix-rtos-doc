###Synopsis

`#include <complex.h>`

`double complex catan(double complex z);`
`float complex catanf(float complex z);`
`long double complex catanl(long double complex z);`

###Description

The functions compute the complex arc tangent of <u>z</u>, with branch cuts outside the interval `[-i, +i]` along the imaginary axis.

Arguments
<u>z</u> - a complex number.
 
###Return value

These functions return the complex arc tangent value, in the range of a strip mathematically unbounded along the imaginary axis and in the interval [-<span>&#960;</span>/2, +<span>&#960;</span>/2] along the real axis.

###Errors

No errors are defined.