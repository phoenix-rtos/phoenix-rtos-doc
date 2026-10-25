# pthread_mutex_timedlock

## Synopsis

```c
#include <pthread.h>
#include <time.h>

int pthread_mutex_timedlock(pthread_mutex_t *restrict mutex,
                            const struct timespec *restrict abstime);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutex_timedlock()` function shall lock the mutex object referenced by _mutex_. If the mutex is already
locked, the calling thread shall block until the mutex becomes available as in the `pthread_mutex_lock()` function. If
the mutex cannot be locked without waiting for another thread to unlock the mutex, this wait shall be terminated when
the specified timeout expires.

The timeout shall expire when the absolute time specified by _abstime_ passes, as measured by the clock on which
timeouts are based (that is, when the value of that clock equals or exceeds _abstime_), or if the absolute time
specified by _abstime_ has already been passed at the time of the call.

The timeout shall be based on the `CLOCK_REALTIME` clock. The resolution of the timeout shall be the resolution of the
clock on which it is based. The `timespec` data type is defined in the `<time.h>` header.

Under no circumstance shall the function fail with a timeout if the mutex can be locked immediately. The validity of the
_abstime_ parameter need not be checked if the mutex can be locked immediately.

As a consequence of the priority inheritance rules (for mutexes initialized with the `PTHREAD_PRIO_INHERIT` protocol),
if a timed mutex wait is terminated because its timeout expires, the priority of the owner of the mutex shall be
adjusted as necessary to reflect the fact that this thread is no longer among the threads waiting for the mutex.

If _mutex_ is a robust mutex and the process containing the owning thread terminated while holding the mutex lock, a
call to `pthread_mutex_timedlock()` shall return the error value `EOWNERDEAD`. If _mutex_ is a robust mutex and the
owning thread terminated while holding the mutex lock, a call to `pthread_mutex_timedlock()` may return the error value
`EOWNERDEAD` even if the process in which the owning thread resides has not terminated. In these cases, the mutex is
locked by the thread but the state it protects is marked as inconsistent. The application should ensure that the state
is made consistent for reuse and when that is complete call `pthread_mutex_consistent()`. If the application is unable
to recover the state, it should unlock the mutex without a prior call to `pthread_mutex_consistent()`, after which the
mutex is marked permanently unusable.

If _mutex_ does not refer to an initialized mutex object, the behavior is undefined.

## Return value

If successful, the `pthread_mutex_timedlock()` function shall return zero; otherwise, an error number shall be returned
to indicate the error.

## Errors

The `pthread_mutex_timedlock()` function shall fail if:

* `EAGAIN` - The mutex could not be acquired because the maximum number of recursive locks for _mutex_ has been
exceeded.

* `EDEADLK` - The mutex type is `PTHREAD_MUTEX_ERRORCHECK` and the current thread already owns the mutex.

* `EINVAL` - The mutex was created with the protocol attribute having the value `PTHREAD_PRIO_PROTECT` and the calling
thread's priority is higher than the mutex' current priority ceiling.

* `EINVAL` - The process or thread would have blocked, and the _abstime_ parameter specified a nanoseconds field value
less than zero or greater than or equal to 1000 million.

* `ENOTRECOVERABLE` - The state protected by the mutex is not recoverable.

* `EOWNERDEAD` - The mutex is a robust mutex and the process containing the previous owning thread terminated while
holding the mutex lock. The mutex lock shall be acquired by the calling thread, and it is up to the new owner to make
the state consistent.

* `ETIMEDOUT` - The mutex could not be locked before the specified timeout expired.

The `pthread_mutex_timedlock()` function may fail if:

* `EDEADLK` - A deadlock condition was detected.

* `EOWNERDEAD` - The mutex is a robust mutex and the previous owning thread terminated while holding the mutex lock. The
mutex lock shall be acquired by the calling thread, and it is up to the new owner to make the state consistent.

This function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
