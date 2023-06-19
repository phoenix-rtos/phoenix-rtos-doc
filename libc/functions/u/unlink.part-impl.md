<!-- Documentation template to fill -->
<!-- #MUST_BE: make good synopsis -->
# Synopsis

`#include <unistd.h>`

`int unlink(const char *path);`

`#include <fcntl.h>`

`int unlinkat(int fd, const char *path, int flag);`

<!-- #MUST_BE: check status according to implementation -->
## Status

Partially implemented

<!-- #MUST_BE: if function shall be posix compliant print the standard signature  -->
## Conformance

IEEE Std 1003.1-2017

<!-- #MUST_BE: update description from opengroup AND READ IT and check if it matches  -->
## Description

The `unlink()` function shall remove a link to a file. If _path_ names a symbolic link, `unlink()` shall remove the
symbolic link named by _path_ and shall not affect any file or directory named by the contents of the symbolic link.
Otherwise, `unlink()` shall remove the link named by the path name pointed to by _path_ and shall decrement the link
count of the file referenced by the link.

When the file's link count becomes `0` and no process has the file open, the space occupied by the file shall be
freed, and the file shall no longer be accessible. If one or more processes have the file open when the last link is
removed, the link shall be removed before `unlink()` returns, but the removal of the file contents shall be postponed
until all references to the file are closed.

The _path_ argument shall not name a directory unless the process has appropriate privileges and the implementation
supports using `unlink()` on directories.

Upon successful completion, `unlink()` shall mark for update the last data modification and last file status change
timestamps of the parent directory. Also, if the file's link count is not `0`, the last file status change timestamp
of the file shall be marked for update.

The `unlinkat()` function shall be equivalent to the `unlink()` or `rmdir()` function except in the case where _path_
specifies a relative path. In this case the directory entry to be removed is determined relative to the directory
associated with the file descriptor _fd_ instead of the current working directory. If the access mode of the open file
description associated with the file descriptor is not `O_SEARCH`, the function shall check whether directory searches
are permitted using the current permissions of the directory underlying the file descriptor. If the access mode is
`O_SEARCH`, the function shall not perform the check.

Values for _flag_ are constructed by a bitwise-inclusive OR of flags from the following list, defined in `<fcntl.h>`:

* `AT_REMOVEDIR` - remove the directory entry specified by _fd_ and _path_ as a directory, not a normal file.

If `unlinkat()` is passed the special value `AT_FDCWD` in the _fd_ parameter, the current working directory shall be
used and the behavior shall be identical to a call to `unlink()` or `rmdir()` respectively, depending on
whether the `AT_REMOVEDIR` bit is set in flag.

<!-- #MUST_BE: check return values by the function  -->
## Return value

Upon successful completion, these functions shall return `0`. Otherwise, these functions shall return `-1` and set
`errno` to indicate the error. If `-1` is returned, the named file shall not be changed.

<!-- #MUST_BE: check what errors can cause the function to fail  -->
## Errors

These functions shall fail and shall not unlink the file if:

* `EACCES` - Search permission is denied for a component of the path prefix, or write permission is denied on the
directory containing the directory entry to be removed.

* `EBUSY` - The file named by the _path_ argument cannot be unlinked because it is being used by the system or
another process and the implementation considers this an error.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of _path_ does not name an existing file or _path_ is an empty string.

* `ENOTDIR` - A component of the _path_ prefix names an existing file that is neither a directory nor a symbolic link to
a directory, or the _path_ argument contains at least one non-`<slash>` character and ends with one or more trailing
`<slash>` characters and the last path name component names an existing file that is neither a directory nor a symbolic
link to a directory.

* `EPERM` - The file named by _path_ is a directory, and either the calling process does not have appropriate
privileges, or the implementation prohibits using `unlink()` on directories.

* `EPERM` or `EACCES` - The `S_ISVTX` flag is set on the directory containing the file referred to by the _path_
argument and the process does not satisfy the criteria specified in XBD Directory Protection.

* `EROFS` - The directory entry to be unlinked is part of a read-only file system.

The `unlinkat()` function shall fail if:

* `EACCES` - The access mode of the open file description associated with _fd_ is not `O_SEARCH` and the permissions of
the directory underlying _fd_ do not permit directory searches.

* `EBADF` - The _path_ argument does not specify an absolute path and the _fd_ argument is neither `AT__fd_CWD` nor a
valid file descriptor open for reading or searching.

* `ENOTDIR` - The _path_ argument is not an absolute path and _fd_ is a file descriptor associated with a non-directory
file.

* `EEXIST` or `ENOTEMPTY` - The flag parameter has the `AT_REMOVEDIR` bit set and the _path_ argument names a directory
that is not an empty directory, or there are hard links to the directory other than dot or a single entry in dot-dot.

* `ENOTDIR` - The flag parameter has the `AT_REMOVEDIR` bit set and _path_ does not name a directory.

These functions may fail and not unlink the file if:

* `EBUSY` - The file named by _path_ is a named `STREAM`.

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

* `ETXTBSY` - The entry to be unlinked is the last directory entry to a pure procedure (shared text) file that is being
executed.

The `unlinkat()` function may fail if:

* `EINVAL` - The value of the flag argument is not valid.

<!-- #MUST_BE: function by default shall be untested, when tested there should be a link to test location and test
command for ia32 test runner  -->
## Tests

Untested

<!-- #MUST_BE: check for pending issues in  -->
## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
