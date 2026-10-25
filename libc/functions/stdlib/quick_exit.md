# quick_exit

## Synopsis

```c
#include <stdlib.h>

_Noreturn void quick_exit(int status);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

The `quick_exit()` function shall cause normal process termination to occur. It shall not call functions registered
with `atexit()` nor any registered signal handlers. If a process calls the `quick_exit()` function more than once, or
calls the `exit()` function in addition to the `quick_exit()` function, the behavior is undefined. If a signal is raised
while the `quick_exit()` function is executing, the behavior is undefined.

The `quick_exit()` function shall first call all functions registered by `at_quick_exit()`, in the reverse order of
their registration, except that a function is called after any previously registered functions that had already been
called at the time it was registered. If, during the call to any such function, a call to the `longjmp()` or
`siglongjmp()` function is made that would terminate the call to the registered function, the behavior is undefined.

If a function registered by a call to `at_quick_exit()` fails to return, the remaining registered functions shall not
be called and the rest of the `quick_exit()` processing shall not be completed.

Finally, the `quick_exit()` function shall terminate the process as if by a call to `_Exit(status)`.

## Return value

The `quick_exit()` function does not return.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
