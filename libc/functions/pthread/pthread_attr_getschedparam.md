# pthread_attr_getschedparam

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getschedparam(const pthread_attr_t *restrict attr,
                               struct sched_param *restrict param);

int pthread_attr_setschedparam(pthread_attr_t *restrict attr,
                               const struct sched_param *restrict param);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_getschedparam()` and `pthread_attr_setschedparam()` functions, respectively, shall get and set the
scheduling parameter attributes in the _attr_ argument. The contents of the _param_ structure are defined in the
`<sched.h>` header. For the `SCHED_FIFO` and `SCHED_RR` policies, the only required member of _param_ is
_sched_priority_.

The _sched_priority_ member holds a POSIX priority, as described in
[Scheduling priorities](../../posix.md#scheduling-priorities). Its valid range is reported by
`sched_get_priority_min()` and `sched_get_priority_max()` for the `SCHED_RR` policy.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getschedparam()` or
`pthread_attr_setschedparam()` does not refer to an initialized thread attributes object.

## Return value

If successful, the `pthread_attr_getschedparam()` and `pthread_attr_setschedparam()` functions shall return zero;
otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_attr_setschedparam()` function shall fail if:

* `ENOTSUP` - An attempt was made to set the attribute to an unsupported value.

The `pthread_attr_setschedparam()` function may fail if:

* `EINVAL` - The value of _param_ is not valid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
