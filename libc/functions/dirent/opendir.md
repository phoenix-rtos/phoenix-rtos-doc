# opendir

## Synopsis

```c
#include <dirent.h>

DIR *fdopendir(int fd);

DIR *opendir(const char *dirname);
```

## Description

The functions open the directory associated with a file descriptor or a name.

Arguments:

_fd_ - the file descriptor.
_dirname_ - the name of the directory to open.

Upon successful return from `fdopendir()`, the file descriptor is under the control of the system, and if any attempt is
made to close the file descriptor, or to modify the state of the associated description, other than by means of
`closedir()`, `readdir()`, `readdir_r()`, `rewinddir()`, or `seekdir()`, the behavior is undefined. Upon calling
`closedir()` the file descriptor is closed.

The `FD_CLOEXEC` flag is set on the file descriptor by a successful call to `fdopendir()`.

The `opendir()` function opens a directory stream corresponding to the directory named by the _dirname_ argument. The
directory stream is positioned at the first entry.

## Return value

Upon successful completion, `fdopendir()` and `opendir()` return a pointer to an object of type `DIR`. Otherwise, these
functions return a null pointer and set `errno` to indicate the error.

### Errors

For `fdopendir()`:

[`EBADF`]  The _fd_ argument is not a valid file descriptor open for reading.
[`ENOTDIR`] The descriptor _fd_ is not associated with a directory.

For the `opendir()` function:

[`EACCES`] Search permission is denied for the component of the path prefix of _dirname_ or read permission is denied
for _dirname_.
[`ELOOP`] A loop exists in symbolic links encountered during resolution of the _dirname_ argument.
[`ENAMETOOLONG`] The length of a component of a path name is longer than {`NAME_MAX`}.
[`ENOENT`] A component of _dirname_ does not name an existing directory or _dirname_ is an empty string.
[`ENOTDIR`] A component of _dirname_ names an existing file that is neither a directory nor a symbolic link to a
directory.
[`ELOOP`] More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the _dirname_ argument.
[`ENAMETOOLONG`] The length of a path name exceeds {`PATH_MAX`}, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds {`PATH_MAX`}.

## POSIX deviations

`opendir()` never fails with `EMFILE` or `ENFILE`. A directory stream opened by `opendir()` doesn't use a file
descriptor: the directory is opened directly at the filesystem server and the stream keeps the identifier of the
directory object, which `readdir()` and `closedir()` pass to the server. Keeping the stream out of the
per-process descriptor table held by the kernel saves a kernel allocation for every open directory and an additional
lookup on every directory operation, which matters on resource-constrained edge and IoT devices running a microkernel,
where the filesystems are user-space servers. The number of directory streams that a process can open is therefore not
limited by {`OPEN_MAX`}, but only by the memory available to the process. A directory stream opened by `fdopendir()`
uses the given file descriptor.
