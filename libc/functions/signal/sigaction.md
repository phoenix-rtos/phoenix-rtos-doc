# sigaction

## Synopsis

```c
#include <signal.h>

int sigaction(int sig, const struct sigaction *restrict act, struct sigaction *restrict oact);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigaction()` function allows the calling process to examine and/or specify the action to be associated with a
specific signal. The argument _sig_ specifies the signal; acceptable values are defined in `<signal.h>`.

The structure `sigaction`, used to describe an action to be taken, is defined in the `<signal.h>` header to include at
least the following members:

* `void (*sa_handler)(int)` - pointer to a signal-catching function or one of the macros `SIG_IGN` or `SIG_DFL`.

* `sigset_t sa_mask` - additional set of signals to be blocked during execution of signal-catching function.

* `int sa_flags` - special flags to affect behavior of signal.

* `void (*sa_sigaction)(int, siginfo_t *, void *)` - pointer to a signal-catching function.

The storage occupied by `sa_handler` and `sa_sigaction` may overlap, and a conforming application shall not use both
simultaneously.

If the argument _act_ is not a null pointer, it points to a structure specifying the action to be associated with the
specified signal. If the argument _oact_ is not a null pointer, the action previously associated with the signal is
stored in the location pointed to by the argument _oact_. If the argument _act_ is a null pointer, signal handling is
unchanged; thus, the call can be used to enquire about the current handling of a given signal. The `SIGKILL` and
`SIGSTOP` signals shall not be added to the signal mask using this mechanism; this restriction shall be enforced by the
system without causing an error to be indicated.

If the `SA_SIGINFO` flag is cleared in the `sa_flags` field of the `sigaction` structure, the `sa_handler` field
identifies the action to be associated with the specified signal. If the `SA_SIGINFO` flag is set in the `sa_flags`
field, the `sa_sigaction` field specifies a signal-catching function.

The `sa_flags` field can be used to modify the behavior of the specified signal. The following flags, defined in the
`<signal.h>` header, can be set in `sa_flags`:

* `SA_NOCLDSTOP` - Do not generate `SIGCHLD` when children stop or stopped children continue. If _sig_ is `SIGCHLD` and
the `SA_NOCLDSTOP` flag is not set in `sa_flags`, and the implementation supports the `SIGCHLD` signal, then a `SIGCHLD`
signal shall be generated for the calling process whenever any of its child processes stop and a `SIGCHLD` signal may be
generated for the calling process whenever any of its stopped child processes are continued. If _sig_ is `SIGCHLD` and
the `SA_NOCLDSTOP` flag is set in `sa_flags`, then the implementation shall not generate a `SIGCHLD` signal in this way.

* `SA_ONSTACK` - If set and an alternate signal stack has been declared with `sigaltstack()`, the signal shall be
delivered to the calling process on that stack. Otherwise, the signal shall be delivered on the current stack.

* `SA_RESETHAND` - If set, the disposition of the signal shall be reset to `SIG_DFL` and the `SA_SIGINFO` flag shall be
cleared on entry to the signal handler. `SIGILL` and `SIGTRAP` cannot be automatically reset when delivered; the system
silently enforces this restriction. Otherwise, the disposition of the signal shall not be modified on entry to the
signal handler. In addition, if this flag is set, `sigaction()` may behave as if the `SA_NODEFER` flag were also set.

* `SA_RESTART` - This flag affects the behavior of interruptible functions; that is, those specified to fail with
`errno` set to `EINTR`. If set, and a function specified as interruptible is interrupted by this signal, the function
shall restart and shall not fail with `EINTR` unless otherwise specified. If an interruptible function which uses a
timeout is restarted, the duration of the timeout following the restart is set to an unspecified value that does not
exceed the original timeout value. If the flag is not set, interruptible functions interrupted by this signal shall fail
with `errno` set to `EINTR`.

