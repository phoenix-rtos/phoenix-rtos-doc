# pthread_rwlock_unlock

## Synopsis

```c
#include <pthread.h>

int pthread_rwlock_unlock(pthread_rwlock_t *rwlock);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_rwlock_unlock()` function shall release a lock held on the read-write lock object referenced by _rwlock_.
Results are undefined if the read-write lock _rwlock_ is not held by the calling thread. Phoenix-RTOS does not track the
owners of a read-write lock; if the lock is not held by any thread, the function returns `EPERM`.

If this function is called to release a read lock from the read-write lock object and there are other read locks
currently held on this read-write lock object, the read-write lock object remains in the read locked state. If this
function releases the last read lock for this read-write lock object, the read-write lock object shall be put in the
unlocked state with no owners.

If this function is called to release a write lock for this read-write lock object, the read-write lock object shall be
put in the unlocked state.

If there are threads blocked on the lock when it becomes available, the scheduling policy shall determine which
thread(s) shall acquire the lock. Whether write locks take precedence over read locks is implementation-defined. In
Phoenix-RTOS write locks take precedence: when the lock becomes available and a writer is blocked on it, one writer is
woken; the blocked readers are woken only when no writer is waiting.

Results are undefined if this function is called with an uninitialized read-write lock.

## Return value

If successful, the `pthread_rwlock_unlock()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_rwlock_unlock()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
