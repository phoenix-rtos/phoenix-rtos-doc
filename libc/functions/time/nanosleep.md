# nanosleep

## Synopsis

```c
#include <time.h>

int nanosleep(const struct timespec *rqtp, struct timespec *rmtp);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `nanosleep()` function shall cause the current thread to be suspended from execution until either the time
interval specified by the _rqtp_ argument has elapsed or a signal is delivered to the calling thread, and its action is
to invoke a signal-catching function or to terminate the process. The suspension time may be longer than requested
because the argument value is rounded up to an integer multiple of the sleep resolution or because of the scheduling of
other activity by the system. But, except for the case of being interrupted by a signal, the suspension time shall not
be less than the time specified by _rqtp_, as measured by the system clock `CLOCK_REALTIME`.

The interval is measured by the kernel on the monotonic clock, so setting the `CLOCK_REALTIME` clock has no effect on
a thread blocked in `nanosleep()`.

The use of the `nanosleep()` function has no effect on the action or blockage of any signal.

## Return value

If the `nanosleep()` function returns because the requested time has elapsed, its return value shall be zero.

If the `nanosleep()` function returns because it has been interrupted by a signal, it shall return a value of `-1` and
set `errno` to indicate the interruption. If the _rmtp_ argument is non-`NULL`, the `timespec` structure referenced by
it is updated to contain the amount of time remaining in the interval (the requested time minus the time actually
slept). The _rqtp_ and _rmtp_ arguments can point to the same object. If the _rmtp_ argument is `NULL`, the remaining
time is not returned.

If `nanosleep()` fails, it shall return a value of `-1` and set `errno` to indicate the error.

## Errors

The `nanosleep()` function shall fail if:

* `EINTR` - The `nanosleep()` function was interrupted by a signal.

* `EINVAL` - The _rqtp_ argument specified a nanosecond value less than zero or greater than or equal to 1000 million.

## POSIX deviations

No POSIX deviations discovered.
