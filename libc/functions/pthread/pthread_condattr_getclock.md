# pthread_condattr_getclock

## Synopsis

```c
#include <pthread.h>

int pthread_condattr_getclock(const pthread_condattr_t *restrict attr,
                              clockid_t *restrict clock_id);

int pthread_condattr_setclock(pthread_condattr_t *attr, clockid_t clock_id);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_condattr_getclock()` function shall obtain the value of the clock attribute from the attributes object
referenced by _attr_.

The `pthread_condattr_setclock()` function shall set the clock attribute in an initialized attributes object referenced
by _attr_. If `pthread_condattr_setclock()` is called with a _clock_id_ argument that refers to a CPU-time clock, the
call shall fail.

The clock attribute is the clock ID of the clock that shall be used to measure the timeout service of
`pthread_cond_timedwait()`. The default value of the clock attribute shall refer to the system clock, which is
`CLOCK_REALTIME`.

The supported values of _clock_id_ are `CLOCK_REALTIME` and `CLOCK_MONOTONIC`. `CLOCK_MONOTONIC_RAW` is also accepted,
and is handled as an alias of `CLOCK_MONOTONIC`. For any other value, including CPU-time clocks,
`pthread_condattr_setclock()` fails with `EINVAL`.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_condattr_getclock()` or
`pthread_condattr_setclock()` does not refer to an initialized condition variable attributes object.

## Return value

If successful, the `pthread_condattr_getclock()` function shall return zero and store the value of the clock attribute
of _attr_ into the object referenced by the _clock_id_ argument. Otherwise, an error number shall be returned to
indicate the error.

If successful, the `pthread_condattr_setclock()` function shall return zero; otherwise, an error number shall be
returned to indicate the error.

## Errors

The `pthread_condattr_setclock()` function may fail if:

* `EINVAL` - The value specified by _clock_id_ does not refer to a known clock, or is a CPU-time clock.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
