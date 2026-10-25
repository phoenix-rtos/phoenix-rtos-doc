# tempnam

## Synopsis

```c
#include <stdio.h>

char *tempnam(const char *dir, const char *pfx);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `tempnam()` function shall generate a path name that may be used for a temporary file.

The `tempnam()` function allows the user to control the choice of a directory. The _dir_ argument points to the name of
the directory in which the file is to be created. If _dir_ is a `null` pointer or points to a string which is not a
name for an appropriate directory, the path prefix defined as `P_tmpdir` in the `<stdio.h>` header (`/var/tmp`) shall be
used. If that directory is not accessible, the root directory (`/`) is used.

Many applications prefer their temporary files to have certain initial letter sequences in their names. The _pfx_
argument should be used for this. This argument may be a `null` pointer or point to a string of up to five bytes to be
used as the beginning of the filename. Only the first five bytes of a longer string are used. If _pfx_ is a `null`
pointer, the prefix `file` is used.

The generated name ends with six characters from the portable filename character set chosen at random, and doesn't
name an existing file at the time of the call. Up to {`TMP_MAX`} names are generated before `tempnam()` gives up.

## Return value

Upon successful completion, `tempnam()` shall allocate space for a string, put the generated path name in that space,
and return a pointer to it. The pointer shall be suitable for use in a subsequent call to `free()`. Otherwise, it shall
return a `null` pointer and set `errno` to indicate the error.

## Errors

The `tempnam()` function shall fail if:

* `ENOMEM` - Insufficient storage space is available.

## POSIX deviations

No POSIX deviations discovered.
