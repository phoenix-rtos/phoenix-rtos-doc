# pthread_exit

## Synopsis

```c
#include <pthread.h>

void pthread_exit(void *value_ptr);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_exit()` function shall terminate the calling thread and make the value _value_ptr_ available to any
successful join with the terminating thread. Any cancellation cleanup handlers that have been pushed and not yet popped
shall be popped in the reverse order that they were pushed and then executed. After all cancellation cleanup handlers
have been executed, if the thread has any thread-specific data, appropriate destructor functions shall be called in an
unspecified order. Thread termination does not release any application visible process resources, including, but not
limited to, mutexes and file descriptors, nor does it perform any process-level cleanup actions, including, but not
limited to, calling any `atexit()` routines that may exist.

An implicit call to `pthread_exit()` is made when a thread other than the thread in which `main()` was first invoked
returns from the start routine that was used to create it. The function's return value shall serve as the thread's
exit status.

The behavior of `pthread_exit()` is undefined if called from a cancellation cleanup handler or destructor function that
was invoked as a result of either an implicit or explicit call to `pthread_exit()`.

After a thread has terminated, the result of access to local (auto) variables of the thread is undefined. Thus,
references to local variables of the exiting thread should not be used for the `pthread_exit()` _value_ptr_ parameter
value.

The process shall exit with an exit status of `0` after the last thread has been terminated. The behavior shall be as
if the implementation called `exit()` with a zero argument at thread termination time.

## Return value

The `pthread_exit()` function cannot return to its caller.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
