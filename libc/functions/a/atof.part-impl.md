# Synopsis

`#include <stdlib.h>`</br>

`double atof(const char *str);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to convert a string to a double-precision number. The call `atol(str)` shall be equivalent to:

`strtod(str,(char **)NULL)`,

except that the handling of errors may differ. If the value cannot be represented, the behavior is undefined.

## Return value

The `atof()` function shall return the converted value if the value can be represented.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
