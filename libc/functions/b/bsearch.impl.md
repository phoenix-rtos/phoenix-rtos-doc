# Synopsis

`#include <stdlib.h>`

`void *bsearch(const void *key, const void *base, size_t nitems, size_t size,
int (*compar)(const void *, const void *));`

## Description

The function searches an ascending order array (with binary search) for an element with specified value.

Arguments:
_key_ - a value to be found,
_base_ - a pointer to the beginning of array area to be searched,
_nitems_ - the number of array elements,
_size_ - the number of bytes taken by each element,
_compar_ - the comparison function.

Function searches an array of _nitems_ objects, the initial member of which is pointed to by _base_, for a
member that matches the object pointed to by _key_.  The size (in bytes) of each member of the array is specified
by _size_.

The contents of the array should be in ascending sorted order according to the comparison function referenced by
`compar`.  The `compar` routine is expected to have two arguments that point to the key object and to an array member,
in that order.  It should return an integer that is less than, equal to, or greater than zero if the key object is
found, respectively, to be less than, to match, or be greater than the array member.

### Return value

The function returns a pointer to a matching member of the array, or a null pointer if no match is found.  
If two members compare as equal, which member is matched is unspecified.

### Errors

No errors are defined.
