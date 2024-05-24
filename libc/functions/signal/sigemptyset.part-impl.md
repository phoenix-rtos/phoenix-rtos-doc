# sigemptyset

## Synopsis

`#include <signal.h>`

`int sigemptyset(sigset_t *set);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigemptyset()` function initializes the signal set pointed to by _set_, such that all signals defined in
POSIX.1-2017 are excluded.

## Return value

Upon successful completion, `sigemptyset()` shall return `0`; otherwise, it shall return `-1` and set `errno`
to indicate the error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
