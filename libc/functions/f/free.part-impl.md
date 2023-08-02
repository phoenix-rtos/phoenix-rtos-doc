# Synopsis

`#include <stdlib.h>`

`void free(void *ptr);`

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `free()` function shall cause the space pointed to by _ptr_ to be deallocated; that is, made available for further
allocation.
If _ptr_ is a null pointer, no action shall occur. Otherwise, if the argument does not match a pointer earlier returned
by a function in `POSIX.1-2017` that allocates memory as if by `malloc()`, or if the space has been deallocated by a
call to `free()` or `realloc()`, the behavior is undefined.

Any use of a pointer that refers to freed space results in undefined behavior.

## Return value

The `free()` function shall not return a value.

## Errors

No errors are defined.

## Tests

Tested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
