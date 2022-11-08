# HAL subsystem

HAL (Hardware Abstraction Layer) is the kernel hardware dependent subsystem used for adopting it to the particular hardware platform. It provides the unified interface for other kernel subsystems. It is the only subsystem required to be changed when kernel is ported to the new hardware architecture.

HAL implements following functionalities:

* kernel initialization,
* basic type definitions,
* definition of syspage structure,
* basic synchronization (spinlocks),
* kernel console,
* string functions (memcpy, memset),
* exception and interrupt handling,
* MMU or MPU management,
* timer support,
* context switching.

Theses functionalities are briefly discussed in this chapter.

## Kernel initialization

After loading kernel into the memory HAL initializaiton is executed. Typically this code is located in `_init.S` file and it is written in assembly language. Initialization function sets specific processor registers (e.g. control registers, segment registers, MPU/MMU registers), prepares kernel address space and passes control to `main()` function.

## Basic types

Phoenix-RTOS 3 microkernel uses basic C types and few kernel-specific types defined in HAL.

## Syspage

The low-level kernel initialization is based on `syspage_t` structure. This structure is prepared during the bootstrap process by operating system loader.  It is stored on physical memory at address chosen by the loader.  The `syspage_t` definition depends on the hardware architecture and provides information like physical memory maps, interrupts tables, preloaded user application etc. It should be treated as the main structure used for operating system configuration.

## Spinlocks

Spinlocks are basic primitives used for active synchronizaton of parallely executed instruction streams. They are implemented using special processor instruction (called test-and-set) used for atomic exchange of the value stored in the processor register with the value stored in the memory. From programmer point of view spinlock behaves like binary semaphore but the main difference is the active waiting. If spinlock is locked on the one processor and code running on other processor tries to lock it again the execution of the the locking operation fails and is repeated until it will be succeeded. To check the spinlock state in the memory the test-and-set instruction is used. In one operation the value indicating the lock is stored in the memory and previous value is retrieved into the register. If the value from memory indicates the lock the operation is repeated.

## Console

Console is used for presenting kernel messages until first process and terminal drivers are started. It is typically based on UART but it can use other display devices (on IA32 there is console based on VGA graphics adapter and keyboard). Console should work from the early boot stage and therefore it should be kept as simple as possible and should use no interrupts and other HAL mechanisms.

## String functions

HAL provides set of string functions used for data copying and string manipulation. They correspond to ANSI C functions provided by compiler but compiler`s functions are not intentionally used. The intention was to implement these functions from scratch to control the details of implementation and external references.

## MMU or MPU management

HAL is responsible for the lowest part of the memory managements subsystem - `pmap`. This layer provides functions used for controlling the MMU or MPU. When no memory control units are available these functions should be empty.

## Exception and interrupts

HAL plays important role in exceptions and interrupts handling. It handles interrupts controller, implements the interrupt and exception stubs and interrupt and exception service routines invocations. Interrupts routines can reside in the kernel address space or in process address space. When interrupt handler is located in process address space the process `pmap` object is passed during the interrupt handler installation and before servicing interrupt the address space is switched.

## Timer

Timer is the fundamental device for operating system kernel. It is used for preemptive scheduling and time management. HAL is responsible for implementation of two timers - scheduler timer and high precision timer. On some architectures they can be based on one hardware device but commonly the are based on two separated devices. The interface provided for upper layer unifies these devices and hides implementation details.

HAL implements one functions for operating on timers and defines two interrupt numbers respectively for timer used for scheduling and for timer used for time management.

## Context switching

Context switching is the most exciting part of HAL. In Phoenix-RTOS is assumed the context switching is based on thread kernel stack switching. When interrupt is raised interrupt stub function (implemented in HAL) is called and stores the current thread context (registers and other data) on the top of the kernel stack before it passes control to the interrupt dispatching function and finally to the registered interrupt service routine. After interrupt dispatching and service routine execution control is returned to the interrupt stub which restores the saved context.

The last register stored on the kernel stack is the current stack pointer and it can be changed by interrupt service routine to another one. This happens if interrupt routine executes the scheduler and context switch appears. In such case the control is passed to the new thread. If the next thread is executing in the separate address space (belongs to other process) before switching to the new thread scheduler switches the address space using `pmap_switch()` function.

Context is described using `cpu_contex_t` structure.

## See also

1. [Kernel](../README.md)
2. [Kernel - HAL for ARMv7 Cortex-M based targets](armv7m.md)
3. [Kernel - HAL for ARMv7 Cortex-A based targets](armv7a.md)
4. [Kernel - HAL for IA32 targets](ia32.md)
5. [Kernel - HAL for RISC-V 64 based targets](riscv64.md)
6. [Table of Contents](../README.md)
