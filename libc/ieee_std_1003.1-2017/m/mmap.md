###Synopsis

`#include <sys/mm.h>`

`void *mmap(void *vaddr, size_t size, int prot, int flags, oid_t *oid, offs_t offs);`

###Description

Function maps part ot the object identified by `oid` into the main process address space at address given by `vaddr`.