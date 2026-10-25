# pthread_condattr_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_condattr_destroy(pthread_condattr_t *attr);

int pthread_condattr_init(pthread_condattr_t *attr);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_condattr_destroy()` function shall destroy a condition variable attributes object; the object becomes, in
effect, uninitialized. An implementation may cause `pthread_condattr_destroy()` to set the object referenced by _attr_
to an invalid value. A destroyed _attr_ attributes object can be reinitialized using `pthread_condattr_init()`; the
results of otherwise referencing the object after it has been destroyed are undefined.

The `pthread_condattr_init()` function shall initialize a condition variable attributes object _attr_ with the default
value for all the attributes defined by the implementation.

Results are undefined if `pthread_condattr_init()` is called specifying an already initialized _attr_ attributes
object.

After a condition variable attributes object has been used to initialize one or more condition variables, any function
affecting the attributes object (including destruction) shall not affect any previously initialized condition
variables.

IEEE Std 1003.1-2017 requires two attributes, the clock attribute and the process-shared attribute. Their default values
are `CLOCK_REALTIME` and `PTHREAD_PROCESS_PRIVATE`. Phoenix-RTOS defines no additional attributes.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_condattr_destroy()` does not refer
to an initialized condition variable attributes object.

## Return value

If successful, the `pthread_condattr_destroy()` and `pthread_condattr_init()` functions shall return zero; otherwise,
an error number shall be returned to indicate the error.

## Errors

The `pthread_condattr_init()` function shall fail if:

* `ENOMEM` - Insufficient memory exists to initialize the condition variable attributes object.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
