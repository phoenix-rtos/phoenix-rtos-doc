# sem_unlink

## Synopsis

```c
#include <semaphore.h>

int sem_unlink(const char *name);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_unlink()` function shall remove the semaphore named by _name_.

The name is removed immediately, so a subsequent `sem_open()` without `O_CREAT` fails and one
with `O_CREAT` creates a new semaphore. Processes that already hold the semaphore open may
keep using it; the semaphore itself is destroyed once the last `sem_close()` returns.

## Return value

Upon successful completion, `sem_unlink()` shall return 0. Otherwise it shall return -1,
the named semaphore shall be unchanged, and `errno` shall be set to indicate the error.

## Errors

This function shall fail if:

* `EINVAL` - _name_ is a null pointer or is not a valid semaphore name,

* `ENAMETOOLONG` - the length of _name_ exceeds `NAME_MAX`,

* `ENOENT` - the named semaphore does not exist.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

None
