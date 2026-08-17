# sem_wait/sem_trywait/sem_timedwait

## Synopsis

```c
#include <time.h>
#include <semaphore.h>

int sem_wait(sem_t *sem);
int sem_trywait(sem_t *sem);
int sem_timedwait(sem_t *restrict sem, const struct timespec *restrict abs_timeout);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_wait()` tries to decrement the semaphore value, if semaphore's value is already 0,
the call blocks until other thread increments it.

`sem_trywait()` is a non-blocking version of `sem_wait()`, meaning that if it
is unable to decrement semaphores value, it fails the call.

`sem_timedwait()` is a version of `sem_wait()` with timeout.
Value of `timeout` parameter specifies an absolute timeout value after which the
call should return if it does not decrement the semaphore value.

## Return value

On success, these functions return `EOK` status. On error, they return `-1` with `errno` set to indicate the error.

## Errors

* `EINVAL` - Passed `sem` is not a valid semaphore.

* `ETIMEDOUT` - (Only `sem_timedwait()`) The timeout expired.

* `EAGAIN` - (Only `sem_trywait()`) Operation would block.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)
