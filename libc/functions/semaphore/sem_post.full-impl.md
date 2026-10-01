# sem_post

## Synopsis

```c
#include <semaphore.h>

int sem_post(sem_t *sem);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_post()` function shall unlock the semaphore referenced by _sem_. If any threads
are blocked on the semaphore, one of them shall be allowed to return successfully;
otherwise the semaphore value shall be incremented.

Both named and unnamed semaphores are accepted. On a named semaphore the waiter released is
the highest priority one that has been waiting longest, which satisfies the scheduling
requirement IEEE Std 1003.1-2017 states for `SCHED_FIFO` and `SCHED_RR`.

## Return value

Upon successful completion, `sem_post()` shall return 0. Otherwise it shall return -1, the
semaphore state shall be unchanged, and `errno` shall be set to indicate the error.

## Errors

This function shall fail if:

* `EOVERFLOW` - the maximum allowable value for a semaphore would be exceeded,

* `EINVAL` - _sem_ is a null pointer or does not refer to a valid semaphore,

* `EBADF` - the named semaphore has been closed or removed.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

None
