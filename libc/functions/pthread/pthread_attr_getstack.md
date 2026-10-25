# pthread_attr_getstack

## Synopsis

```c
#include <pthread.h>

int pthread_attr_getstack(const pthread_attr_t *restrict attr,
                          void **restrict stackaddr, size_t *restrict stacksize);

int pthread_attr_setstack(pthread_attr_t *attr, void *stackaddr,
                          size_t stacksize);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_attr_getstack()` and `pthread_attr_setstack()` functions, respectively, shall get and set the thread
creation stack attributes _stackaddr_ and _stacksize_ in the _attr_ object.

The stack attributes specify the area of storage to be used for the created thread's stack. The base (lowest
addressable byte) of the storage shall be _stackaddr_, and the size of the storage shall be _stacksize_ bytes. The
_stacksize_ shall be at least `PTHREAD_STACK_MIN`. The `pthread_attr_setstack()` function may fail with `EINVAL` if
_stackaddr_ does not meet implementation-defined alignment requirements. All pages within the stack described by
_stackaddr_ and _stacksize_ shall be both readable and writable by the thread.

If the `pthread_attr_getstack()` function is called before the _stackaddr_ attribute has been set, the behavior is
unspecified.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_attr_getstack()` or
`pthread_attr_setstack()` does not refer to an initialized thread attributes object.

## Return value

Upon successful completion, these functions shall return a value of `0`; otherwise, an error number shall be returned
to indicate the error.

The `pthread_attr_getstack()` function shall store the stack attribute values in _stackaddr_ and _stacksize_ if
successful.

## Errors

The `pthread_attr_setstack()` function shall fail if:

* `EINVAL` - The value of _stacksize_ is less than `PTHREAD_STACK_MIN` or exceeds an implementation-defined limit.

The `pthread_attr_setstack()` function may fail if:

* `EINVAL` - The value of _stackaddr_ does not have proper alignment to be used as a stack, or
  `((char *) stackaddr + stacksize)` lacks proper alignment.

* `EACCES` - The stack page(s) described by _stackaddr_ and _stacksize_ are not both readable and writable by the
  thread.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
