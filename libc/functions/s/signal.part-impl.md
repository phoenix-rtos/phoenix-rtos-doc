# Synopsis 
`#include <signal.h>`</br>
` void (*signal(int sig, void (*func)(int)))(int);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `signal()` function chooses one of three ways in which receipt of the signal number _sig_ is to be subsequently
handled. If the value of func is `SIG_DFL,` default handling for that signal shall occur. If the value of func is
`SIG_IGN,` the signal shall be ignored. Otherwise, the application shall ensure that _func_ points to a function to be called
when that signal occurs. An invocation of such a function because of a signal, or (recursively) of any further functions called by
that invocation (other than functions in the standard library), is called a "signal handler".
When a signal occurs, and _func_ points to a function, it is implementation-defined whether the equivalent of a:

    `signal(sig, `SIG_DFL);`


is executed or the implementation prevents some implementation-defined set of signals (at least including _sig_) from
occurring until the current signal handling has completed. (If the value of _sig_ is `SIGILL`, the implementation may
alternatively define that no action is taken.) Next the equivalent of:

    `(*func)(sig);`


is executed. If and when the function returns, if the value of sig was `SIGFPE`, `SIGILL`, or `SIGSEGV` or any other
implementation-defined value corresponding to a computational exception, the behavior is undefined. Otherwise, the program shall
resume execution at the point it was interrupted. The ISO C standard places a restriction on applications relating to the use
of `raise()` from signal handlers.    This
restriction does not apply to POSIX applications, as POSIX.1-2017 requires `raise()` to
be async-signal-safe (see Signal Actions). 
  If
the process is multi-threaded,   or if the process is
single-threaded and a signal handler is executed other than as the result of:



* The process calling `abort()`, `raise()`, `kill()`, ``pthread_kill()`,` or `sigqueue()`   to generate a signal that is not blocked


*   A pending signal being unblocked and being delivered before the call that unblocked it returns 




the behavior is undefined if the signal handler refers to any object 
other than `errno`   with static storage duration other than by assigning a value to an object declared as
volatile `sig_atomic_t,` or if the signal handler calls any function defined in this standard other than    one of the
functions listed in Signal Concepts. 
At program start-up, the equivalent of:

    `signal(sig, SIG_IGN);`


is executed for some signals, and the equivalent of:

    `signal(sig, SIG_DFL);`


is executed for all other signals (see `exec()`). 
The `signal()` function shall not change the setting of `errno` if successful.


## Return value


If the request can be honored, `signal()` shall return the value of _func_ for the most recent call to `signal()`
for the specified signal sig. Otherwise, `SIG_ERR` shall be returned and a positive value shall be stored in `errno`.


## Errors


The `signal()` function shall fail if:


 * `EINVAL` - 
The _sig_ argument is not a valid signal number or an attempt is made to catch a signal that cannot be caught or ignore a
signal that cannot be ignored. 

The `signal()` function may fail if:


 * `EINVAL` -  An
attempt was made to set the action to `SIG_DFL` for a signal that cannot be caught or ignored (or both). 


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
