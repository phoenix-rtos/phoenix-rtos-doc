# pthread_mutexattr_getprotocol

## Synopsis

```c
#include <pthread.h>

int pthread_mutexattr_getprotocol(const pthread_mutexattr_t *restrict attr,
                                  int *restrict protocol);

int pthread_mutexattr_setprotocol(pthread_mutexattr_t *attr, int protocol);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_mutexattr_getprotocol()` and `pthread_mutexattr_setprotocol()` functions, respectively, shall get and set
the protocol attribute of a mutex attributes object pointed to by _attr_ which was previously created by the function
`pthread_mutexattr_init()`.

The _protocol_ attribute defines the protocol to be followed in utilizing mutexes. The value of _protocol_ may be one
of:

* `PTHREAD_PRIO_INHERIT`

* `PTHREAD_PRIO_NONE`

* `PTHREAD_PRIO_PROTECT`

which are defined in the `<pthread.h>` header.

When a thread owns a mutex with the `PTHREAD_PRIO_NONE` protocol attribute, its priority and scheduling shall not be
affected by its mutex ownership.

When a thread is blocking higher priority threads because of owning one or more mutexes with the `PTHREAD_PRIO_INHERIT`
protocol attribute, it shall execute at the higher of its priority or the priority of the highest priority thread
waiting on any of the mutexes owned by this thread and initialized with this protocol.

When a thread owns one or more mutexes initialized with the `PTHREAD_PRIO_PROTECT` protocol, it shall execute at the
higher of its priority or the highest of the priority ceilings of all the mutexes owned by this thread and initialized
with this attribute, regardless of whether other threads are blocked on any of these mutexes or not.

While a thread is holding a mutex which has been initialized with the `PTHREAD_PRIO_INHERIT` or `PTHREAD_PRIO_PROTECT`
protocol attributes, it shall not be subject to being moved to the tail of the scheduling queue at its priority in the
event that its original priority is changed, such as by a call to `sched_setparam()`. Likewise, when a thread unlocks a
mutex that has been initialized with the `PTHREAD_PRIO_INHERIT` or `PTHREAD_PRIO_PROTECT` protocol attributes, it shall
not be subject to being moved to the tail of the scheduling queue at its priority in the event that its original
priority is changed.

If a thread simultaneously owns several mutexes initialized with different protocols, it shall execute at the highest of
the priorities that it would have obtained by each of these protocols.

When a thread makes a call to `pthread_mutex_lock()`, the mutex was initialized with the protocol attribute having the
value `PTHREAD_PRIO_INHERIT`, when the calling thread is blocked because the mutex is owned by another thread, that
owner thread shall inherit the priority level of the calling thread as long as it continues to own the mutex. The
implementation shall update its execution priority to the maximum of its assigned priority and all its inherited
priorities. Furthermore, if this owner thread itself becomes blocked on another mutex with the protocol attribute having
the value `PTHREAD_PRIO_INHERIT`, the same priority inheritance effect shall be propagated to this other owner thread,
in a recursive manner.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_mutexattr_getprotocol()` or
`pthread_mutexattr_setprotocol()` does not refer to an initialized mutex attributes object.

## Return value

Upon successful completion, the `pthread_mutexattr_getprotocol()` and `pthread_mutexattr_setprotocol()` functions shall
return zero; otherwise, an error number shall be returned to indicate the error.

## Errors

The `pthread_mutexattr_setprotocol()` function shall fail if:

* `ENOTSUP` - The value specified by _protocol_ is an unsupported value.

The `pthread_mutexattr_getprotocol()` and `pthread_mutexattr_setprotocol()` functions may fail if:

* `EINVAL` - The value specified by _protocol_ is invalid.

* `EPERM` - The caller does not have the privilege to perform the operation.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
