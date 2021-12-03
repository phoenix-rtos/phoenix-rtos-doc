# Synopsis 
`#include <signal.h>`</br>

` int sigaddset(sigset_t *set, int signo); `</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `sigaddset()` function adds the individual signal specified by the _signo_ to the signal set pointed to by
_set_.
Applications shall call either `sigemptyset()` or `sigfillset()` at least once for each object of type `sigset_t` prior to any other use
of that object. If such an object is not initialized in this way, but is nonetheless supplied as an argument to any of ``pthread_sigmask()`,` `sigaction()`,
`sigaddset()`, `sigdelset()`, `sigismember()`, `sigpending()`, `sigprocmask()`, `sigsuspend()`, `sigtimedwait()`, `sigwait()`, or `sigwaitinfo()`, the results are undefined.


## Return value


Upon successful completion, `sigaddset()` shall return `0`; otherwise, it shall return `-1` and set `errno` to indicate
the error.


## Errors


The `sigaddset()` function may fail if:


 - `EINVAL` - The value of the _signo_ argument is an invalid or unsupported signal number.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
