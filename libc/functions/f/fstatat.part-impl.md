# fstatat

## Synopsis

`#include <fcntl.h>`

`#include <sys/stat.h>`

`int fstatat(int fd, const char *restrict path,`

`struct stat *restrict buf, int flag);`

`int lstat(const char *restrict path, struct stat *restrict buf);`

`int stat(const char *restrict path, struct stat *restrict buf);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to get file status. The `stat()` function shall obtain information about the named file and write it to
the area pointed to by the buf argument. The _path_ argument points to a path name naming a file. Read, write, or
execute permission of the named file is not required. An implementation that provides additional or alternate
file access control mechanisms may, under implementation-defined conditions, cause `stat()` to fail. In particular,
the system may deny the existence of the file specified by _path_.

If the named file is a symbolic link, the `stat()` function shall continue path name resolution using the contents
of the symbolic link, and shall return information pertaining to the resulting file if the file exists.

The buf argument is a pointer to a stat structure, as defined in the `<sys/stat.h>` header, into which information is
placed concerning the file.

The `stat()` function shall update any time-related fields, before writing into the stat structure. If the named file is
a shared memory object, the implementation shall update in the stat structure pointed to by the buf argument the
`st_uid,` `st_gid,` `st_size,` and `st_mode` fields, and only the `S_IRUSR,` `S_IWUSR,` `S_IRGRP,` `S_IWGRP,` `S_IROTH,`
and `S_IWOTH` file permission bits need be valid. The implementation may update other fields and flags.

If the named file is a typed memory object, the implementation shall update in the stat structure pointed to by the buf
argument the `st_uid,` `st_gid,` `st_size,` and `st_mode` fields, and only the `S_IRUSR,` `S_IWUSR,` `S_IRGRP,`
`S_IWGRP,` `S_IROTH,` and `S_IWOTH` file permission bits need be valid. The implementation may update other fields and
flags.

For all other file types defined in this volume of `POSIX.1-2017`, the structure members `st_mode,` `st_ino,` `st_dev,`
`st_uid,` `st_gid,` `st_atim,` `st_ctim,` and `st_mtim` shall have meaningful values and the value of the member
`st_nlink` shall be set to the number of links to the file.

The `lstat()` function shall be equivalent to `stat()`, except when _path_ refers to a symbolic link. In that case
`lstat()` shall return information about the link, while `stat()` shall return information about the file the link
references.

For symbolic links, the `st_mode` member shall contain meaningful information when used with the file type macros. The
file mode bits in `st_mode` are unspecified. The structure members `st_ino,` `st_dev,` `st_uid,` `st_gid,` `st_atim,`
`st_ctim,` and `st_mtim` shall have meaningful values and the value of the `st_nlink` member shall be set to the number
of (hard) links to the symbolic link. The value of the `st_size` member shall be set to the length of the path name
contained in the symbolic link not including any terminating null byte.

The `fstatat()` function shall be equivalent to the `stat()` or `lstat()` function, depending on the value of flag
(see below), except in the case where _path_ specifies a relative path. In this case the status shall be retrieved from
a file relative to the directory associated with the file descriptor _fd_ instead of the current working directory. If
the access mode of the open file description associated with the file descriptor is not `O_SEARCH,` the function shall
check whether directory searches are permitted using the current permissions of the directory underlying the file
descriptor. If the access mode is `O_SEARCH,` the function shall not perform the check.

Values for flag are constructed by a bitwise-inclusive `OR` of flags from the following list, defined in `<fcntl.h>`:

`AT_SYMLINK_NOFOLLOW`

If _path_ names a symbolic link, the status of the symbolic link is returned.

If `fstatat()` is passed the special value `AT_FDCWD` in the _fd_ parameter, the current working directory shall be used
and the behavior shall be identical to a call to `stat()` or `lstat()` respectively, depending on whether
the `AT_SYMLINK_NOFOLLOW` bit is set in flag.

## Return value

Upon successful completion, these functions shall return `0`. Otherwise, these functions shall return `-1` and set
`errno` to indicate the error.

## Errors

These functions shall fail if:

* `EACCES` - Search permission is denied for a component of the _path_ prefix.

* `EIO` - An error occurred while reading from the file system.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of _path_ does not name an existing file or _path_ is an empty string.

* `ENOTDIR` - A component of the _path_ prefix names an existing file that is neither a directory nor a symbolic link to
a directory, or the _path_ argument contains at least one non- `/` character and ends with one or more trailing `/`
characters and the last path name component names an existing file that is neither a directory nor a symbolic link
to a directory.

* `EOVERFLOW` - The file size in bytes or the number of blocks allocated to the file or the file serial number cannot
be represented correctly in the structure pointed to by buf.

The `fstatat()` function shall fail if:

* `EACCES` - The access mode of the open file description associated with _fd_ is not `O_SEARCH` and the permissions of
the directory underlying _fd_ do not permit directory searches.

* `EBADF` - The _path_ argument does not specify an absolute path and the _fd_ argument is neither `AT_FDCWD` nor a
valid file descriptor open for reading or searching.

* `ENOTDIR` - The _path_ argument is not an absolute path and _fd_ is a file descriptor associated with a non-directory
file.

These functions may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

* `EOVERFLOW` - A value to be stored would overflow one of the members of the stat structure.

The `fstatat()` function may fail if:

* `EINVAL` - The value of the flag argument is not valid.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
