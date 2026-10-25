# seekdir

## Synopsis

```c
#include <dirent.h>

void seekdir(DIR *dirp, long loc);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `seekdir()` function shall set the position of the next `readdir()` operation on the directory stream specified by
_dirp_ to the position specified by _loc_. The value of _loc_ should have been returned from an earlier call to
`telldir()` using the same directory stream. The new position reverts to the one associated with the directory stream
when `telldir()` was performed.

If the value of _loc_ was not obtained from an earlier call to `telldir()`, or if a call to `rewinddir()` occurred
between the call to `telldir()` and the call to `seekdir()`, the results of subsequent calls to `readdir()` are
unspecified.

## Return value

The `seekdir()` function shall not return a value.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
