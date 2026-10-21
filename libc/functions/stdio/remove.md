# remove

## Synopsis

```c
#include <stdio.h>

int remove(const char *path);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `remove()` function shall cause the file named by the path name pointed to by _path_ to be no longer accessible by
that name. A subsequent attempt to open that file using that name shall fail, unless it is created as new.

* If _path_ does not name a directory, `remove(path)` shall be equivalent to `unlink(path)`.
* If _path_ names a directory, `remove(path)` shall be equivalent to `rmdir(path)`.

## Return value

Refer to `rmdir()` or `unlink()`.

## Errors

Refer to `rmdir()` or `unlink()`.

## POSIX deviations

The length of a path name component is not checked against `NAME_MAX` by libphoenix (except in `mkdir()`), but by the
filesystem server, against the name length limit of the filesystem, which may differ from `NAME_MAX`. The error reported
for a too long component therefore depends on the filesystem: for example `jffs2` reports `ENAMETOOLONG` already when
the name is looked up, while `dummyfs` reports `ENAMETOOLONG` only when a new directory entry is created, and otherwise
the lookup of the name fails with `ENOENT`. On targets where `NAME_MAX` is 64 (armv7m, armv7r, armv8m and armv8r),
`dummyfs` accepts names of up to 255 bytes, so files with names longer than `NAME_MAX` can exist.
