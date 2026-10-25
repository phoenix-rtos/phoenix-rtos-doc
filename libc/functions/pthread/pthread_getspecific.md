# pthread_getspecific

## Synopsis

```c
#include <pthread.h>

void *pthread_getspecific(pthread_key_t key);

int pthread_setspecific(pthread_key_t key, const void *value);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_getspecific()` function shall return the value currently bound to the specified _key_ on behalf of the
calling thread.

The `pthread_setspecific()` function shall associate a thread-specific _value_ with a _key_ obtained via a previous
call to `pthread_key_create()`. Different threads may bind different values to the same key. These values are typically
pointers to blocks of dynamically allocated memory that have been reserved for use by the calling thread.

The effect of calling `pthread_getspecific()` or `pthread_setspecific()` with a _key_ value not obtained from
`pthread_key_create()` or after _key_ has been deleted with `pthread_key_delete()` is undefined.

Both `pthread_getspecific()` and `pthread_setspecific()` may be called from a thread-specific data destructor function.
A call to `pthread_getspecific()` for the thread-specific data key being destroyed shall return the value `NULL`,
unless the value is changed (after the destructor starts) by a call to `pthread_setspecific()`. Calling
`pthread_setspecific()` from a thread-specific data destructor routine may result either in lost storage (after at
least `PTHREAD_DESTRUCTOR_ITERATIONS` attempts at destruction) or in an infinite loop.

## Return value

The `pthread_getspecific()` function shall return the thread-specific data value associated with the given _key_. If
no thread-specific data value is associated with _key_, then the value `NULL` shall be returned.

If successful, the `pthread_setspecific()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

No errors are returned from `pthread_getspecific()`.

The `pthread_setspecific()` function shall fail if:

* `ENOMEM` - Insufficient memory exists to associate the non-`NULL` value with the key.

The `pthread_setspecific()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
