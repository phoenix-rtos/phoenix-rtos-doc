# sem_post

## Synopsis

```c
#include <semaphore.h>

int sem_post(sem_t *sem);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_post()` increments value of passed semaphore.
More specifically, if there is a wait queue for the semaphore, it wakes up
thread first in queue.
If the queue is empty, the semaphore's value is incremented.

## Return value

On success, `sem_post()` returns `EOK` status.
On error, `sem_post()` returns `-1` with `errno` set to indicate the error.

## Errors

* `EINVAL` - Passed `sem` is not a valid semaphore.

* `EOVERFLOW` - Semaphore value increment would overflow its max value.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)
