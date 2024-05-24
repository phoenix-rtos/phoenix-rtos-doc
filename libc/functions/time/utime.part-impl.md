# utime

## Synopsis

`#include <time.h>`

`int utime(const char *path, const struct utimbuf *times);`

## Status

Declared, not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `utime()` function shall set the access and modification times of the file named by the _path_ argument.

If _times_ is a null pointer, the access and modification times of the file shall be set to the current time.
The effective user ID of the process shall match the owner of the file, or the process has write permission to the file
or has appropriate privileges, to use `utime()` in this manner.

If _times_ is not a null pointer, _times_ shall be interpreted as a pointer to a `utimbuf` structure and the access and
modification times shall be set to the values contained in the designated structure. Only a process with the effective
user ID equal to the user ID of the file or a process with appropriate privileges may use `utime()` this way.

The `utimbuf` structure is defined in the `<utime.h>` header. The times in the structure `utimbuf` are measured in
seconds since the Epoch.

Upon successful completion, the `utime()` function shall mark the last file status change timestamp for update; see
`<sys/stat.h>`.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` shall be set to
indicate the error, and the file times shall not be affected.

## Errors

The `utime()` function shall fail if:

* `EACCES` - Search permission is denied by a component of the _path_ prefix; or the _times_ argument is a `null`
 pointer and the effective user ID of the process does not match the owner of the file, the process does not have write
 permission for the file, and the process does not have appropriate privileges.
* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.
* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.
* `ENOENT` - A component of _path_ does not name an existing file or _path_ is an empty string.
* `ENOTDIR` - A component of the _path_ prefix names an existing file that is neither a directory nor a symbolic link
 to a directory, or the _path_ argument contains at least one non- `<slash>` character and ends with one or more
 trailing `<slash>` characters and the last path name component names an existing file that is neither a directory nor a
 symbolic link to a directory.
* `EPERM` - The _times_ argument is not a `null` pointer and the effective user ID of the calling process does not
 match the owner of the file and the calling process does not have appropriate privileges.
* `EROFS` - The file system containing the file is read-only.

The `utime()` function may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.  
* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
 intermediate result with a length that exceeds `PATH_MAX`.  

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
