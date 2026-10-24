# creat

## Synopsis

```c
#include <sys/stat.h>

#include <fcntl.h>

int creat(const char *path, mode_t mode);
```

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

Refer to [open](open.md).

## Errors

Refer to [open](open.md).

## POSIX deviations

`creat()` has the POSIX deviations of [open](open.md). In particular, the length of a path name component is checked by
the filesystem server against the name length limit of the filesystem instead of `NAME_MAX`. On ia32, where `NAME_MAX`
is 256 and `ext2` accepts names of up to 255 bytes, a name longer than `NAME_MAX` is rejected with `ENAMETOOLONG` when
the new directory entry is created, and so is a name of exactly 256 bytes. On targets where `NAME_MAX` is 64 (armv7m,
armv7r, armv8m, and armv8r), a file with a name of up to 255 bytes can be created.
