# realloc

## Synopsis

`#include <stdlib.h>`

`void *realloc(void *ptr, size_t size);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `realloc()` function shall deallocate the old object pointed to by _ptr_ and return a pointer to a new object that
has the size specified by _size_. The contents of the new object shall be the same as that of the old object prior to
deallocation, up to the least of the new and old sizes. Any bytes in the new object beyond the size of the old object
have indeterminate values. If the _size_ of the space requested is zero, the behavior shall be implementation-defined:
either a `null` pointer is returned, or the behavior shall be as if the size were some non-zero value, except that the
behavior is undefined if the returned pointer is used to access an object. If the space cannot be allocated, the object
shall remain unchanged.

If _ptr_ is a `null` pointer, `realloc()` shall be equivalent to `malloc()` for the specified _size_.

If _ptr_ does not match a pointer returned earlier by `calloc()`, `malloc()`, or `realloc()` or if the space has
previously been deallocated by a call to `free()` or `realloc()`, the behavior is undefined.

The order and contiguity of storage allocated by successive calls to `realloc()` is unspecified. The pointer returned if
the allocation succeeds shall be suitably aligned so that it may be assigned to a pointer to any type of object and then
used to access such an object in the space allocated (until the space is explicitly freed or reallocated). Each such
allocation shall yield a pointer to an object disjoint from any other object. The pointer returned shall point to the
start (the lowest byte address) of the allocated space. If the space cannot be allocated, a `null`
pointer shall be returned.

## Return value

Upon successful completion, `realloc()` shall return a pointer to the (possibly moved) allocated space. If size is `0`,
either:

* A `null` pointer shall be returned and, if _ptr_ is not a `null` pointer, errno shall be set to an
implementation-defined value.

* A pointer to the allocated space shall be returned, and the memory object pointed to by _ptr_ shall be freed.
The application shall ensure that the pointer is not used to access an object.

If there is not enough available memory, `realloc()` shall return a `null` pointer and set
errno to `ENOMEM`.  If `realloc()` returns a `null`
pointer and `errno` has been set to `ENOMEM`, the
memory referenced by _ptr_ shall not be changed.

## Errors

The `realloc()` function shall fail if:

* `ENOMEM` - Insufficient memory is available.

## Tests

Untested

## Known bugs

None
