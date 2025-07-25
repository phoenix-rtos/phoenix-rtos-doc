# freopen

## Synopsis

`#include <stdio.h>`

`FILE *freopen(const char *restrict pathname, const char *restrict mode, FILE *restrict stream);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to open the stream. The `freopen()` function shall first attempt to flush the stream associated with
_stream_ as if by a call to `fflush(stream)`. Failure to flush the stream successfully shall be ignored. If _pathname_
is not a `null` pointer, `freopen()` shall close any file descriptor associated with _stream_. Failure to close the
file descriptor successfully shall be ignored. The error and end-of-file indicators for the stream shall be cleared.

The `freopen()` function shall open the file whose _pathname_ is the string pointed to by _pathname_ and associate the
stream pointed to by _stream_ with it. The _mode_ argument shall be used just as in `fopen()`.

The original stream shall be closed regardless of whether the subsequent open succeeds.

If _pathname_ is a `null` pointer, the `freopen()` function shall attempt to change the mode of the stream to that
specified by _mode_, as if the name of the file currently associated with the stream had been used. In this case, the
file descriptor associated with the stream need not be closed if the call to `freopen()` succeeds. It is
implementation-defined which changes of _mode_ are permitted (if any), and under what circumstances.

After a successful call to the `freopen()` function, the orientation of the stream shall be cleared, the encoding rule
shall be cleared, and the associated `mbstate_t` object shall be set to describe an initial conversion state.

If _pathname_ is not a `null` pointer, or if _pathname_ is a `null` pointer and the specified mode change necessitates
the file descriptor associated with the stream to be closed and reopened, the file descriptor associated with the
reopened stream shall be allocated and opened as if by a call to `open()` with the following flags:

| `freopen()` Mode       | `open()` Flags                |
| ---------------------- | ----------------------------- |
| `r` or `rb`            | `O_RDONLY`                    |
| `w` or `wb`            | `O_WRONLY\|O_CREAT\|O_TRUNC`  |
| `a` or `ab`            | `O_WRONLY\|O_CREAT\|O_APPEND` |
| `r+` or `rb+` or `r+b` | `O_RDWR`                      |
| `w+` or `wb+` or `w+b` | `O_RDWR\|O_CREAT\|O_TRUNC`    |
| `a+` or `ab+` or `a+b` | `O_RDWR\|O_CREAT\|O_APPEND`   |

## Return value

Upon successful completion, `freopen()` shall return the value of _stream_. Otherwise, a `null` pointer shall be
returned, and `errno` shall be set to indicate the error.

## Errors

The `freopen()` function shall fail if:

* `EACCES` - Search permission is denied on a component of the path prefix, or the file exists, and the permissions
specified by _mode_ are denied, or the file does not exist and write permission is denied for the parent directory of
the file to be created.

* `EBADF` - The file descriptor underlying the stream is not a valid file descriptor when _pathname_ is a `null`
pointer.

* `EINTR` - A signal was caught during `freopen()`.

* `EISDIR` - The named file is a directory and _mode_ requires write access.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the path argument.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENAMETOOLONG` - The length of a component of a _pathname_ is longer than `NAME_MAX`.

* `ENFILE` - The maximum allowable number of files is currently open in the system.

* `ENOENT` - The _mode_ string begins with 'r' and a component of _pathname_ does not name an existing file, or _mode_
begins with 'w' or 'a' and a component of the path prefix of _pathname_ does not name an existing file, or _pathname_
is an empty string.

* `ENOENT` or `ENOTDIR` - The _pathname_ argument contains at least one non- `/` character and ends with one or more
trailing `/` characters. If _pathname_ without the trailing `/` characters would name an existing file, a `ENOENT`
error shall not occur.

* `ENOSPC` - The directory or file system that would contain the new file cannot be expanded, the file does not exist,
and it was to be created.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a
directory, or the _pathname_ argument contains at least one non- `/` character and ends with one or more trailing `/`
characters and the last _pathname_ component names an existing file that is neither a directory nor a symbolic link to a
directory.

* `ENXIO` - The named file is a character special or block special file, and the device associated with this special
file does not exist.

* `EOVERFLOW` - The named file is a regular file and the size of the file cannot be represented correctly in an object
of type `off_t`.

* `EROFS` - The named file resides on a read-only file system and _mode_ requires write access.

The `freopen()` function may fail if:

* `EBADF` - The _mode_ with which the file descriptor underlying the stream was opened does not support the requested
mode when _pathname_ is a `null` pointer.

* `EINVAL` - The value of the _mode_ argument is not valid.

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the path argument.

* `ENAMETOOLONG` - The length of a _pathname_ exceeds `PATH_MAX`, or _pathname_ resolution of a symbolic link produced
an intermediate result with a length that exceeds `PATH_MAX`.

* `ENOMEM` - Insufficient storage space is available.

* `ENXIO` - A request was made of a nonexistent device, or the request was outside the capabilities of the device.

* `ETXTBSY` - The file is a pure procedure (shared text) file that is being executed and _mode_ requires write access.

## Tests

Untested

## Known bugs

None
