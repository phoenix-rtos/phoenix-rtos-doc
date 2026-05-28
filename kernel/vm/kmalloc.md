# Fine-grained allocator

`vm_kmalloc()` is the main dynamic allocator used by the kernel. It allocates variable-size objects by routing requests
to zone allocators grouped by power-of-two size classes.

Typical users include process, thread, port, and VM metadata allocation.

## Allocation model

The allocator keeps size-class lists. For a requested size, it selects the smallest power-of-two class that can hold the
object. Allocation then uses the first zone in that class. If no zone has a free block, the allocator creates a new zone
and adds it to the class list and address-index tree.

When a zone becomes full, it is removed from the free-zone list for that class. When a block is freed, the allocator
finds the owning zone by address and returns the block to that zone. Empty zones can be destroyed so their backing pages
return to the page allocator.

## API

```{function} void *vm_kmalloc(size_t sz)

Allocates a kernel memory block.

:param sz: Requested size in bytes.
:returns: Kernel virtual address of the allocated block, or `NULL` when allocation fails.
```

```{function} void vm_kfree(void *p)

Frees a block previously allocated with `vm_kmalloc()`.

:param p: Pointer returned by `vm_kmalloc()`.
```

```{function} void vm_kmallocGetStats(size_t *allocsz)

Returns allocator statistics.

:param allocsz: Output total memory allocated by kmalloc zones.
```

```{function} void vm_kmallocDump(void)

Prints allocator debug information.
```

```{function} int _kmalloc_init(void)

Initializes the kernel allocator.

:returns: `EOK` on success or a negative error code.
```
