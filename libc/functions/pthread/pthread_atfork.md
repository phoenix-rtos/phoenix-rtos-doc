# pthread_atfork

## Synopsis

```c
#include <pthread.h>

int pthread_atfork(void (*prepare)(void), void (*parent)(void),
                   void (*child)(void));
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_atfork()` function shall declare fork handlers to be called before and after `fork()`, in the context of
the thread that called `fork()`. The _prepare_ fork handler shall be called before `fork()` processing commences. The
_parent_ fork handler shall be called after `fork()` processing completes in the parent process. The _child_ fork
handler shall be called after `fork()` processing completes in the child process. If no handling is desired at one or
more of these three points, the corresponding fork handler address(es) may be set to `NULL`.

If a `fork()` call in a multithreaded process leads to a _child_ fork handler calling any function that is not
async-signal-safe, the behavior is undefined.

The order of calls to `pthread_atfork()` is significant. The _parent_ and _child_ fork handlers shall be called in the
order in which they were established by calls to `pthread_atfork()`. The _prepare_ fork handlers shall be called in the
opposite order.

## Return value

Upon successful completion, `pthread_atfork()` shall return a value of zero; otherwise, an error number shall be
returned to indicate the error.

## Errors

The `pthread_atfork()` function shall fail if:

* `ENOMEM` - Insufficient table space exists to record the fork handler addresses.

The `pthread_atfork()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
