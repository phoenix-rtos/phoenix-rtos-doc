# Synopsis 
`#include <math.h>`</br>

` double cos(double x);`</br>

` float cosf(float x);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description

These functions shall compute the cosine of their argument _x_, measured in radians.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept(FE_ALL_EXCEPT)` before calling these functions. On return, if `errno` is non-zero or `fetestexcept(FE_INVALID | FE_DIVBYZERO | FE_OVERFLOW | FE_UNDERFLOW)` is non-zero, an error has occurred.


## Return value


Upon successful completion, these functions shall return the cosine of _x_.

* If _x_ is `NaN`, a `NaN` shall be returned.

* If _x_ is `±0`, the value `1.0` shall be returned.

* If _x_ is `±Inf`, a domain error shall occur, and a `NaN` shall be returned.

## Errors


These functions shall fail if:

* Domain Error
 
  The _x_ argument is `±Inf`. 

  If the integer expression `(math_errhandling & MATH_ERRNO)` is non-zero, then `errno` shall be set to `EDOM`. If the integer expression `(math_errhandling & MATH_ERREXCEPT)` is non-zero, then the invalid floating-point exception shall be raised. 


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
