# modf

## Synopsis

`#include <math.h>`

`double modf(double x, double *iptr);`

`float modff(float value, float *iptr);`

`long double modfl(long double value, long double *iptr);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall break the argument _x_ into integral and fractional parts, each of which has the same sign as the
argument. It stores the integral part as a double (for the `modf()` function), a float (for the `modff()` function), or
a long double (for the `modfl()` function), in the object pointed to by _iptr_.

## Return value

Upon successful completion, these functions shall return the signed fractional part of _x_.

* If _x_ is `NaN`, a `NaN` shall be returned, and _*iptr_ shall be set to a `NaN`.
* If _x_ is `±Inf`, `±0` shall be returned, and _*iptr_ shall be set to `±Inf`.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
