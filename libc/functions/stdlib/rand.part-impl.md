# rand

## Synopsis

`#include <stdlib.h>`

`int rand(void);`

`int rand_r(unsigned *seed);`

`void srand(unsigned seed);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `rand()` function shall compute a sequence of pseudo-random integers in the range `[0, RAND_MA]` with a period of
at least `232`.

 The `rand()` function need not be thread-safe.  The `rand_r()` function shall compute a sequence of pseudo-random
 integers in the range `[0, RAND_MA]`. (The value of the ``RAND_MA`` macro shall be at least `32767`.) If ``rand_r()``
 is called with the same initial value for the object pointed to by _seed_ and that object is not modified between
 successive returns and calls to `rand_r()`, the same sequence shall be generated.  The `srand()` function uses the
 argument as a seed for a new sequence of pseudo-random numbers to be returned by subsequent calls to `rand()`. If
 `srand()` is then called with the same seed value, the sequence of pseudo-random numbers shall be repeated. If `rand()`
 is called before any calls to `srand()` are made, the same sequence shall be generated as when `srand()` is first
 called with a seed value of `1`. The implementation shall behave as if no function defined in this volume of
 POSIX.1-2017 calls `rand()` or `srand()`.

## Return value

* The `rand()` function shall return the next pseudo-random number in the sequence.
* The `rand_r()` function shall return a pseudo-random integer.
* The `srand()` function shall not return a value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
