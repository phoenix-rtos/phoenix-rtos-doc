# pthread_getschedparam

## Synopsis

```c
#include <pthread.h>

int pthread_getschedparam(pthread_t thread, int *restrict policy,
                          struct sched_param *restrict param);

int pthread_setschedparam(pthread_t thread, int policy,
                          const struct sched_param *param);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_getschedparam()` and `pthread_setschedparam()` functions shall, respectively, get and set the scheduling
policy and parameters of individual threads within a multithreaded process to be retrieved and set. For `SCHED_FIFO`
and `SCHED_RR`, the only required member of the `sched_param` structure is the priority _sched_priority_. For
`SCHED_OTHER`, the affected scheduling parameters are implementation-defined.

The `pthread_getschedparam()` function shall retrieve the scheduling policy and scheduling parameters for the thread
whose thread ID is given by _thread_ and shall store those values in _policy_ and _param_, respectively. The priority
value returned from `pthread_getschedparam()` shall be the value specified by the most recent
`pthread_setschedparam()`, `pthread_setschedprio()`, or `pthread_create()` call affecting the target thread. It shall
not reflect any temporary adjustments to its priority as a result of any priority inheritance or ceiling functions. The
`pthread_setschedparam()` function shall set the scheduling policy and associated scheduling parameters for the thread
whose thread ID is given by _thread_ to the policy and associated parameters provided in _policy_ and _param_,
respectively.

The _policy_ parameter may have the value `SCHED_OTHER`, `SCHED_FIFO`, or `SCHED_RR`. The scheduling parameters for the
`SCHED_OTHER` policy are implementation-defined. The `SCHED_FIFO` and `SCHED_RR` policies shall have a single scheduling
parameter, _priority_. The _sched_priority_ member holds a POSIX priority, as described in [Scheduling
priorities](../../posix.md#scheduling-priorities).

If the `pthread_setschedparam()` function fails, the scheduling parameters shall not be changed for the target thread.

## Return value

If successful, the `pthread_getschedparam()` and `pthread_setschedparam()` functions shall return zero; otherwise, an
error number shall be returned to indicate the error.

## Errors

The `pthread_setschedparam()` function shall fail if:

* `ENOTSUP` - An attempt was made to set the policy or scheduling parameters to an unsupported value.

The `pthread_setschedparam()` function may fail if:

* `EINVAL` - The value specified by _policy_ or one of the scheduling parameters associated with the scheduling policy
  _policy_ is invalid.

* `EPERM` - The caller does not have appropriate privileges to set either the scheduling parameters or the scheduling
  policy of the specified thread.

* `EPERM` - The implementation does not allow the application to modify one of the parameters to the value specified.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
