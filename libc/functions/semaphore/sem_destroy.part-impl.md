# sem_destroy

## Synopsis

```c
#include <semaphore.h>

int sem_destroy(sem_t *sem);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_destroy()` destroys unnamed semaphore `sem`, deallocating all resources
previously assigned to passed semaphore.

## Return value

On success, `sem_destroy()` return `EOK` status.
On error, `sem_destroy()` returns `-1` with `errno` set to indicate the error.

## Errors

* `EINVAL` - Passed `sem` is not a valid semaphore.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)

## Known bugs

None
