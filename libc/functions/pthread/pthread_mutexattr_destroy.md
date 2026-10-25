# pthread_mutexattr_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_mutexattr_destroy(pthread_mutexattr_t *attr);

int pthread_mutexattr_init(pthread_mutexattr_t *attr);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutexattr_destroy()` function shall destroy a mutex attributes object; the object becomes, in effect,
uninitialized. An implementation may cause `pthread_mutexattr_destroy()` to set the object referenced by _attr_ to an
invalid value.

A destroyed _attr_ attributes object can be reinitialized using `pthread_mutexattr_init()`; the results of otherwise
referencing the object after it has been destroyed are undefined.

The `pthread_mutexattr_init()` function shall initialize a mutex attributes object _attr_ with the default value for all
the attributes defined by the implementation. The default values are:

* type - `PTHREAD_MUTEX_DEFAULT` (the same type as `PTHREAD_MUTEX_NORMAL`),

* robust - `PTHREAD_MUTEX_STALLED`,

* protocol - `PTHREAD_PRIO_INHERIT` (see POSIX deviations),

* prioceiling - the lowest priority, returned by `sched_get_priority_min(SCHED_RR)`,

* process-shared - `PTHREAD_PROCESS_PRIVATE`.

Results are undefined if `pthread_mutexattr_init()` is called specifying an already initialized _attr_ attributes
object.

After a mutex attributes object has been used to initialize one or more mutexes, any function affecting the attributes
object (including destruction) shall not affect any previously initialized mutexes.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_mutexattr_destroy()` does not refer
to an initialized mutex attributes object.

## Return value

Upon successful completion, `pthread_mutexattr_destroy()` and `pthread_mutexattr_init()` shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `pthread_mutexattr_init()` function shall fail if:

* `ENOMEM` - Insufficient memory exists to initialize the mutex attributes object.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

IEEE Std 1003.1-2017 requires the default value of the _protocol_ attribute to be `PTHREAD_PRIO_NONE`. In Phoenix-RTOS
`pthread_mutexattr_init()` sets it to `PTHREAD_PRIO_INHERIT`, the same protocol which is used by default for kernel
mutexes. Priority inheritance prevents unbounded priority inversion, which is the safer default in real-time systems. To
get a mutex with the `PTHREAD_PRIO_NONE` protocol, set it explicitly with `pthread_mutexattr_setprotocol()`.
