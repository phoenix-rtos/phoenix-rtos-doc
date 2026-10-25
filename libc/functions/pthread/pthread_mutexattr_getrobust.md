# pthread_mutexattr_getrobust

## Synopsis

```c
#include <pthread.h>

int pthread_mutexattr_getrobust(const pthread_mutexattr_t *restrict attr,
                                int *restrict robust);

int pthread_mutexattr_setrobust(pthread_mutexattr_t *attr, int robust);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutexattr_getrobust()` and `pthread_mutexattr_setrobust()` functions, respectively, shall get and set the
mutex robust attribute. This attribute is set in the _robust_ parameter. Valid values for _robust_ include:

* `PTHREAD_MUTEX_STALLED` - No special actions are taken if the owner of the mutex is terminated while holding the mutex
lock. This can lead to deadlocks if no other thread can unlock the mutex. This is the default value.

* `PTHREAD_MUTEX_ROBUST` - If the process containing the owning thread of a robust mutex terminates while holding the
mutex lock, the next thread that acquires the mutex shall be notified about the termination by the return value
`EOWNERDEAD` from the locking function. If the owning thread of a robust mutex terminates while holding the mutex lock,
the next thread that attempts to acquire the mutex may be notified about the termination by the return value
`EOWNERDEAD`. The notified thread can then attempt to make the state protected by the mutex consistent again, and if
successful can mark the mutex state as consistent by calling `pthread_mutex_consistent()`. After a subsequent successful
call to `pthread_mutex_unlock()`, the mutex lock shall be released and can be used normally by other threads. If the
mutex is unlocked without a call to `pthread_mutex_consistent()`, it shall be in a permanently unusable state and all
attempts to lock the mutex shall fail with the error `ENOTRECOVERABLE`. The only permissible operation on such a mutex
is `pthread_mutex_destroy()`.

Phoenix-RTOS notifies the next owner with `EOWNERDEAD` whenever the owning thread of a robust mutex terminates while
holding the mutex lock, also when its process has not terminated.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_mutexattr_getrobust()` or
`pthread_mutexattr_setrobust()` does not refer to an initialized mutex attributes object.

## Return value

Upon successful completion, the `pthread_mutexattr_getrobust()` function shall return zero and store the value of the
robust attribute of _attr_ into the object referenced by the _robust_ parameter. Otherwise, an error value shall be
returned to indicate the error. If successful, the `pthread_mutexattr_setrobust()` function shall return zero;
otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_mutexattr_setrobust()` function shall fail if:

* `EINVAL` - The value of _robust_ is invalid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
