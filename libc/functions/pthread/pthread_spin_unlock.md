# pthread_spin_unlock

## Synopsis

```c
#include <pthread.h>

int pthread_spin_unlock(pthread_spinlock_t *lock);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_spin_unlock()` function shall release the spin lock referenced by _lock_ which was locked via the
`pthread_spin_lock()` or `pthread_spin_trylock()` functions.

The results are undefined if the lock is not held by the calling thread.

If there are threads spinning on the lock when `pthread_spin_unlock()` is called, the lock becomes available and an
unspecified spinning thread shall acquire the lock.

The results are undefined if this function is called with an uninitialized thread spin lock.

## Return value

Upon successful completion, the `pthread_spin_unlock()` function shall return zero; otherwise, an error number shall be
returned to indicate the error.

## Errors

This function shall not return an error code of `EINTR`.

## POSIX deviations

No POSIX deviations discovered.
