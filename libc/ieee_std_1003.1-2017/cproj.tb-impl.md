###Synopsis

`#include <complex.h>`

`double complex cproj(double complex z);`
`float complex cprojf(float complex z);`
`long double complex cprojl(long double complex z);`

###Description

The functions compute a projection of <u>z</u> onto the Riemann sphere: <u>z</u> projects to <u>z</u>, except that all complex infinities (even those with one infinite part and one `NaN` part) project to positive infinity on the real axis. If <u>z</u> has an infinite part, then `cproj`(<u>z</u>) is equivalent to:

`INFINITY + I * copysign(0.0, cimag(z))`


###Return value

These functions return the value of the projection onto the Riemann sphere.

###Errors

No errors are defined.

###Implementation tasks

* Implement the functions: cproj(), cprojf() and cprojl(),