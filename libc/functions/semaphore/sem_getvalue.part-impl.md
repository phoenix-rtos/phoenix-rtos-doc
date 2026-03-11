# sem_getvalue

## Synopsis

```c
#include <semaphore.h>

int sem_getvalue(sem_t *restrict sem, int *restrict value);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_getvalue()` retrieves current value of specified semaphore.
This call may block if semaphore is contested by another calling thread.

## Return value

On success, `sem_getvalue()` returns `EOK` status. On error, it returns `-1` with `errno` set to indicate the error.

## Errors

* `EINVAL` - Passed `sem` is not a valid semaphore.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)
