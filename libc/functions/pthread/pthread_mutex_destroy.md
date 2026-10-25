# pthread_mutex_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_mutex_destroy(pthread_mutex_t *mutex);

int pthread_mutex_init(pthread_mutex_t *restrict mutex,
                       const pthread_mutexattr_t *restrict attr);

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutex_destroy()` function shall destroy the mutex object referenced by _mutex_; the mutex object becomes,
in effect, uninitialized. An implementation may cause `pthread_mutex_destroy()` to set the object referenced by _mutex_
to an invalid value.

A destroyed mutex object can be reinitialized using `pthread_mutex_init()`; the results of otherwise referencing the
object after it has been destroyed are undefined.

It shall be safe to destroy an initialized mutex that is unlocked. Attempting to destroy a locked mutex, or a mutex that
another thread is attempting to lock, or a mutex that is being used in a `pthread_cond_timedwait()` or
`pthread_cond_wait()` call by another thread, results in undefined behavior.

The `pthread_mutex_init()` function shall initialize the mutex referenced by _mutex_ with attributes specified by
_attr_. If _attr_ is `NULL`, the default mutex attributes are used; the effect shall be the same as passing the address
of a default mutex attributes object. Upon successful initialization, the state of the mutex becomes initialized and
unlocked.

Attempting to initialize an already initialized mutex results in undefined behavior.

In cases where default mutex attributes are appropriate, the macro `PTHREAD_MUTEX_INITIALIZER` can be used to initialize
mutexes. The effect shall be equivalent to dynamic initialization by a call to `pthread_mutex_init()` with parameter
_attr_ specified as `NULL`, except that no error checks are performed.

The behavior is undefined if the value specified by the _mutex_ argument to `pthread_mutex_destroy()` does not refer to
an initialized mutex.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_mutex_init()` does not refer to an
initialized mutex attributes object.

## Return value

If successful, the `pthread_mutex_destroy()` and `pthread_mutex_init()` functions shall return zero; otherwise, an error
number shall be returned to indicate the error.

## Errors

The `pthread_mutex_init()` function shall fail if:

* `EAGAIN` - The system lacked the necessary resources (other than memory) to initialize another mutex.

* `ENOMEM` - Insufficient memory exists to initialize the mutex.

* `EPERM` - The caller does not have the privilege to perform the operation.

The `pthread_mutex_init()` function may fail if:

* `EINVAL` - The attributes object referenced by _attr_ has the robust mutex attribute set without the process-shared
attribute being set.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

IEEE Std 1003.1-2017 requires the default value of the _protocol_ attribute of a mutex to be `PTHREAD_PRIO_NONE`. In
Phoenix-RTOS the default protocol is `PTHREAD_PRIO_INHERIT`, so a mutex initialized by `pthread_mutex_init()` with
_attr_ set to `NULL`, or by `PTHREAD_MUTEX_INITIALIZER`, uses priority inheritance. Kernel mutexes inherit priority by
default to prevent unbounded priority inversion, which is the safer behavior in real-time systems. To get a mutex with
the `PTHREAD_PRIO_NONE` protocol, set it explicitly with `pthread_mutexattr_setprotocol()`.
