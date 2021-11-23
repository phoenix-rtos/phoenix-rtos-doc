# Synopsis 
`#include <unistd.h>`</br>
` unsigned alarm(unsigned seconds);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The purpose is to schedule an alarm signal. The `alarm()` function shall cause the system to generate a `SIGALRM` signal for the process after the number of realtime
seconds specified by _seconds_ have elapsed. Processor scheduling delays may prevent the process from handling the signal as
soon as it is generated.

If _seconds_ is `0`, a pending alarm request, if any, is canceled.

Alarm requests are not stacked, only one `SIGALRM` generation can be scheduled in this manner. If the `SIGALRM` signal has not yet
been generated, the call shall result in rescheduling the time at which the `SIGALRM` signal is generated.

Interactions between `alarm()` and `setitimer()` are unspecified. 


## Return value

If there is a previous `alarm()` request with time remaining, `alarm()` shall return a non-zero value that is the number of seconds until the previous request would have generated a `SIGALRM` signal. Otherwise, `alarm()` shall return `0`.

## Errors


The `alarm()` function is always successful, and no return value is reserved to indicate an error.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
