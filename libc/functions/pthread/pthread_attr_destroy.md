# pthread_attr_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_attr_destroy(pthread_attr_t *attr);

int pthread_attr_init(pthread_attr_t *attr);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_destroy()` function shall destroy a thread attributes object. An implementation may cause
`pthread_attr_destroy()` to set _attr_ to an implementation-defined invalid value. A destroyed _attr_ attributes object
can be reinitialized using `pthread_attr_init()`; the results of otherwise referencing the object after it has been
destroyed are undefined.

The `pthread_attr_init()` function shall initialize a thread attributes object _attr_ with the default value for all
the individual attributes used by a given implementation. In Phoenix-RTOS the default values are:

* _detachstate_ - `PTHREAD_CREATE_JOINABLE`,

* _inheritsched_ - `PTHREAD_EXPLICIT_SCHED`,

* _schedpolicy_ - `SCHED_RR`,

* _schedparam_ - the default priority of Phoenix-RTOS threads (see
  [Scheduling priorities](../../posix.md#scheduling-priorities)),

* _contentionscope_ - `PTHREAD_SCOPE_SYSTEM`,

* _stackaddr_ - `NULL` (the stack is allocated by `pthread_create()`),

* _stacksize_ - `PTHREAD_STACK_MIN` rounded up to a multiple of the page size,

* _guardsize_ - `0`.

The resulting attributes object (possibly modified by setting individual attribute values) when used by
`pthread_create()` defines the attributes of the thread created. A single attributes object can be used in multiple
simultaneous calls to `pthread_create()`. Results are undefined if `pthread_attr_init()` is called specifying an already
initialized _attr_ attributes object.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_destroy()` does not refer to an
initialized thread attributes object.

## Return value

Upon successful completion, `pthread_attr_destroy()` and `pthread_attr_init()` shall return a value of `0`; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `pthread_attr_init()` function shall fail if:

* `ENOMEM` - Insufficient memory exists to initialize the thread attributes object.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
