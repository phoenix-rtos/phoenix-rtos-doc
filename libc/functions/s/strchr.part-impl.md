# Synopsis 
`#include <string.h>`</br>

`char *strchr(const char *s, int c);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The `strchr()` function shall locate the first occurrence of _c_ (converted to a char) in the string pointed to
by _s_. The terminating `NUL` character is considered to be part of the string.


## Return value


Upon completion, `strchr()` shall return a pointer to the byte, or a `null` pointer if the byte was not found.


## Errors


No errors are defined.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
