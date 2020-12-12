###Synopsis

`#include <stdlib.h>`

`void exit(int status);`

###Description

`exit()` function terminates a process.

Arguments:
    
<u>status</u> - a value returned to the system; the most popular values are `0`, `EXIT_SUCCESS`, `EXIT_FAILURE`.

There can any other value be returned, though only the least significant `8` bits (that is, `status & 0377`) are available from `wait()` and `waitpid()`; the full value is available from `waitid()` and in the `siginfo_t` passed to a signal handler for `SIGCHLD`. 

The `exit()` function first calls all functions registered by `atexit()`, in the reverse order of their registration, except that a function is called after any previously registered functions that had already been called at the time it was registered. Each function is called as many times as it was registered. If, during the call to any such function, a call to the `longjmp()` function is made that would terminate the call to the registered function, the behavior is undefined.

If a function registered by a call to `atexit()` fails to return, the remaining registered functions are not called and the rest of the `exit()` processing is not completed. If `exit()` is called more than once, the behavior is undefined.

The `exit()` function flushes all open streams with unwritten buffered data and close all open streams. Finally, the process is terminated. 

###Return value

The `exit()` function does not return.

###Errors

No errors are defined.

###Implementation tasks

* None
