# tmpnam

## Synopsis

`#include <stdio.h>`

`char *tmpnam(char *s);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `tmpnam()` function shall generate a string that is a valid path name that does not name an existing file. The
function is potentially capable of generating `TMP_MAX` different strings, but any or all of them may already be in
use by existing files and thus not be suitable return values.

The `tmpnam()` function generates a different string each time it is called from the same process, up to `TMP_MAX`
times. If it is called more than `TMP_MAX` times, the behavior is implementation-defined.

The implementation shall behave as if no function defined in this volume of POSIX.1-2017, except `tempnam()`, calls
`tmpnam()`.

The `tmpnam()` function need not be thread-safe if called with a `NULL` parameter.

## Return value

Upon successful completion, `tmpnam()` shall return a pointer to a string. If no suitable string can be generated, the
`tmpnam()` function shall return a `null` pointer.

If the argument _s_ is a `null` pointer, `tmpnam()` shall leave its result in an internal static object and return a
pointer to that object. Subsequent calls to `tmpnam()` may modify the same object. If the argument _s_ is not a `null`
pointer, it is presumed to point to an array of at least `L_tmpnam chars`; `tmpnam()` shall write its result in that
array and shall return the argument as its value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
