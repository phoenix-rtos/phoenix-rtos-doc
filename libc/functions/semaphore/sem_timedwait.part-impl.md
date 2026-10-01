# sem_timedwait

## Synopsis

```c
#include <semaphore.h>

int sem_timedwait(sem_t *restrict sem, const struct timespec *restrict abstime);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sem_timedwait()` function shall lock the semaphore referenced by _sem_ as
`sem_wait()` does, except that the wait is bounded by _abstime_, an absolute deadline on
the `CLOCK_REALTIME` clock. If the semaphore cannot be locked before the deadline passes,
the call shall fail.

The deadline is an absolute time rather than an interval, so an unrelated change to the
system clock moves it. A deadline that has already passed is not an error: the call still
succeeds if the semaphore can be locked at once, and only fails with `ETIMEDOUT` when it
cannot.

For a named semaphore the deadline is sent to `posixsrv` and resolved there, at the moment
the request is parked, so the time the message spends in flight is not charged against it.

_abstime_ is only validated once the semaphore is found to be unavailable, so a call that
can be satisfied immediately succeeds whatever _abstime_ contains.

## Return value

Upon successful completion, `sem_timedwait()` shall return 0 with the semaphore locked.
Otherwise it shall return -1, the semaphore state shall be unchanged, and `errno` shall be
set to indicate the error.

## Errors

This function shall fail if:

* `ETIMEDOUT` - the semaphore could not be locked before the deadline passed,

* `EINVAL` - _sem_ is a null pointer or does not refer to a valid semaphore, or the
  `tv_nsec` field of _abstime_ is negative or 1000 million or more,

* `EBADF` - the named semaphore has been closed or removed.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

The deadline is converted to microseconds internally, so a `tv_sec` beyond
`TIME_T_MAX / 1000000` overflows and the wait ends early.

A blocking call is not interruptible and is not a cancellation point.
