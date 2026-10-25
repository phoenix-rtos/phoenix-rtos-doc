# pthread_spin_lock

## Synopsis

```c
#include <pthread.h>

int pthread_spin_lock(pthread_spinlock_t *lock);

int pthread_spin_trylock(pthread_spinlock_t *lock);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_spin_lock()` function shall lock the spin lock referenced by _lock_. The calling thread shall acquire the
lock if it is not held by another thread. Otherwise, the thread shall spin (that is, shall not return from the
`pthread_spin_lock()` call) until the lock becomes available. The results are undefined if the calling thread holds the
lock at the time the call is made.

In Phoenix-RTOS a thread spinning on a held lock calls `sched_yield()` between the attempts, so that the thread holding
the lock can run on a single-processor target.

The `pthread_spin_trylock()` function shall lock the spin lock referenced by _lock_ if it is not held by any thread.
Otherwise, the function shall fail.

The results are undefined if any of these functions is called with an uninitialized spin lock.

## Return value

Upon successful completion, these functions shall return zero; otherwise, an error number shall be returned to indicate
the error.

## Errors

The `pthread_spin_lock()` function may fail if:

* `EDEADLK` - A deadlock condition was detected.

The `pthread_spin_trylock()` function shall fail if:

* `EBUSY` - A thread currently holds the lock.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
