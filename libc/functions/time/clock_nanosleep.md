# clock_nanosleep

## Synopsis

```c
#include <time.h>

int clock_nanosleep(clockid_t clock_id, int flags,
                    const struct timespec *rqtp, struct timespec *rmtp);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If the flag `TIMER_ABSTIME` is not set in the _flags_ argument, the `clock_nanosleep()` function shall cause the
current thread to be suspended from execution until either the time interval specified by the _rqtp_ argument has
elapsed, or a signal is delivered to the calling thread and its action is to invoke a signal-catching function, or the
process is terminated. The clock used to measure the time shall be the clock specified by _clock_id_.

If the flag `TIMER_ABSTIME` is set in the _flags_ argument, the `clock_nanosleep()` function shall cause the current
thread to be suspended from execution until either the time value of the clock specified by _clock_id_ reaches the
absolute time specified by the _rqtp_ argument, or a signal is delivered to the calling thread and its action is to
invoke a signal-catching function, or the process is terminated. If, at the time of the call, the time value specified
by _rqtp_ is less than or equal to the time value of the specified clock, then `clock_nanosleep()` shall return
immediately, and the calling process shall not be suspended.

The suspension time caused by this function may be longer than requested because the argument value is rounded up to
an integer multiple of the sleep resolution, or because of the scheduling of other activity by the system. But, except
for the case of being interrupted by a signal, the suspension time for the relative `clock_nanosleep()` function (that
is, with the `TIMER_ABSTIME` flag not set) shall not be less than the time interval specified by _rqtp_, as measured by
the corresponding clock. The suspension for the absolute `clock_nanosleep()` function (that is, with the
`TIMER_ABSTIME` flag set) shall be in effect at least until the value of the corresponding clock reaches the absolute
time specified by _rqtp_, except for the case of being interrupted by a signal.

The use of the `clock_nanosleep()` function shall have no effect on the action or blockage of any signal.

The `clock_nanosleep()` function shall fail if the _clock_id_ argument refers to the CPU-time clock of the calling
thread. It is unspecified whether _clock_id_ values of other CPU-time clocks are allowed.

The supported clocks are `CLOCK_REALTIME`, `CLOCK_MONOTONIC` and `CLOCK_MONOTONIC_RAW`. For every CPU-time clock
(`CLOCK_PROCESS_CPUTIME_ID`, `CLOCK_THREAD_CPUTIME_ID` and the clocks returned by `clock_getcpuclockid()`)
`clock_nanosleep()` fails with `ENOTSUP`.

## Return value

If the `clock_nanosleep()` function returns because the requested time has elapsed, its return value shall be zero.

If the `clock_nanosleep()` function returns because it has been interrupted by a signal, it shall return the
corresponding error value. For the relative `clock_nanosleep()` function, if the _rmtp_ argument is non-`NULL`, the
`timespec` structure referenced by it shall be updated to contain the amount of time remaining in the interval (the
requested time minus the time actually slept). The _rqtp_ and _rmtp_ arguments can point to the same object. If the
_rmtp_ argument is `NULL`, the remaining time is not returned. The absolute `clock_nanosleep()` function has no effect
on the structure referenced by _rmtp_.

If `clock_nanosleep()` fails, it shall return the corresponding error value.

## Errors

The `clock_nanosleep()` function shall fail if:

* `EINTR` - The `clock_nanosleep()` function was interrupted by a signal.

* `EINVAL` - The _rqtp_ argument specified a nanosecond value less than zero or greater than or equal to 1000 million;
or the `TIMER_ABSTIME` flag was specified in _flags_ and the _rqtp_ argument is outside the range for the clock
specified by _clock_id_; or the _clock_id_ argument does not specify a known clock, or specifies the CPU-time clock of
the calling thread.

* `ENOTSUP` - The _clock_id_ argument specifies a clock for which `clock_nanosleep()` is not supported, such as a
CPU-time clock.

## POSIX deviations

No POSIX deviations discovered.
