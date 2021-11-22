# Synopsis 

`#include <time.h>`</br>

`time_t time(time_t *tloc);`</br>


## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description





The `time()` function shall return the value of time in seconds since the Epoch. 

The _tloc_ argument points to an area where the return value is also stored. If _tloc_ is a `null` pointer, no value is stored.



## Return value



Upon successful completion, `time()` shall return the value of time. Otherwise, `(time_t)-1` shall be returned.



## Errors



The `time()` function may fail if:

* `EOVERFLOW` - the number of seconds since the Epoch will not fit in an object of type `time_t`. </br>

## Tests

Untested

## Known bugs

None

## See Also 

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
