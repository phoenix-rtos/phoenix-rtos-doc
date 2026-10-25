# telldir

## Synopsis

```c
#include <dirent.h>

long telldir(DIR *dirp);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `telldir()` function shall obtain the current location associated with the directory stream specified by _dirp_.

If the most recent operation on the directory stream was a `seekdir()`, the directory position returned from the
`telldir()` shall be the same as that supplied as a _loc_ argument for `seekdir()`.

The location is the offset of the next directory entry in the directory, which `readdir()` passes to the filesystem
server.

## Return value

Upon successful completion, `telldir()` shall return the current location of the specified directory stream.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
