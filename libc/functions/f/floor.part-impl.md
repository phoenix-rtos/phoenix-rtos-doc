# Synopsis 
`#include <math.h>`</br>

` double floor(double x);`</br>

` float floorf(float x);`</br>

` long double floorl(long double x);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


These functions shall compute the largest integral value not greater than _x_.


## Return value


The result shall have the same sign as _x_.

Upon successful completion, these functions shall return the largest integral value not greater than _x_, expressed as a double, float, or long double, as appropriate for the return type of the function.

If _x_ is `NaN`, a `NaN` shall be returned.

If _x_ is `±0` or `±Inf`, _x_ shall be returned.


## Errors


No errors are defined.



## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
