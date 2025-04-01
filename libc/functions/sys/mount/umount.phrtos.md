# umount

## Synopsis

`#include <sys/mount.h>`

`int umount(const char *path);`

## Status

Declared, not implemented

## Conformance

Feniks-RTOS specific

## Description

`umount()` remove the attachment of the filesystem mounted on target under _path_.

## Return value

On success, zero is returned. On error, `-1` is returned, and `errno` is set to indicate the error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../../index.md)
2. [Table of Contents](../../../../index.md)
