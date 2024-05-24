# frexp

## Synopsis

`#include <math.h>`

`double frexp(double num, int *exp);`

`float frexpf(float num, int *exp);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to extract mantissa and exponent from a double precision number. These functions shall break a
floating-point number _num_ into a normalized fraction and an integral power of 2. The integer exponent shall be
stored in the int object pointed to by _exp_.

## Return value

For finite arguments, these functions shall return the value `x`, such that `x` has a magnitude in the interval `[½,1)`
or `0`, and _num_ equals `x` times `2` raised to the power _*exp_.

* If _num_ is `NaN`, a `NaN` shall be returned, and the value of _*exp_ is unspecified.
* If _num_ is `±0`, `±0` shall be returned, and the value of _*exp_ shall be `0`.
* If _num_ is `±Inf`, _num_ shall be returned, and the value of _*exp_ is unspecified.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
