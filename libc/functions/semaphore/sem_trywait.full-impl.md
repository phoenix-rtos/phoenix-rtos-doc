# sem_trywait

## Synopsis

```c
#include <semaphore.h>

int sem_trywait(sem_t *sem);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_trywait()` function shall lock the semaphore referenced by _sem_ only if it can be
locked without delay, that is if its value is greater than zero. The call never blocks.

Both named and unnamed semaphores are accepted.

## Return value

Upon successful completion, `sem_trywait()` shall return 0 with the semaphore locked.
Otherwise it shall return -1, the semaphore state shall be unchanged, and `errno` shall be
set to indicate the error.

## Errors

This function shall fail if:

* `EAGAIN` - the semaphore was already locked, so it cannot be locked without delay,

* `EINVAL` - _sem_ is a null pointer or does not refer to a valid semaphore,

* `EBADF` - the named semaphore has been closed or removed.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

None
