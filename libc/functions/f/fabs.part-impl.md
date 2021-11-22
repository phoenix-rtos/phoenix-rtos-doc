# Synopsis 
`#include <math.h>`</br>

` double fabs(double x);`</br>

` float fabsf(float x);`</br>

` long double fabsl(long double x);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


These functions shall compute the absolute value of their argument _x_.


## Return value


Upon successful completion, these functions shall return the absolute value of _x_.
If
_x_ is `NaN`, a `NaN` shall be returned.

If _x_ is `±0`, `+0` shall be returned.

If _x_ is `±Inf`, `+Inf` shall be returned. 


## Errors


No errors are defined.




## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
