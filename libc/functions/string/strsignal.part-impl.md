# strsignal

## Synopsis

`#include <string.h>`

`char *strsignal(int signum);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strsignal()` function shall map the signal number in _signum_ to an implementation-defined string and shall return
a pointer to it. It shall use the same set of messages as the `psignal()` function.

The application shall not modify the string returned. The returned pointer might be invalidated, or the string content
might be overwritten by a subsequent call to `strsignal()` or `setlocale()`. The returned pointer might also be
invalidated if the calling thread is terminated.

The contents of the message strings returned by `strsignal()` should be determined by the setting of the `LC_MESSAGES`
 category in the current locale.

The implementation shall behave as if no function defined in this standard calls `strsignal()`.

Since no return value is reserved to indicate an error, an application wishing to check for error situations should set
`errno` to `0`, then call `strsignal()`, then check `errno`.

The `strsignal()` function need not be thread-safe.

## Return value

Upon successful completion, `strsignal()` shall return a pointer to a string. Otherwise, if _signum_ is not a valid
signal number, the return value is unspecified.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None
