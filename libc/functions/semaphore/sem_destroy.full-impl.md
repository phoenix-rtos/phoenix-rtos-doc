# sem_destroy

## Synopsis

```c
#include <semaphore.h>

int sem_destroy(sem_t *sem);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_destroy()` function shall destroy the unnamed semaphore indicated by _sem_, which
may then be reinitialised with `sem_init()`.

Destroying a semaphore on which threads are currently blocked has undefined results.
`sem_destroy()` does not apply to named semaphores; release those with `sem_close()`.

## Return value

Upon successful completion, `sem_destroy()` shall return 0. Otherwise it shall return -1
and set `errno` to indicate the error.

## Errors

This function shall fail if:

* `EINVAL` - _sem_ is a null pointer or does not refer to an unnamed semaphore.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

None
