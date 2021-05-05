### Synopsis

`#include <sys/mm.h>`

`int munmap(void *vaddr, size_t size);`

###Conformance
IEEE Std 1003.1-2001

### Description
Deletes the mappings for the specified address range, causing further references to addresses within the range to generate invalid memory references.

### Return value

### Errors