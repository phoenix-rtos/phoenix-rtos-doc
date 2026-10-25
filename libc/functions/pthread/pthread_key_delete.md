# pthread_key_delete

## Synopsis

```c
#include <pthread.h>

int pthread_key_delete(pthread_key_t key);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_key_delete()` function shall delete a thread-specific data key previously returned by
`pthread_key_create()`. The thread-specific data values associated with _key_ need not be `NULL` at the time
`pthread_key_delete()` is called. It is the responsibility of the application to free any application storage or
perform any cleanup actions for data structures related to the deleted key or associated thread-specific data in any
threads; this cleanup can be done either before or after `pthread_key_delete()` is called. Any attempt to use _key_
following the call to `pthread_key_delete()` results in undefined behavior.

The `pthread_key_delete()` function shall be callable from within destructor functions. No destructor functions shall
be invoked by `pthread_key_delete()`. Any destructor function that may have been associated with _key_ shall no longer
be called upon thread exit.

## Return value

If successful, the `pthread_key_delete()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_key_delete()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
