# Memory management

Functions allow managing process address spaces.

## `syscalls_sys_mmap`

````C
GETFROMSTACK(ustack, void **, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
GETFROMSTACK(ustack, int, prot, 2);
GETFROMSTACK(ustack, int, flags, 3);
GETFROMSTACK(ustack, int, fildes, 4);
GETFROMSTACK(ustack, off_t, offs, 5);
````

Maps part of object given by `fildes`, `offs` and `size` at `vaddr` with protection attributes given by
`prot` using mapping mode defined by `flags`.

## `syscalls_sys_munmap`

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
````

Unmaps part of address space defined by `vaddr` and `size`.

## `syscalls_meminfo`

````C
GETFROMSTACK(ustack, meminfo_t *, info, 0);
````

Returns memory map entries associated with calling process.

## `syscalls_va2pa`

````C
GETFROMSTACK(ustack, void *, va, 0);
````

Converts virtual address given by `va` to physical address.

## `syscalls_sys_mprotect`

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, len, 1);
GETFROMSTACK(ustack, int, prot, 2);
````

Sets protection access to a memory region given by `vaddr` of size `len` to `prot`.
