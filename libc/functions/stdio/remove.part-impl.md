# remove

## Synopsis

`#include <stdio.h>`

`int remove(const char *path);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `remove()` function shall cause the file named by the path name pointed to by _path_ to be no longer accessible by
that name. A subsequent attempt to open that file using that name shall fail, unless it is created as new.

* If _path_ does not name a directory, `remove(path)` shall be equivalent to `unlink(path)`.
* If _path_ names a directory, `remove(path)` shall be equivalent to `rmdir(path)`.

## Return value

Refer to `rmdir()` or `unlink()`.

## Errors

Refer to `rmdir()` or `unlink()`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
