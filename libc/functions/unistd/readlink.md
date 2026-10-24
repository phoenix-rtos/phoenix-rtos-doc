# readlink

## Synopsis

```c
#include <unistd.h>

ssize_t readlink(const char *restrict path, char *restrict buf, size_t bufsize);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `readlink()` function shall place the contents of the symbolic link referred to by _path_ in the buffer _buf_ which
has size _bufsize_. If the number of bytes in the symbolic link is less than _bufsize_, the contents of the remainder of
_buf_ are unspecified. If the _buf_ argument is not large enough to contain the link content, the first _bufsize_ bytes
shall be placed in _buf_.

If the value of _bufsize_ is greater than `SSIZE_MAX`, the result is implementation-defined.

Upon successful completion, `readlink()` shall mark for update the last data access timestamp of the symbolic link.

Applications should not assume that the contents of the symbolic link placed in _buf_ are null-terminated.

## Return value

Upon successful completion, `readlink()` shall return the count of bytes placed in the buffer. Otherwise, it shall
return a value of `-1`, leave the buffer unchanged, and set `errno` to indicate the error.

## Errors

The `readlink()` function shall fail if:

* `EACCES` - Search permission is denied for a component of the path prefix of _path_.

* `EINVAL` - The _path_ argument names a file that is not a symbolic link.

* `EIO` - An I/O error occurred while reading from the file system.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than the name length limit of the filesystem,
which may differ from `NAME_MAX` (see POSIX deviations).

* `ENOENT` - A component of _path_ does not name an existing file or _path_ is an empty string.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a
directory, or the _path_ argument contains at least one non-`<slash>` character and ends with one or more trailing
`<slash>` characters and the last path name component names an existing file that is neither a directory nor a symbolic
link to a directory.

The `readlink()` function may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

## POSIX deviations

The length of a path name component is not checked against `NAME_MAX` by libphoenix, but by the filesystem server,
against the name length limit of the filesystem, which may differ from `NAME_MAX`. `readlink()` only looks the name
up, so the error reported for a too-long component depends on the filesystem: `jffs2` reports `ENAMETOOLONG`, while
`ext2` and `dummyfs` check the length only when a new directory entry is created, so the lookup of the name fails with
`ENOENT`. Checking every component in libphoenix would require knowing the name length limit of every mounted
filesystem in each process, so the check is left to the filesystem server, which knows its own limit.
