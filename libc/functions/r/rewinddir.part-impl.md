# Name

rewinddir - reset the position of a directory stream to the beginning of a directory

## Synopsis

`#include <dirent.h>`

`void rewinddir(DIR *dirp);`

## Description

The `rewinddir()` function shall reset the position of the directory stream to which `dirp` refers to the beginning of the directory. It shall also cause the directory stream to refer to the current state of the corresponding directory, as a call to `opendir()` would have done. If `dirp` does not refer to a directory stream, the effect is undefined.

After a call to the `fork()` function, either the parent or child (but not both) may continue processing the directory stream using `readdir()`, `rewinddir()`, or `seekdir()`. If both the parent and child processes use these functions, the result is undefined.

## Return value

The `rewinddir()` function shall not return a value.

## Errors

No errors are defined.

## Application usage

The `rewinddir()` function should be used in conjunction with `opendir()`, `readdir()`, and `closedir()` to examine the contents of the directory. This method is recommended for portability.

## Tests

Untested

## Known bugs

None
