# atexit

## Synopsis

`#include <stdlib.h>`

`int atexit(void (*func)(void));`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to register a function to run at process termination. The `atexit()` function shall register the function
pointed to by _func_, to be called without arguments at normal
program termination. At normal program termination, all functions registered by the `atexit()` function shall be called,
in the reverse order of their registration, except that a function is called after any previously registered functions
that had already been called at the time it was registered. Normal termination occurs either by a call to `exit()`
or a return from `main()`.

At least 32 functions can be registered with `atexit()`.
After a successful call to any of the exec functions, any functions previously
registered by `atexit()` shall no longer be registered.

## Return value

Upon successful completion, `atexit()` shall return `0`, otherwise, it shall return a non-zero value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
