# pthread_mutexattr_getpshared

## Synopsis

```c
#include <pthread.h>

int pthread_mutexattr_getpshared(const pthread_mutexattr_t *restrict attr,
                                 int *restrict pshared);

int pthread_mutexattr_setpshared(pthread_mutexattr_t *attr, int pshared);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutexattr_getpshared()` function shall obtain the value of the process-shared attribute from the
attributes object referenced by _attr_.

The `pthread_mutexattr_setpshared()` function shall set the process-shared attribute in an initialized attributes
object referenced by _attr_.

The process-shared attribute is set to `PTHREAD_PROCESS_SHARED` to permit a mutex to be operated upon by any thread that
has access to the memory where the mutex is allocated, even if the mutex is allocated in memory that is shared by
multiple processes. The default value of the attribute shall be `PTHREAD_PROCESS_PRIVATE`.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_mutexattr_getpshared()` or
`pthread_mutexattr_setpshared()` does not refer to an initialized mutex attributes object.

## Return value

Upon successful completion, `pthread_mutexattr_setpshared()` shall return zero; otherwise, an error number shall be
returned to indicate the error.

Upon successful completion, `pthread_mutexattr_getpshared()` shall return zero and store the value of the
process-shared attribute of _attr_ into the object referenced by the _pshared_ parameter. Otherwise, an error number
shall be returned to indicate the error.

## Errors

The `pthread_mutexattr_setpshared()` function shall fail if:

* `ENOTSUP` - The value of _pshared_ is `PTHREAD_PROCESS_SHARED` (see POSIX deviations).

The `pthread_mutexattr_setpshared()` function may fail if:

* `EINVAL` - The new value specified for the attribute is outside the range of legal values for that attribute.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

Phoenix-RTOS doesn't support process-shared mutexes (the Thread Process-Shared Synchronization option,
`_POSIX_THREAD_PROCESS_SHARED` is not defined). `pthread_mutexattr_setpshared()` fails with `ENOTSUP` when _pshared_ is
`PTHREAD_PROCESS_SHARED`, an error that the standard does not define for it, and `pthread_mutexattr_getpshared()` always
reports `PTHREAD_PROCESS_PRIVATE`. A Phoenix-RTOS mutex is a kernel object identified by a handle which is valid only in
the process that created it, so a mutex placed in memory shared by several processes can't be used by threads of the
other processes.
