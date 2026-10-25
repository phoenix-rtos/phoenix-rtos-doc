# pthread_cond_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_cond_destroy(pthread_cond_t *cond);

int pthread_cond_init(pthread_cond_t *restrict cond,
                      const pthread_condattr_t *restrict attr);

pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_cond_destroy()` function shall destroy the given condition variable specified by _cond_; the object
becomes, in effect, uninitialized. An implementation may cause `pthread_cond_destroy()` to set the object referenced by
_cond_ to an invalid value. A destroyed condition variable object can be reinitialized using `pthread_cond_init()`; the
results of otherwise referencing the object after it has been destroyed are undefined.

It shall be safe to destroy an initialized condition variable upon which no threads are currently blocked. Attempting to
destroy a condition variable upon which other threads are currently blocked results in undefined behavior.

The `pthread_cond_init()` function shall initialize the condition variable referenced by _cond_ with attributes
referenced by _attr_. If _attr_ is `NULL`, the default condition variable attributes shall be used; the effect is the
same as passing the address of a default condition variable attributes object. Upon successful initialization, the state
of the condition variable shall become initialized.

Attempting to initialize an already initialized condition variable results in undefined behavior.

In cases where default condition variable attributes are appropriate, the macro `PTHREAD_COND_INITIALIZER` can be used
to initialize condition variables. The effect shall be equivalent to dynamic initialization by a call to
`pthread_cond_init()` with parameter _attr_ specified as `NULL`, except that no error checks are performed.

The behavior is undefined if the value specified by the _cond_ argument to `pthread_cond_destroy()` does not refer to
an initialized condition variable.

The behavior is undefined if the value specified by the _attr_ argument to `pthread_cond_init()` does not refer to an
initialized condition variable attributes object.

## Return value

If successful, the `pthread_cond_destroy()` and `pthread_cond_init()` functions shall return zero; otherwise, an error
number shall be returned to indicate the error.

## Errors

The `pthread_cond_init()` function shall fail if:

* `EAGAIN` - The system lacked the necessary resources (other than memory) to initialize another condition variable.

* `ENOMEM` - Insufficient memory exists to initialize the condition variable.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
