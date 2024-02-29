# clearenv

## Synopsis

`#include <stdlib.h>`</br>

`int clearenv(void);`</br>

## Status

Partially implemented

## Conformance

Various UNIX variants (DG/UX, HP-UX, QNX, ...)

## Description

The `clearenv()` function clears the environment of all name-value pairs and sets the value of the external variable
environ to `NULL`. After this call, new variables can be added to the environment using `putenv()` and `setenv()`.

## Return value

Upon successful completion, zero shall be returned.

## Errors

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
