# sem_wait

## Synopsis

```c
#include <semaphore.h>

int sem_wait(sem_t *sem);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_wait()` function shall lock the semaphore referenced by _sem_. If the semaphore
value is greater than zero it is decremented and the call returns at once; otherwise the
calling thread shall block until it can perform the decrement or the call is interrupted.

Both named and unnamed semaphores are accepted. Waiters on a named semaphore are released
highest priority first, and in first-in-first-out order among equal priorities.

A call that blocks on a named semaphore is a message send to `posixsrv` and is not
interruptible: it never fails with `EINTR`, and it is not a cancellation point although
IEEE Std 1003.1-2017 lists it as one. See [POSIX implementation](../../posix.md) for the
scope of that deviation. Use `sem_timedwait()` where a thread has to regain control.

## Return value

Upon successful completion, `sem_wait()` shall return 0 with the semaphore locked.
Otherwise it shall return -1, the semaphore state shall be unchanged, and `errno` shall be
set to indicate the error.

## Errors

This function shall fail if:

* `EINVAL` - _sem_ is a null pointer or does not refer to a valid semaphore,

* `EBADF` - the named semaphore has been closed or removed.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

A blocking call is not interruptible and is not a cancellation point.
