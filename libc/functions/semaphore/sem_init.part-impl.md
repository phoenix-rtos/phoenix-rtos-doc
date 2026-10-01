# sem_init

## Synopsis

```c
#include <semaphore.h>

int sem_init(sem_t *sem, int pshared, unsigned int value);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_init()` function shall initialise the unnamed semaphore referred to by _sem_ to
_value_, which shall not exceed `SEM_VALUE_MAX`. The semaphore is usable by any thread of
the calling process until it is destroyed with `sem_destroy()`.

A non-zero _pshared_ requests a semaphore shared between processes. Phoenix-RTOS does not
implement process-shared unnamed semaphores; use a named semaphore, created with
`sem_open()`, when several processes have to share one.

Initialising a semaphore that is already initialised, or one on which threads are blocked,
has undefined results.

## Return value

Upon successful completion, `sem_init()` shall return 0. Otherwise it shall return -1 and
set `errno` to indicate the error.

## Errors

This function shall fail if:

* `EINVAL` - _sem_ is a null pointer, or _value_ exceeds `SEM_VALUE_MAX`,

* `ENOSPC` - a resource required to initialise the semaphore has been exhausted,

* `ENOSYS` - _pshared_ is non-zero; process-shared unnamed semaphores are not supported.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

None
