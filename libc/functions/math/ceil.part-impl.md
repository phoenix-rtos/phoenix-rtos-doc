# ceil

## Synopsis

`#include <math.h>`

`double ceil(double x);`

`float ceilf(float x);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall compute the smallest integral value not less than _x_.

## Return value

The result shall have the same sign as _x_.

Upon successful completion, `ceil()` and `ceilf()` shall return the smallest integral value not less than _x_, expressed
as a type double, float, or long double, respectively.

* If _x_ is `NaN`, a `NaN` shall be returned.

* If _x_ is `±0` or `±Inf`, _x_ shall be returned.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
