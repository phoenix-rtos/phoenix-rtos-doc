# pthread_create

## Synopsis

```c
#include <pthread.h>

int pthread_create(pthread_t *restrict thread,
                   const pthread_attr_t *restrict attr,
                   void *(*start_routine)(void*), void *restrict arg);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_create()` function shall create a new thread, with attributes specified by _attr_, within a process. If
_attr_ is `NULL`, the default attributes shall be used (see `pthread_attr_init()`). If the attributes specified by
_attr_ are modified later, the thread's attributes shall not be affected. Upon successful completion,
`pthread_create()` shall store the ID of the created thread in the location referenced by _thread_.

The thread is created executing _start_routine_ with _arg_ as its sole argument. If the _start_routine_ returns, the
effect shall be as if there was an implicit call to `pthread_exit()` using the return value of _start_routine_ as the
exit status. Note that the thread in which `main()` was originally invoked differs from this. When it returns from
`main()`, the effect shall be as if there was an implicit call to `exit()` using the return value of `main()` as the
exit status.

The signal state of the new thread shall be initialized as follows:

* The signal mask shall be inherited from the creating thread.

* The set of signals pending for the new thread shall be empty.

The thread-local current locale and the alternate stack shall not be inherited.

The floating-point environment shall be inherited from the creating thread.

If `pthread_create()` fails, no new thread is created and the contents of the location referenced by _thread_ are
undefined.

The new thread shall have a CPU-time clock accessible, and the initial value of this clock shall be set to zero.

Unless the _stackaddr_ attribute is set, the stack of the new thread is allocated by `pthread_create()`, with the size
of the _stacksize_ and _guardsize_ attributes rounded up to a multiple of the page size, and it is freed after the
thread is joined or, for a detached thread, after it terminates.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_create()` does not refer to an
initialized thread attributes object.

## Return value

If successful, the `pthread_create()` function shall return zero; otherwise, an error number shall be returned to
indicate the error.

## Errors

The `pthread_create()` function shall fail if:

* `EAGAIN` - The system lacked the necessary resources to create another thread, or the system-imposed limit on the
  total number of threads in a process `PTHREAD_THREADS_MAX` would be exceeded.

* `EPERM` - The caller does not have appropriate privileges to set the required scheduling parameters or scheduling
  policy.

The `pthread_create()` function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
