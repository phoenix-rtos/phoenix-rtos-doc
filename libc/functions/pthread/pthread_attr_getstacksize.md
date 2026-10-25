# pthread_attr_getstacksize

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getstacksize(const pthread_attr_t *restrict attr,
                              size_t *restrict stacksize);

int pthread_attr_setstacksize(pthread_attr_t *attr, size_t stacksize);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_getstacksize()` and `pthread_attr_setstacksize()` functions, respectively, shall get and set the
thread creation _stacksize_ attribute in the _attr_ object.

The _stacksize_ attribute shall define the minimum stack size (in bytes) allocated for the created threads stack. In
Phoenix-RTOS the default value of the attribute is `PTHREAD_STACK_MIN` rounded up to a multiple of the page size. When
the stack is allocated by `pthread_create()`, its size is rounded up to a multiple of the page size.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getstacksize()` or
`pthread_attr_setstacksize()` does not refer to an initialized thread attributes object.

## Return value

Upon successful completion, `pthread_attr_getstacksize()` and `pthread_attr_setstacksize()` shall return a value of
`0`; otherwise, an error number shall be returned to indicate the error.

The `pthread_attr_getstacksize()` function stores the _stacksize_ attribute value in _stacksize_ if successful.

## Errors

The `pthread_attr_setstacksize()` function shall fail if:

* `EINVAL` - The value of _stacksize_ is less than `PTHREAD_STACK_MIN` or exceeds a system-imposed limit.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
