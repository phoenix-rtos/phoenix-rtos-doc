# clock_getres

## Synopsis

```c
#include <time.h>

int clock_getres(clockid_t clock_id, struct timespec *res);

int clock_gettime(clockid_t clock_id, struct timespec *tp);

int clock_settime(clockid_t clock_id, const struct timespec *tp);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `clock_getres()` function shall return the resolution of any clock. Clock resolutions are implementation-defined
and cannot be set by a process. If the argument _res_ is not `NULL`, the resolution of the specified clock shall be
stored in the location pointed to by _res_. If _res_ is `NULL`, the clock resolution is not returned. If the time
argument of `clock_settime()` is not a multiple of _res_, then the value is truncated to a multiple of _res_.

The `clock_gettime()` function shall return the current value _tp_ for the specified clock, _clock_id_.

The `clock_settime()` function shall set the specified clock, _clock_id_, to the value specified by _tp_. Time values
that are between two consecutive non-negative integer multiples of the resolution of the specified clock shall be
truncated down to the smaller multiple of the resolution.

A clock may be system-wide (that is, visible to all processes) or per-process (measuring time that is meaningful only
within a process). All implementations shall support a _clock_id_ of `CLOCK_REALTIME` as defined in `<time.h>`. This
clock represents the clock measuring real time for the system. For this clock, the values returned by `clock_gettime()`
and specified by `clock_settime()` represent the amount of time (in seconds and nanoseconds) since the Epoch.

The supported clocks are `CLOCK_REALTIME`, `CLOCK_MONOTONIC`, `CLOCK_MONOTONIC_RAW` (which has the same value as
`CLOCK_MONOTONIC`), `CLOCK_PROCESS_CPUTIME_ID`, `CLOCK_THREAD_CPUTIME_ID` and the CPU-time clocks of processes returned
by `clock_getcpuclockid()`. Every clock is derived from the kernel timer, and the resolution of every clock is 1
microsecond.

If the value of the `CLOCK_REALTIME` clock is set via `clock_settime()`, the new value of the clock shall be used to
determine the time of expiration for absolute time services based upon the `CLOCK_REALTIME` clock. If the absolute time
requested at the invocation of such a time service is before the new value of the clock, the time service shall expire
immediately as if the clock had reached the requested time normally.

Setting the value of the `CLOCK_REALTIME` clock via `clock_settime()` shall have no effect on threads that are blocked
waiting for a relative time service based upon this clock, including the `nanosleep()` function. Consequently, these
time services shall expire when the requested relative interval elapses, independently of the new or old value of the
clock.

The `CLOCK_MONOTONIC` clock represents the monotonic clock for the system. For this clock, the value returned by
`clock_gettime()` represents the amount of time (in seconds and nanoseconds) since an unspecified point in the past
(the system start-up time). This point does not change after system start-up time. The value of the `CLOCK_MONOTONIC`
clock cannot be set via `clock_settime()`. This function shall fail if it is invoked with a _clock_id_ argument of
`CLOCK_MONOTONIC`.

If the value of the `CLOCK_REALTIME` clock is set via `clock_settime()`, the new value of the clock shall be used to
determine the time at which the system shall awaken a thread blocked on an absolute `clock_nanosleep()` call based upon
the `CLOCK_REALTIME` clock. If the absolute time requested at the invocation of such a time service is before the new
value of the clock, the call shall return immediately as if the clock had reached the requested time normally.

Setting the value of the `CLOCK_REALTIME` clock via `clock_settime()` shall have no effect on any thread that is
blocked on a relative `clock_nanosleep()` call. Consequently, the call shall return when the requested relative
interval elapses, independently of the new or old value of the clock.

Appropriate privileges to set a particular clock are implementation-defined. Every process may set the
`CLOCK_REALTIME` clock. Only the `CLOCK_REALTIME` clock can be set, `clock_settime()` fails with `EINVAL` for the
other clocks.

Implementations shall support clock ID values obtained by invoking `clock_getcpuclockid()`, which represent the CPU-time
clock of a given process. Implementations shall also support the special `clockid_t` value `CLOCK_PROCESS_CPUTIME_ID`,
which represents the CPU-time clock of the calling process when invoking one of the `clock_*()` functions. For these
clock IDs, the values returned by `clock_gettime()` represent the amount of execution time of the process associated
with the clock.

Implementations shall also support the special `clockid_t` value `CLOCK_THREAD_CPUTIME_ID`, which represents the
CPU-time clock of the calling thread when invoking one of the `clock_*()` functions. For this clock ID, the values
returned by `clock_gettime()` shall represent the amount of execution time of the calling thread.

## Return value

A return value of `0` shall indicate that the call succeeded. A return value of `-1` shall indicate that an error
occurred, and `errno` shall be set to indicate the error.

## Errors

The `clock_getres()`, `clock_gettime()`, and `clock_settime()` functions shall fail if:

* `EINVAL` - The _clock_id_ argument does not specify a known clock.

The `clock_gettime()` function shall fail if:

* `EOVERFLOW` - The number of seconds will not fit in an object of type `time_t`.

The `clock_settime()` function shall fail if:

* `EINVAL` - The _tp_ argument to `clock_settime()` is outside the range for the given clock ID.

* `EINVAL` - The _tp_ argument specified a nanosecond value less than zero or greater than or equal to 1000 million.

* `EINVAL` - The value of the _clock_id_ argument is `CLOCK_MONOTONIC`.

The `clock_settime()` function may fail if:

* `EPERM` - The requesting process does not have appropriate privileges to set the specified clock.

## POSIX deviations

No POSIX deviations discovered.
