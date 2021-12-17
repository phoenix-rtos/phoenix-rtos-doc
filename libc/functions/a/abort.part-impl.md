# Synopsis 
`#include <stdlib.h>`</br>

` void abort(void);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The purpose is to generate an abnormal process abort. The `abort()` function shall cause abnormal process termination to occur, unless the signal `SIGABRT` is being caught and the signal handler does not return.
The abnormal termination processing shall include the default actions defined for `SIGABRT` and may include an attempt to effect `fclose()` on all open streams. 
The `SIGABRT` signal shall be sent to the calling process as if by means of `raise()` with the argument `SIGABRT`.
The status made available to `wait()`, `waitid()`, or `waitpid()` by `abort()` shall be that of a process terminated by the `SIGABRT` signal.  The
`abort()` function shall override blocking or ignoring the `SIGABRT` signal.


## Return value

The `abort()` function shall not return.

## Errors


No errors are defined.




## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
