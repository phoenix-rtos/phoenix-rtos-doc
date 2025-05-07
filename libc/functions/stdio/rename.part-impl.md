# rename

## Synopsis

```c
#include <stdio.h>

int rename(const char *old, const char *new);

#include <fcntl.h>

int renameat(int oldfd, const char *old, int newfd, const char *new);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `rename()` function shall change the name of a file. The _old_ argument points to the path name of the file to be
renamed. The _new_ argument points to the new path name of the file. If the _new_ argument does not resolve to an
existing directory entry for a file of type directory and the new argument contains at least one non- `<slash>`
character and ends with one or more trailing ``<slash>`` characters after all symbolic links have been processed,
`rename()`shall fail.

If either the _old_ or _new_ argument names a symbolic link, `rename()` shall operate on the symbolic link itself,
and shall not resolve the last component of the argument. If the _old_ argument and the _new_ argument resolve to
either the same existing directory entry or different directory entries for the same existing file, `rename()`
shall return successfully and perform no other action.

If the _old_ argument points to the path name of a file that is not a directory, the _new_ argument shall not point
to the path name of a directory. If the link named by the _new_ argument exists, it shall be removed and _old_ renamed
to _new_. In this case, a link named _new_ shall remain visible to other threads throughout the renaming operation and
refer either to the file referred to by _new_ or _old_ before the operation began. Write access permission is required
for both the directory containing _old_ and the directory containing _new_.

If the _old_ argument points to the path name of a directory, the _new_ argument shall not point to the path name of a
file that is not a directory. If the directory named by the _new_ argument exists, it shall be removed and _old_ renamed
to _new_. In this case, a link named _new_ shall exist throughout the renaming operation and shall refer either to the
directory referred to by _new_ or _old_ before the operation began. If _new_ names an existing directory, it shall be
required to be an empty directory.

If either path name argument refers to a path whose final component is either dot or dot-dot, `rename()` shall fail.

If the _old_ argument points to a path name of a symbolic link, the symbolic link shall be renamed. If the _new_
argument points to a path name of a symbolic link, the symbolic link shall be removed.

The _old_ path name shall not name an ancestor directory of the _new_ path name. Write access permission is required for
the directory containing _old_ and the directory containing _new_. If the _old_ argument points to the path name of a
directory, write access permission may be required for the directory named by _old_, and, if it exists, the directory
named by _new_.

If the link named by the _new_ argument exists and the file's link count becomes `0` when it is removed and no process
has the file open, the space occupied by the file shall be freed, and the file shall no longer be accessible. If one or
more processes have the file open when the last link is removed, the link shall be removed before `rename()` returns,
but the removal of the file contents shall be postponed until all references to the file are closed.

Upon successful completion, `rename()` shall mark for update the last data modification and last file status change
timestamps of the parent directory of each file.

If the `rename()` function fails for any reason other than `EIO`, any file named by _new_ shall be unaffected.

The `renameat()` function shall be equivalent to the `rename()` function except in the case where either _old_ or _new_
specifies a relative path. If _old_ is a relative path, the file to be renamed is located relative to the directory
associated with the file descriptor _oldfd_ instead of the current working directory. If _new_ is a relative path, the
same happens only relative to the directory associated with _newfd_. If the access mode of the open file description
associated with the file descriptor is not `O_SEARCH,` the function shall check whether directory searches are permitted
using the current permissions of the directory underlying the file descriptor. If the access mode is `O_SEARCH,` the
function shall not perform the check.

If `renameat()` is passed the special value `AT_FDCWD` in the _oldfd_ or _newfd_ parameter, the current working
directory shall be used in the determination of the file for the respective path parameter.

## Return value

Upon successful completion, the `rename()` function shall return `0`. Otherwise, it shall return `-1`, errno shall be
set to indicate the error, and neither the file named by _old_ nor the file named by _new_ shall be changed or
created.

Upon successful completion, the `renameat()` function shall return `0`. Otherwise, it shall return `-1` and set errno to
indicate the error.

## Errors

The `rename()` and `renameat()` functions shall fail if:

* `EACCES` - A component of either path prefix denies search permission; or one of the directories containing _old_
 or _new_ denies write permissions; or, write permission is required and is denied for a directory pointed to by the
 _old_ or _new_ arguments.

* `EBUSY` - The directory named by _old_ or _new_ is currently in use by the system or another process, and the
 implementation considers this an error.

* `EEXIST` or `ENOTEMPTY` - The link named by _new_ is a directory that is not an empty directory.

* `EINVAL` - The _old_ path name names an ancestor directory of the _new_ path name, or either path name argument
 contains a final component that is dot or dot-dot.

* `EIO` - A physical I/O error has occurred.

* `EISDIR` - The _new_ argument points to a directory and the _old_ argument points to a file that is not a directory.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the path argument.

* `EMLINK` - The file named by _old_ is a directory, and the link count of the parent directory of _new_ would exceed
 `LINK_MAX`.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - The link named by _old_ does not name an existing file, a component of the path prefix of _new_ does not
 exist, or either _old_ or _new_ points to an empty string.

* `ENOSPC` - The directory that would contain _new_ cannot be extended.

* `ENOTDIR` - A component of either path prefix names an existing file that is neither a directory nor a symbolic
 link to a directory; or the _old_ argument names a directory and the _new_ argument names a non-directory file; or the
 _old_ argument contains at least one non- `<slash>` character and ends with one or more trailing `<slash>` characters
 and the last path name component names an existing file that is neither a directory nor a symbolic link to a directory;
 or the _old_ argument names an existing non-directory file and the _new_ argument names a nonexistent file, contains at
 least one non- `<slash>` character, and ends with one or more trailing `<slash>` characters; or the _new_ argument
 names an existing non-directory file, contains at least one non- `<slash>` character, and ends with one or more
 trailing `<slash>` characters.  

* `EPERM` or `EACCES` - The S_ISVTX flag is set on the directory containing the file referred to by _old_ and the
 process does not satisfy the criteria specified in XBD Directory Protection with respect to old; or _new_ refers to
 an existing file, the S_ISVTX flag is set on the directory containing this file, and the process does not satisfy the
 criteria specified in XBD Directory Protection with respect to this file.

* `EROFS` - The requested operation requires writing in a directory on a read-only file system.

* `EXDEV` - The links named by _new_ and _old_ are on different file systems and the implementation does not support
 links between file systems.

  In addition, the `renameat()` function shall fail if:

* `EACCES` - The access mode of the open file description associated with _oldfd_ or _newfd_ is not O_SEARCH and the
 permissions of the directory underlying _oldfd_ or _newfd_, respectively, do not permit directory searches.

* `EBADF` - The _old_ argument does not specify an absolute path and the _oldfd_ argument is neither AT_FDCWD nor a
 valid file descriptor open for reading or searching, or the _new_ argument does not specify an absolute path and the
 _newfd_ argument is neither AT_FDCWD nor a valid file descriptor open for reading or searching.

* `ENOTDIR` - The _old_ or _new_ argument is not an absolute path and _oldfd_ or _newfd_, respectively, is a file
 descriptor associated with a non-directory file.

The `rename()` and `renameat()` functions may fail if:

* `EBUSY` - The file named by the _old_ or _new_ arguments is a named STREAM.

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the path argument.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
 intermediate result with a length that exceeds `PATH_MAX`.

* `ETXTBSY` - The file named by _new_ exists and is the last directory entry to a pure procedure (shared text) file
 that is being executed.

The following sections are informative.

## Tests

Untested

## Known bugs

None
