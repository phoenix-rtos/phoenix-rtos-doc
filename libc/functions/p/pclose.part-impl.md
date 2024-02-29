# pclose

## Synopsis

`#include <stdio.h>`

`int pclose(FILE *stream);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pclose()` function shall close a stream that was opened by `popen()`, wait for the command to terminate, and return
the termination status of the process that was running the command language interpreter. However, if a call caused the
termination status to be unavailable to `pclose()`, then `pclose()` shall return `-1` with `errno` set to `ECHILD` to
report this situation. This can happen if the application calls one of the following functions:

* `wait()`

* `waitpid()` with a pid argument less than or equal to 0 or equal to the process ID of the command line interpreter

* Any other function not defined in `POSIX.1-2017` that could do one of the above

In any case, `pclose()` shall not return before the child process created by `popen()` has terminated.

If the command language interpreter cannot be executed, the child termination status returned by `pclose()` shall be as
if the command language interpreter terminated using `exit(127)` or `_exit(127)`.

The `pclose()` function shall not affect the termination status of any child of the calling process other than the one
created by `popen()` for the associated stream.

If the argument _stream_ to `pclose()` is not a pointer to a stream created by `popen()`, the result of `pclose()` is
undefined.

If a thread is canceled during execution of `pclose()`, the behavior is undefined.

## Return value

Upon successful return, `pclose()` shall return the termination status of the command language interpreter. Otherwise,
`pclose()` shall return `-1` and set `errno` to indicate the error.

## Errors

The `pclose()` function shall fail if:

* [`ECHILD`] - The status of the child process could not be obtained, as described above.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
