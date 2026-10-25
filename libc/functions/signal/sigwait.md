# sigwait

## Synopsis

```c
#include <signal.h>

int sigwait(const sigset_t *restrict set, int *restrict sig);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigwait()` function shall select a pending signal from _set_, atomically clear it from the system's set of pending
signals, and return that signal number in the location referenced by _sig_. If prior to the call to `sigwait()` there
are multiple pending instances of a single signal number, it is implementation-defined whether upon successful return
there are any remaining pending signals for that signal number. Signals are not queued, so multiple pending instances
of a signal number are kept as one pending signal, which is cleared by `sigwait()`. If no signal in _set_ is pending at
the time of the call, the thread shall be suspended until one or more becomes pending. The signals defined by _set_
shall have been blocked at the time of the call to `sigwait()`; otherwise, the behavior is undefined. The effect of
`sigwait()` on the signal actions for the signals in _set_ is unspecified.

If more than one thread is using `sigwait()` to wait for the same signal, no more than one of these threads shall
return from `sigwait()` with the signal number. If more than a single thread is blocked in `sigwait()` for a signal when
that signal is generated for the process, it is unspecified which of the waiting threads returns from `sigwait()`. If
the signal is generated for a specific thread, as by `pthread_kill()`, only that thread shall return.

The selection order between multiple pending signals is unspecified. Realtime signals (`SIGRTMIN` to `SIGRTMAX`) are not
supported.

A signal caught by a signal-catching function while the thread waits in `sigwait()` doesn't end the wait: `sigwait()`
continues to wait for a signal from _set_.

## Return value

Upon successful completion, `sigwait()` shall store the signal number of the received signal at the location referenced
by _sig_ and return zero. Otherwise, an error number shall be returned to indicate the error.

## Errors

The `sigwait()` function may fail if:

* `EINVAL` - The _set_ argument contains an invalid or unsupported signal number.

## POSIX deviations

No POSIX deviations discovered.
