# Memory management

Memory management is the most important part of any operating system kernel, as it has a great impact on the overall
system performance and scalability. The main goal of the memory management is to provide physical memory for the purpose
of kernel and running programs represented by processes.

In most modern general-purpose operating systems, memory management is based on paging technique and the Memory
Management Unit (MMU) is used. The MMU is available across many popular hardware architectures (e.g. IA32, x86-64, ARMv7
Cortex-A, RISC-V) and is used for translating the linear addresses used by programs executed on the processor core into
the physical memory addresses. This translation is based on linear-physical address associations defined inside MMU
which are specific for each running process allowing to separate them from each other. The evolution of paging
technique and current use of it in general purpose operating systems are briefly discussed in the further parts of this
chapter.

The assumption of use of paging technique as the basic method of accessing the memory for running processes is
insufficient when operating system shall handle many hardware architectures starting from low-power microcontrollers and
ending with advanced multicore architectures with gigabytes of physical memory because MMU is available only on
some of them. Moreover, many modern architectures used for IoT device development and massively parallelized multicore
computers are equipped with a non-uniform physical memory (NUMA) with different access characteristics. For example,
in modern microcontrollers, some physical memory segments can be tightly coupled with processor enabling to run
real-time application demanding minimal jitter (e.g. for signal processing). On multicore architectures, some physical
memory segments can be tightly coupled with particular set of processing cores while others segments can be accessible
over switched buses which results in delayed access and performance degradation. Having this in mind in Phoenix-RTOS it
was decided to redefine the traditional approach to memory management and some new memory management abstractions and
mechanisms were proposed. These abstractions and mechanisms allow unifying the approach for memory management on many
types of memory architectures. To understand the details and purpose of these mechanisms memory hardware architecture
issues are briefly discussed in this chapter before Phoenix-RTOS memory management functions are briefly presented.

```{toctree}
:maxdepth: 1

page.md
mapper.md
zalloc.md
kmalloc.md
objects.md
protection.md
subsystem.md
```
