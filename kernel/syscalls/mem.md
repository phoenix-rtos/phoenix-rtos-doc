# Memory management

Functions allow managing process address spaces.

## `syscalls_memMap` (`syscalls_mmap`)

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
GETFROMSTACK(ustack, int, prot, 2);
GETFROMSTACK(ustack, int, flags, 3);
GETFROMSTACK(ustack, oid_t *, oid, 4);
GETFROMSTACK(ustack, offs_t, offs, 5);
````

Maps part of object given by `oid`, `offs` and `size` at `vaddr` with protection attributes given by `prot` using
mapping mode defined by `flags`.

## `syscalls_memUnmap` (`syscalls_munmap`)

````C
GETFROMSTACK(ustack, void *, vaddr, 0);
GETFROMSTACK(ustack, size_t, size, 1);
````

Unmaps part of address space defined by `vaddr` and `size`.

## `syscalls_memDump` (`syscalls_mmdump`)

Returns memory map entries associated with calling process.

## `syscalls_memGetInfo` (`syscalls_meminfo`)

````C
GETFROMSTACK(ustack, meminfo_t *, info, 0);
````

## `syscalls_memGetPhysAddr` (`syscalls_va2pa`)

````C
GETFROMSTACK(ustack, void *, va, 0);
````
