# sem_getvalue

## Synopsis

```c
#include <semaphore.h>

int sem_getvalue(sem_t *restrict sem, int *restrict value);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_getvalue()` function shall store the current value of the semaphore referenced by
_sem_ in the integer referenced by _value_. The value is a snapshot: it may already be
stale when the call returns, because another thread may lock or unlock the semaphore in the
meantime.

IEEE Std 1003.1-2017 allows an implementation to report either zero or a negative number
when threads are blocked on the semaphore. This implementation always reports the value
itself, which is never negative.

Both named and unnamed semaphores are accepted.

## Return value

Upon successful completion, `sem_getvalue()` shall return 0. Otherwise it shall return -1
and set `errno` to indicate the error.

## Errors

This function shall fail if:

* `EINVAL` - _sem_ is a null pointer or does not refer to a valid semaphore,

* `EBADF` - the named semaphore has been closed or removed.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

None
