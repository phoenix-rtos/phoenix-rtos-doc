# Synopsis

`#include <unistd.h>`</br>

`int chdir(const char *path);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to change working directory. The `chdir()` function shall cause the directory named by the pathname
pointed to by the _path_ argument to become the current working directory, that is, the starting point for path searches
for pathnames not beginning with `'/'`.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned, the current working directory
shall remain unchanged, and `errno` shall be set to indicate the error.

## Errors

The `chdir()` function shall fail if:

* `EACCES` - Search permission is denied for any component of the pathname.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a component of a pathname is longer than `NAME_MAX`.

* `ENOENT` - A component of _path_ does not name an existing directory or path is an empty string.

* `ENOTDIR` - A component of the pathname names an existing file that is neither a directory nor a symbolic link
 to a directory.

The `chdir()` function may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the _path_ argument.

* `ENAMETOOLONG` - The length of a pathname exceeds `PATH_MAX`, or pathname resolution of a symbolic link produced an
 intermediate result with alength that exceeds `PATH_MAX`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
