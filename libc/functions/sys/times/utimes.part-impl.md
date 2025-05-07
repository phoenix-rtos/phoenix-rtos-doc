# utimes

## Synopsis

```c
#include <sys/stat.h>

int futimens(int fd, const struct timespec times[2]);

#include <fcntl.h>

int utimensat(int fd, const char *path,
              const struct timespec times[2], int flag);

#include <sys/time.h>

int utimes(const char *path, const struct timeval times[2]);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `futimens()` and `utimensat()` functions shall set the access and modification times of a file to the values of the
 _times_ argument. The `futimens()` function changes the times of the file associated with the file descriptor _fd_.

 The `utimensat()` function changes the times of the file pointed to by the _path_ argument, relative to the directory
 associated with the file descriptor _fd_. Both functions allow time specifications accurate to the nanosecond.

For `futimens()` and `utimensat()`, the _times_ argument is an array of two `timespec` structures. The first array
member represents the date and time of last access, and the second member represents the date and time of last
modification. The times in the `timespec` structure are measured in seconds and nanoseconds since the Epoch. The
file's relevant timestamp shall be set to the greatest value supported by the file system that is not greater than the
specified time.

If the `tv_nsec` field of a `timespec` structure has the special value `UTIME_NOW`, the file's relevant timestamp shall
be set to the greatest value supported by the file system that is not greater than the current time. If the `tv_nsec`
field has the special value `UTIME_OMIT`, the file's relevant timestamp shall not be changed. In either case, the
`tv_sec` field shall be ignored.

If the _times_ argument is a `null` pointer, both the access and modification timestamps shall be set to the greatest
value supported by the file system that is not greater than the current time. If `utimensat()` is passed a relative
path in the _path_ argument, the file to be used shall be relative to the directory associated with the file descriptor
_fd_ instead of the current working directory. If the access mode of the open file description associated with the file
descriptor is not `O_SEARCH`, the function shall check whether directory searches are permitted using the current
permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH`, the function shall not
perform the check.

If `utimensat()` is passed the special value `AT_FDCWD` in the _fd_ parameter, the current working directory shall be
used.

Only a process with the effective user ID equal to the user ID of the file, or with write access to the file, or with
appropriate privileges may use `futimens()` or `utimensat()` with a `null` pointer as the _times_ argument or with both
`tv_nsec` fields set to the special value `UTIME_NOW`. Only a process with the effective user ID equal to the user ID of
the file or with appropriate privileges may use `futimens()` or `utimensat()` with a non-`null` _times_ argument that
does not have both tv_nsec fields set to `UTIME_NOW` and does not have both tv_nsec fields set to `UTIME_OMIT`. If both
`tv_nsec` fields are set to `UTIME_OMIT`, no ownership or permissions check shall be performed for the file, but other
error conditions may still be detected (including `EACCES` errors related to the _path_ prefix).

Values for the _flag_ argument of `utimensat()` are constructed by a bitwise-inclusive OR of flags from the following
list, defined in `<fcntl.h>`:

* `AT_SYMLINK_NOFOLLOW` - If _path_ names a symbolic link, then the access and modification times of the symbolic link
are changed.

Upon successful completion, `futimens()` and `utimensat()` shall mark the last file status change timestamp for update,
with the exception that if both `tv_nsec` fields are set to UTIME_OMIT, the file status change timestamp need not be
marked for update.

The `utimes()` function shall be equivalent to the `utimensat()` function with the special value `AT_FDCWD` as the _fd_
argument and the _flag_ argument set to zero, except that the _times_ argument is a _timeval_ structure rather than a
`timespec` structure, and accuracy is only to the microsecond, not nanosecond, and rounding towards the nearest second
may occur.

## Return value

Upon successful completion, these functions shall return `0`. Otherwise, these functions shall return `-1` and set
`errno` to indicate the error. If `-1` is returned, the file times shall not be affected.

## Errors

These functions shall fail if:

* `EACCES` - The _times_ argument is a `null` pointer, or both `tv_nsec` values are `UTIME_NOW`, and the effective user
ID of the process does not match the owner of the file and write access is denied.
* `EINVAL` - Either of the times argument structures specified a `tv_nsec` value that was neither `UTIME_NOW` nor
`UTIME_OMIT`, and was a value less than zero or greater than or equal to 1000 million.
* `EINVAL` - A new file timestamp would be a value whose `tv_sec` component is not a value supported by the file system.
* `EPERM` - The times argument is not a `null` pointer, does not have both `tv_nsec` fields set to `UTIME_NOW`, does not
have both `tv_nsec` fields set to `UTIME_OMIT`, the calling process' effective user ID does not match the owner of the
file, and the calling process does not have appropriate privileges.
* `EROFS` - The file system containing the file is read-only.

The `futimens()` function shall fail if:

* `EBADF` - The _fd_ argument is not a valid file descriptor.

The `utimensat()` function shall fail if:

* `EACCES` - The access mode of the open file description associated with _fd_ is not `O_SEARCH` and the permissions of
the directory underlying _fd_ do not permit directory searches.
* `EBADF` - The _path_ argument does not specify an absolute path and the fd argument is neither `AT_FDCWD` nor a valid
file descriptor open for reading or searching.
* `ENOTDIR` - The _path_ argument is not an absolute path and _fd_ is a file descriptor associated with a non-directory
file.

The `utimensat()` and `utimes()` functions shall fail if:

* `EACCES` - Search permission is denied by a component of the _path_ prefix.
* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.
* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.
* `ENOENT` - A component of _path_ does not name an existing file or _path_ is an empty string.
* `ENOTDIR` - A component of the _path_ prefix names an existing file that is neither a directory nor a symbolic link
to a directory, or the _path_ argument contains at least one non- `<slash>` character and ends with one or more
trailing `<slash>` characters and the last path name component names an existing file that is neither a directory nor a
symbolic link to a directory.

The `utimensat()` and `utimes()` functions may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.
* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

The `utimensat()` function may fail if:

* `EINVAL` - The value of the flag argument is not valid.

## Tests

Untested

## Known bugs

None
