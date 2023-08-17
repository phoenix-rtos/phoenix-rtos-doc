# Fine-grained allocator

Fine-grained allocator implemented by `vm_kmalloc()` function is the main method of dynamic memory allocation used by
the Phoenix-RTOS kernel. The operating system kernel uses dynamic data structures to manage dynamic data structures
created during the operating system runtime (e.g. process descriptors, threads descriptors, ports). Size of these
structures varies from few bytes to tens of kilobytes. The allocator can allocate either the group of memory pages and
manage the fragments allocated within the page.

## Architecture

Fine-grained allocator is based on zone allocator. The architecture is presented on the following picture.

Main allocator data structure is `sizes[]` table. Table entries point to list of zone allocators consisting of fragments
with sizes proportional to the entry number. Fragments have sizes equal to `2^e` where `e` is the entry number.

## Memory allocation

The first step of the allocation process is the calculation of entry number. The best fit strategy is used, so the
requested size is rounded to the nearest power of two. After calculating the entry number the fragment is allocated
from the first zone associated with the entry number.

If the selected entry is empty and there are no empty zones associated with the entry, the new zone is created and added
to the list. New zone is added either to `sizes[]` table and to the zone RB-tree. The zone RB-tree is used to find the
proper zone when a fragment is released.

If the allocated fragment is the last free fragment from the zone, the zone is removed from the entry zone list and is
linked with the used zones list.

## Memory deallocation

When fragment is deallocated the first step is to find proper zone based on its virtual address. The zone RB-tree is
searched. When zone is established the fragment is released using `vm_zfree()` call and returned to the zone. When zone
is empty it is released and allocated memory is returned to the operating system pool.

## See also

1. [Kernel - Memory management](README.md)
2. [Kernel - Memory management - Page allocator](page.md)
3. [Kernel - Memory management - Memory mapper](mapper.md)
4. [Kernel - Memory management - Zone allocator](zalloc.md)
5. [Kernel - Memory management - Memory objects](objects.md)
6. [Table of Contents](../../README.md)
