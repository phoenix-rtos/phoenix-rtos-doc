# pthread_attr_getdetachstate

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getdetachstate(const pthread_attr_t *attr,
                                int *detachstate);

int pthread_attr_setdetachstate(pthread_attr_t *attr, int detachstate);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The _detachstate_ attribute controls whether the thread is created in a detached state. If the thread is created
detached, then use of the ID of the newly created thread by the `pthread_detach()` or `pthread_join()` function is an
error.

The `pthread_attr_getdetachstate()` and `pthread_attr_setdetachstate()` functions, respectively, shall get and set the
_detachstate_ attribute in the _attr_ object.

For `pthread_attr_getdetachstate()`, _detachstate_ shall be set to either `PTHREAD_CREATE_DETACHED` or
`PTHREAD_CREATE_JOINABLE`.

For `pthread_attr_setdetachstate()`, the application shall set _detachstate_ to either `PTHREAD_CREATE_DETACHED` or
`PTHREAD_CREATE_JOINABLE`.

A value of `PTHREAD_CREATE_DETACHED` shall cause all threads created with _attr_ to be in the detached state, whereas
using a value of `PTHREAD_CREATE_JOINABLE` shall cause all threads created with _attr_ to be in the joinable state. The
default value of the _detachstate_ attribute shall be `PTHREAD_CREATE_JOINABLE`.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getdetachstate()` or
`pthread_attr_setdetachstate()` does not refer to an initialized thread attributes object.

## Return value

Upon successful completion, `pthread_attr_getdetachstate()` and `pthread_attr_setdetachstate()` shall return a value of
`0`; otherwise, an error number shall be returned to indicate the error.

The `pthread_attr_getdetachstate()` function stores the value of the _detachstate_ attribute in _detachstate_ if
successful.

## Errors

The `pthread_attr_setdetachstate()` function shall fail if:

* `EINVAL` - The value of _detachstate_ was not valid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
