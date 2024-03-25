# creat

## Synopsis

`#include <sys/stat.h>`

`#include <fcntl.h>`

`int creat(const char *path, mode_t mode);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to create a new file or rewrite an existing one. The `creat()` function shall behave as if it is
implemented as follows:

```c
int creat(const char *path, mode_t mode)
{
	return open(path, O_WRONLY|O_CREAT|O_TRUNC, mode);
}
```

## Return value

Refer to [open](../fcntl/open.part-impl.md).

## Errors

Refer to [open](../fcntl/open.part-impl.md).

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
