# Synopsis

`#include <time.h>`

`char *ctime(const time_t *clock);`

`char *ctime_r(const time_t *clock, char *buf);`

## Description

The `ctime()` function converts the time pointed to by _clock_, representing time in seconds since the Epoch, to
local time in the form of a string. It is equivalent to:

`asctime(localtime(clock))`.

Arguments:
_clock_ - time in seconds since the Epoch.
_buf_ - the buffer to which the string representing local time is put.

The `ctime()` function returns value in an array of characters. It is not thread-safe.

The `ctime_r()` function converts the calendar time pointed to by _clock_ to local time in exactly the same form as
`ctime()` and puts the string into the 32 bytes array pointed to by _buf_. It returns _buf_.

Unlike `ctime()`, the `ctime_r()` function does not set `tzname`.

These functions are included only for compatibility with older implementations. They have undefined behavior if the
resulting string is too long, so the use of them is discouraged. Also, these functions do not support localized date
and time formats. To avoid these problems, applications should use `strftime()` to generate strings from broken-down
times.

Values for the broken-down time structure can be obtained by calling `gmtime()` or `localtime()`.

The `ctime_r()` function is thread-safe and returns values in a user-supplied buffer instead of possibly using a static
data area that may be overwritten by each call.

Attempts to use `ctime()` or `ctime_r()` for times before the Epoch or for times beyond the year `9999` produce
undefined results. Refer to `asctime()`.

These functions may be removed in a future version.

## Return value

The `ctime()` function returns the pointer returned by `asctime()` with that broken-down time as an argument.

Upon successful completion, `ctime_r()` returns a pointer to the string pointed to by _buf_. When an error is
encountered, a null pointer is returned.

## Errors

No errors are defined.

## Implementation tasks

* Add environment parsing for setting timezone and daylight.
