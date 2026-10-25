# statvfs

## Synopsis

```c
#include <sys/statvfs.h>

int fstatvfs(int fildes, struct statvfs *buf);

int statvfs(const char *restrict path, struct statvfs *restrict buf);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fstatvfs()` function shall obtain information about the file system containing the file referenced by _fildes_.

The `statvfs()` function shall obtain information about the file system containing the file named by _path_.

For both functions, the _buf_ argument is a pointer to a `statvfs` structure that shall be filled. Read, write, or
execute permission of the named file is not required.

The following flags can be returned in the `f_flag` member:

* `ST_RDONLY` - Read-only file system.

* `ST_NOSUID` - Setuid/setgid bits ignored by exec.

It is unspecified whether all members of the `statvfs` structure have meaningful values on all file systems. The
information is provided by the server of the file system containing the file.

## Return value

Upon successful completion, `statvfs()` shall return `0`. Otherwise, it shall return `-1` and set `errno` to indicate
the error.

## Errors

The `fstatvfs()` and `statvfs()` functions shall fail if:

* `EIO` - An I/O error occurred while reading the file system.

* `EINTR` - A signal was caught during execution of the function.

* `EOVERFLOW` - One of the values to be returned cannot be represented correctly in the structure pointed to by _buf_.

The `fstatvfs()` function shall fail if:

* `EBADF` - The _fildes_ argument is not an open file descriptor.

The `statvfs()` function shall fail if:

* `EACCES` - Search permission is denied on a component of the path prefix.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a component of a pathname is longer than `NAME_MAX`.

* `ENOENT` - A component of _path_ does not name an existing file or _path_ is an empty string.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to
a directory, or the _path_ argument contains at least one non-`<slash>` character and ends with one or more trailing
`<slash>` characters and the last pathname component names an existing file that is neither a directory nor a symbolic
link to a directory.

The `statvfs()` function may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a pathname exceeds `PATH_MAX`, or pathname resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

## POSIX deviations

No POSIX deviations discovered.
