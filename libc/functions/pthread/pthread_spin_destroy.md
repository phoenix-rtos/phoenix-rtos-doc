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

The supported value of _pshared_ is `PTHREAD_PROCESS_PRIVATE` (see POSIX deviations).

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

* `ENOTSUP` - The value of _pshared_ is `PTHREAD_PROCESS_SHARED` (see POSIX deviations).

These functions shall not return an error code of `EINTR`.

## POSIX deviations

With the Thread Process-Shared Synchronization option, IEEE Std 1003.1-2017 requires a spin lock initialized with
`PTHREAD_PROCESS_SHARED` to be usable by any thread that has access to the memory where it is allocated, even if that
memory is shared by multiple processes. Phoenix-RTOS does not support this option (`_POSIX_THREAD_PROCESS_SHARED` is not
defined), and `pthread_spin_init()` returns `ENOTSUP` for `PTHREAD_PROCESS_SHARED`, an error that the standard does not
define for it. Spin locks reject it consistently with the other synchronization objects, which are built on per-process
kernel resources.
