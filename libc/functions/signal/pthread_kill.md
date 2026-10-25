# pthread_kill

## Synopsis

```c
#include <signal.h>

int pthread_kill(pthread_t thread, int sig);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_kill()` function shall request that a signal be delivered to the specified _thread_.

As in `kill()`, if _sig_ is zero, error checking shall be performed, but no signal shall actually be sent.

## Return value

Upon successful completion, the function shall return a value of zero. Otherwise, the function shall return an error
number. If the `pthread_kill()` function fails, no signal shall be sent.

## Errors

The `pthread_kill()` function shall fail if:

* `EINVAL` - The value of the _sig_ argument is an invalid or unsupported signal number.

The `pthread_kill()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
