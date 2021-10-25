###Synopsis

`#include <stdlib.h>`

`void *bsearch(const void *key, const void *base, size_t nitems, size_t size, int (*compar)(const void *, const void *));`

###Description

The function searches an ascending order array (with binary search) for an element with specified value.

Arguments:
<u>key</u> - a value to be found,
<u>base</u> - a pointer to the beginning of array area to be searched,
<u>nitems</u> - the number of array elements,
<u>size</u> - the number of bytes taken by each element,
<u>compar</u> - the comparison function.

Function searches an array of <u>nitems</u> objects, the initial member of which is pointed to by <u>base</u>, for a member that matches the object pointed to by <u>key</u>.  The size (in bytes) of each member of the array is specified by <u>size</u>.

The contents of the array should be in ascending sorted order according to the comparison function referenced by `compar`.  The `compar` routine is expected to have two arguments which point to the key object and to an array member, in that order.  It should return an integer which is less than, equal to, or greater than zero if the key object is found, respectively, to be less than, to match, or be greater than the array member.

###Return value

The function returns a pointer to a matching member of the array, or a null pointer if no match is found.  
If two members compare as equal, which member is matched is unspecified.

###Errors

No errors are defined.