# mkdtemp

## Synopsis

```c
#include <stdlib.h>

char *mkdtemp(char *template);

int mkstemp(char *template);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `mkdtemp()` function shall create a directory with a unique name derived from _template_. The application shall
ensure that the string provided in _template_ is a path name ending with at least six trailing `'X'` characters. The
`mkdtemp()` function shall modify the contents of _template_ by replacing six or more `'X'` characters at the end of
the path name with the same number of characters from the portable filename character set. The characters shall be
chosen such that the resulting path name does not duplicate the name of an existing file at the time of the call to
`mkdtemp()`. The `mkdtemp()` function shall use the resulting path name to create the new directory as if by a call to:

```c
mkdir(pathname, S_IRWXU)
```

The `mkstemp()` function shall create a regular file with a unique name derived from _template_ and return a file
descriptor for the file open for reading and writing. The application shall ensure that the string provided in
_template_ is a path name ending with at least six trailing `'X'` characters. The `mkstemp()` function shall modify the
contents of _template_ by replacing six or more `'X'` characters at the end of the path name with the same number of
characters from the portable filename character set. The characters shall be chosen such that the resulting path name
does not duplicate the name of an existing file at the time of the call to `mkstemp()`. The `mkstemp()` function shall
use the resulting path name to create the file, and obtain a file descriptor for it, as if by a call to:

```c
open(pathname, O_RDWR|O_CREAT|O_EXCL, S_IRUSR|S_IWUSR)
```

By behaving as if the `O_EXCL` flag for `open()` is set, the function prevents any possible race condition between
testing whether the file exists and opening it for use.

Exactly the last six `'X'` characters are replaced with characters chosen at random; any additional trailing `'X'`
characters are treated as a fixed part of the template.

## Return value

Upon successful completion, the `mkdtemp()` function shall return the value of _template_. Otherwise, it shall return a
`null` pointer and shall set `errno` to indicate the error.

Upon successful completion, the `mkstemp()` function shall return an open file descriptor. Otherwise, it shall return
`-1` and shall set `errno` to indicate the error.

## Errors

The `mkdtemp()` function shall fail if:

* `EACCES` - Search permission is denied on a component of the path prefix, or write permission is denied on the parent
directory of the directory to be created.

* `EINVAL` - The string pointed to by _template_ does not end in `"XXXXXX"`.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the path of the directory to be created.

* `EMLINK` - The link count of the parent directory would exceed {`LINK_MAX`}.

* `ENAMETOOLONG` - The length of a component of a path name is longer than {`NAME_MAX`}.

* `ENOENT` - A component of the path prefix specified by the _template_ argument does not name an existing directory.

* `ENOSPC` - The file system does not contain enough space to hold the contents of the new directory or to extend the
parent directory of the new directory.

* `ENOTDIR` - A component of the path prefix names an existing file that is neither a directory nor a symbolic link to
a directory.

* `EROFS` - The parent directory resides on a read-only file system.

The `mkdtemp()` function may fail if:

* `ELOOP` - More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the path of the directory to
be created.

* `ENAMETOOLONG` - The length of a path name exceeds {`PATH_MAX`}, or path name resolution of a symbolic link produced
an intermediate result with a length that exceeds {`PATH_MAX`}.

The error conditions for the `mkstemp()` function are defined in `open()`.

## POSIX deviations

No POSIX deviations discovered.
