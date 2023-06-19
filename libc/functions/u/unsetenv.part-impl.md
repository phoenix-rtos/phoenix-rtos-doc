# Synopsis

`#include <stdlib.h>`

`int unsetenv(const char *name);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `unsetenv()` function shall remove an environment variable from the environment of the calling process. The name
argument points to a string, which is the name of the variable to be removed. The named argument shall not contain
a `'='` character. If the named variable does not exist in the current environment, the environment shall be
unchanged and the function is considered to have completed successfully.

The `unsetenv()` function shall update the list of pointers to which `environ` points.

## Return value

Upon successful completion, zero shall be returned. Otherwise, `-1` shall be returned, `errno` set to indicate the
error, and the environment shall be unchanged.

## Errors

The function shall fail if:

* `EINVAL` - The name argument points to an empty string, or points to a string containing a `'='` character.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
