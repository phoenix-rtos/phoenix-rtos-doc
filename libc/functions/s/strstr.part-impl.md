# Synopsis 
`#include <string.h>`</br>

` char *strstr(const char *s1, const char *s2);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `strstr()` function shall locate the first occurrence in the string pointed to by _s1_ of the sequence of bytes
(excluding the terminating NUL character) in the string pointed to by _s2_.


## Return value


Upon successful completion, `strstr()` shall return a pointer to the located string or a `null` pointer if the string is not
found.
If _s2_ points to a string with zero length, the function shall return _s1_.


## Errors


No errors are defined.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
