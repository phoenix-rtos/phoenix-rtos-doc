# rewinddir

## Synopsis

```c
#include <dirent.h>

void rewinddir(DIR *dirp);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `rewinddir()` function shall reset the position of the directory stream to which _dirp_ refers to the beginning of
the directory. It shall also cause the directory stream to refer to the current state of the corresponding directory,
as a call to `opendir()` would have done. If _dirp_ does not refer to a directory stream, the effect is undefined.

After a call to the `fork()` function, either the parent or child (but not both) may continue processing the directory
stream using `readdir()`, `rewinddir()`, or `seekdir()`. If both the parent and child processes use these functions,
the result is undefined.

## Return value

The `rewinddir()` function shall not return a value.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
