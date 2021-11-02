# Synopsis 
`#include <unistd.h>`</br>
` int rmdir(const char *path);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `rmdir()` function shall remove a directory whose name is given by _path_. The directory shall be removed only if
it is an empty directory.

If the directory is the root directory or the current working directory of any process, it is unspecified whether the function
succeeds, or whether it shall fail and set errno to `EBUSY`.

If _path_ names a symbolic link, then `rmdir()` shall fail and set errno to `ENOTDIR`.

If the _path_ argument refers to a path whose final component is either `dot` or `dot-dot`, `rmdir()` shall fail.

If the directory's link count becomes `0` and no process has the directory open, the space occupied by the directory shall be
freed and the directory shall no longer be accessible. If one or more processes have the directory open when the last link is
removed, the dot and dot-dot entries, if present, shall be removed before `rmdir()` returns and no new entries may be created
in the directory, but the directory shall not be removed until all references to the directory are closed.

If the directory is not an empty directory, `rmdir()` shall fail and set errno to `EEXIST` or `ENOTEMPTY`.

Upon successful completion, `rmdir()` shall mark for update the last data modification and last file status change
timestamps of the parent directory.


## Return value


Upon successful completion, the function `rmdir()` shall return `0`. Otherwise, `-1` shall be returned, and `errno` set to
indicate the error. If `-1` is returned, the named directory shall not be changed.


## Errors


The `rmdir()` function shall fail if:


 * `EACCES` - Search permission is denied on a component of the _path_ prefix, or write permission is denied on the parent directory of the
directory to be removed.

 * `EBUSY` - The directory to be removed is currently in use by the system or some process and the implementation considers this to be an
error.
`EEXIST` or `ENOTEMPTY`

The _path_ argument names a directory that is not an empty directory, or there are hard links to the directory other than dot
or a single entry in dot-dot.

 * `EINVAL` - The _path_ argument contains a last component that is dot.

 * `EIO` - A physical I/O error has occurred.

 * `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

 * `ENAMETOOLONG` - The length of a component of a pathname is longer than `NAME_MAX`.

 * `ENOENT` - A component of _path_ does not name an existing file, or the path argument names a nonexistent directory or points
to an empty string.

 * `ENOTDIR` - A component of _path_ names an existing file that is neither a directory nor a symbolic link to a directory.

 * `EPERM` or `EACCES` - The `S_ISVTX` flag is set on the directory containing the file referred to by the _path_ argument and the process does not
satisfy the criteria specified in XBD Directory Protection. 

 * `EROFS` - The directory entry to be removed resides on a read-only file system.


The `rmdir()` function may fail if:


 * `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

 * `ENAMETOOLONG` - The length of a pathname exceeds `PATH_MAX`, or pathname resolution of a symbolic link produced an intermediate result with a
length that exceeds `PATH_MAX`.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
