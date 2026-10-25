# pthread_mutexattr_gettype

## Synopsis

```c
#include <pthread.h>

int pthread_mutexattr_gettype(const pthread_mutexattr_t *restrict attr,
                              int *restrict type);

int pthread_mutexattr_settype(pthread_mutexattr_t *attr, int type);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutexattr_gettype()` and `pthread_mutexattr_settype()` functions, respectively, shall get and set the
mutex _type_ attribute. This attribute is set in the _type_ parameter to these functions. The default value of the
_type_ attribute is `PTHREAD_MUTEX_DEFAULT`.

The type of mutex is contained in the _type_ attribute of the mutex attributes. Valid mutex types include:

* `PTHREAD_MUTEX_NORMAL`

* `PTHREAD_MUTEX_ERRORCHECK`

* `PTHREAD_MUTEX_RECURSIVE`

* `PTHREAD_MUTEX_DEFAULT`

The mutex type affects the behavior of calls which lock and unlock the mutex. See `pthread_mutex_lock()` for details.
An implementation may map `PTHREAD_MUTEX_DEFAULT` to one of the other mutex types. In Phoenix-RTOS
`PTHREAD_MUTEX_DEFAULT` is mapped to `PTHREAD_MUTEX_NORMAL`, so `pthread_mutexattr_gettype()` reports
`PTHREAD_MUTEX_NORMAL` for the default attribute.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_mutexattr_gettype()` or
`pthread_mutexattr_settype()` does not refer to an initialized mutex attributes object.

## Return value

Upon successful completion, the `pthread_mutexattr_gettype()` function shall return zero and store the value of the
_type_ attribute of _attr_ into the object referenced by the _type_ parameter. Otherwise, an error shall be returned to
indicate the error.

If successful, the `pthread_mutexattr_settype()` function shall return zero; otherwise, an error number shall be
returned to indicate the error.

## Errors

The `pthread_mutexattr_settype()` function shall fail if:

* `EINVAL` - The value _type_ is invalid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
