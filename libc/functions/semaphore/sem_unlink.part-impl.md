# sem_unlink

## Synopsis

```c
#include <semaphore.h>

int sem_unlink(const char *name);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

`sem_unlink()` unlinks semaphore referred to by `name` from the system.

Semaphores identifier is removed from semaphore namespace, however the resources
will be deallocated only after all remaining processes close their respective
instances of the semaphore.

## Return value

On success, `sem_unlink()` return `EOK` status.
On error, `sem_unlink()` returns `-1` with `errno` set to indicate the error.

## Errors

* `ENOENT` - No semaphore identified by `name` can be found on the system.

* `ENODEV` - The semaphore system has not yet been initialized.

## Tests

Tested in [test-posix](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/posix)

## Known bugs

None
