# Synopsis 
`#include <string.h>`</br>
` void *memmove(void *s1, const void *s2, size_t n);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `memmove()` function shall copy _n_ bytes from the object pointed to by _s2_ into the object pointed to by
_s1_. Copying takes place as if the _n_ bytes from the object pointed to by _s2_ are first copied into a temporary
array of _n_ bytes that does not overlap the objects pointed to by _s1_ and _s2_, and then the _n_ bytes from
the temporary array are copied into the object pointed to by _s1_.


## Return value


The `memmove()` function shall return _s1_; no return value is reserved to indicate an error.


## Errors


No errors are defined.




## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
