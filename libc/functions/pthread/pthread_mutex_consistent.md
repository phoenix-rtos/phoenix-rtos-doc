# pthread_mutex_consistent

## Synopsis

```c
#include <pthread.h>

int pthread_mutex_consistent(pthread_mutex_t *mutex);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

If _mutex_ is a robust mutex in an inconsistent state, the `pthread_mutex_consistent()` function can be used to mark
the state protected by the mutex referenced by _mutex_ as consistent again.

If an owner of a robust mutex terminates while holding the mutex, the mutex becomes inconsistent and the next thread
that acquires the mutex lock shall be notified of the state by the return value `EOWNERDEAD`. In this case, the mutex
does not become normally usable again until the state is marked consistent.

If the thread which acquired the mutex lock with the return value `EOWNERDEAD` terminates before calling either
`pthread_mutex_consistent()` or `pthread_mutex_unlock()`, the next thread that acquires the mutex lock shall be notified
about the state of the mutex by the return value `EOWNERDEAD`.

The behavior is undefined if the value specified by the _mutex_ argument to `pthread_mutex_consistent()` does not refer
to an initialized mutex.

## Return value

Upon successful completion, the `pthread_mutex_consistent()` function shall return zero. Otherwise, an error value shall
be returned to indicate the error.

## Errors

The `pthread_mutex_consistent()` function shall fail if:

* `EINVAL` - The mutex object referenced by _mutex_ is not robust or does not protect an inconsistent state.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
