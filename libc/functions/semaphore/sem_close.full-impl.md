# sem_close

## Synopsis

```c
#include <semaphore.h>

int sem_close(sem_t *sem);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_close()` function shall release any state associated with the named semaphore
_sem_, previously returned by `sem_open()`, and deallocate the memory that call reserved.

If the semaphore has been unlinked with `sem_unlink()`, closing the last open reference to
it also destroys it. `sem_close()` does not apply to unnamed semaphores; destroy those with
`sem_destroy()`.

Using _sem_ after it has been closed has undefined results.

## Return value

Upon successful completion, `sem_close()` shall return 0. Otherwise it shall return -1 and
set `errno` to indicate the error.

## Errors

This function shall fail if:

* `EINVAL` - _sem_ is a null pointer or does not refer to a named semaphore.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

None
