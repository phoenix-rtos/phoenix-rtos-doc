# Synopsis 
`#include <stdio.h>`</br>

` void setbuf(FILE *restrict stream, char *restrict buf);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description

The purpose is to assign buffering to a stream.

Except that it returns no value, the function call:

`setbuf(stream, buf)`

shall be equivalent to:

`setvbuf(stream, buf, _IOFBF, BUFSIZ)`

if _`buf`_ is not a `null` pointer, or to:

`setvbuf(stream, buf, _IONBF, BUFSIZ)`s

if _`buf`_ is a `null` pointer.


## Return value

The `setbuf()` function shall not return a value.


## Errors


Although the `setvbuf()` interface may set errno in defined ways, the value
of `errno` after a call to `setbuf()` is unspecified.


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
