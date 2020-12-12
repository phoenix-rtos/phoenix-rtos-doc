###Synopsis

`#include <complex.h>`

`double cimag(double complex z);`
`float cimagf(float complex z);`
`long double cimagl(long double complex z);`

###Description

The functions compute the imaginary part of <u>z</u>.

Arguments:
<u>z</u> - a variable of complex type.

###Return value

These functions return the imaginary part value of the complex variable <u>z</u> as a real.

###Errors

No errors are defined.

###Implementation tasks

Implement the functions `cimag()`, `cimagf()`, `cimagl()` 

###Tests

======

###Examples

For a variable <u>z</u> of complex type the following equation is true:

<u>z</u> == `creal`(<u>z</u>) + `cimag()`(<u>z</u>)*`I`


