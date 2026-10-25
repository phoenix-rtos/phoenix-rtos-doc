# pthread_mutexattr_getprioceiling

## Synopsis

```c
#include <pthread.h>

int pthread_mutexattr_getprioceiling(const pthread_mutexattr_t *restrict attr,
                                     int *restrict prioceiling);

int pthread_mutexattr_setprioceiling(pthread_mutexattr_t *attr, int prioceiling);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutexattr_getprioceiling()` and `pthread_mutexattr_setprioceiling()` functions, respectively, shall get
and set the priority ceiling attribute of a mutex attributes object pointed to by _attr_ which was previously created by
the function `pthread_mutexattr_init()`.

The _prioceiling_ attribute contains the priority ceiling of initialized mutexes. The values of _prioceiling_ are
within the range of priorities of the `SCHED_RR` scheduling policy (see POSIX deviations). They are POSIX priorities, as
described in [Scheduling priorities](../../posix.md#scheduling-priorities). The default value of the attribute is the
lowest priority, returned by `sched_get_priority_min(SCHED_RR)`.

The _prioceiling_ attribute defines the priority ceiling of initialized mutexes, which is the minimum priority level at
which the critical section guarded by the mutex is executed. In order to avoid priority inversion, the priority ceiling
of the mutex shall be set to a priority higher than or equal to the highest priority of all the threads that may lock
that mutex. The priority ceiling is used only by mutexes with the protocol attribute set to `PTHREAD_PRIO_PROTECT`.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_mutexattr_getprioceiling()` or
`pthread_mutexattr_setprioceiling()` does not refer to an initialized mutex attributes object.

## Return value

Upon successful completion, the `pthread_mutexattr_getprioceiling()` and `pthread_mutexattr_setprioceiling()` functions
shall return zero; otherwise, an error number shall be returned to indicate the error.

## Errors

These functions may fail if:

* `EINVAL` - The value specified by _prioceiling_ is invalid.

* `EPERM` - The caller does not have the privilege to perform the operation.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

IEEE Std 1003.1-2017 defines the values of _prioceiling_ within the range of priorities of the `SCHED_FIFO` scheduling
policy. Phoenix-RTOS supports only the `SCHED_RR` policy, so `pthread_mutexattr_setprioceiling()` checks _prioceiling_
against the range of `SCHED_RR` priorities, returned by `sched_get_priority_min(SCHED_RR)` and
`sched_get_priority_max(SCHED_RR)`, and fails with `EINVAL` for a value outside of it. The Phoenix-RTOS kernel schedules
all threads with a single priority-based round-robin policy, which keeps the scheduler small and its behaviour
predictable on resource-constrained real-time targets.
