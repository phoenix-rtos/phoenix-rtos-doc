# geteuid

## Synopsis

`#include <unistd.h>`

`uid_t geteuid(void);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `geteuid()` function shall return the effective user ID of the calling process. The `geteuid()` function shall not
modify `errno`.

## Return value

The `geteuid()` function shall always be successful, and no return value is reserved to indicate an error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
