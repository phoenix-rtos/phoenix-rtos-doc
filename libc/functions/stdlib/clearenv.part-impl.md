# clearenv

## Synopsis

`#include <stdlib.h>`

`int clearenv(void);`

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
