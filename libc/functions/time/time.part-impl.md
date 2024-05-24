# time

## Synopsis

`#include <time.h>`

`time_t time(time_t *tloc);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `time()` function shall return the value of time in seconds since the Epoch.

The _tloc_ argument points to an area where the return value is also stored. If _tloc_ is a `NULL` pointer, no value is
stored.

## Return value

Upon successful completion, `time()` shall return the value of time. Otherwise, `(time_t)-1` shall be returned.

## Errors

The `time()` function may fail if:

* `EOVERFLOW` - the number of seconds since the Epoch will not fit in an object of type `time_t`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../index.md)
2. [Table of Contents](../../../index.md)
