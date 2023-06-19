# Zone allocator

Zone allocator is used to allocate memory inside the allocated pages mapped into the address space. The main idea of
this allocator is to allocate the memory area and divide it into similar chunks aligned to their size. Zone allocator
is used when equal fragments of memory should be allocated dynamically with minimum processing overhead. The good use
case is allocation of network buffer headers.

Each zone used for allocation is described using `vm_zone_t` header.

```c
    typedef struct _vm_zone_t {
        struct _vm_zone_t *next;
        struct _vm_zone_t *prev;
        rbnode_t linkage;
        size_t blocksz;
        volatile unsigned int blocks;
        volatile unsigned int used;
        void *vaddr;
        void *first;
        page_t *pages;
    } vm_zone_t;
```

For purposes of fine-grained allocator (described in the next chapter) zones are linked using the `next` and `prev`
attributes. Attribute `linkage` is used for adding zone headers into the red-black tree used by fine-grained allocator
for memory deallocation. Attributes `blocksz` and `blocks` define the chunk size and number of chunks in the zone.
Attribute `used` stores the number of chunks already allocated. Virtual address at which page set is mapped is pointed
by `vaddr`. The first page descriptor of pages sets constituting the zone is pointed by `pages` attribute. Attribute
`first` points the first free chunk in the zone.

## Chunk allocation

Functions used for chunk allocations are presented below.

```c
extern int _vm_zoneCreate(vm_zone_t *zone, size_t blocksz, unsigned int blocks);
```

Function creates the new zone containing the `blocks` number of blocks. The size of single block is given by `blocksz`
argument. During the zone creation a new page set is allocated and mapped into the kernel address space. The address of
the mapping is returned to the zone header given by `zone` pointer. The final number of blocks in the zone can be
greater than requested (because of the allocation with the page size granulation). The final block size can be greater
than requested because block size should be aligned.

```c
extern int _vm_zoneDestroy(vm_zone_t *zone);
```

Function destroys zone given by the argument.

```c
extern void *_vm_zalloc(vm_zone_t *zone, addr_t *addr);
```

Function allocates bucket of memory from zone given by `zone`. The `addr` stores the physical address of allocated
bucket.

```c
extern void _vm_zfree(vm_zone_t *zone, void *vaddr);
```

## See also

1. [Kernel - Memory management](README.md)
2. [Kernel - Memory management - Page allocator](page.md)
3. [Kernel - Memory management - Memory mapper](mapper.md)
4. [Kernel - Memory management - Fine grained allocator](kmalloc.md)
5. [Kernel - Memory management - Memory objects](objects.md)
6. [Table of Contents](../../README.md)
