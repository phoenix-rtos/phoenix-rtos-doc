# Synopsis

`#include <stdlib.h>`

`void qsort(void *base, size_t _nel_, size_t width, int (*_compar_)(const void *, const void *));`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `qsort()` function shall sort an array of _nel_ objects, the initial element of which is pointed to by _base_.
The size of each object, in bytes, is specified by the _width_ argument. If the _nel_ argument has the value zero,
the comparison function pointed to by _compar_ shall not be called and no rearrangement shall take place.

The application shall ensure that the comparison function pointed to by _compar_ does not alter
the contents of the array.

The implementation may reorder elements of the array between calls to the comparison function, but shall not alter the
contents of any individual element.

When the same objects (consisting of _width_ bytes, irrespective of their current positions in the array) are passed
more than once to the comparison function, the results shall be consistent with one another. That is, they shall
define a total ordering on the array.

The contents of the array shall be sorted in ascending order according to a comparison function. The _compar_
argument is a pointer to the comparison function, which is called with two arguments that point to the elements being
compared. The application shall ensure that the function returns an integer less than, equal to, or greater than
`0`, if the first argument is considered respectively less than, equal to, or greater than the second. If two members
compare as equal, their order in the sorted array is unspecified.

## Return value

The `qsort()` function shall not return a value.

## Errors

No errors are defined.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
