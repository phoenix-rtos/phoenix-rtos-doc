# sigismember

## Synopsis

```c
#include <signal.h>

int sigismember(const sigset_t *set, int signo);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigismember()` function shall test whether the signal specified by _signo_ is a member of the set pointed to by
_set_.

Applications should call either `sigemptyset()` or `sigfillset()` at least once for each object of type `sigset_t`
prior to any other use of that object. If such an object is not initialized in this way, but is nonetheless supplied as
an argument to any of `pthread_sigmask()`, `sigaction()`, `sigaddset()`, `sigdelset()`, `sigismember()`,
`sigpending()`, `sigprocmask()`, `sigsuspend()`, `sigtimedwait()`, `sigwait()`, or `sigwaitinfo()`, the
results are undefined.

## Return value

Upon successful completion, `sigismember()` shall return `1` if the specified signal is a member of the specified
set, or `0` if it is not. Otherwise, it shall return `-1` and set `errno` to indicate the error.

## Errors

The `sigismember()` function may fail if:

* `EINVAL` - The _signo_ argument is not a valid signal number, or is an unsupported signal number.

## POSIX deviations

No POSIX deviations discovered.
