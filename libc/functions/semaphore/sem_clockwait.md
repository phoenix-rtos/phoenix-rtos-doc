# sem_clockwait

## Synopsis

```c
#include <semaphore.h>

int sem_clockwait(sem_t *restrict sem, clockid_t clock_id,
	const struct timespec *restrict abstime);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

The `sem_clockwait()` function shall lock the semaphore referenced by _sem_ as `sem_wait()`
does, except that the wait is bounded by _abstime_, an absolute deadline measured on the
clock named by _clock_id_. If the semaphore cannot be locked before the deadline passes,
the call shall fail.

`CLOCK_REALTIME` and `CLOCK_MONOTONIC` are supported, as the standard requires;
`CLOCK_MONOTONIC_RAW` is accepted as a synonym for `CLOCK_MONOTONIC`. Any other clock is
rejected. `sem_timedwait()` is the same call fixed to `CLOCK_REALTIME`.

A `CLOCK_REALTIME` deadline is an absolute time, so an unrelated change to the system clock
moves it; a `CLOCK_MONOTONIC` deadline is unaffected by such a change. On a board with no
real-time clock the two read alike, and only differ once the realtime clock has been set.

For a named semaphore the deadline and the clock are sent to `posixsrv` and resolved there,
at the moment the request is parked, so the time the message spends in flight is not charged
against it.

_abstime_ and _clock_id_ are checked before the semaphore is examined, so an invalid one is
rejected even when the semaphore could have been locked at once. The standard requires the
error only for a call that would have blocked, which leaves either behaviour open.

The function was added in IEEE Std 1003.1-2024. See the deviation described for
`sem_wait()`, which applies here too.

## Return value

Upon successful completion, `sem_clockwait()` shall return 0 with the semaphore locked.
Otherwise it shall return -1, the semaphore state shall be unchanged, and `errno` shall be
set to indicate the error.

## Errors

This function shall fail if:

* `ETIMEDOUT` - the semaphore could not be locked before the deadline passed,

* `EINVAL` - _sem_ is a null pointer or does not refer to a valid semaphore, the `tv_nsec`
  field of _abstime_ is negative or 1000 million or more, or _clock_id_ is not a supported
  clock,

* `EBADF` - the named semaphore has been closed or removed.

## Tests

Tested in [test-libc-semaphore](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master/libc/semaphore)

## Known bugs

The deadline is converted to microseconds internally, so a `tv_sec` beyond
`TIME_T_MAX / 1000000` overflows and the wait ends early.
