# sem_timedwait

## Synopsis

```c
#include <semaphore.h>

int sem_timedwait(sem_t *restrict sem, const struct timespec *restrict abstime);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2024

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

A call that blocks on a named semaphore is not interruptible and is not a cancellation point, exactly as described for
`sem_wait()`, so the deadline is the only way for the calling thread to regain control.

The clock is fixed at `CLOCK_REALTIME`. Use `sem_clockwait()`, added in
IEEE Std 1003.1-2024, where the deadline has to be measured on another clock.

For a named semaphore _abstime_ is converted to microseconds, so its `tv_sec` field must not exceed
`TIME_T_MAX / 1000000` (see POSIX deviations).

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

## POSIX deviations

For a named semaphore the deadline is converted to microseconds by `posixsrv`, so the `tv_sec` field of _abstime_ must
not exceed `TIME_T_MAX / 1000000`. A later deadline overflows the conversion and the wait ends early. IEEE Std
1003.1-2024 accepts any valid `timespec`. For an unnamed semaphore a deadline beyond this range is treated as an
infinite one.
