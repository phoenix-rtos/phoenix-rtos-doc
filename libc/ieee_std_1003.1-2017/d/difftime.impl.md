###Synopsis

`#include <time.h>`

`double difftime(time_t time1, time_t time0);`

###Description

The `difftime()` function computes the difference between two calendar times (as returned by `time()`): <u>time1</u>- <u>time0</u>.

Arguments:
<u>time1</u> - time in seconds since the Epoch.
<u>time2</u> - the buffer to which the string representing local time is put.
 
###Return value

The `difftime()` function returns the difference expressed in seconds.

###Errors

No errors are defined.

