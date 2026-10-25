# raise

## Synopsis

```c
#include <signal.h>

int raise(int sig);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `raise()` function shall send the signal _sig_ to the executing thread or process. If a signal handler is called,
the `raise()` function shall not return until after the signal handler does.

The effect of the `raise()` function shall be equivalent to calling:

```c
pthread_kill(pthread_self(), sig);
```

## Return value

Upon successful completion, `0` shall be returned. Otherwise, a non-zero value shall be returned and `errno` shall be
set to indicate the error.

## Errors

The `raise()` function shall fail if:

* `EINVAL` - The value of the _sig_ argument is an invalid signal number.

## POSIX deviations

The default actions of the job control signals are not implemented: `SIGSTOP`, `SIGTSTP`, `SIGTTIN` and `SIGTTOU` do not
stop the process and `SIGCONT` does not continue it. With the default disposition these signals are ignored (see the
deviations of `kill()`).
