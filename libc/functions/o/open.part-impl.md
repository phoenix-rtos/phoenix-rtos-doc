# Synopsis

`#include <sys/stat.h>`

`#include <fcntl.h>`

`int open(const char *path, int oflag, ...);`

`int openat(int fd, const char *path, int oflag, ...);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `open()` function shall establish the connection between a file and a file descriptor. It shall create an open file
description that refers to a file and a file descriptor that refers to that open file description. The file descriptor
is used by other I/O functions to refer to that file. The _path_ argument points to a pathname naming the file.

The `open()` function shall return a file descriptor for the named file, allocated as described in File Descriptor
Allocation. The open file description is new, and therefore the file descriptor shall not share it with any other
process in the system. The `FD_CLOEXEC` file descriptor flag associated with the new file descriptor shall be
cleared unless the `O_CLOEXEC` flag is set in _oflag_.

The file offset used to mark the current position within the file shall be set to the beginning of the file.

The file status flags and file access modes of the open file description shall be set according to the value of _oflag_.

Values for _oflag_ are constructed by a bitwise-inclusive OR of flags from the following list, defined in `<fcntl.h>`.
Applications shall specify exactly one of the first five values (file access modes) below in the value of _oflag_:

* `O_EXEC` - Open for execute only (non-directory files). The result is unspecified if this flag is applied to a
directory.
* `O_RDONLY` - Open for reading only.
* `O_RDWR` - Open for reading and writing. The result is undefined if this flag is applied to a `FIFO`.
* `O_SEARCH` - Open directory for search only. The result is unspecified if this flag is applied to a non-directory
file.
* `O_WRONLY` - Open for writing only.

Any combination of the following may be used:

* `O_APPEND` - If set, the file offset shall be set to the end of the file prior to each write.
* `O_CLOEXEC` - If set, the `FD_CLOEXEC` flag for the new file descriptor shall be set.
* `O_CREAT` - If the file exists, this flag has no effect except as noted under `O_EXCL` below. Otherwise, if
`O_DIRECTORY` is not set the file shall be created as a regular file; the user ID of the file shall be set to the
effective user ID of the process; the group ID of the file shall be set to the group ID of the file's parent directory
or to the effective group ID of the process; and the access permission bits (see `<sys/stat.h>`) of the file mode shall
be set to the value of the argument following the _oflag_ argument taken as type `mode_t` modified as follows: a bitwise
`AND` is performed on the file-mode bits and the corresponding bits in the complement of the process' file mode creation
mask. Thus, all bits in the file mode whose corresponding bit in the file mode creation mask is set are cleared. When
bits other than the file permission bits are set, the effect is unspecified. The argument following the _oflag_ argument
does not affect whether the file is open for reading, writing, or for both. Implementations shall provide a way to
initialize the file's group ID to the group ID of the parent directory. Implementations may, but need not, provide
an implementation-defined way to initialize the file's group ID to the effective group ID of the calling process.

* `O_DIRECTORY` - If _path_ resolves to a non-directory file, fail and set `errno` to `ENOTDIR`.

* `O_DSYNC` - Write I/O operations on the file descriptor shall complete as defined by synchronized I/O data integrity
completion.

* `O_EXCL` - If `O_CREAT` and `O_EXCL` are set, `open()` shall fail if the file exists. The check for the existence of
the file and the
creation of the file if it does not exist shall be atomic with respect to other threads executing `open()` naming the
same filename in the same directory with `O_EXCL` and `O_CREAT` set. If `O_EXCL` and `O_CREAT` are set, and _path_ names
a symbolic link, `open()` shall fail and set `errno` to `EEXIST`, regardless of the contents of the symbolic link. If
`O_EXCL` is set and `O_CREAT` is not set, the result is undefined.

* `O_NOCTTY` - If set and path identifies a terminal device, `open()` shall not cause the terminal device to become the
controlling terminal for the process. If _path_ does not identify a terminal device, `O_NOCTTY` shall be ignored.

* `O_NOFOLLOW` - If _path_ names a symbolic link, fail and set `errno` to `ELOOP`.

* `O_NONBLOCK`
  * When opening a `FIFO` with `O_RDONLY` or `O_WRONLY` set:

    * If `O_NONBLOCK` is set, an `open()` for reading-only shall return without delay. An `open()` for writing-only
    shall return an error if no process currently has the file open for reading.

    * If `O_NONBLOCK` is clear, an `open()` for reading-only shall block the calling thread until a thread opens the
    file for writing. An `open()` for writing-only shall block the calling thread until a thread opens the file for
    reading.

  * When opening a block special or character special file that supports non-blocking opens:

    * If `O_NONBLOCK` is set, the `open()` function shall return without blocking for the device to be ready or
    available. Subsequent behavior of the device is device-specific.

    * If `O_NONBLOCK` is clear, the `open()` function shall block the calling thread until the device is ready or
    available before returning.

  * Otherwise, the `O_NONBLOCK` flag shall not cause an error, but it is unspecified whether the file status flags will
  include the `O_NONBLOCK` flag.

* `O_RSYNC` - Read I/O operations on the file descriptor shall complete at the same level of integrity as specified by
the `O_DSYNC` and `O_SYNC` flags. If both `O_DSYNC` and `O_RSYNC` are set in _oflag_, all I/O operations on the file
descriptor shall complete as defined by synchronized I/O data integrity completion. If both `O_SYNC` and `O_RSYNC` are
set in flags, all I/O operations on the file descriptor shall complete as defined by synchronized I/O file integrity
completion.

* `O_SYNC` - Write I/O operations on the file descriptor shall complete as defined by synchronized I/O file integrity
completion. The `O_SYNC` flag shall be supported for regular files, even if the Synchronized Input and Output option
is not supported.

* `O_TRUNC` - If the file exists and is a regular file, and the file is successfully opened `O_RDWR` or `O_WRONLY,` its
length shall be truncated to `0`, and the mode and owner shall be unchanged. It shall have no effect on `FIFO` special
files or terminal device files. Its effect on other file types is implementation-defined. The result of using `O_TRUNC`
without either `O_RDWR` or `O_WRONLY` is undefined.

* `O_TTY_INIT` - If path identifies a terminal device other than a pseudo-terminal, the device is not already open in
any process, and either `O_TTY_INIT` is set in _oflag_ or `O_TTY_INIT` has the value zero, `open()` shall set any
non-standard termios structure terminal parameters to a state that provides conforming behavior; see XBD Parameters
that Can be Set. It is unspecified whether `O_TTY_INIT` has any effect if the device is already open in any process. If
_path_ identifies the slave side of a pseudo-terminal that is not already open in any process, `open()` shall set any
non-standard termios structure terminal parameters to a state that provides conforming behavior, regardless of whether
`O_TTY_INIT` is set. If _path_ does not identify a terminal device, `O_TTY_INIT` shall be ignored.

If `O_CREAT` and `O_DIRECTORY` are set and the requested access mode is neither `O_WRONLY` nor `O_RDWR,` the result is
unspecified.

If `O_CREAT` is set and the file did not previously exist, upon successful completion, `open()` shall mark for update
the last data access, last data modification, and last file status change timestamps of the file and the last data
modification and last file status change timestamps of the parent directory.

If `O_TRUNC` is set and the file did previously exist, upon successful completion, `open()` shall mark for update the
last data modification and last file status change timestamps of the file.

If both the `O_SYNC` and `O_DSYNC` flags are set, the effect is as if only the `O_SYNC` flag was set.

If path refers to a `STREAMS` file, _oflag_ may be constructed from `O_NONBLOCK` OR'ed with either `O_RDONLY,`
`O_WRONLY,` or `O_RDWR`. Other flag values are not applicable to `STREAMS` devices and shall have no effect on them.
The value `O_NONBLOCK` affects the operation of `STREAMS` drivers and certain functions applied to file descriptors
associated with `STREAMS` files. For `STREAMS` drivers, the implementation of `O_NONBLOCK` is device-specific.

The application shall ensure that it specifies the `O_TTY_INIT` flag on the first open of a terminal device since
system boot or since the device was closed by the process that last had it open. The application need not specify the
`O_TTY_INIT` flag when opening pseudo-terminals.  If _path_ names the master side of a pseudo-terminal device, then it
is unspecified whether `open()` locks the slave side so that it cannot be opened. Conforming applications shall call
`unlockpt()` before opening the slave side.

The largest value that can be represented correctly in an object of type `off_t` shall be established as the offset
maximum in the open file description.

The `openat()` function shall be equivalent to the `open()` function except in the case where _path_ specifies a
relative path. In this case the file to be opened is determined relative to the directory associated with the file
descriptor _fd_ instead of the current working directory. If the access mode of the open file description associated
with the file descriptor is not `O_SEARCH,` the function shall check whether directory searches are permitted using
the current permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH,` the function
shall not perform the check.

