# pause

## Synopsis

```c
#include <unistd.h>

int pause(void);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `pause()` function shall suspend the calling thread until delivery of a signal whose action is either to execute a
signal-catching function or to terminate the process.

If the action is to terminate the process, `pause()` shall not return.

If the action is to execute a signal-catching function, `pause()` shall return after the signal-catching function
returns.

The `pause()` function is equivalent to `sigsuspend()` called with the current signal mask of the calling thread.

## Return value

Since `pause()` suspends thread execution indefinitely unless interrupted by a signal, there is no successful completion
return value. A value of `-1` shall be returned and `errno` set to indicate the error.

## Errors

The `pause()` function shall fail if:

* `EINTR` - A signal is caught by the calling process and control is returned from the signal-catching function.

## POSIX deviations

No POSIX deviations discovered.
