# system

## Synopsis

`#include <stdlib.h>`

`int system(const char *command);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If command is a `null` pointer, the `system()` function shall determine whether the host environment has a command
processor. If command is not a `null` pointer, the `system()` function shall pass the string pointed to by command
to that command processor to be executed in an implementation-defined manner; this might then cause the program calling
`system()` to behave in a non-conforming manner or to terminate.
The
`system()` function shall behave as if a child process were created using `fork()`,
and the child process invoked the `sh` utility using `execl()` as follows:

``` c
execl(<shell path>, "sh", "-c", command, (char *)0);
```

Where `<shell path>` is an unspecified path name for the sh utility. It is
unspecified whether the handlers registered with `pthread_atfork()` are called
as part of the creation of the child process.

The `system()` function shall ignore the `SIGINT` and `SIGQUIT` signals, and shall block the `SIGCHLD` signal, while
waiting for the command to terminate. If this might cause the application to miss a signal that would have killed it,
then the application should examine the return value from `system()` and take whatever action is appropriate to the
application if the command terminated due to receipt of a signal.

The `system()` function shall not affect the termination status of any child of the calling processes other than the
process or processes it itself creates.

The `system()` function shall not return until the child process has terminated.

The `system()` function need not be thread-safe.

## Return value

If command is a null pointer, `system()` shall return non-zero to indicate that a command processor is available, or
zero if none is available.   The `system()` function shall always return non-zero when command is `NULL`.

If
command is not a null pointer, `system()` shall return the termination status of the command language interpreter in
the format specified by `waitpid()`. The termination status shall be as defined for
the `sh` utility; otherwise, the termination status is unspecified. If some error prevents
the command language interpreter from executing after the child process is created, the return value from `system()`
shall be as if the command language interpreter had terminated using `exit(127)` or `_exit(127)`. If a child process
cannot be created, or if the termination status for the command language interpreter cannot be obtained, `system()`
shall return `-1` and set `errno` to indicate the error.

## Errors

  The `system()` function may set `errno` values as described by `fork()`.

In addition, `system()` may fail if:

* `ECHILD` - The status of the child process created by `system()` is no longer available.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
