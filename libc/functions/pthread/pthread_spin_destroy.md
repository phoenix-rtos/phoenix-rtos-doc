# pthread_spin_destroy

## Synopsis

```c
#include <pthread.h>

int pthread_spin_destroy(pthread_spinlock_t *lock);

int pthread_spin_init(pthread_spinlock_t *lock, int pshared);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_spin_destroy()` function shall destroy the spin lock referenced by _lock_ and release any resources used by
the lock. The effect of subsequent use of the lock is undefined until the lock is reinitialized by another call to
`pthread_spin_init()`. The results are undefined if `pthread_spin_destroy()` is called when a thread holds the lock, or
if this function is called with an uninitialized thread spin lock.

The `pthread_spin_init()` function shall allocate any resources required to use the spin lock referenced by _lock_ and
initialize the lock to an unlocked state. In Phoenix-RTOS a spin lock is a single integer updated with atomic
operations and needs no other resources.

The results are undefined if `pthread_spin_init()` is called specifying an already initialized spin lock. The results
are undefined if a spin lock is used without first being initialized.

If the `pthread_spin_init()` function fails, the lock is not initialized and the contents of _lock_ are undefined.

Only the object referenced by _lock_ may be used for performing synchronization. The result of referring to copies of
that object in calls to `pthread_spin_destroy()`, `pthread_spin_lock()`, `pthread_spin_trylock()`, or
`pthread_spin_unlock()` is undefined.

## Return value

Upon successful completion, these functions shall return zero; otherwise, an error number shall be returned to indicate
the error.

## Errors

The `pthread_spin_init()` function shall fail if:

* `EAGAIN` - The system lacks the necessary resources to initialize another spin lock.

* `ENOMEM` - Insufficient memory exists to initialize the lock.

* `EINVAL` - The value of _pshared_ is neither `PTHREAD_PROCESS_PRIVATE` nor `PTHREAD_PROCESS_SHARED`.

These functions shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
