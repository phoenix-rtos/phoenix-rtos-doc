# Synopsis 
`#include <math.h>`</br>

` double copysign(double x, double y);`</br>

` float copysignf(float x, float y);`</br>

` long double copysignl(long double x, long double y);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


These functions shall produce a value with the magnitude of _x_ and the sign of _y_. On implementations that represent
a signed zero but do not treat negative zero consistently in arithmetic operations, these functions regard the sign of zero as
positive.


## Return value


Upon successful completion, these functions shall return a value with the magnitude of _x_ and the sign of _y_.


## Errors


No errors are defined.




## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
