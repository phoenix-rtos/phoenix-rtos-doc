# asctime

## Synopsis

`#include <time.h>`

`char *asctime(const struct tm *timeptr);`

`char *asctime_r(const struct tm *restrict tm, char *restrict buf);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `asctime()` function shall convert the broken-down time in the structure pointed to by _timeptr_ into a string in
the form:

`Sun Sep 16 01:03:52 1973\n\0`

using the equivalent of the following algorithm:

```c
char *asctime(const struct tm *timeptr)
{
	static char wday_name[7][3] = {
		"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"
	};
	static char mon_name[12][3] = {
		"Jan", "Feb", "Mar", "Apr", "May", "Jun",
		"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
	};
	static char result[26];

	sprintf(result, "%.3s %.3s%3d %.2d:%.2d:%.2d %d\n",
		wday_name[timeptr->tm_wday],
		mon_name[timeptr->tm_mon],
		timeptr->tm_mday, timeptr->tm_hour,
		timeptr->tm_min, timeptr->tm_sec,
		1900 + timeptr->tm_year);
	return result;
}
```

However, the behavior is undefined if `timeptr->tm_wday` or `timeptr->tm_mon` are not within the
normal ranges as defined in `<time.h>`, or if `timeptr->tm_year`
exceeds `INT_MAX-1990,` or if the above algorithm would attempt to generate more than 26 bytes of output (including
the terminating `null`).

The _tm_ structure is defined in the `<time.h>` header.
The
`asctime()`, `ctime()`, `gmtime()`, and
`localtime()` functions shall return values in one of two static objects: a
broken-down time structure and an array of type `char`. Execution of the functions may overwrite the information
returned in either of these objects by any of the other functions.

The `asctime()` function need not be thread-safe.

The `asctime_r()` function shall convert the broken-down time in the structure pointed to by _tm_ into a string (of
the same form as that returned by `asctime()`, and with the
same undefined behavior when input or output is out of range)
that is placed in the user-supplied buffer pointed to by _buf_ (which shall contain at least 26 bytes)
and then return _buf_.

## Return value

Upon successful completion, `asctime()` shall return a pointer to the string. If the function is unsuccessful,
it shall return `NULL`.

Upon successful completion, `asctime_r()` shall return a pointer to a character string containing the date and time.
This string is pointed to by the argument _buf_. If the function is unsuccessful, it shall return `NULL`.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
