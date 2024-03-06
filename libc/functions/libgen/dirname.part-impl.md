# dirname

## Synopsis

`#include <libgen.h>`

`char *dirname(char *path);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `dirname()` function shall take a pointer to a character string that contains a path name, and return a pointer to a
string that is a path name of the parent directory of that file. The `dirname()` function shall not perform path name
resolution. The result shall not be affected by whether _path_ exists or by its file type. Trailing `'/'`
characters in the _path_ that are not also leading `'/'` characters shall not be counted as part of the _path_.

If _path_ does not contain a `'/'`, then `dirname()` shall return a pointer to the string ".". If
_path_ is a null pointer or points to an empty string, `dirname()` shall return a pointer to the string `"."`
.

The `dirname()` function may modify the string pointed to by _path_, and may return a pointer to static storage that
may then be overwritten by a subsequent call to `dirname()`.

The `dirname()` function need not be thread-safe.

## Return value

The `dirname()` function shall return a pointer to a string as described above.

The `dirname()` function may modify the string pointed to by _path_, and may return a pointer to internal storage. The
returned pointer might be invalidated, or the storage might be overwritten by a subsequent call to `dirname()`.
The returned pointer might also be invalidated if the calling thread is terminated.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
