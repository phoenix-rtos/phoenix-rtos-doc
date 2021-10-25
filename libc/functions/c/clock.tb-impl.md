###Synopsis

`#include <time.h>`

`clock_t clock(void);`

###Description

The function reports CPU time used.

Arguments:
None

The `clock()` function returns an approximation to the processor time used by the process since the beginning of an implementation-defined era related only to the process invocation.

It should be called at the start of the program and its return value subtracted from the value returned by subsequent calls. The value returned by `clock()` is defined for compatibility across systems that have clocks with different resolutions. The resolution on any particular system need not be to microsecond accuracy.

###Return value

The elapsed processor time (as measured in clock ticks) since the beginning of the program execution. 
To determine this time in seconds the value returned by `clock()` should be divided by the value of the macro `CLOCKS_PER_SEC`, which is defined to be one million in <`time.h`>. If the processor time used is not available or its value cannot be represented, the function shall return the value `(clock_t)-1`.

###Errors

No errors are defined.

###Implementation tasks

1. add the definition of `CLOCKS_PER_SEC` into <`time.h`>,
2. create the implementation of the `clock()` function. 


