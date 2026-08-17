# sem_init

## Synopsis

```c
#include <semaphore.h>

int sem_init(sem_t *sem, int pshared, unsigned int value);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_init()` initializes an unnamed semaphore with initial value of `value`.

## Return value

On success, `sem_init()` returns `EOK` status. On error, it returns `-1` with `errno` set to indicate the error.

## Errors

* `EINVAL` - Passed `sem` is not a valid semaphore, or `value` exceeds `SEM_VALUE_MAX`.

* `ENOSYS` - `pshared` parameter value is non-zero.

## Remarks

Phoenix-RTOS does not support sharing unnamed semaphores between processes.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)
