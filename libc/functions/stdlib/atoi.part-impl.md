# atoi

## Synopsis

`#include <stdlib.h>`

`int atoi(const char *str);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to convert a string to an integer. The call `atoi(str)` shall be equivalent to:

`(int) strtol(str, (char **)NULL, 10)`

Except that the handling of errors may differ. If the value cannot be represented, the behavior is undefined.

## Return value

The `atoi()` function shall return the converted value if the value can be represented.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
