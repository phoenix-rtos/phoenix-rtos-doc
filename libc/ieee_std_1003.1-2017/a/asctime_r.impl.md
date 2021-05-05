###Synopsis
`#include <time.h>`

`char *asctime_r(const struct tm *timeptr, char *buf);`

###Description

The `asctime_r` function shall convert the broken-down time in the structure pointed to by timeptr into a string in the form:

Sun Sep 16 01:03:52 1973\n\0
The resulting string is placed in the user-supplied buffer pointed to by buf (which shall contain at least 26 bytes).

Arguments:
<u>timeptr</u> - a pointer to a structure with the broken-down time.

The behavior is undefined if timeptr->tm_wday or timeptr->tm_mon are not within the normal ranges as defined in <time.h>, or if timeptr->tm_year exceeds {INT_MAX}-1990, or if the above algorithm would attempt to generate more than 26 bytes of output (including the terminating NULL).

###Return value

Upon successful completion, the `asctime` function shall return a pointer to the string which is also placed in buf.
If the function is unsuccessful, it shall return NULL.

###Errors
No errors are defined.
