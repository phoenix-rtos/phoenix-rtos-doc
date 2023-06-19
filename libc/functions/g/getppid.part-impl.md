# Synopsis

`#include <unistd.h>`

`pid_t getppid(void);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getppid()` function shall return the parent process ID of the calling process.

## Return value

The `getppid()` function shall always be successful, and no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
