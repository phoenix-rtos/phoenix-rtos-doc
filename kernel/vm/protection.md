# Other memory protection mechanisms

Entry-level microcontrollers based on ARM Cortex-M architecture massively used in common electronics devices are
typically equipped with embedded FLASH memories and tens of kilobytes of SRAM. Both FLASH and SRAM are accessible using
the same address space. Because of small amount of RAM, the MMU is useless and can lead to memory usage overhead.

To provide separation of running processes and used by them physical memory the Memory Protection Unit is used. Memory
Protection Unit takes part in memory addressing and typically allows partitioning memory access by defining set of
segments that can be used during the program execution. The number of these segments is usually limited (4, 8, 16). The
access to defined memory segments can be even associated with processor execution mode, so program executed in
supervisor mode can operate on more segments than when it is executed in user mode. Processor execution modes and
methods of transitioning between them have been Discussed in chapter [Processes and threads](../proc/index.md).

There are two strategies for using MPU and memory segmentation. First and more flexible is strategy of switching whole
MPU context when process context is switched. This demands to reload of all segments defined by MPU for the executed
process with the new set defined for the newly chosen process. The big advantage of this technique is that processes are
strictly separated because each of them uses its own set of user segments and shares the privileged segments
(e.g. kernel segments). There are two disadvantages of this technique caused by typical MPU limitations. The process of
redefining segments is slow because it requires the invalidation of cache memories. The method of defining segments in
MPU is limited because segment address and size definition depend on chosen granulation. For example, some segments can
be defined only if all set of MPU registers is used.

The second strategy, used in Phoenix-RTOS, is based on memory regions/segments defined for the whole operating system
and shared between processes. It means that processes can use during its execution few assigned predefined memory
regions called further memory maps. These regions are defined during operating system bootstrap with respect of MPU
register semantics and can be inline with physical memory characteristics. For example, separate regions can be defined
for TCM (Tightly Coupled Memory) with short access time and separate regions can be defined for cached RAM. The set of
regions assigned to the process is defined during process start-up. When a process context is switched the proper
process set of MPU definition is activated using enable/disable bits. This can be done much faster in comparison to
reloading the whole region definitions. The main disadvantage of described approach is the limited number of regions
that can be used by running processes. This results in a weaker separation of running processes because they must use
shared memory regions and erroneous thread of one process can destroy data in another process sharing the same memory
region. But it should be emphasized that this technique complemented with proper definition of memory regions can allow
fulfilling safety requirements of many types of applications e.g. applications based on software partitioning into two
parts with different safety requirements.

Discussion of techniques used for protecting memory when direct physical memory access is used should be complemented by
presentation of memory segmentation mechanisms popularized widely by x86 microprocessors. The segmentation technique was
developed on early computers to simplify the program loading and execution process. When a process is to be executed,
its corresponding segmentation is loaded into non-contiguous memory though every segment is loaded into a contiguous
block of available memory. The location of program segments in physical memory is defined by special set of processor
registers called segment registers and processor instructions are using offsets calculated according to segment base
addresses. This technique prevents from using relocation/recalculation of program addresses after it is loaded to memory
and before its execution is started. This technique was heavily extended in second generation of x86 processors (80286)
by adding the ability to define segments attributes, limits and privilege levels. Those techniques of processes
separation was used on some early operating system for PC like MS Windows 3.0 and IBM OS/2. Nowadays, it has been
replaced with paging.
