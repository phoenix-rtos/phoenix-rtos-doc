# Synopsis

`#include <ctype.h>`

`int tolower(int c);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `tolower()` function has as a domain a type `int`, the value of which is representable as a `unsigned char` or the
value of `EOF`.

If the argument has any other value, the behavior is undefined.

If the argument of `tolower()` represents an uppercase letter, and there exists a corresponding lowercase letter as
defined by character type information in the current locale respectively the result shall be the corresponding lowercase
letter.

All other arguments in the domain are returned unchanged.

## Return value

Upon successful completion, the `tolower()` function shall return the lowercase letter corresponding to the argument
passed, otherwise, they shall return the argument unchanged.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
