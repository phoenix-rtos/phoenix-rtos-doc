# sigprocmask

## Synopsis

```c
#include <signal.h>

int pthread_sigmask(int how,
                    const sigset_t *restrict set,
                    sigset_t *restrict oset);

int sigprocmask(int how,
                const sigset_t *restrict set,
                sigset_t *restrict oset);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pthread_sigmask()` function shall examine or change (or both) the calling thread's signal mask, regardless of the
number of threads in the process. The function shall be equivalent to `sigprocmask()`, without the restriction that the
call be made in a single-threaded process.
In a single-threaded process, the `sigprocmask()` function shall examine or change (or both) the signal mask of the
calling thread.
If the argument _set_ is not a `null` pointer, it points to a set of signals to be used to change the currently blocked
set.
The argument how indicates the way in which the set is changed, and the application shall ensure it consists of one of
the following values:

* `SIG_BLOCK`
The resulting set shall be the union of the current set and the signal set pointed to by _set_.

* `SIG_SETMASK`
The resulting set shall be the signal set pointed to by _set_.

* `SIG_UNBLOCK`
The resulting set shall be the intersection of the current set and the complement of the signal set pointed to by
_set_.

If the argument _oset_ is not a `null` pointer, the previous mask shall be stored in the location pointed to by oset.
If _set_ is a `null` pointer, the value of the argument how is not significant and the thread's signal mask shall be
unchanged; thus the call can be used to inquire about currently blocked signals.
If there are any pending unblocked signals after the call to `sigprocmask()`, at least one of those signals shall be
delivered before the call to `sigprocmask()` returns.
It is not possible to block those signals which cannot be ignored. This shall be enforced by the system without causing
an error to be indicated.
If any of the `SIGFPE`, `SIGILL`, `SIGSEGV`, or `SIGBUS` signals are generated while they are blocked, the result is
undefined, unless the signal was generated by the action of another process, or by one of the functions `kill()`,
`pthread_kill()`,`raise()`, or`sigqueue()`.
If `sigprocmask()` fails, the thread's signal mask shall not be changed.
The use of the `sigprocmask()` function is unspecified in a multithreaded process.

## Return value

Upon successful completion `pthread_sigmask()` shall return `0`; otherwise, it shall return the corresponding error
number.
Upon successful completion, `sigprocmask()` shall return `0`; otherwise, `-1` shall be returned, `errno` shall be set to
indicate the error, and the signal mask of the process shall be unchanged.

## Errors

The `pthread_sigmask()` and `sigprocmask()` functions shall fail if:

* `EINVAL` - The value of how argument is not equal to one of the defined values. </br>
  
The `pthread_sigmask()` function shall not return an error code of `EINT`.

## Tests

Untested

## Known bugs

None
