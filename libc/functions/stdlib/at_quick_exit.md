# at_quick_exit

## Synopsis

```c
#include <stdlib.h>

int at_quick_exit(void (*func)(void));
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2024

## Description

The `at_quick_exit()` function shall register the function pointed to by _func_, to be called without arguments should
`quick_exit()` be called. It is unspecified whether a call to the `at_quick_exit()` function that does not happen before
the `quick_exit()` function is called will succeed.

At least 32 functions can be registered with `at_quick_exit()`.

## Return value

Upon successful completion, `at_quick_exit()` shall return `0`; otherwise, it shall return a non-zero value.

## Errors

No errors are defined.

## POSIX deviations

No POSIX deviations discovered.
