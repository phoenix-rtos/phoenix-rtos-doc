# mkfifo

## Synopsis

`#include <sys/stat.h>`

`int mkfifo(const char *path, mode_t mode);`

`#include <fcntl.h>`

`int mkfifoat(int fd, const char *path, mode_t mode);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `mkfifo()` function shall create a new `FIFO` special file named by the path name pointed to by _path_. The file
permission bits of the new `FIFO` shall be initialized from _mode_. The file permission bits of the _mode_ argument
shall be modified by the process' file creation mask.

When bits in _mode_ other than the file permission bits are set, the effect is implementation-defined.

If _path_ names a symbolic link, `mkfifo()` shall fail and set `errno` to `EEXIST`.

The `FIFO`'s user ID shall be set to the process' effective user ID. The `FIFO`'s group ID shall be set to the group ID
of the parent directory or to the effective group ID of the process. Implementations shall provide a way to initialize
the `FIFO`'s group ID to the group ID of the parent directory. Implementations may, but need not, provide an
implementation-defined way to initialize the FIFO's group ID to the effective group ID of the calling process.

Upon successful completion, `mkfifo()` shall mark for update the last data access, last data modification, and last
file status change timestamps of the file. Also, the last data modification and last file status change timestamps of
the directory that contains the new entry shall be marked for update.

The `mkfifoat()` function shall be equivalent to the `mkfifo()` function except in the case where _path_ specifies a
relative path. In this case the newly created `FIFO` is created relative to the directory associated with the file
descriptor _fd_ instead of the current working directory. If the access mode of the open file description associated
with the file descriptor is not `O_SEARCH`, the function shall check whether directory searches are permitted using the
current permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH`, the function
shall not perform the check.

If `mkfifoat()` is passed the special value `AT_FDCWD` in the _fd_ parameter, the current working directory shall be
used and the behavior shall be identical to a call to `mkfifo()`.

## Return value

Upon successful completion, these functions shall return `0`. Otherwise, these functions shall return `-1` and set
`errno` to indicate the error. If `-1` is returned, no FIFO shall be created.

## Errors

These functions shall fail if:

* `EACCES` - A component of the _path_ prefix denies search permission, or write permission is denied on the parent
directory of the `FIFO` to be created.

* `EEXIST` - The named file already exists.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of the path prefix of _path_ does not name an existing file or _path_ is an empty string.

* `ENOENT` or `ENOTDIR` - The _path_ argument contains at least one non- `<slash>` character and ends with one or more
trailing `<slash>` characters. If _path_ without the trailing `<slash>` characters would name an existing file, a
`ENOENT` error shall not occur.

* `ENOSPC` - The directory that would contain the new file cannot be extended, or the file system is out of
file-allocation resources.

* `ENOTDIR` - A component of the _path_ prefix names an existing file that is neither a directory nor a symbolic link
to a directory.

* `EROFS` - The named file resides on a read-only file system.

The `mkfifoat()` function shall fail if:

* `EACCES` - The access mode of the open file description associated with _fd_ is not `O_SEARCH` and the permissions
of the directory underlying _fd_ do not permit directory searches.

* `EBADF` - The _path_ argument does not specify an absolute path and the _fd_ argument is neither `AT_FDCWD`
nor a valid file descriptor open for reading or searching.

* `ENOTDIR` - The _path_ argument is not an absolute path and _fd_ is a file descriptor associated with a
non-directory file.

These functions may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

## Tests

Untested

## Known bugs

None
