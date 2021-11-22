# Synopsis 
`#include <signal.h>`</br>

` int sigsuspend(const sigset_t *sigmask); `</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `sigsuspend()` function shall replace the current signal mask of the calling thread with the set of signals pointed to
by _sigmask_ and then suspend the thread until delivery of a signal whose action is either to execute a signal-catching
function or to terminate the process. This shall not cause any other signals that may have been pending on the process to become
pending on the thread.
If the action is to terminate the process then `sigsuspend()` shall never return. If the action is to execute a
signal-catching function, then `sigsuspend()` shall return after the signal-catching function returns, with the signal mask
restored to the set that existed prior to the `sigsuspend()` call.
It is not possible to block signals that cannot be ignored. This is enforced by the system without causing an error to be
indicated.


## Return value


Since `sigsuspend()` suspends thread execution indefinitely, there is no successful completion return value. If a return
occurs, `-1` shall be returned and `errno` set to indicate the error.


## Errors


The `sigsuspend()` function shall fail if:


 * `EINTR` - A signal is caught by the calling process and control is returned from the signal-catching function.



The following sections are informative.

## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
