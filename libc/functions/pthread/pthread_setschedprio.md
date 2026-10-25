# pthread_setschedprio

## Synopsis

```c
#include <pthread.h>

int pthread_setschedprio(pthread_t thread, int prio);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_setschedprio()` function shall set the scheduling priority for the thread whose thread ID is given by
_thread_ to the value given by _prio_.

The _prio_ argument is a POSIX priority, as described in [Scheduling priorities](../../posix.md#scheduling-priorities).
Its valid range is reported by `sched_get_priority_min()` and `sched_get_priority_max()` for the `SCHED_RR` policy.

If the `pthread_setschedprio()` function fails, the scheduling priority of the target thread shall not be changed.

## Return value

If successful, the `pthread_setschedprio()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_setschedprio()` function may fail if:

* `EINVAL` - The value of _prio_ is invalid for the scheduling policy of the specified thread.

* `EPERM` - The caller does not have appropriate privileges to set the scheduling priority of the specified thread.

The `pthread_setschedprio()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