The _oflag_ parameter and the optional fourth parameter correspond exactly to the parameters of `open()`.

If `openat()` is passed the special value `AT_FDCWD` in the _fd_ parameter, the current working directory shall be used
and the behavior shall be identical to a call to `open()`.

## Return value

Upon successful completion, these functions shall open the file and return a non-negative integer representing the file
descriptor. Otherwise, these functions shall return `-1` and set `errno` to indicate the error. If `-1` is returned, no
files shall be created or modified.

## Errors

These functions shall fail if:

* `EACCES` - Search permission is denied on a component of the _path_ prefix, or the file exists and the permissions
specified by _oflag_ are denied, or the file does not exist and write permission is denied for the parent directory of
the file to be created, or `O_TRUNC` is specified and write permission is denied.

* `EEXIST` - `O_CREAT` and `O_EXCL` are set, and the named file exists.

* `EINTR` - A signal was caught during `open()`.

* `EINVAL` - The implementation does not support synchronized I/O for this file.

* `EIO` - The _path_ argument names a `STREAMS` file and a hangup or error occurred during the `open()`.

* `EISDIR` - The named file is a directory and _oflag_ includes O_WRONLY or `O_RDWR`, or includes `O_CREAT` without
`O_DIRECTORY`.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument, or `O_NOFOLLOW` was
specified and the _path_ argument names a symbolic link.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENAMETOOLONG` - The length of a component of a pathname is longer than `NAME_MAX`.

* `ENFILE` - The maximum allowable number of files is currently open in the system.

* `ENOENT` - `O_CREAT` is not set and a component of _path_ does not name an existing file, or `O_CREAT` is set and a
component of the _path_
prefix of _path_ does not name an existing file, or _path_ points to an empty string.

* `ENOENT` or `ENOTDIR` - `O_CREAT` is set, and the path argument contains at least one non- `<slash>` character and
ends with one or more trailing `<slash>` characters. If path without the trailing `<slash>` characters would name an
existing file, an `ENOENT` error shall not occur.

* `ENOSR` -  The path argument names a `STREAMS`-based file and the system is unable to allocate a `STREAM`.

* `ENOSPC` - The directory or file system that would contain the new file cannot be expanded, the file does not exist,
and `O_CREAT` is specified.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a
directory; or `O_CREAT` and `O_EXCL` are not specified, the path argument contains at least one non- `<slash>` character
and ends with one or more trailing `<slash>` characters, and the last pathname component names an existing file that is
neither a directory nor a symbolic link to a directory; or `O_DIRECTORY` was specified and the path argument resolves
to a non-directory file.

* `ENXIO` - `O_NONBLOCK` is set, the named file is a `FIFO`, `O_WRONLY` is set, and no process has the file open for
reading.

* `ENXIO` - The named file is a character special or block special file, and the device associated with this special
file does not exist.

* `EOVERFLOW` - The named file is a regular file and the size of the file cannot be represented correctly in an object
of type off_t.

* `EROFS` - The named file resides on a read-only file system and either `O_WRONLY`, `O_RDWR`, `O_CREAT` (if the file
does not exist), or `O_TRUNC` is set in the _oflag_ argument.

The `openat()` function shall fail if:

* `EACCES` - The access mode of the open file description associated with _fd_ is not `O_SEARCH` and the permissions of
the directory underlying _fd_ do not permit directory searches.

* `EBADF` - The path argument does not specify an absolute path and the _fd_ argument is neither `AT_FDCWD` nor a valid
file descriptor open for reading or searching.

* `ENOTDIR` - The path argument is not an absolute path and _fd_ is a file descriptor associated with a non-directory
file.

These functions may fail if:

* `EAGAIN` - The path argument names the slave side of a pseudo-terminal device that is locked.

* `EINVAL` - The value of the _oflag_ argument is not valid.

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the path argument.

* `ENAMETOOLONG` - The length of a pathname exceeds `PATH_MAX`, or pathname resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

* `ENOMEM` -  The path argument names a `STREAMS` file and the system is unable to allocate resources.

* `EOPNOTSUPP` - The path argument names a socket.

* `ETXTBSY` - The file is a pure procedure (shared text) file that is being executed and _oflag_ is `O_WRONLY` or
`O_RDWR`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
