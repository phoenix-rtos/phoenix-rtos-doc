# pthread_mutex_lock

## Synopsis

```c
#include <pthread.h>

int pthread_mutex_lock(pthread_mutex_t *mutex);

int pthread_mutex_trylock(pthread_mutex_t *mutex);

int pthread_mutex_unlock(pthread_mutex_t *mutex);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The mutex object referenced by _mutex_ shall be locked by a call to `pthread_mutex_lock()` that returns zero or
`EOWNERDEAD`. If the mutex is already locked by another thread, the calling thread shall block until the mutex becomes
available. This operation shall return with the mutex object referenced by _mutex_ in the locked state with the calling
thread as its owner. If a thread attempts to relock a mutex that it has already locked, `pthread_mutex_lock()` shall
behave as described in the Relock column of the following table. If a thread attempts to unlock a mutex that it has not
locked or a mutex which is unlocked, `pthread_mutex_unlock()` shall behave as described in the Unlock When Not Owner
column of the following table.

| Mutex Type   | Robustness | Relock             | Unlock When Not Owner |
|--------------|------------|--------------------|-----------------------|
| `NORMAL`     | non-robust | deadlock           | undefined behavior    |
| `NORMAL`     | robust     | deadlock           | error returned        |
| `ERRORCHECK` | either     | error returned     | error returned        |
| `RECURSIVE`  | either     | recursive          | error returned        |
| `DEFAULT`    | non-robust | undefined behavior | undefined behavior    |
| `DEFAULT`    | robust     | undefined behavior | error returned        |

If the mutex type is `PTHREAD_MUTEX_DEFAULT`, the behavior of `pthread_mutex_lock()` may correspond to one of the three
other standard mutex types as described in the table above. In Phoenix-RTOS `PTHREAD_MUTEX_DEFAULT` is the same type as
`PTHREAD_MUTEX_NORMAL`.

Where the table indicates recursive behavior, the mutex shall maintain the concept of a lock count. When a thread
successfully acquires a mutex for the first time, the lock count shall be set to one. Every time a thread relocks this
mutex, the lock count shall be incremented by one. Each time the thread unlocks the mutex, the lock count shall be
decremented by one. When the lock count reaches zero, the mutex shall become available for other threads to acquire.

The `pthread_mutex_trylock()` function shall be equivalent to `pthread_mutex_lock()`, except that if the mutex object
referenced by _mutex_ is currently locked (by any thread, including the current thread), the call shall return
immediately. If the mutex type is `PTHREAD_MUTEX_RECURSIVE` and the mutex is currently owned by the calling thread, the
mutex lock count shall be incremented by one and the `pthread_mutex_trylock()` function shall immediately return
success.

The `pthread_mutex_unlock()` function shall release the mutex object referenced by _mutex_. The manner in which a mutex
is released is dependent upon the mutex's type attribute. If there are threads blocked on the mutex object referenced by
_mutex_ when `pthread_mutex_unlock()` is called, resulting in the mutex becoming available, the scheduling policy shall
determine which thread shall acquire the mutex.

(In the case of `PTHREAD_MUTEX_RECURSIVE` mutexes, the mutex shall become available when the count reaches zero and the
calling thread no longer has any locks on this mutex.)

If a signal is delivered to a thread waiting for a mutex, upon return from the signal handler the thread shall resume
waiting for the mutex as if it was not interrupted.

If _mutex_ is a robust mutex and the process containing the owning thread terminated while holding the mutex lock, a
call to `pthread_mutex_lock()` shall return the error value `EOWNERDEAD`. If _mutex_ is a robust mutex and the owning
thread terminated while holding the mutex lock, a call to `pthread_mutex_lock()` may return the error value
`EOWNERDEAD` even if the process in which the owning thread resides has not terminated. In these cases, the mutex is
locked by the thread but the state it protects is marked as inconsistent. The application should ensure that the state
is made consistent for reuse and when that is complete call `pthread_mutex_consistent()`. If the application is unable
to recover the state, it should unlock the mutex without a prior call to `pthread_mutex_consistent()`, after which the
mutex is marked permanently unusable. Phoenix-RTOS marks the state of a robust mutex as inconsistent whenever its owning
thread terminates, so `EOWNERDEAD` is returned also when the process of the owning thread has not terminated.

If _mutex_ does not refer to an initialized mutex object, the behavior of `pthread_mutex_lock()`,
`pthread_mutex_trylock()`, and `pthread_mutex_unlock()` is undefined.

## Return value

If successful, the `pthread_mutex_lock()`, `pthread_mutex_trylock()`, and `pthread_mutex_unlock()` functions shall
return zero; otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_mutex_lock()` and `pthread_mutex_trylock()` functions shall fail if:

* `EAGAIN` - The mutex could not be acquired because the maximum number of recursive locks for _mutex_ has been
exceeded.

* `EINVAL` - The mutex was created with the protocol attribute having the value `PTHREAD_PRIO_PROTECT` and the calling
thread's priority is higher than the mutex's current priority ceiling.

* `ENOTRECOVERABLE` - The state protected by the mutex is not recoverable.

* `EOWNERDEAD` - The mutex is a robust mutex and the process containing the previous owning thread terminated while
holding the mutex lock. The mutex lock shall be acquired by the calling thread, and it is up to the new owner to make
the state consistent.

The `pthread_mutex_lock()` function shall fail if:

* `EDEADLK` - The mutex type is `PTHREAD_MUTEX_ERRORCHECK` and the current thread already owns the mutex.

The `pthread_mutex_trylock()` function shall fail if:

* `EBUSY` - The mutex could not be acquired because it was already locked.

The `pthread_mutex_unlock()` function shall fail if:

* `EPERM` - The mutex type is `PTHREAD_MUTEX_ERRORCHECK` or `PTHREAD_MUTEX_RECURSIVE`, or the mutex is a robust mutex,
and the current thread does not own the mutex.

The `pthread_mutex_lock()` and `pthread_mutex_trylock()` functions may fail if:

* `EOWNERDEAD` - The mutex is a robust mutex and the previous owning thread terminated while holding the mutex lock. The
mutex lock shall be acquired by the calling thread, and it is up to the new owner to make the state consistent.

The `pthread_mutex_lock()` function may fail if:

* `EDEADLK` - A deadlock condition was detected.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
