# usleep

## Synopsis

`#include <unistd.h>`

`int usleep(useconds_t useconds);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1, 2004

## Description

The `usleep()` function shall cause the calling thread to be suspended from execution until either the number of
real-time microseconds specified by the argument _useconds_ has elapsed or a signal is delivered to the calling
thread and its action is to invoke a signal-catching function or to terminate the process. The suspension time
may be longer than requested due to the scheduling of other activity by the system.

The _useconds_ argument shall be less than one million. If the value of _useconds_ is `0`, then the call has no effect.

If a `SIGALRM` signal is generated for the calling process during execution of `usleep()` and if the `SIGALRM`
signal is being ignored or blocked from delivery, it is unspecified whether `usleep()` returns when the `SIGALRM`
signal is scheduled. If the signal is being blocked, it is also unspecified whether it remains pending after
`usleep()` returns or it is discarded.

If a `SIGALRM` signal is generated for the calling process during execution of `usleep()`, except as a result of a
prior call to `alarm()`, and if the `SIGALRM` signal is not being ignored or blocked from delivery, it is unspecified
whether that signal has any effect other than causing `usleep()` to return.

If a signal-catching function interrupts `usleep()` and examines or changes either the time a `SIGALRM` is scheduled
to be generated, the action associated with the `SIGALRM` signal, or whether the `SIGALRM` signal is blocked from
delivery, the results are unspecified.

If a signal-catching function interrupts `usleep()` and calls `siglongjmp()` or `longjmp()` to restore an environment
saved prior to the `usleep()` call, the action associated with the `SIGALRM` signal and the time at which a `SIGALRM`
signal is scheduled to be generated are unspecified. It is also unspecified whether the `SIGALRM` signal is blocked,
unless the thread's signal mask is restored as part of the environment.

Implementations may place limitations on the granularity of timer values. For each interval timer, if the requested
timer value requires a finer granularity than the implementation supports, the actual timer value shall be rounded up
to the next supported value.

Interactions between `usleep()` and any of the following are unspecified:

* `nanosleep()`
* `setitimer()`
* `timer_create()`
* `timer_delete()`
* `timer_getoverrun()`
* `timer_gettime()`
* `timer_settime()`
* `ualarm()`
* `sleep()`

The `usleep()` function need not be reentrant. A function that is not required to be reentrant is not required to be
thread-safe.

## Return value

Upon successful completion, `usleep()` shall return `0`; otherwise, it shall return `-1` and set `errno` to indicate
the error.

## Errors

The `usleep()` function may fail if:

* `EINVAL` - The time interval specified one million or more microseconds.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
