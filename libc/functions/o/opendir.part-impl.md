# opendir

## Synopsis

`#include <dirent.h>`

`DIR *fdopendir(int fd);`

`DIR *opendir(const char *dirname);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `fdopendir()` function shall be equivalent to the `opendir()` function except that the directory is specified by a
file descriptor rather than by a name. The file offset associated with the file descriptor at the time of the call
determines which entries are returned.

Upon successful return from `fdopendir()`, the file descriptor is under the control of the system, and if any attempt is
made to close the file descriptor, or to modify the state of the associated description, other than by means of
`closedir()`, `readdir()`, `readdir_r()`, `rewinddir()`, or `seekdir()`, the behavior is undefined. Upon calling
`closedir()` the file descriptor shall be closed.

It is unspecified whether the `FD_CLOEXEC` flag will be set on the file descriptor by a successful call to
`fdopendir()`.

The `opendir()` function shall open a directory stream corresponding to the directory named by the _dirname_ argument.

The directory stream is positioned at the first entry. If the type `DIR` is implemented using a file descriptor,
applications shall only be able to open up to a total of ``OPEN_MAX`` files and directories.

If the type `DIR` is implemented using a file descriptor, the descriptor shall be obtained as if the `O_DIRECTORY`
flag was passed to `open()`.

## Return value

Upon successful completion, these functions shall return a pointer to an object of type `DIR`. Otherwise, these
functions shall return a `null` pointer and set errno to indicate the error.

## Errors

The `fdopendir()` function shall fail if:

* `EBADF` - The _fd_ argument is not a valid file descriptor open for reading.

* `ENOTDIR` - The descriptor _fd_ is not associated with a directory.

The `opendir()` function shall fail if:

* `EACCES` - Search permission is denied for the component of the path prefix of _dirname_ or read permission is denied
for _dirname_.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _dirname_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of _dirname_ does not name an existing directory or _dirname_ is an empty string.

* `ENOTDIR` - A component of _dirname_ names an existing file that is neither a directory nor a symbolic link to a
directory.

The `opendir()` function may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _dirname_ argument.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

* `ENFILE` - Too many files are currently open in the system.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
