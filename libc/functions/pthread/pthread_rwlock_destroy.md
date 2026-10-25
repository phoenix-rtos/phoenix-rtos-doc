# pthread_rwlock_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_rwlock_destroy(pthread_rwlock_t *rwlock);

int pthread_rwlock_init(pthread_rwlock_t *restrict rwlock,
                        const pthread_rwlockattr_t *restrict attr);

pthread_rwlock_t rwlock = PTHREAD_RWLOCK_INITIALIZER;
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_rwlock_destroy()` function shall destroy the read-write lock object referenced by _rwlock_ and release any
resources used by the lock. The effect of subsequent use of the lock is undefined until the lock is reinitialized by
another call to `pthread_rwlock_init()`. Results are undefined if `pthread_rwlock_destroy()` is called when any thread
holds _rwlock_. Attempting to destroy an uninitialized read-write lock results in undefined behavior.

The `pthread_rwlock_init()` function shall allocate any resources required to use the read-write lock referenced by
_rwlock_ and initialize the lock to an unlocked state with attributes referenced by _attr_. If _attr_ is `NULL`, the
default read-write lock attributes shall be used; the effect is the same as passing the address of a default read-write
lock attributes object. Once initialized, the lock can be used any number of times without being reinitialized. Results
are undefined if `pthread_rwlock_init()` is called specifying an already initialized read-write lock. Results are
undefined if a read-write lock is used without first being initialized.

If the `pthread_rwlock_init()` function fails, _rwlock_ shall not be initialized and the contents of _rwlock_ are
undefined.

In cases where default read-write lock attributes are appropriate, the macro `PTHREAD_RWLOCK_INITIALIZER` can be used to
initialize read-write locks. The effect shall be equivalent to dynamic initialization by a call to
`pthread_rwlock_init()` with the _attr_ parameter specified as `NULL`, except that no error checks are performed.

In Phoenix-RTOS a read-write lock is built on a kernel mutex and two kernel condition variables. A lock initialized with
`PTHREAD_RWLOCK_INITIALIZER` allocates them on its first use.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_rwlock_init()` does not refer to an
initialized read-write lock attributes object.

## Return value

If successful, the `pthread_rwlock_destroy()` and `pthread_rwlock_init()` functions shall return zero; otherwise, an
error number shall be returned to indicate the error.

## Errors

The `pthread_rwlock_init()` function shall fail if:

* `EAGAIN` - The system lacked the necessary resources (other than memory) to initialize another read-write lock.

* `ENOMEM` - Insufficient memory exists to initialize the read-write lock.

* `EPERM` - The caller does not have the privilege to perform the operation.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
