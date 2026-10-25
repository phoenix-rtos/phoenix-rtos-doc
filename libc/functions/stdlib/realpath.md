# realpath

## Synopsis

```c
#include <stdlib.h>

char *realpath(const char *restrict file_name,
               char *restrict resolved_name);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `realpath()` function shall derive, from the path name pointed to by _file_name_, an absolute path name that
resolves to the same directory entry, whose resolution does not involve `'.'`, `'..'`, or symbolic links. If
_resolved_name_ is a `null` pointer, the generated path name shall be stored as a null-terminated string in a buffer
allocated as if by a call to `malloc()`. Otherwise, if {`PATH_MAX`} is defined as a constant in the `<limits.h>` header,
then the generated path name shall be stored as a null-terminated string, up to a maximum of {`PATH_MAX`} bytes, in the
buffer pointed to by _resolved_name_.

If _resolved_name_ is not a `null` pointer and {`PATH_MAX`} is not defined as a constant in the `<limits.h>` header, the
behavior is undefined.

## Return value

Upon successful completion, `realpath()` shall return a pointer to the buffer containing the resolved name. Otherwise,
`realpath()` shall return a `null` pointer and set `errno` to indicate the error.

If the _resolved_name_ argument is a `null` pointer, the pointer returned by `realpath()` can be passed to `free()`.

If the _resolved_name_ argument is not a `null` pointer and the `realpath()` function fails, the contents of the buffer
pointed to by _resolved_name_ are undefined.

## Errors

The `realpath()` function shall fail if:

* `EACCES` - Search permission was denied for a component of the path prefix of _file_name_.

* `EINVAL` - The _file_name_ argument is a `null` pointer.

* `EIO` - An error occurred while reading from the file system.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _file_name_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than the name length limit of the filesystem,
which may differ from `NAME_MAX` (see POSIX deviations).

* `ENOENT` - A component of _file_name_ does not name an existing file or _file_name_ points to an empty string.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to a
directory, or the _file_name_ argument contains at least one non-`<slash>` character and ends with one or more trailing
`<slash>` characters and the last path name component names an existing file that is neither a directory nor a symbolic
link to a directory.

The `realpath()` function may fail if:

* `EACCES` - The _file_name_ argument does not begin with a `<slash>` and none of the symbolic links (if any) processed
during path name resolution of _file_name_ had contents that began with a `<slash>`, and either search permission was
denied for the current directory or read or search permission was denied for a directory above the current directory
in the file hierarchy.

* `ELOOP` - More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the _file_name_ argument.

* `ENAMETOOLONG` - The length of a path name exceeds {`PATH_MAX`}, or path name resolution of a symbolic link produced
an intermediate result with a length that exceeds {`PATH_MAX`}.

* `ENOMEM` - Insufficient storage space is available.

## POSIX deviations

The length of a path name component is not checked against `NAME_MAX` by libphoenix, but by the filesystem server,
against the name length limit of the filesystem, which may differ from `NAME_MAX`. The error reported for a too long
component of the path name therefore depends on the filesystem (see the deviations of `open()`).
