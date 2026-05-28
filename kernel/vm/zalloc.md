# Zone allocator

The zone allocator allocates fixed-size blocks from a page-backed area. It is used directly by kernel code that needs
many objects of the same size and indirectly by the kernel `vm_kmalloc()` allocator.

Each zone is described by `vm_zone_t`, declared in `vm/zone.h`.

| Field | Meaning |
| --- | --- |
| `next`, `prev` | Links used by the kmalloc size-class lists. |
| `linkage` | Red-black tree node used to find a zone by block address. |
| `blocksz` | Aligned block size. |
| `blocks` | Number of blocks in the zone. |
| `used` | Number of allocated blocks. |
| `vaddr` | Kernel virtual address where zone pages are mapped. |
| `first` | First free block. |
| `pages` | First page descriptor backing the zone. |

## API

```{function} int _vm_zoneCreate(vm_zone_t *zone, size_t blocksz, unsigned int blocks)

Creates a zone, allocates backing pages, maps them into the kernel map, and initializes the free-block list.

:param zone: Zone descriptor to initialize.
:param blocksz: Requested block size.
:param blocks: Requested number of blocks.
:returns: `EOK` on success or a negative error code.
```

The final block size can be larger than `blocksz` because it is aligned. The final number of blocks can be larger than
`blocks` because the backing allocation is page-sized.

```{function} int _vm_zoneDestroy(vm_zone_t *zone)

Destroys a zone and returns its backing pages to the page allocator.

:param zone: Zone to destroy.
:returns: `EOK` on success or a negative error code.
```

```{function} void *_vm_zalloc(vm_zone_t *zone, addr_t *addr)

Allocates one block from a zone.

:param zone: Source zone.
:param addr: Optional output physical address for the allocated block.
:returns: Kernel virtual address of the block, or `NULL` when no block is available.
```

```{function} void _vm_zfree(vm_zone_t *zone, void *block)

Returns a block to its zone.

:param zone: Zone that owns the block.
:param block: Kernel virtual address returned by `_vm_zalloc()`.
```

```{function} void _zone_init(vm_map_t *map, vm_object_t *kernel, void **bss, void **top)

Initializes the zone allocator during VM startup.

:param map: Kernel map used for zone mappings.
:param kernel: Kernel memory object.
:param bss: Current end of kernel BSS and early heap metadata.
:param top: Current top of early heap mapping.
```
