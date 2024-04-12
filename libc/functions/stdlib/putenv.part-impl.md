# putenv

## Synopsis

`#include <stdlib.h>`

`int putenv(char *string);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `putenv()` function shall use the string argument to set environment variable values. The string argument should
point to a string of the form "name = value". The `putenv()` function shall make the value of the environment variable
name equal to value by altering an existing variable or creating a new one. In either case, the string pointed to by
string shall become part of the environment, so altering the string shall change the environment.

The `putenv()` function need not be thread-safe.

## Return value

Upon successful completion, `putenv()` shall return `0`; otherwise, it shall return a non-zero value and set `errno` to
indicate the error.

## Errors

The function may fail if:

* [`EINVAL`] - The string argument doesn't contain `'='`.

* [`ENOMEM`] - Insufficient memory was available.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
