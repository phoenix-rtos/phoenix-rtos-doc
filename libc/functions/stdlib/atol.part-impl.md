# atol

## Synopsis

`#include <stdlib.h>`

`long atol(const char *nptr);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to convert a string to a long integer. Except as noted below, the call `atol(nptr)`
shall be equivalent to:

`strtol(`_`nptr`_`, (char **)NULL, 10)`

The handling of errors may differ. If the value cannot be represented, the behavior is undefined.

## Return value

This function shall return the converted value if the value can be represented.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
