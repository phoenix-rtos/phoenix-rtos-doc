# Synopsis

`#include <unistd.h>`

`uid_t getuid(void);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getuid()` function shall return the real user ID of the calling process. The `getuid()` function shall not modify
`errno`.

## Return value

The `getuid()` function shall always be successful and no return value is reserved to indicate the error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
