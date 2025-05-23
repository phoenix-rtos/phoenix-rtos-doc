# Memory management subsystem

Memory management subsystem provides following functionalities:

* physical memory allocation,
* address space allocation (inside memory regions),
* linear addresses to physical addresses mapping (when paging is available),
* dynamic, fine-grained kernel memory allocation,
* objects memory mapping and memory sharing.

These functions will be briefly discussed and elaborated more in the particular chapters.

## Physical memory allocation

Physical memory allocation is the lowest level of the memory management subsystem. It is used to provide memory for the
purposes of kernel or mapped object. They are two ways of obtaining physical memory depending on the type of hardware
memory architecture. When paging technique is used the memory is allocated using physical memory pages (page frames).
On architecture with direct physical memory access the physical memory is allocated using address space allocation in
the particular memory map. It is planned to generalize these techniques in the next version of Phoenix-RTOS memory
management subsystem. To understand the physical memory allocation algorithm on architectures using paging technique
please refer to [Physical memory allocation using memory pages](page.md).

## Memory mapper

When the page allocator allocates a set of pages, the set must be mapped into an address space to be accessible.
The memory address space is managed by the next memory management layer, i.e. the memory mapper. The memory mapper uses
a memory map structures to describe memory segments located in address spaces. In MMU architectures, each process owns
a separate memory map, and there is one kernel memory map defining the kernel address space. In non-MMU architectures,
there is only one map shared by all processes and the kernel.

## Hardware dependent layer (pmap)

The `pmap` abstraction constitutes the lowest level of the memory management implemented in the HAL. This abstraction
implements an interface for managing the MMU and hides hardware details from the upper layers. Its most important
function is the `pmap_enter()`, which is used for mapping the page into the process virtual address space.

## Kernel fine-grained allocator

These two abstractions allow for memory allocation based on the needs of the kernel and processes with the resolution of
page size. Such resolution is too large for dynamic allocation of kernel structures and could result in internal memory
fragmentation and memory wasting. To omit these problems, zone allocator and fine-grained allocator are developed. They
constitute the next layers of the memory management subsystem.

## Memory objects

First introduced in the Mach operating system, a memory object defines an entity containing data that could be
partially or completely loaded into the memory and mapped into one or more address spaces. A good example of this is a
binary object representing the program image (e.g. `/bin/sh`).

Memory objects were introduced so that processes could share physical memory; they allow for identifying and defining
sets of memory pages or segments of physical memory in non-MMU architectures. When one process maps an object into its
memory map, the object occupies some physical pages. When another process uses the same object, the same pages (in the
case of a read-only mapping) or their copies (in the case of a write mapping) are mapped.

## Implementation structure

The memory management subsystem is located in the `src/vm` subdirectory. The lowest `pmap` layer is implemented in
the HAL.
