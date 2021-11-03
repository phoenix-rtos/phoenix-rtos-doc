# Synopsis 
`#include <unistd.h>`</br>
` int link(const char *path1, const char *path2);`</br>
`#include <fcntl.h>`</br>
` int linkat(int fd1, const char *path1, int fd2, const char *path2, int flag);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `link()` function shall create a new link (directory entry) for the existing file, _path1_.

The _path1_ argument points to a pathname naming an existing file. The _path2_ argument points to a pathname naming
the new directory entry to be created. The `link()` function shall atomically create a new link for the existing file and the
link count of the file shall be incremented by one.

If _path1_ names a directory, `link()` shall fail unless the process has appropriate privileges and the implementation
supports using `link()` on directories.

If _path1_ names a symbolic link, it is implementation-defined whether `link()` follows the symbolic link, or creates
a new link to the symbolic link itself.

Upon successful completion, `link()` shall mark for update the last file status change timestamp of the file. Also, the
last data modification and last file status change timestamps of the directory that contains the new entry shall be marked for
update.

If `link()` fails, no link shall be created and the link count of the file shall remain unchanged.

The implementation may require that the calling process has permission to access the existing file.

The `linkat()` function shall be equivalent to the `link()` function except that symbolic links shall be handled as
specified by the value of _flag_ (see below) and except in the case where either _path1_ or _path2_ or both are
relative paths. In this case a relative path _path1_ is interpreted relative to the directory associated with the file
descriptor _fd1_ instead of the current working directory and similarly for _path2_ and the file descriptor _fd2_.

If the access mode of the open file description associated with the file descriptor is not `O_SEARCH,` the function shall check
whether directory searches are permitted using the current permissions of the directory underlying the file descriptor. If the
access mode is `O_SEARCH,` the function shall not perform the check.

Values for _flag_ are constructed by a bitwise-inclusive OR of flags from the following list, defined in `<fcntl.h>`:

`AT_SYMLINK_FOLLOW`

If _path1_ names a symbolic link, a new link for the target of the symbolic link is created.

If `linkat()` is passed the special value `AT_FDCWD` in the _fd1_ or _fd2_ parameter, the current working directory
shall be used for the respective path argument. If both _fd1_ and _fd2_ have value `AT_FDCWD,` the behavior shall be
identical to a call to `link()`, except that symbolic links shall be handled as specified by the value of _flag_.

If the `AT_SYMLINK_FOLLOW` flag is clear in the _flag_ argument and the _path1_ argument names a symbolic link, a new
link is created for the symbolic link _path1_ and not its target.


## Return value


Upon successful completion, these functions shall return `0`. Otherwise, these functions shall return `-1` and set `errno` to
indicate the error.



## Errors


These functions shall fail if:


 * `EACCES` - A component of either path prefix denies search permission, or the requested link requires writing in a directory that denies
write permission, or the calling process does not have permission to access the existing file and this is required by the
implementation.

 * `EEXIST` - The _path2_ argument resolves to an existing directory entry or refers to a symbolic link.

 * `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path1_ or _path2_ argument.

 * `EMLINK` - The number of links to the file named by _path1_ would exceed `LINK_MAX`.

 * `ENAMETOOLONG` - The length of a component of a pathname is longer than `NAME_MAX`.

 * `ENOENT` - A component of either path prefix does not exist; the file named by _path1_ does not exist; or _path1_ or
_path2_ points to an empty string.
`ENOENT` or `ENOTDIR`

The _path1_ argument names an existing non-directory file, and the _path2_ argument contains at least one non-
`<slash>` character and ends with one or more trailing `<slash>` characters. If _path2_ without the trailing
`<slash>` characters would name an existing file, an `ENOENT` error shall not occur.

 * `ENOSPC` - The directory to contain the link cannot be extended.

 * `ENOTDIR` - A component of either path prefix names an existing file that is neither a directory nor a symbolic link to a directory, or the
_path1_ argument contains at least one non- `<slash>` character and ends with one or more trailing `<slash>`
characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory,
or the _path1_ argument names an existing non-directory file and the _path2_ argument names a nonexistent file, contains
at least one non- `<slash>` character, and ends with one or more trailing `<slash>` characters.

 * `EPERM` - The file named by _path1_ is a directory and either the calling process does not have appropriate privileges or the
implementation prohibits using `link()` on directories.

 * `EROFS` - The requested link requires writing in a directory on a read-only file system.

 * `EXDEV` - The link named by _path2_ and the file named by _path1_ are on different file systems and the implementation does not
support links between file systems.

 * `EXDEV` - _path1_ refers to a named `STREAM`. 

The `linkat()` function shall fail if:


 * `EACCES` - The access mode of the open file description associated with _fd1_ or _fd2_ is not O_SEARCH and the permissions of
the directory underlying _fd1_ or _fd2_, respectively, do not permit directory searches.

 * `EBADF` - The _path1_ or _path2_ argument does not specify an absolute path and the _fd1_ or _fd2_ argument,
respectively, is neither AT_FDCWD nor a valid file descriptor open for reading or searching.

 * `ENOTDIR` - The _path1_ or _path2_ argument is not an absolute path and _fd1_ or _fd2_, respectively, is a file
descriptor associated with a non-directory file.

These functions may fail if:


 * `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path1_ or _path2_ argument.
`ENAMETOOLONG`

The length of a pathname exceeds `PATH_MAX`, or pathname resolution of a symbolic link produced an intermediate result with a
length that exceeds `PATH_MAX`.


The `linkat()` function may fail if:


 * `EINVAL` - The value of the _flag_ argument is not valid.





## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
