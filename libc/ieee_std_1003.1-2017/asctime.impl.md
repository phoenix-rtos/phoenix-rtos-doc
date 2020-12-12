###Synopsis
`#include <time.h>`

`char *asctime(const struct tm *timeptr);`

`char *asctime_r(const struct tm *timeptr, char *buf);`

###Description

The `asctime` function converts the broken-down time in the structure pointed to by <u>timeptr</u> into a string in the form:

`Thu Mar 26 13:03:52 2020\n\0`

The `asctime_r()` function converts the broken-down time in the structure pointed to by <u>timeptr</u> into a string (of the same form as that returned by `asctime()`, and with the same undefined behavior when input or output is out of range) that is placed in the user-supplied buffer pointed to by <u>buf</u> (which contains at least `26` bytes) and then return <u>buf</u>. 

Arguments:
<u>timeptr</u> - a pointer to a structure with the broken-down time.

<u>buf</u> - a buffer to save the resulting string.

The behavior is undefined if <u>timeptr</u>->tm_wday or <u>timeptr</u>->tm_mon are not within the normal ranges as defined in <`time.h`>, or if <u>timeptr</u>->tm_year exceeds {`INT_MAX`}-`1990`, or if the above algorithm would attempt to generate more than `26` bytes of output (including the terminating `NULL`).

###Return value

Upon successful completion, the `asctime()` function returns a pointer to the string.
If the function is unsuccessful, it returns `NULL`.

Upon successful completion, `asctime_r()` returns a pointer to a character string containing the date and time. This string is also pointed to by the argument <u>buf</u>. If the function is unsuccessful, it returns `NULL`. 

###Errors
No errors are defined.

###Comments
The `asctime()` and `asctime_r()` functions may be removed in a future version.


