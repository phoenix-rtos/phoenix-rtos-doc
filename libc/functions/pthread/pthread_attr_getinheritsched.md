# pthread_attr_getinheritsched

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getinheritsched(const pthread_attr_t *restrict attr,
                                 int *restrict inheritsched);

int pthread_attr_setinheritsched(pthread_attr_t *attr,
                                 int inheritsched);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_getinheritsched()` and `pthread_attr_setinheritsched()` functions, respectively, shall get and set the
_inheritsched_ attribute in the _attr_ argument.

When the attributes objects are used by `pthread_create()`, the _inheritsched_ attribute determines how the other
scheduling attributes of the created thread shall be set.

The supported values of _inheritsched_ shall be:

* `PTHREAD_INHERIT_SCHED` - Specifies that the thread scheduling attributes shall be inherited from the creating thread,
  and the scheduling attributes in this _attr_ argument shall be ignored.

* `PTHREAD_EXPLICIT_SCHED` - Specifies that the thread scheduling attributes shall be set to the corresponding values
  from this attributes object.

The symbols `PTHREAD_INHERIT_SCHED` and `PTHREAD_EXPLICIT_SCHED` are defined in the `<pthread.h>` header. In
Phoenix-RTOS the default value of the attribute is `PTHREAD_EXPLICIT_SCHED`.

The following thread scheduling attributes defined by POSIX.1-2017 are affected by the _inheritsched_ attribute:
scheduling policy (_schedpolicy_), scheduling parameters (_schedparam_), and scheduling contention scope
(_contentionscope_). In Phoenix-RTOS only the priority of the created thread depends on the _inheritsched_ attribute.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getinheritsched()` or
`pthread_attr_setinheritsched()` does not refer to an initialized thread attributes object.

## Return value

If successful, the `pthread_attr_getinheritsched()` and `pthread_attr_setinheritsched()` functions shall return zero;
otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_attr_setinheritsched()` function shall fail if:

* `ENOTSUP` - An attempt was made to set the attribute to an unsupported value.

The `pthread_attr_setinheritsched()` function may fail if:

* `EINVAL` - The value of _inheritsched_ is not valid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
