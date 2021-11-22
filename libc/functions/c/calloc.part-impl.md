# Synopsis 
`#include <stdlib.h>`</br>

` void *calloc(size_t nelem, size_t elsize);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description


The purpose is to allocate a memory. The `calloc()` function shall allocate unused space for an array of _nelem_ elements each of whose size in bytes is
_elsize_. The space shall be initialized to all bits `0`.

The order and contiguity of storage allocated by successive calls to `calloc()` is unspecified. The pointer returned if the
allocation succeeds shall be suitably aligned so that it may be assigned to a pointer to any type of object and then used to access
such an object or an array of such objects in the space allocated (until the space is explicitly freed or reallocated). Each such
allocation shall yield a pointer to an object disjoint from any other object. The pointer returned shall point to the start (lowest
byte address) of the allocated space. If the space cannot be allocated, a `null` pointer shall be returned. If the size of the space
requested is `0`, the behavior is implementation-defined: either a `null` pointer shall be returned, or the behavior shall be as if the
size were some non-zero value, except that the behavior is undefined if the returned pointer is used to access an object.


## Return value


Upon successful completion with both _nelem_ and _elsize_ non-zero, `calloc()` shall return a pointer to the allocated space. If either _nelem_ or _elsize_ is `0`, then either:

* A `null` pointer shall be returned and `errno` may be set to an implementation-defined value, or

* A pointer to the allocated space shall be returned. The application shall ensure that the pointer is not used to access an object.

Otherwise, it shall return a `null` pointer and set `errno` to indicate the error.

## Errors


The `calloc()` function shall fail if:


 * `ENOMEM` - Insufficient memory is available. 


## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
