# getgid

## Synopsis

`#include <unistd.h>`

`gid_t getgid(void);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getgid()` function shall return the real group ID of the calling process. The `getgid()` function shall not
modify `errno`.

## Return value

The `getgid()` function shall always be successful, and no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
