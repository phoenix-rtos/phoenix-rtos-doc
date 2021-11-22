# Synopsis 
`#include <unistd.h>`</br>

` unsigned sleep(unsigned seconds);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `sleep()` function shall cause the calling thread to be suspended from execution until either the number of realtime
seconds specified by the argument _seconds_ has elapsed or a signal is delivered to the calling thread and its action is to
invoke a signal-catching function or to terminate the process. The suspension time may be longer than requested due to the
scheduling of other activity by the system.
In single-threaded programs, `sleep()` may make use of `SIGALRM`. In multi-threaded programs, `sleep()` shall not make
use of `SIGALRM` and the remainder of this  does not apply.
If a `SIGALRM` signal is generated for the calling process during execution of `sleep()` and if the `SIGALRM` signal is being
ignored or blocked from delivery, it is unspecified whether `sleep()` returns when the `SIGALRM` signal is scheduled. If the
signal is being blocked, it is also unspecified whether it remains pending after `sleep()` returns or it is discarded.
If a `SIGALRM` signal is generated for the calling process during execution of `sleep()`, except as a result of a prior call
to `alarm()`, and if the `SIGALRM` signal is not being ignored or blocked from delivery,
it is unspecified whether that signal has any effect other than causing `sleep()` to return.
If a signal-catching function interrupts `sleep()` and examines or changes either the time a `SIGALRM` is scheduled to be
generated, the action associated with the `SIGALRM` signal, or whether the `SIGALRM` signal is blocked from delivery, the results are
unspecified.
If a signal-catching function interrupts `sleep()` and calls `siglongjmp()`
or `longjmp()` to restore an environment saved prior to the `sleep()` call, the
action associated with the `SIGALRM` signal and the time at which a SIGALRM signal is scheduled to be generated are unspecified. It
is also unspecified whether the `SIGALRM` signal is blocked, unless the signal mask of the process is restored as part of the
environment.

Interactions between `sleep()` and `setitimer()` are unspecified. 


## Return value


If `sleep()` returns because the requested time has elapsed, the value returned shall be `0`. If `sleep()` returns due
to delivery of a signal, the return value shall be the "unslept" amount (the requested time minus the time actually slept) in
seconds.


## Errors


No errors are defined.



## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
