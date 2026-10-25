# pthread_attr_getguardsize

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getguardsize(const pthread_attr_t *restrict attr,
                              size_t *restrict guardsize);

int pthread_attr_setguardsize(pthread_attr_t *attr,
                              size_t guardsize);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_getguardsize()` function shall get the _guardsize_ attribute in the _attr_ object. This attribute
shall be returned in the _guardsize_ parameter.

The `pthread_attr_setguardsize()` function shall set the _guardsize_ attribute in the _attr_ object. The new value of
this attribute shall be obtained from the _guardsize_ parameter. If _guardsize_ is zero, a guard area shall not be
provided for threads created with _attr_. If _guardsize_ is greater than zero, a guard area of at least size
_guardsize_ bytes shall be provided for each thread created with _attr_.

The _guardsize_ attribute controls the size of the guard area for the created thread's stack. The _guardsize_ attribute
provides protection against overflow of the stack pointer. If a thread's stack is created with guard protection, the
implementation allocates extra memory at the overflow end of the stack as a buffer against stack overflow of the stack
pointer. If an application overflows into this buffer an error shall result (possibly in a `SIGSEGV` signal being
delivered to the thread).

A conforming implementation may round up the value contained in _guardsize_ to a multiple of the configurable system
variable `PAGESIZE`. If an implementation rounds up the value of _guardsize_ to a multiple of `PAGESIZE`, a call to
`pthread_attr_getguardsize()` specifying _attr_ shall store in the _guardsize_ parameter the guard size specified by the
previous `pthread_attr_setguardsize()` function call. Phoenix-RTOS rounds the guard size up to a multiple of the page
size when the thread is created.

The default value of the _guardsize_ attribute is implementation-defined. In Phoenix-RTOS it is `0`.

If the _stackaddr_ attribute has been set (that is, the caller is allocating and managing its own thread stacks), the
_guardsize_ attribute shall be ignored and no protection shall be provided by the implementation. It is the
responsibility of the application to manage stack overflow along with stack allocation and management in this case.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getguardsize()` or
`pthread_attr_setguardsize()` does not refer to an initialized thread attributes object.

## Return value

If successful, the `pthread_attr_getguardsize()` and `pthread_attr_setguardsize()` functions shall return zero;
otherwise, an error number shall be returned to indicate the error.

## Errors

These functions shall fail if:

* `EINVAL` - The parameter _guardsize_ is invalid.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
