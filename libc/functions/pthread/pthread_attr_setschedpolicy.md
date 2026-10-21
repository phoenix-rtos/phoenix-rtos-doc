# pthread_attr_setschedpolicy

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getschedpolicy(const pthread_attr_t *restrict attr,
                                int *restrict policy);

int pthread_attr_setschedpolicy(pthread_attr_t *attr, int policy);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_getschedpolicy()` and `pthread_attr_setschedpolicy()` functions, respectively, shall get and set the
_schedpolicy_ attribute in the _attr_ argument.

The supported value of _policy_ is `SCHED_RR`, which is defined in the `<sched.h>` header. It is also the default value
of the attribute. When threads executing with the scheduling policy `SCHED_RR` are waiting on a mutex, they shall
acquire the mutex in priority order when the mutex is unlocked.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getschedpolicy()` or
`pthread_attr_setschedpolicy()` does not refer to an initialized thread attributes object.

## Return value

If successful, the `pthread_attr_getschedpolicy()` and `pthread_attr_setschedpolicy()` functions shall return zero;
otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_attr_setschedpolicy()` function shall fail if:

* `ENOTSUP` - An attempt was made to set the attribute to an unsupported value (`SCHED_FIFO` or `SCHED_OTHER`).

The `pthread_attr_setschedpolicy()` function may fail if:

* `EINVAL` - The value of _policy_ is not valid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

IEEE Std 1003.1-2017 requires the supported values of _policy_ to include `SCHED_FIFO`, `SCHED_RR` and `SCHED_OTHER`.
Phoenix-RTOS supports only `SCHED_RR`, and `pthread_attr_setschedpolicy()` returns `ENOTSUP` for `SCHED_FIFO` and
`SCHED_OTHER`. The Phoenix-RTOS kernel schedules all threads with a single priority-based round-robin policy, which
keeps the scheduler small and its behaviour predictable on resource-constrained real-time targets. See [Scheduling
priorities](../../posix.md#scheduling-priorities) for the mapping of POSIX priorities.
