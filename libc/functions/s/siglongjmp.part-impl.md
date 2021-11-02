# Synopsis 
`#include <setjmp.h>`</br>
` void siglongjmp(sigjmp_buf env, int val); `</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `siglongjmp()` function shall be equivalent to the `longjmp()` function,
except as follows:



* References to `setjmp()` shall be equivalent to `sigsetjmp()`.





* The `siglongjmp()` function shall restore the saved signal mask if and only if the env argument was initialized by a call to `sigsetjmp()` with a non-zero savemask argument.





## Return value


After `siglongjmp()` is completed, program execution shall continue as if the corresponding invocation of `sigsetjmp()` had just returned the value specified by _val_. The `siglongjmp()`
function shall not cause `sigsetjmp()` to return `0`; if _val_ is `0`, `sigsetjmp()` shall return the value `1`.


## Errors


No errors are defined.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
