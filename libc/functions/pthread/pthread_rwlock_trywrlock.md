# pthread_rwlock_trywrlock

## Synopsis

```c
#include <pthread.h>

int pthread_rwlock_trywrlock(pthread_rwlock_t *rwlock);

int pthread_rwlock_wrlock(pthread_rwlock_t *rwlock);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_rwlock_trywrlock()` function shall apply a write lock like the `pthread_rwlock_wrlock()` function, with the
exception that the function shall fail if any thread currently holds _rwlock_ (for reading or writing).

The `pthread_rwlock_wrlock()` function shall apply a write lock to the read-write lock referenced by _rwlock_. The
calling thread shall acquire the write lock if no thread (reader or writer) holds the read-write lock _rwlock_.
Otherwise, if another thread holds the read-write lock _rwlock_, the calling thread shall block until it can acquire the
lock. If a deadlock condition occurs or the calling thread already owns the read-write lock for writing or reading, the
call shall either deadlock or return `EDEADLK`. Phoenix-RTOS does not track the owners of a read-write lock, so in this
case the call deadlocks.

While a thread is blocked in `pthread_rwlock_wrlock()`, new read locks are not granted (see `pthread_rwlock_rdlock()`),
so that the writer is not starved by readers.

Results are undefined if any of these functions are called with an uninitialized read-write lock.

If a signal is delivered to a thread waiting for a read-write lock for writing, upon return from the signal handler the
thread resumes waiting for the read-write lock for writing as if it was not interrupted.

## Return value

The `pthread_rwlock_trywrlock()` function shall return zero if the lock for writing on the read-write lock object
referenced by _rwlock_ is acquired. Otherwise, an error number shall be returned to indicate the error.

If successful, the `pthread_rwlock_wrlock()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_rwlock_trywrlock()` function shall fail if:

* `EBUSY` - The read-write lock could not be acquired for writing because it was already locked for reading or writing.

The `pthread_rwlock_wrlock()` function may fail if:

* `EDEADLK` - A deadlock condition was detected, or the current thread already owns the read-write lock for writing or
  reading.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
