# pthread_testcancel

## Synopsis

```c
#include <pthread.h>

int pthread_setcancelstate(int state, int *oldstate);

int pthread_setcanceltype(int type, int *oldtype);

void pthread_testcancel(void);
```

## Status

`pthread_setcancelstate()` and `pthread_testcancel()` are implemented, `pthread_setcanceltype()` is not implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_setcancelstate()` function shall atomically both set the calling thread's cancelability state to the
indicated _state_ and return the previous cancelability state at the location referenced by _oldstate_. Legal values
for _state_ are `PTHREAD_CANCEL_ENABLE` and `PTHREAD_CANCEL_DISABLE`.

The cancelability state of any newly created threads, including the thread in which `main()` was first invoked, shall
be `PTHREAD_CANCEL_ENABLE`.

The `pthread_testcancel()` function shall create a cancellation point in the calling thread. The
`pthread_testcancel()` function shall have no effect if cancelability is disabled.

## Return value

If successful, the `pthread_setcancelstate()` function shall return zero; otherwise, an error number shall be returned
to indicate the error.

## Errors

The `pthread_setcancelstate()` function may fail if:

* `EINVAL` - The specified state is not `PTHREAD_CANCEL_ENABLE` or `PTHREAD_CANCEL_DISABLE`.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

`PTHREAD_CANCEL_DEFERRED` and `PTHREAD_CANCEL_ASYNCHRONOUS` are not defined.

If cancelability of the target is enabled when another thread calls `pthread_cancel()`, the cancellation processing
does not run in the target thread. `pthread_cancel()` calls the cleanup handlers and the thread-specific data
destructors of the target in the calling thread before it returns, and then terminates the target wherever it is
executing, not at a cancellation point. A target blocked in a call handled by `posixsrv`, such as `sem_wait()` on a
named semaphore or a read from an empty pipe, is terminated only when the call returns. See
[Blocking operations are not interruptible](../../posix.md#blocking-operations-are-not-interruptible).

A cancellation request made while cancelability is disabled is acted upon only by `pthread_testcancel()`, not by the
other cancellation points.
