# pthread_detach

## Synopsis

```c
#include <pthread.h>

int pthread_detach(pthread_t thread);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_detach()` function shall indicate to the implementation that storage for the thread _thread_ can be
reclaimed when that thread terminates. If _thread_ has not terminated, `pthread_detach()` shall not cause it to
terminate.

The behavior is undefined if the value specified by the _thread_ argument to `pthread_detach()` does not refer to a
joinable thread.

## Return value

If the call succeeds, `pthread_detach()` shall return `0`; otherwise, an error number shall be returned to indicate the
error.

## Errors

The `pthread_detach()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
