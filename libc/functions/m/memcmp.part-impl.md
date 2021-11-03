# Synopsis 
`#include <string.h>`</br>
` int memcmp(const void *s1, const void *s2, size_t n);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description

The `memcmp()` function shall compare the first _n_ bytes (each interpreted as unsigned char) of the object
pointed to by _s1_ to the first _n_ bytes of the object pointed to by _s2_.

The sign of a non-zero return value shall be determined by the sign of the difference between the values of the first pair of
bytes (both interpreted as type unsigned char) that differ in the objects being compared.


## Return value


The `memcmp()` function shall return an integer greater than, equal to, or less than `0`, if the object pointed to by
_s1_ is greater than, equal to, or less than the object pointed to by _s2_, respectively.


## Errors


No errors are defined.




## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
