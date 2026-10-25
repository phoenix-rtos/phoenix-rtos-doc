# pthread_rwlock_rdlock

## Synopsis

```c
#include <pthread.h>

int pthread_rwlock_rdlock(pthread_rwlock_t *rwlock);

int pthread_rwlock_tryrdlock(pthread_rwlock_t *rwlock);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_rwlock_rdlock()` function shall apply a read lock to the read-write lock referenced by _rwlock_. The
calling thread acquires the read lock if a writer does not hold the lock and there are no writers blocked on the lock.

If a writer holds the lock, the calling thread shall not acquire the read lock. Whether the calling thread acquires the
lock when a writer does not hold the lock and there are writers blocked on the lock is implementation-defined. In
Phoenix-RTOS the calling thread does not acquire the read lock while any writer is blocked on the lock, regardless of
the priorities of the threads, so that waiting writers are not starved by a continuous stream of readers. If the read
lock is not acquired, the calling thread shall block until it can acquire the lock. The calling thread may deadlock if
at the time the call is made it holds a write lock.

A thread may hold multiple concurrent read locks on _rwlock_ (that is, successfully call the `pthread_rwlock_rdlock()`
function _n_ times). If so, the application shall ensure that the thread performs matching unlocks (that is, it calls
the `pthread_rwlock_unlock()` function _n_ times).

The maximum number of simultaneous read locks that an implementation guarantees can be applied to a read-write lock
shall be implementation-defined. In Phoenix-RTOS the number of read locks is limited only by the range of `size_t`.

The `pthread_rwlock_tryrdlock()` function shall apply a read lock as in the `pthread_rwlock_rdlock()` function, with the
exception that the function shall fail if the equivalent `pthread_rwlock_rdlock()` call would have blocked the calling
thread. In no case shall the `pthread_rwlock_tryrdlock()` function ever block; it always either acquires the lock or
fails and returns immediately.

Results are undefined if any of these functions are called with an uninitialized read-write lock.

If a signal is delivered to a thread waiting for a read-write lock for reading, upon return from the signal handler the
thread resumes waiting for the read-write lock for reading as if it was not interrupted.

## Return value

If successful, the `pthread_rwlock_rdlock()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

The `pthread_rwlock_tryrdlock()` function shall return zero if the lock for reading on the read-write lock object
referenced by _rwlock_ is acquired. Otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_rwlock_tryrdlock()` function shall fail if:

* `EBUSY` - The read-write lock could not be acquired for reading because a writer holds the lock or a writer with the
  appropriate priority was blocked on it.

The `pthread_rwlock_rdlock()` and `pthread_rwlock_tryrdlock()` functions may fail if:

* `EAGAIN` - The read lock could not be acquired because the maximum number of read locks for _rwlock_ has been
  exceeded.

The `pthread_rwlock_rdlock()` function may fail if:

* `EDEADLK` - A deadlock condition was detected, or the current thread already owns the read-write lock for writing.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
