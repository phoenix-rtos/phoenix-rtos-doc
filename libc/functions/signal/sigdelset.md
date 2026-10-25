# sigdelset

## Synopsis

```c
#include <signal.h>

int sigdelset(sigset_t *set, int signo);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigdelset()` function deletes the individual signal specified by _signo_ from the signal set pointed to by
_set_.

Applications should call either `sigemptyset()` or `sigfillset()` at least once for each object of type `sigset_t`
prior to any other use of that object. If such an object is not initialized in this way, but is nonetheless supplied as
an argument to any of `pthread_sigmask()`, `sigaction()`, `sigaddset()`, `sigdelset()`, `sigismember()`,
`sigpending()`, `sigprocmask()`, `sigsuspend()`, `sigtimedwait()`, `sigwait()`, or `sigwaitinfo()`, the
results are undefined.

## Return value

Upon successful completion, `sigdelset()` shall return `0`; otherwise, it shall return `-1` and set `errno` to
indicate the error.

## Errors

The `sigdelset()` function may fail if:

* `EINVAL` - The _signo_ argument is not a valid signal number, or is an unsupported signal number.

## POSIX deviations

No POSIX deviations discovered.
