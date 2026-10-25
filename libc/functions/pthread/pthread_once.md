# pthread_once

## Synopsis

```c
#include <pthread.h>

int pthread_once(pthread_once_t *once_control,
                 void (*init_routine)(void));
pthread_once_t once_control = PTHREAD_ONCE_INIT;
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The first call to `pthread_once()` by any thread in a process, with a given _once_control_, shall call the
_init_routine_ with no arguments. Subsequent calls of `pthread_once()` with the same _once_control_ shall not call the
_init_routine_. On return from `pthread_once()`, _init_routine_ shall have completed. The _once_control_ parameter shall
determine whether the associated initialization routine has been called.

The `pthread_once()` function is not a cancellation point. However, if _init_routine_ is a cancellation point and is
canceled, the effect on _once_control_ shall be as if `pthread_once()` was never called.

If the call to _init_routine_ is terminated by a call to `longjmp()`, `_longjmp()`, or `siglongjmp()`, the behavior is
undefined.

The constant `PTHREAD_ONCE_INIT` is defined in the `<pthread.h>` header.

The behavior of `pthread_once()` is undefined if _once_control_ has automatic storage duration or is not initialized by
`PTHREAD_ONCE_INIT`.

## Return value

Upon successful completion, `pthread_once()` shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_once()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
