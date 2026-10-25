# pthread_rwlockattr_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_rwlockattr_destroy(pthread_rwlockattr_t *attr);

int pthread_rwlockattr_init(pthread_rwlockattr_t *attr);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_rwlockattr_destroy()` function shall destroy a read-write lock attributes object. A destroyed _attr_
attributes object can be reinitialized using `pthread_rwlockattr_init()`; the results of otherwise referencing the
object after it has been destroyed are undefined.

The `pthread_rwlockattr_init()` function shall initialize a read-write lock attributes object _attr_ with the default
value for all the attributes defined by the implementation. The only attribute supported by Phoenix-RTOS is the
process-shared attribute, with the default value `PTHREAD_PROCESS_PRIVATE` (see `pthread_rwlockattr_getpshared()`).

Results are undefined if `pthread_rwlockattr_init()` is called specifying an already initialized _attr_ attributes
object.

After a read-write lock attributes object has been used to initialize one or more read-write locks, any function
affecting the attributes object (including destruction) shall not affect any previously initialized read-write locks.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_rwlockattr_destroy()` does not refer
to an initialized read-write lock attributes object.

## Return value

If successful, the `pthread_rwlockattr_destroy()` and `pthread_rwlockattr_init()` functions shall return zero;
otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_rwlockattr_init()` function shall fail if:

* `ENOMEM` - Insufficient memory exists to initialize the read-write lock attributes object.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
