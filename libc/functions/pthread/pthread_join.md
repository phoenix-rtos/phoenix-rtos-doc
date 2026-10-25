# pthread_join

## Synopsis

```c
#include <pthread.h>

int pthread_join(pthread_t thread, void **value_ptr);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_join()` function shall suspend execution of the calling thread until the target thread terminates, unless
the target thread has already terminated. On return from a successful `pthread_join()` call with a non-`NULL`
_value_ptr_ argument, the value passed to `pthread_exit()` by the terminating thread shall be made available in the
location referenced by _value_ptr_. When a `pthread_join()` returns successfully, the target thread has been
terminated. The results of multiple simultaneous calls to `pthread_join()` specifying the same target thread are
undefined. If the thread calling `pthread_join()` is canceled, then the target thread shall not be detached.

It is unspecified whether a thread that has exited but remains unjoined counts against `PTHREAD_THREADS_MAX`.

The behavior is undefined if the value specified by the _thread_ argument to `pthread_join()` does not refer to a
joinable thread.

The behavior is undefined if the value specified by the _thread_ argument to `pthread_join()` refers to the calling
thread.

## Return value

If successful, the `pthread_join()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_join()` function may fail if:

* `EDEADLK` - A deadlock was detected.

The `pthread_join()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
