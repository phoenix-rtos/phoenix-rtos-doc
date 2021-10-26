# Synopsis

`#include <math.h>`

`double acos(double x);`

`float acosf(float x);`

`long double acosl(long double x);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The function computes the principal value of the arc cosine of argument <u>x</u>, expressed in radians.

### Arguments

`x` - value whose arc cosine is computed, in the interval [`-1`,`1`].

If the argument is out of this interval, a domain error occurs.

An application wishing to check for error situations should set `errno` to zero and call `feclearexcept`(`FE_ALL_EXCEPT`) before calling this function. On return, if `errno` is non-zero or `fetestexcept`(`FE_INVALID` | `FE_DIVBYZERO` | `FE_OVERFLOW` | `FE_UNDERFLOW`) is non-zero, an error has occurred.

## Return value

The principal value of the arc cosine of `x`, expressed in radians.

For finite values of `x` not in the range [-`1`,`1`], a domain error occurs, and a `NaN` is returned.

## Errors

[EDOM] (domain error) - the `x` argument is finite and is not in the range [-`1`,`1`].

## Tests

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
