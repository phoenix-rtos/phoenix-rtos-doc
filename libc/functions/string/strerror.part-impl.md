# strerror

## Synopsis

```c
#include <string.h>

char *strerror(int errnum);

char *strerror_l(int errnum, locale_t locale);

int strerror_r(int errnum, char *strerrbuf, size_t buflen);
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `strerror()` function shall map the error number in _errnum_ to a locale-dependent error message string and shall
return a pointer to it. Typically, the values for _errnum_ come from `errno`, but `strerror()` shall map any value of
type int to a message.

The application shall not modify the string returned. The returned string pointer might be invalidated, or the string
content might be overwritten by a subsequent call to `strerror()`, or by a subsequent call to `strerror_l()` in the same
thread. The returned pointer and the string content might also be invalidated if the calling thread is terminated.

The string may be overwritten by a subsequent call to `strerror_l()` in the same thread.

The contents of the error message strings returned by `strerror()` should be determined by the setting of the
`LC_MESSAGES` category in the current _locale_.

The implementation shall behave as if no function defined in this volume of POSIX.1-2017 calls `strerror()`.

The `strerror()` and `strerror_l()` functions shall not change the setting of `errno` if successful.

Since no return value is reserved to indicate an error of `strerror()`, an application wishing to check for error
situations should set `errno` to `0`, then call `strerror()`, then check `errno`. Similarly, since `strerror_l()` is
required to return a string for some errors, an application wishing to check for all error situations should set `errno`
to `0`, then call `strerror_l()`, then check `errno`.

The `strerror()` function need not be thread-safe.

The `strerror_l()` function shall map the error number in _errnum_ to a locale-dependent error message string in the
_locale_ represented by _locale_ and shall return a pointer to it.

The `strerror_r()` function shall map the error number in _errnum_ to a locale-dependent error message string and shall
return the string in the buffer pointed to by _strerrbuf_, with length _buflen_.

If the value of _errnum_ is a valid error number, the message string shall indicate what error occurred; if the value of
_errnum_ is zero, the message string shall either be an empty string or indicate that no error occurred; otherwise, if
these functions complete successfully, the message string shall indicate that an unknown error occurred.

The behavior is undefined if the _locale_ argument to `strerror_l()` is the special _locale_ object `LC_GLOBAL_LOCALE`
or is not a valid _locale_ object handle.

## Return value

Upon completion, whether successful or not, `strerror()` shall return a pointer to the generated message string. On
error `errno` may be set, but no return value is reserved to indicate an error.

Upon successful completion, `strerror_l()` shall return a pointer to the generated message string. If errnum is not a
valid error number, `errno` may be set to `[EINVAL]`, but a pointer to a message string shall still be returned. If any
other error occurs, `errno` shall be set to indicate the error and a null pointer shall be returned.

Upon successful completion, `strerror_r()` shall return `0`. Otherwise, an error number shall be returned to indicate
the error.

## Errors

These functions may fail if:

- `[EINVAL]` The value of _errnum_ is neither a valid error number nor zero.

The `strerror_r()` function may fail if:

- `[ERANGE]` Insufficient storage was supplied via _strerrbuf_ and _buflen_ to contain the generated message string.

## Tests

Tested

## Known bugs

None
