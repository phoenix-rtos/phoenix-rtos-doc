# sigfillset

## Synopsis

`#include <signal.h>`

`int sigfillset(sigset_t *set);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sigfillset()` function shall initialize the signal set pointed to by _set_, such that all signals defined in this
volume of POSIX.1-2017 are included.

## Return value

Upon successful completion, `sigfillset()` shall return `0`; otherwise, it shall return `-1` and set `errno` to indicate
the error.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../functions.md)
2. [Table of Contents](../../../README.md)
