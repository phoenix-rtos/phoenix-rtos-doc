# Synopsis 
`#include <string.h>`</br>

`char *strpbrk(const char *s1, const char *s2);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `strpbrk()` function shall locate the first occurrence in the string pointed to by _s1_ of any byte from the
string pointed to by _s2_.


## Return value


Upon successful completion, `strpbrk()` shall return a pointer to the byte or a `null` pointer if no byte from _s2_
occurs in _s1_.


## Errors


No errors are defined.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
