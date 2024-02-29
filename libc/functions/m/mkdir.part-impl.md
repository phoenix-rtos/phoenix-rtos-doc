# mkdir

## Synopsis

`#include <sys/stat.h>`

`int mkdir(const char *path, mode_t mode);`

`#include <fcntl.h>`

`int mkdirat(int fd, const char *path, mode_t mode);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `mkdir()` function shall create a new directory with name _path_. The file permission bits of the new directory
shall be initialized from mode. These file permission bits of the mode argument shall be modified by the process'
file creation mask.

When bits in mode other than the file permission bits are set, the meaning of these additional bits is
implementation-defined.

The directory's user ID shall be set to the process' effective user ID. The directory's group ID shall be set to the
group ID of the parent directory or to the effective group ID of the process. Implementations shall provide a way to
initialize the directory's group ID to the group ID of the parent directory. Implementations may, but need not, provide
an implementation-defined way to initialize the directory's group ID to the effective group ID of the calling process.

The newly created directory shall be an empty directory.

If _path_ names a symbolic link, `mkdir()` shall fail and set errno to `EEXIST`.

Upon successful completion, `mkdir()` shall mark for update the last data access, last data modification, and last file
status change timestamps of the directory. Also, the last data modification and last file status change timestamps of
the directory that contains the new entry shall be marked for update.

The `mkdirat()` function shall be equivalent to the `mkdir()` function except in the case where _path_ specifies a
relative path. In this case the newly created directory is created relative to the directory associated with the file
descriptor _fd_ instead of the current working directory. If the access mode of the open file description associated
with the file descriptor is not `O_SEARCH,` the function shall check whether directory searches are permitted using the
current permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH,` the function
shall not perform the check.

If `mkdirat()` is passed the special value `AT_FDCWD` in the _fd_ parameter, the current working directory shall be used
and the behavior shall be identical to a call to `mkdir()`.

## Return value

Upon successful completion, these functions shall return `0`. Otherwise, these functions shall return `-1` and set
`errno` to indicate the error. If `-1` is returned, no directory shall be created.

## Errors

These functions shall fail if:

* `EACCES` - Search permission is denied on a component of the path prefix, or write permission is denied on the parent
 directory of the directory to be created.

* `EEXIST` - The named file exists.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the path argument.

* `EMLINK` - The link count of the parent directory would exceed `LINK_MAX`.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of the path prefix specified by path does not name an existing directory or path is an empty
 string.

* `ENOSPC` - The file system does not contain enough space to hold the contents of the new directory or to extend the
 parent directory of the new directory.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to
 a directory.

* `EROFS` - The parent directory resides on a read-only file system.

In addition, the `mkdirat()` function shall fail if:

* `EACCES` - The access mode of the open file description associated with _fd_ is not O_SEARCH and the permissions of
 the directory underlying _fd_ do not permit directory searches.

* `EBADF` - The path argument does not specify an absolute path and the _fd_ argument is neither `AT_FDCWD` nor a valid
 file descriptor open for reading or searching.

* `ENOTDIR` - The path argument is not an absolute path and _fd_ is a file descriptor associated with a non-directory
 file.

These functions may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the path argument.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
 intermediate result with a length that exceeds `PATH_MAX`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
