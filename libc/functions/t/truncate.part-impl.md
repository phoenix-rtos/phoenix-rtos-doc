# truncate

## Synopsis

`#include <unistd.h>`

`int truncate(const char *path, off_t length);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `truncate()` function shall cause the regular file named by path to have a size which shall be equal to `length`
bytes.

If the file previously was larger than _length_, the extra data is discarded. If the file was previously shorter than
_length_, its size is increased, and the extended area appears as if it were zero-filled. The application shall ensure
that the process has write permission for the file.

If the request caused the file size to exceed the soft file size limit for the process, the request shall fail, and
the implementation shall generate the `SIGXFSZ` signal for the process.

The `truncate()` function shall not modify the file offset for any open file descriptions associated with the file. Upon
successful completion, `truncate()` shall mark for update the last data modification and last file status change
timestamps of the file, and the `S_ISUID` and `S_ISGID` bits of the file mode may be cleared.

## Return value

Upon successful completion, `ftruncate()` shall return `0`, otherwise, `-1` shall be returned and `errno` set to
indicate the error.

## Errors

The `ftruncate()` function shall fail if:

* `EINTR` - A signal was caught during execution.

* `EINVAL` - The _length_ argument was less than `0`.

* `EFBIG` or `EINVAL` - The _length_ argument was greater than the maximum file size.

* `EIO` - An I/O error occurred while reading from or writing to a file system.

* `EACCES` - A component of the path prefix denies search permission, or write permission is denied on the file.

* `EISDIR` - The named file is a directory.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`

* `ENOENT` - A component of _path_ does not name an existing file or _path_ is an empty string.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to
 a directory, or the _path argument_ contains at least one non- `<slash>` character and ends with one or more trailing
 `<slash>` characters and the last path name component names an existing file that is neither a directory nor a symbolic
 link to a directory.

* `EROFS` - The named file resides on a read-only file system.

The truncate() function may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
 intermediate result with a length that exceeds `PATH_MAX`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
