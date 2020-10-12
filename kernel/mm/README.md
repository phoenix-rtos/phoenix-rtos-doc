# Memory management

Memory management is the most important part of any operating system kernel, as it has a great impact on the overall system performance and scalability. In most modern general-purpose operating systems, memory management is based on paging and the Memory Management Unit (MMU), which is available across many popular hardware architectures (IA32, IA32E, ARMv9). Unfortunately, there are very few operating systems which are able to manage memory either on platforms with and without a MMU. The main goal of the Phoenix-RTOS microkernel is to manage memory on both MMU and non-MMU architectures.

## Memory management on architectures equipped with MMU
MMU architectures are typical for processors used in servers, personal computers and mobile devices such as tablets and smartphones. In this architecture, the program accesses a virtual memory address space which is mapped into the physical memory by MMU hardware using a data structure called a page table located in the physical memory. The role of the MMU in memory address translation is illustrated in the figure below.

<img src="http://r.dcs.redcdn.pl/http/o2/phoesys/documentation/mem-mmu.png" style="width: 450px">

The piece of the virtual address space mapped into the physical memory is called a memory page. Typically, the page size used in modern systems is 4KB, but in the past, e.g. the PDP-10, VAX-11 architectures, it was much smaller (512 or 1KB).

### Initial concept of paging technique
The concept of paging was first introduced in the late 1960s in order to organize the program memory overlaying for hierarchical memory systems consisting of transistor-based memory, core memory, magnetic disks and tapes. Historically, the virtual address space size was comparable to the physical memory size. The page table was used to point to the data location in the hierarchical memory system and to associate the physical memory location, called a page frame, with the virtual page. When the program accessed the virtual page, processor checked whether the page was present in the physical memory via the presence bit in the page table. If the page was not present in the physical memory, the program execution was interrupted and the page was loaded by the operating system into the physical memory via additional bits defining the data location in the page table. Once the presence bit was successfully loaded and set, the program execution was resumed. The original paging technique is presented below.

<img src="http://r.dcs.redcdn.pl/http/o2/phoesys/documentation/mem-paging1.png" style="width: 650px">

### Current use of paging technique

Over the years, paging has morphed into a technique used for defining the process memory space and for process separation. In general-purpose operating systems, paging is fundamental for memory management. Each process runs in its own virtual memory space and uses all address ranges for their needs. The address space is defined by a set of virtual-to-physical address associations for the MMU defined in the physical memory and stored in a structure which is much more complicated than a page table used in early computers. This is necessary in order to optimize memory consumption and speed up the virtual-to-physical memory translations. When a process is executed on a selected processor, the address space is switched to its virtual space, which prevents it from interfering with other processes. The address space is switched by providing the MMU with new sets of virtual-to-physical associations. In this scheme, some physical pages (for example parts of the program text) can be shared among processes by mapping them simultaneously into two or more processes to minimize the overall memory usage.

<img src="http://r.dcs.redcdn.pl/http/o2/phoesys/documentation/mem-paging2.png" style="width: 600px">

A memory management system which relies on paging describes the whole physical memory using physical pages.

## Non-MMU architectures
Non-MMU architectures are typical for entry-level microcontrollers like NXP Kinetis and ST STM32 families. They are equipped with embedded flash and tens of kilobytes of SRAM. Both FLASH and SRAM are accessible using the same address space. This address space is also used for communication with internal devices like reset and clock controller, timers, bus controllers, serial interfaces etc. In light of the above, it becomes clear that memory management must be quite advanced while ensuring minimum memory consumption. These two opposing goals affect data structures used for memory management.

## Memory management subsystem structure
Memory management subsystem provides following functionalities:

  * physical memory allocation
  * address space allocation and physical memory mapping
  * dynamic memory allocation inside the kernel
  * physical memory sharing.
 


<! img src="http://r.dcs.redcdn.pl/http/o2/phoesys/documentation/mem-layers.png" style="width: 600px">

### Hardware dependent layer (pmap)

The `pmap` abstraction constitutes the lowest level of the memory management implemented in the HAL. This abstraction implements an interface for managing the MMU and hides hardware details from the upper layers. Its most important function is the `pmap_enter()`, which is used for mapping the page into the process virtual address space.

### Page allocator
The first layer located on top of the `pmap` is the page allocator. In MMU architectures, it is responsible for allocating a set of physical memory pages. Each physical page is represented by the `page_t` descriptor. In non-MMU architectures, the page allocator allocates fake `page_t` structures used by other layers.

### Memory mapper
When the page allocator allocates a set of pages, the set must be mapped into an address space to be accessible. The memory address space is managed by the next memory management layer, i.e. the memory mapper. The memory mapper uses a memory map structures to describe memory segments located in address spaces. In MMU architectures, each process owns a separate memory map, and there is one kernel memory map defining the kernel address space. In non-MMU architectures, there is only one map shared by all processes and the kernel.

### Kernel fine-grained allocator
These two abstractions allow for memory allocation based on the needs of the kernel and processes with the resolution of page size. Such resolution is too large for dynamic allocation of kernel structures and could result in internal memory fragmentation and memory wasting. To omit these problems, zone allocator and fine-grained allocator are developed. They constitute the next layers of the memory management subsystem.

### Memory objects
First introduced in the Mach operating system, a memory object defines an entity containing data which could be partially or completely loaded into the memory and mapped into one or more address spaces. A good example of this is a binary object representing the program image (e.g. `/bin/sh`).

Memory objects were introduced so that processes could share physical memory; they allowing for identifying and defining sets of memory pages or segments of physical memory in non-MMU architectures. When one process maps an object into its memory map, the object occupies some physical pages. When another process uses the same object, the same pages (in the case of a read-only mapping) or their copies (in the case of a write mapping) are mapped.


## Implementation structure

The memory management subsystem is located in the `src/vm` subdirectory. The lowest `pmap` layer is implemented in the HAL.

## Chapter information
In this chapter main functions of the Phoenix-RTOS memory management are discussed.
