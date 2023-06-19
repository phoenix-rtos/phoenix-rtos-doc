# Synopsis

`#include <unistd.h>`

`gid_t getegid(void);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getegid()` function shall return the effective group ID of the calling process. The `getegid()` function shall
not modify `errno`.

## Return value

The `getegid()` function shall always be successful and no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
