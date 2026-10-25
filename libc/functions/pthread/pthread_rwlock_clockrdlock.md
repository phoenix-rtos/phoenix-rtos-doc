# pthread_rwlock_clockrdlock

## Synopsis

```c
#include <pthread.h>

int pthread_rwlock_clockrdlock(pthread_rwlock_t *restrict rwlock,
                               clockid_t clock_id, const struct timespec *restrict abstime);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

The `pthread_rwlock_clockrdlock()` function shall apply a read lock to the read-write lock referenced by _rwlock_ as in
the `pthread_rwlock_rdlock()` function. However, if the lock cannot be acquired without waiting for other threads to
unlock the lock, this wait shall be terminated when the specified timeout expires. The timeout shall expire when the
absolute time specified by _abstime_ passes, as measured by the clock on which timeouts are based (that is, when the
value of that clock equals or exceeds _abstime_), or if the absolute time specified by _abstime_ has already been passed
at the time of the call.

The timeout shall be based on the clock specified by the _clock_id_ argument. The resolution of the timeout shall be the
resolution of the clock on which it is based. Implementations shall support passing `CLOCK_REALTIME` and
`CLOCK_MONOTONIC` to `pthread_rwlock_clockrdlock()` as the _clock_id_ argument (`CLOCK_MONOTONIC_RAW` is also accepted,
as an alias of `CLOCK_MONOTONIC`).

Under no circumstances shall the function fail with a timeout if the lock can be acquired immediately. The validity of
the _abstime_ parameter need not be checked if the lock can be immediately acquired.

If a signal that causes a signal handler to be executed is delivered to a thread blocked on a read-write lock via a call
to `pthread_rwlock_clockrdlock()`, upon return from the signal handler the thread shall resume waiting for the lock as
if it was not interrupted.

The calling thread may deadlock if at the time the call is made it holds a write lock on _rwlock_. The results are
undefined if this function is called with an uninitialized read-write lock.

## Return value

The `pthread_rwlock_clockrdlock()` function shall return zero if the lock for reading on the read-write lock object
referenced by _rwlock_ is acquired. Otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_rwlock_clockrdlock()` function shall fail if:

* `ETIMEDOUT` - The lock could not be acquired before the specified timeout expired.

The `pthread_rwlock_clockrdlock()` function may fail if:

* `EAGAIN` - The read lock could not be acquired because the maximum number of read locks for _rwlock_ would be
exceeded.

* `EDEADLK` - A deadlock condition was detected, or the calling thread already holds a write lock on _rwlock_.

* `EINVAL` - The _abstime_ nanosecond value is less than zero or greater than or equal to 1000 million, or the function
was passed an invalid or unsupported _clock_id_ value.

This function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
