# sigtimedwait

## Synopsis

```c
#include <signal.h>

int sigtimedwait(const sigset_t *restrict set,
                 siginfo_t *restrict info,
                 const struct timespec *restrict timeout);

int sigwaitinfo(const sigset_t *restrict set,
                siginfo_t *restrict info);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigtimedwait()` function shall be equivalent to `sigwaitinfo()` except that if none of the signals specified by
_set_ are pending, `sigtimedwait()` shall wait for the time interval specified in the `timespec` structure referenced
by _timeout_. If the `timespec` structure pointed to by _timeout_ is zero-valued and if none of the signals specified
by _set_ are pending, then `sigtimedwait()` shall return immediately with an error. If _timeout_ is the `NULL` pointer,
`sigtimedwait()` waits without a time limit, like `sigwaitinfo()`.

The `sigwaitinfo()` function selects the pending signal from the set specified by _set_. The selection order between
multiple pending signals is unspecified. If no signal in _set_ is pending at the time of the call, the calling thread
shall be suspended until one or more signals in _set_ become pending or until it is interrupted by an unblocked, caught
signal.

The `sigwaitinfo()` function shall be equivalent to the `sigwait()` function, except that the return value and the error
reporting method are different (see Return value), and that if the _info_ argument is non-`NULL`, the selected signal
number shall be stored in the `si_signo` member, and the cause of the signal shall be stored in the `si_code` member. If
any value is queued to the selected signal, the first such queued value shall be dequeued and, if the _info_ argument is
non-`NULL`, the value shall be stored in the `si_value` member of _info_. If no value is queued, the content of the
`si_value` member is undefined. If no further signals are queued for the selected signal, the pending indication for
that signal shall be reset.

## Return value

Upon successful completion (that is, one of the signals specified by _set_ is pending or is generated) `sigwaitinfo()`
and `sigtimedwait()` shall return the selected signal number. Otherwise, the function shall return a value of `-1` and
set `errno` to indicate the error.

## Errors

The `sigtimedwait()` function shall fail if:

* `EAGAIN` - No signal specified by _set_ was generated within the specified timeout period.

The `sigtimedwait()` and `sigwaitinfo()` functions may fail if:

* `EINTR` - The wait was interrupted by an unblocked, caught signal. These functions fail with `EINTR` in this case.

The `sigtimedwait()` function may also fail if:

* `EINVAL` - The _timeout_ argument specified a `tv_nsec` value less than zero or greater than or equal to 1000
million. The error is reported also when a signal in _set_ is pending.

## POSIX deviations

No POSIX deviations discovered.
