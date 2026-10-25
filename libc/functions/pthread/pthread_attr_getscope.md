# pthread_attr_getscope

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getscope(const pthread_attr_t *restrict attr,
                          int *restrict contentionscope);

int pthread_attr_setscope(pthread_attr_t *attr, int contentionscope);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_getscope()` and `pthread_attr_setscope()` functions, respectively, shall get and set the
_contentionscope_ attribute in the _attr_ object.

The _contentionscope_ attribute may have the values `PTHREAD_SCOPE_SYSTEM`, signifying system scheduling contention
scope, or `PTHREAD_SCOPE_PROCESS`, signifying process scheduling contention scope. The symbols `PTHREAD_SCOPE_SYSTEM`
and `PTHREAD_SCOPE_PROCESS` are defined in the `<pthread.h>` header.

Phoenix-RTOS supports only the `PTHREAD_SCOPE_SYSTEM` value, which is also the default value of the attribute. All
threads are scheduled by the kernel and compete for the processor with all other threads in the system.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getscope()` or
`pthread_attr_setscope()` does not refer to an initialized thread attributes object.

## Return value

If successful, the `pthread_attr_getscope()` and `pthread_attr_setscope()` functions shall return zero; otherwise, an
error number shall be returned to indicate the error.

## Errors

The `pthread_attr_setscope()` function shall fail if:

* `ENOTSUP` - An attempt was made to set the attribute to an unsupported value (`PTHREAD_SCOPE_PROCESS`).

The `pthread_attr_setscope()` function may fail if:

* `EINVAL` - The value of _contentionscope_ is not valid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
