###Synopsis

`#include <stdlib.h>`

`int atexit(void (*func)(void));`

###Description

Function causes the specified function `func` to be called when the program terminates normally.

Arguments:
<u>func</u>  - a function to be called without arguments when the program terminates normally.

The `atexit()` function registers the function pointed to by <u>func</u>, to be called without arguments at normal program termination. At normal program termination, all functions registered by the `atexit()` function are called, in the reverse order of their registration, except that a function is called after any previously registered functions that had already been called at the time it was registered. Normal termination occurs either by a call to `exit()` or a return from `main()`.

After a successful call to any of the `exec` functions, any functions previously registered by `atexit()` are no longer registered.

The functions registered by a call to `atexit()` must return to ensure that all registered functions are called.

###Return value
Upon successful completion, `atexit()` returns `0`; otherwise, it returns `-1`.

###Errors
No errors are defined.

###Comments

The application calls `sysconf()` to obtain the value of {`ATEXIT_MAX`}, the number of functions that can be registered. There is no way for an application to tell how many functions have already been registered with `atexit()`.
Since the behavior is undefined if the `exit()` function is called more than once, portable applications calling `atexit()` must ensure that the `exit()` function is not called at normal process termination when all functions registered by the `atexit()` function are called.
All functions registered by the `atexit()` function are called at normal process termination, which occurs by a call to the `exit()` function or a return from `main()` or on the last thread termination, when the behavior is as if the implementation called `exit()` with a zero argument at thread termination time.
If, at normal process termination, a function registered by the `atexit()` function is called and a portable application needs to stop further `exit()` processing, it must call the `_exit()` function or the `_Exit()` function or one of the functions which cause abnormal process termination.
