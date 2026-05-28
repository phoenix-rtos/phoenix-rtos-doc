# Physical page allocator

The page allocator is the lowest VM layer. On MMU targets it allocates physical page sets. On NOMMU targets it allocates
`page_t` descriptors used by the common mapping code.

The public internal interface is declared in `vm/page.h`:

```{function} page_t *vm_pageAlloc(size_t size, vm_flags_t flags)

Allocates a physically contiguous set of pages large enough to hold `size` bytes.

:param size: Requested size in bytes.
:param flags: Page owner and usage flags stored in each allocated `page_t`.
:returns: Pointer to the first `page_t` in the allocated range, or `NULL` when allocation fails.
```

```{function} void vm_pageFree(page_t *page)

Releases a range previously returned by `vm_pageAlloc()`.

:param page: First page descriptor in the range.
```

```{function} page_t *_page_get(addr_t addr)

Returns a page descriptor for a physical address.

:param addr: Physical address.
:returns: Matching page descriptor, or `NULL` when `addr` is outside known physical memory.
```

```{function} void _page_init(pmap_t *pmap, void **bss, void **top)

Initializes the allocator during VM startup.

:param pmap: Kernel page-map context.
:param bss: Current end of kernel BSS and early heap metadata.
:param top: Current top of early heap mapping.
```

## MMU targets

On MMU targets `_page_init()` discovers physical memory through the architecture `pmap_getPage()` function. Each
reported page is represented by `page_t`. Free pages are inserted into size-class lists used by a buddy allocator.

The allocator keeps the following accounting:

| Field | Meaning |
| --- | --- |
| `freesz` | Free physical memory. |
| `allocsz` | Allocated physical memory. |
| `bootsz` | Memory reserved by boot firmware or the loader. |

Allocation uses the first free list large enough for the requested size. Larger blocks are split until the requested
size class is reached. Freeing a block sets `PAGE_FREE` and merges adjacent free buddies when their size and physical
addresses match.

## Page flags

Architecture `pmap.h` headers define the exact bit layout, but the common code uses these groups:

| Flag group | Examples | Meaning |
| --- | --- | --- |
| State | `PAGE_FREE` | Page is available for allocation. |
| Owner | `PAGE_OWNER_BOOT`, `PAGE_OWNER_KERNEL`, `PAGE_OWNER_APP` | Page owner domain. |
| Kernel use | `PAGE_KERNEL_*` | Kernel page purpose, such as syspage, CPU data, page table, stack, or heap. |

Kernel page tables are allocated with `PAGE_OWNER_KERNEL | PAGE_KERNEL_PTABLE`. Kernel heap pages use
`PAGE_OWNER_KERNEL | PAGE_KERNEL_HEAP`. Anonymous and object-backed user pages use `PAGE_OWNER_APP`.

## Boot map output

The kernel can print a compact memory map during boot. The letters are debug output from page descriptors:

| Letter | Meaning |
| :---: | --- |
| `.` | Free page. |
| `x` | Physical memory gap. |
| `B` | Bootloader or firmware-reserved page. |
| `A` | Application page. |
| `K` | Kernel page with no more specific kernel-purpose flag. |
| `Y` | Kernel syspage. |
| `C` | CPU-specific kernel page. |
| `P` | Page-table page. |
| `S` | Kernel stack page. |
| `H` | Kernel heap page. |
| `U` | Unknown page type. |

## NOMMU targets

On NOMMU targets the allocator manages a pool of `page_t` descriptors rather than real page frames. Real memory ranges
are assigned by the mapper, and all processes share one memory map. This keeps the VM object and mapping APIs usable on
targets without hardware page translation.
