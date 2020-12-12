###Synopsis

`#include <complex.h>`

`double complex creal(double complex z);`
`float complex crealf(float complex z);`
`long double complex creall(long double complex z);`

###Description

The functions compute the real part of <u>z</u>.
For a variable <u>z</u> of type `complex` the following equation is true:
    <u>z</u> == `creal`(<u>z</u>) + `cimag`(<u>z</u>)*`I`

###Return value

These functions return the real part value of the complex argument.

###Errors

No errors are defined.

###Implementation tasks

* Implement the functions: `creal()`, `crealf()` and `creall()`. 