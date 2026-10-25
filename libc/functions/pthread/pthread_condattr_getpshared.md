# pthread_condattr_getpshared

## Synopsis

```c
#include <pthread.h>

int pthread_condattr_getpshared(const pthread_condattr_t *restrict attr,
                                int *restrict pshared);

int pthread_condattr_setpshared(pthread_condattr_t *attr, int pshared);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_condattr_getpshared()` function shall obtain the value of the process-shared attribute from the attributes
object referenced by _attr_.

The `pthread_condattr_setpshared()` function shall set the process-shared attribute in an initialized attributes object
referenced by _attr_.

The process-shared attribute is set to `PTHREAD_PROCESS_SHARED` to permit a condition variable to be operated upon by
any thread that has access to the memory where the condition variable is allocated, even if the condition variable is
allocated in memory that is shared by multiple processes. The default value of the attribute is
`PTHREAD_PROCESS_PRIVATE`.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_condattr_getpshared()` or
`pthread_condattr_setpshared()` does not refer to an initialized condition variable attributes object.

## Return value

If successful, the `pthread_condattr_setpshared()` function shall return zero; otherwise, an error number shall be
returned to indicate the error.

If successful, the `pthread_condattr_getpshared()` function shall return zero and store the value of the process-shared
attribute of _attr_ into the object referenced by the _pshared_ parameter. Otherwise, an error number shall be returned
to indicate the error.

## Errors

The `pthread_condattr_setpshared()` function may fail if:

* `EINVAL` - The new value specified for the attribute is outside the range of legal values for that attribute.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
