# Memory management

Memory syscall handlers unpack arguments from the user stack with `GETFROMSTACK()` and operate on the current
process map.

````{function} syscalls_sys_mmap(ustack)
Maps memory in the current process address space.

The handler rounds `size` up to a page boundary, validates the output pointer, resolves the object from `fildes` when
the mapping is not anonymous, and calls `vm_mmap()` with `PROT_USER` added to the requested protections.

:param ustack: User stack containing `void **vaddr`, `size_t size`, `int prot`, `int flags`, `int fildes`, and
  `off_t offs` at indexes `0` through `5`.
:returns: `EOK` on success, with `*vaddr` updated to the mapped address. Returns `-EFAULT` when `vaddr` is outside the
  process map, `-ENOMEM` when a contiguous or final mapping allocation fails, or a negative error from descriptor or
  VM object lookup.
````


````{function} syscalls_sys_munmap(ustack)
Unmaps memory from the current process address space.

:param ustack: User stack containing `void *vaddr` at index `0` and `size_t size` at index `1`.
:returns: `EOK` on success or a negative error returned by `vm_munmap()`.
````

````{function} syscalls_sys_mprotect(ustack)
Changes protection bits for a mapped region in the current process.

:param ustack: User stack containing `void *vaddr`, `size_t len`, and `int prot` at indexes `0` through `2`.
:returns: `EOK` on success or a negative error returned by `vm_mprotect()`.
````

````{function} syscalls_meminfo(ustack)
Copies kernel memory information to a user-provided `meminfo_t` structure.

:param ustack: User stack containing `meminfo_t *info` at index `0`.
:returns: Nothing. The handler calls `vm_meminfo()` only when `info` belongs to the current process map.
````

````{function} syscalls_va2pa(ustack)
Resolves a user virtual address to a physical address in the current process page map.

:param ustack: User stack containing `void *va` at index `0`.
:returns: Physical address formed from the resolved page frame and the low 12 bits of `va`.
````