# Synopsis

`#include <stdlib.h>`

`void *malloc(size_t size);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `malloc()` function shall allocate unused space for an object whose size in bytes is specified by _size_ and whose
value is unspecified.

The order and contiguity of storage allocated by successive calls to `malloc()` is unspecified. The pointer returned if
the allocation succeeds shall be suitably aligned so that it may be assigned to a pointer to any type of object and then
used to access such an object in the space allocated (until the space is explicitly freed or reallocated). Each such
allocation shall yield a pointer to an object disjoint from any other object. The pointer returned points to the start
(lowest byte address) of the allocated space. If the space cannot be allocated, a null pointer shall be returned. If the
_size_ of the space requested is `0`, the behavior is implementation-defined: either a null pointer shall be returned,
or the behavior shall be as if the _size_ were some non-zero value, except that the behavior is undefined if the
returned pointer is used to access an object.

## Return value

Upon successful completion with _size_ not equal to `0`, `malloc()` shall return a pointer to the allocated space.

If _size_ is 0, either:

* A null pointer shall be returned    and `errno` may be set to an implementation-defined value,  or
* A pointer to the allocated space shall be returned. The application shall ensure that the pointer is not used to
access an object.

Otherwise, it shall return a null pointer and set `errno` to indicate the error.

## Errors

The `malloc()` function shall fail if:

* `ENOMEM` - Insufficient storage space is available.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
