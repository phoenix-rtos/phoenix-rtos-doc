
###Synopsis

`#include <complex.h>`

`double cacos(double complex z);`
`float cacosf(float complex z);`
`long double cacosl(long double complex z);`

###Description

The functions compute a complex arc cosine value.

Arguments
<u>z</u> - a complex number.
 
These functions compute the complex  arc cosine of <u>z</u>, with branch cuts outside the interval [-`1`, +`1`] along the real axis.
 
###Return value

These functions return the complex arc cosine of <u>z</u>, in the range of a strip mathematically unbounded along the imaginary axis and in the interval [0,&#x03C0] along the real axis.

###Errors

No errors are defined.