* `SA_SIGINFO` - If cleared and the signal is caught, the signal-catching function shall be entered as
`void func(int signo);`, where _signo_ is the only argument to the signal-catching function. In this case, the
application shall use the `sa_handler` member to describe the signal-catching function and the application shall not
modify the `sa_sigaction` member. If `SA_SIGINFO` is set and the signal is caught, the signal-catching function shall
be entered as `void func(int signo, siginfo_t *info, void *context);`, where two additional arguments are passed to the
signal-catching function. The second argument shall point to an object of type `siginfo_t` explaining the reason why
the signal was generated; the third argument can be cast to a pointer to an object of type `ucontext_t` to refer to the
receiving thread's context that was interrupted when the signal was delivered. In this case, the application shall use
the `sa_sigaction` member to describe the signal-catching function and the application shall not modify the
`sa_handler` member. The `si_signo` member contains the system-generated signal number. The `si_errno` member may
contain implementation-defined additional error information; if non-zero, it contains an error number identifying the
condition that caused the signal to be generated. The `si_code` member contains a code identifying the cause of the
signal.

* `SA_NOCLDWAIT` - If _sig_ does not equal `SIGCHLD`, the behavior is unspecified. Otherwise, the child processes of the
calling process shall not be transformed into zombie processes when they terminate.

* `SA_NODEFER` - If set and _sig_ is caught, _sig_ shall not be added to the thread's signal mask on entry to the signal
handler unless it is included in `sa_mask`. Otherwise, _sig_ shall always be added to the thread's signal mask on entry
to the signal handler.

When a signal is caught by a signal-catching function installed by `sigaction()`, a new signal mask is calculated and
installed for the duration of the signal-catching function (or until a call to either `sigprocmask()` or `sigsuspend()`
is made). This mask is formed by taking the union of the current signal mask and the value of the `sa_mask` for the
signal being delivered, and unless `SA_NODEFER` or `SA_RESETHAND` is set, then including the signal being delivered. If
and when the user's signal handler returns normally, the original signal mask is restored.

Once an action is installed for a specific signal, it shall remain installed until another action is explicitly
requested (by another call to `sigaction()`), until the `SA_RESETHAND` flag causes resetting of the handler, or until
one of the `exec` functions is called.

If the previous action for _sig_ had been established by `signal()`, the values of the fields returned in the structure
pointed to by _oact_ are unspecified, and in particular `oact->sa_handler` is not necessarily the same value passed to
`signal()`. However, if a pointer to the same structure or a copy thereof is passed to a subsequent call to
`sigaction()` via the _act_ argument, handling of the signal shall be as if the original call to `signal()` were
repeated.

If `sigaction()` fails, no new signal handler is installed.

It is unspecified whether an attempt to set the action for a signal that cannot be caught or ignored to `SIG_DFL` is
ignored or causes an error to be returned with `errno` set to `EINVAL`.

If `SA_SIGINFO` is not set in `sa_flags`, then the disposition of subsequent occurrences of _sig_ when it is already
pending is implementation-defined; the signal-catching function shall be invoked with a single argument. If
`SA_SIGINFO` is set in `sa_flags`, then subsequent occurrences of _sig_ generated by `sigqueue()` or as a result of any
signal-generating function that supports the specification of an application-defined value (when _sig_ is already
pending) shall be queued in FIFO order until delivered or accepted; the signal-catching function shall be invoked with
three arguments. The application specified value is passed to the signal-catching function as the `si_value` member of
the `siginfo_t` structure.

The result of the use of `sigaction()` and a `sigwait()` function concurrently within a process on the same signal is
unspecified.

## Return value

Upon successful completion, `sigaction()` shall return `0`; otherwise, `-1` shall be returned, `errno` shall be set to
indicate the error, and no new signal-catching function shall be installed.

## Errors

The `sigaction()` function shall fail if:

* `EINVAL` - The _sig_ argument is not a valid signal number or an attempt is made to catch a signal that cannot be
caught or ignore a signal that cannot be ignored.

The `sigaction()` function may fail if:

* `EINVAL` - An attempt was made to set the action to `SIG_DFL` for a signal that cannot be caught or ignored (or both).

## POSIX deviations

Job control is not supported: `SIGSTOP`, `SIGTSTP`, `SIGTTIN` and `SIGTTOU` do not stop the process and `SIGCONT` does
not continue it (see the deviations of `kill()`). Child processes are never stopped or continued, so `SIGCHLD` is
generated only when a child process terminates, regardless of the `SA_NOCLDSTOP` flag. Stopping and continuing
processes is outside the scope of the lightweight system, which is aimed at embedded devices.
