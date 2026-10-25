# scandir

## Synopsis

```c
#include <dirent.h>

int alphasort(const struct dirent **d1, const struct dirent **d2);

int scandir(const char *dir, struct dirent ***namelist,
            int (*sel)(const struct dirent *),
            int (*compar)(const struct dirent **, const struct dirent **));
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `alphasort()` function can be used as the comparison function for the `scandir()` function to sort the directory
entries, _d1_ and _d2_, into alphabetical order. Sorting happens as if by calling the `strcoll()` function on the
`d_name` element of the `dirent` structures passed as the two parameters. If the `strcoll()` function fails, the
return value of `alphasort()` is unspecified.

The `alphasort()` function shall not change the setting of `errno` if successful. Since no return value is reserved
to indicate an error, an application wishing to check for error situations should set `errno` to `0`, then call
`alphasort()`, then check `errno`.

The `scandir()` function shall scan the directory _dir_, calling the function referenced by _sel_ on each directory
entry. Entries for which the function referenced by _sel_ returns non-zero shall be stored in strings allocated as if by
a call to `malloc()`, and sorted as if by a call to `qsort()` with the comparison function _compar_, except that
_compar_ need not provide total ordering. The strings are collected in array _namelist_ which shall be allocated as if
by a call to `malloc()`. If _sel_ is a `null` pointer, all entries shall be selected. If the comparison function
_compar_ does not provide total ordering, the order in which the directory entries are stored is unspecified. If
_compar_ is a `null` pointer, the entries are not sorted.

## Return value

Upon successful completion, the `alphasort()` function shall return an integer greater than, equal to, or less than
`0`, according to whether the name of the directory entry pointed to by _d1_ is lexically greater than, equal to, or
less than the directory pointed to by _d2_ when both are interpreted as appropriate to the current locale. There is no
return value reserved to indicate an error.

Upon successful completion, the `scandir()` function shall return the number of entries in the array and a pointer to
the array through the parameter _namelist_. Otherwise, the `scandir()` function shall return `-1`.

## Errors

The `scandir()` function shall fail if:

* `EACCES` - Search permission is denied for the component of the path prefix of _dir_ or read permission is denied
for _dir_.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the _dir_ argument.

* `ENAMETOOLONG` - The length of a component of a path name is longer than the name length limit of the filesystem,
which may differ from `NAME_MAX` (see POSIX deviations).

* `ENOENT` - A component of _dir_ does not name an existing directory or _dir_ is an empty string.

* `ENOMEM` - Insufficient storage space is available.

* `ENOTDIR` - A component of _dir_ names an existing file that is neither a directory nor a symbolic link to a
directory.

* `EOVERFLOW` - One of the values to be returned or passed to a callback function cannot be represented correctly.

The `scandir()` function may fail if:

* `ELOOP` - More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the _dir_ argument.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENAMETOOLONG` - The length of a path name exceeds {`PATH_MAX`}, or path name resolution of a symbolic link
produced an intermediate result with a length that exceeds {`PATH_MAX`}.

* `ENFILE` - Too many files are currently open in the system.

## POSIX deviations

The length of a path name component is not checked against `NAME_MAX` by libphoenix, but by the filesystem server,
against the name length limit of the filesystem, which may differ from `NAME_MAX`. The error reported for a too long
component of the path name therefore depends on the filesystem (see the deviations of `open()`).
