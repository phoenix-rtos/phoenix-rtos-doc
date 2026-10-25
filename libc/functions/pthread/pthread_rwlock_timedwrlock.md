# pthread_rwlock_timedwrlock

## Synopsis

```c
#include <pthread.h>
#include <time.h>

int pthread_rwlock_timedwrlock(pthread_rwlock_t *restrict rwlock,
                               const struct timespec *restrict abstime);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_rwlock_timedwrlock()` function shall apply a write lock to the read-write lock referenced by _rwlock_ as in
the `pthread_rwlock_wrlock()` function. However, if the lock cannot be acquired without waiting for other threads to
unlock the lock, this wait shall be terminated when the specified timeout expires. The timeout shall expire when the
absolute time specified by _abstime_ passes, as measured by the clock on which timeouts are based (that is, when the
value of that clock equals or exceeds _abstime_), or if the absolute time specified by _abstime_ has already been passed
at the time of the call.

The timeout shall be based on the `CLOCK_REALTIME` clock. The resolution of the timeout shall be the resolution of the
`CLOCK_REALTIME` clock. Under no circumstances shall the function fail with a timeout if the lock can be acquired
immediately. The validity of the _abstime_ parameter need not be checked if the lock can be immediately acquired. In
Phoenix-RTOS _abstime_ is checked only when the lock cannot be acquired immediately.

`pthread_rwlock_clockwrlock()` is the same function with a selectable clock.

If a signal that causes a signal handler to be executed is delivered to a thread blocked on a read-write lock via a call
to `pthread_rwlock_timedwrlock()`, upon return from the signal handler the thread shall resume waiting for the lock as
if it was not interrupted.

The calling thread may deadlock if at the time the call is made it holds the read-write lock. The results are undefined
if this function is called with an uninitialized read-write lock.

## Return value

The `pthread_rwlock_timedwrlock()` function shall return zero if the lock for writing on the read-write lock object
referenced by _rwlock_ is acquired. Otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_rwlock_timedwrlock()` function shall fail if:

* `ETIMEDOUT` - The lock could not be acquired before the specified timeout expired.

The `pthread_rwlock_timedwrlock()` function may fail if:

* `EDEADLK` - A deadlock condition was detected, or the calling thread already holds the _rwlock_.

* `EINVAL` - The _abstime_ nanosecond value is less than zero or greater than or equal to 1000 million.

This function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
