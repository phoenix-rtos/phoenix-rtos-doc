# setenv

## Synopsis

`#include <stdlib.h>`

`int setenv(const char *envname, const char *envval, int overwrite);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `setenv()` function shall update or add a variable in the environment of the calling process. The _envname_
argument points to a string containing the name of an environment variable to be added or altered. The environment
variable shall be set to the value to which _envval_ points. The function shall fail if _envname_ points to a string
which contains a `'='` character. If the environment variable named by _envname_ already exists and the value of
overwrite is non-zero, the function shall return success and the environment shall be updated. If the environment
variable named by _envname_ already exists and the value of overwrite is zero, the function shall return success and
the environment shall remain unchanged

The `setenv()` function shall update the list of pointers to which environ points.

The strings described by _envname_ and _envval_ are copied by this function.

The `setenv()` function need not be thread-safe.

## Return value

Upon successful completion, zero shall be returned. Otherwise, `-1` shall be returned, `errno` set to indicate the
error, and the environment shall be unchanged.

## Errors

The `seteuid()` function shall fail if:

* `EINVAL` - The envname argument points to an empty string or points to a string containing a `'='` character.

* `ENOMEM` - Insufficient memory was available to add a variable or its value to the environment.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
