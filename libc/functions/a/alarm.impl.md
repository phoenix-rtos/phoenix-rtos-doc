###Synopsis
`#include <unistd.h>`

`unsigned int alarm(unsigned int seconds);`

###Description

The `alarm()` function delivers alarm (`SIGALARM`) to the calling process after number of <u>seconds</u> specified.

Arguments:
<u>seconds</u> - number of seconds to wait. 

Processor scheduling delays may prevent the process from handling the signal as soon as it is generated.
If seconds is `0`, a pending alarm request, if any, is canceled.

###Return value
If there is a previous `alarm()` request with time remaining, `alarm()` returns a non-zero value that is the number of seconds until the previous request would have generated a `SIGALRM` signal. Otherwise, `alarm()` returns `0`.

###Errors
No errors are defined.

###Comments
Alarm requests are not stacked; only one `SIGALRM` generation can be scheduled in this manner. If the `SIGALRM` signal has not yet been generated, the call shall result in rescheduling the time at which the `SIGALRM` signal is generated.

###Implementation tasks

* 

###Tests

======

###EXAMPLES
None.