# pthread_cancel

## Synopsis

```c
#include <pthread.h>

int pthread_cancel(pthread_t thread);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_cancel()` function shall request that _thread_ be canceled. The target thread's cancelability state and
type determines when the cancellation takes effect. When the cancellation is acted on, the cancellation cleanup handlers
for _thread_ shall be called. When the last cancellation cleanup handler returns, the thread-specific data destructor
functions shall be called for _thread_. When the last destructor function returns, _thread_ shall be terminated.

The cancellation processing in the target thread shall run asynchronously with respect to the calling thread returning
from `pthread_cancel()`.

## Return value

If successful, the `pthread_cancel()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_cancel()` function shall not return an error code of `EINTR`.

## POSIX deviations

If cancelability of the target is enabled when another thread calls `pthread_cancel()`, the cancellation processing
does not run in the target thread. `pthread_cancel()` calls the cleanup handlers and the thread-specific data
destructors of the target in the calling thread before it returns, and then terminates the target wherever it is
executing, not at a cancellation point. A target blocked in a call handled by `posixsrv`, such as `sem_wait()` on a
named semaphore or a read from an empty pipe, is terminated only when the call returns. See
[Blocking operations are not interruptible](../../posix.md#blocking-operations-are-not-interruptible).

## Known bugs

* [pthread_cancel() does not take effect after pthread_setcancelstate() re-enables
  cancellation](https://github.com/phoenix-rtos/phoenix-rtos-project/issues/1645)
