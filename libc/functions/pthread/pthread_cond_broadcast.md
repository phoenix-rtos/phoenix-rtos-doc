# pthread_cond_broadcast

## Synopsis

```c
#include <pthread.h>

int pthread_cond_broadcast(pthread_cond_t *cond);

int pthread_cond_signal(pthread_cond_t *cond);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

These functions shall unblock threads blocked on a condition variable.

The `pthread_cond_broadcast()` function shall unblock all threads currently blocked on the specified condition variable
_cond_.

The `pthread_cond_signal()` function shall unblock at least one of the threads that are blocked on the specified
condition variable _cond_ (if any threads are blocked on _cond_).

If more than one thread is blocked on a condition variable, the scheduling policy shall determine the order in which
threads are unblocked. When each thread unblocked as a result of a `pthread_cond_broadcast()` or `pthread_cond_signal()`
returns from its call to `pthread_cond_wait()` or `pthread_cond_timedwait()`, the thread shall own the mutex with which
it called `pthread_cond_wait()` or `pthread_cond_timedwait()`. The thread(s) that are unblocked shall contend for the
mutex according to the scheduling policy (if applicable), and as if each had called `pthread_mutex_lock()`.

The `pthread_cond_broadcast()` or `pthread_cond_signal()` functions may be called by a thread whether it
currently owns the mutex that threads calling `pthread_cond_wait()` or `pthread_cond_timedwait()` have associated with
the condition variable during their waits; however, if predictable scheduling behavior is required, then that mutex
shall be locked by the thread calling `pthread_cond_broadcast()` or `pthread_cond_signal()`.

The `pthread_cond_broadcast()` and `pthread_cond_signal()` functions shall have no effect if there are no threads
currently blocked on _cond_.

The behavior is undefined if the value specified by the _cond_ argument to `pthread_cond_broadcast()` or
`pthread_cond_signal()` does not refer to an initialized condition variable.

## Return value

If successful, the `pthread_cond_broadcast()` and `pthread_cond_signal()` functions shall return zero; otherwise, an
error number shall be returned to indicate the error.

## Errors

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
