# exit

## Synopsis

`#include <stdlib.h>`

`void exit(int status);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The value of _status_ may be 0, `EXIT_SUCCESS,` `EXIT_FAILURE,` or any other value, though only the least significant
8 bits (that is, `(_status_ & 0377)`) shall be available from `wait()` and `waitpid()`. The full value shall be
available from `waitid()` and in the `siginfo_t` passed to a signal handler for `SIGCHLD`.

The `exit()` function shall first call all functions registered by `atexit()`, in the reverse order of their
registration, except that a function is called after any previously registered functions that had already been called at
the time it was registered. Each function is called as many times as it was registered. If, during the call to any such
function, a call to the `longjmp()` function is made that would terminate the call to the registered function, the
behavior is undefined.

If a function registered by a call to `atexit()` fails to return, the remaining registered functions shall not be called
and the rest of the `exit()` processing shall not be completed. If `exit()` is called more than once, the behavior is
undefined.

The `exit()` function shall then flush all open streams with unwritten buffered data and close all open streams.
Finally, the process shall be terminated with the same consequences as described in Consequences of Process
Termination.

## Return value

The `exit()` function does not return.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
