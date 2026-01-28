# sem_close

## Synopsis

```c
#include <semaphore.h>

int sem_close(sem_t *sem);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_close()` closes a previously opened named semaphore, deallocating resources
previously assigned to passed semaphore.

## Return value

On success, `sem_close()` returns `EOK` status.
On error, `sem_close()` returns `-1` with `errno` set to indicate the error.

## Errors

* `EINVAL` - Passed `sem` is not a valid semaphore.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)
