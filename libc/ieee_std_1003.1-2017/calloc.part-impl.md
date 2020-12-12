###Synopsis

`#include <stdlib.h>`

`void *calloc(size_t nitems, size_t size);`

###Description

The function allocates memory.

Arguments:
<u>nitems</u> -  a number of items to allocate,
<u>size</u> - an item size.

The function allocates <u>nitems</u> of <u>size</u> bytes of memory and returns a pointer to the allocated memory. The allocated memory is aligned such that it can be used for any data type, including AltiVec- and SSE-related types. The allocated memory is filled with bytes of value zero.

###Return value
The allocated memory address on success, `NULL` otherwise.

###Errors

[`ENOMEM`] - insufficient memory is available.

###Implementation tasks

* `ENOMEM` error sygnalling.

###Tests

======

###EXAMPLES
None.
