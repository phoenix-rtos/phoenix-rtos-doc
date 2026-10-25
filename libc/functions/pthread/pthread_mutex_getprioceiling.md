# pthread_mutex_getprioceiling

## Synopsis

```c
#include <pthread.h>

int pthread_mutex_getprioceiling(const pthread_mutex_t *restrict mutex,
                                 int *restrict prioceiling);

int pthread_mutex_setprioceiling(pthread_mutex_t *restrict mutex,
                                 int prioceiling, int *restrict old_ceiling);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutex_getprioceiling()` function shall return the current priority ceiling of the mutex.

The `pthread_mutex_setprioceiling()` function shall attempt to lock the mutex as if by a call to `pthread_mutex_lock()`,
except that the process of locking the mutex need not adhere to the priority protect protocol. On acquiring the mutex it
shall change the mutex's priority ceiling and then release the mutex as if by a call to `pthread_mutex_unlock()`. When
the change is successful, the previous value of the priority ceiling shall be returned in _old_ceiling_.

If the `pthread_mutex_setprioceiling()` function fails, the mutex priority ceiling shall not be changed.

The values of _prioceiling_ and _old_ceiling_ are POSIX priorities, as described in [Scheduling
priorities](../../posix.md#scheduling-priorities). A mutex has a priority ceiling only if its protocol attribute is
`PTHREAD_PRIO_PROTECT`; for a mutex with the `PTHREAD_PRIO_NONE` or `PTHREAD_PRIO_INHERIT` protocol both functions fail
with `EINVAL`.

## Return value

If successful, the `pthread_mutex_getprioceiling()` and `pthread_mutex_setprioceiling()` functions shall return zero;
otherwise, an error number shall be returned to indicate the error.

## Errors

These functions shall fail if:

* `EINVAL` - The protocol attribute of _mutex_ is `PTHREAD_PRIO_NONE`.

* `EPERM` - The implementation requires appropriate privileges to perform the operation and the caller does not have
appropriate privileges.

The `pthread_mutex_setprioceiling()` function shall fail if:

* `EAGAIN` - The mutex could not be acquired because the maximum number of recursive locks for _mutex_ has been
exceeded.

* `EDEADLK` - The mutex type is `PTHREAD_MUTEX_ERRORCHECK` and the current thread already owns the mutex.

* `EINVAL` - The mutex was created with the protocol attribute having the value `PTHREAD_PRIO_PROTECT` and the calling
thread's priority is higher than the mutex's current priority ceiling, and the implementation adheres to the priority
protect protocol in the process of locking the mutex.

* `ENOTRECOVERABLE` - The mutex is a robust mutex and the state protected by the mutex is not recoverable.

* `EOWNERDEAD` - The mutex is a robust mutex and the process containing the previous owning thread terminated while
holding the mutex lock. The mutex lock shall be acquired by the calling thread, and it is up to the new owner to make
the state consistent (see `pthread_mutex_lock()`).

The `pthread_mutex_setprioceiling()` function may fail if:

* `EDEADLK` - A deadlock condition was detected.

* `EINVAL` - The priority requested by _prioceiling_ is out of range.

* `EOWNERDEAD` - The mutex is a robust mutex and the previous owning thread terminated while holding the mutex lock. The
mutex lock shall be acquired by the calling thread, and it is up to the new owner to make the state consistent (see
`pthread_mutex_lock()`).

These functions shall not return an error code of `EINTR`.

## POSIX deviations

IEEE Std 1003.1-2017 defines the values of the priority ceiling within the range of priorities of the `SCHED_FIFO`
scheduling policy. Phoenix-RTOS supports only the `SCHED_RR` policy, so _prioceiling_ is checked against the range of
`SCHED_RR` priorities, returned by `sched_get_priority_min(SCHED_RR)` and `sched_get_priority_max(SCHED_RR)`, and
`pthread_mutex_setprioceiling()` fails with `EINVAL` for a value outside of it. The Phoenix-RTOS kernel schedules all
threads with a single priority-based round-robin policy, which keeps the scheduler small and its behaviour predictable
on resource-constrained real-time targets.
