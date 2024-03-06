# HAL

HAL (Hardware Abstraction Layer) is the kernel hardware-dependent subsystem used for adapting it to the particular
hardware platform. It provides a unified interface for other kernel subsystems. It is the only subsystem required to be
changed when the kernel is ported to the new hardware architecture.

HAL implements the following functionalities:

* Kernel initialization,
* Basic type definitions,
* Definition of syspage structure,
* Basic synchronization (spinlocks),
* Kernel console,
* String functions (memcpy, memset),
* Exception and interrupt handling,
* MMU or MPU management,
* Timer support,
* Context switching.

These functionalities are briefly discussed in this chapter.

## Kernel initialization

After loading kernel into the memory HAL initialization is executed. Typically, this code is located in `_init.S`
file, and it is written in assembly language. The initialization function sets specific processor registers
(e.g. control registers, segment registers, MPU/MMU registers), prepares kernel address space, and passes
control to `main()` function.

## Basic types

Phoenix-RTOS 3 microkernel uses basic C types and a few kernel-specific types defined in HAL.

## Syspage

The low-level kernel initialization is based on `syspage_t` structure. This structure is prepared during the bootstrap
process by the operating system loader.  It is stored in physical memory at the address chosen by the loader.
The `syspage_t`definition depends on the hardware architecture and provides information like physical memory maps,
interrupts tables,
preloaded user application, etc. It should be treated as the main structure used for operating system configuration.

## Spinlocks

Spinlocks are basic primitives used for active synchronization of parallelly executed instruction streams. They are
implemented using special processor instruction (called test-and-set) used for the atomic exchange of the value stored
in the processor register with the value stored in the memory. From a programmer's point of view, spinlock behaves like
a binary semaphore, but the main difference is the active waiting. If spinlock is locked on one processor and code
running on another processor tries to lock it again the execution of the locking operation fails and is repeated until
it will be succeeded. To check the spinlock state in the memory the test-and-set instruction is used. In one operation
the value indicating the lock is stored in the memory and the previous value is retrieved into the register. If the
value from memory indicates the lock the operation is repeated.

## Console

The console is used for presenting kernel messages until the first process and terminal drivers are started. It is
typically based on UART, but it can use other display devices (on IA32 there is a console based on a VGA
graphics adapter and keyboard). The console should work from the early boot stage, and therefore it should be kept as
simple as possible and should use no interrupts and other HAL mechanisms.

## String functions

HAL provides a set of string functions used for data copying and string manipulation. They correspond to ANSI
C functions provided by the compiler, but the compiler's functions are not intentionally used. The
intention was to implement these functions from scratch to control the details of implementation and external
references.

## MMU or MPU management

HAL is responsible for the lowest part of the memory management subsystem - `pmap`. This layer provides functions used
for controlling the MMU or MPU. When no memory control units are available these functions should be empty.

## Exception and interrupts

HAL plays an important role in exception and interrupts handling. It handles the interrupt's controller, implements the
interrupt and exception stubs, and interrupt and exception service routines invocations. Interrupts routines can reside
in the kernel address space or in the process address space. When the interrupt handler is located in the
process address space the process `pmap` object is passed during the interrupt handler installation and
before servicing interrupt the address
space is switched.

## Timer

Timer is the fundamental device for the operating system kernel. It is used for preemptive scheduling and time
management. HAL is responsible for the implementation of two timers - a scheduler timer and high precision timer.
On some architectures, they can be based on one hardware device, but commonly they are based on two separate devices.
The interface provided for the upper layer unifies these devices and hides implementation details.

HAL implements one function for operating on timers and defines two interrupt numbers respectively for timers used for
scheduling and for timers used for time management.

## Context switching

Context switching is the most exciting part of HAL. In Phoenix-RTOS is assumed the context switching is based on thread
kernel stack switching. When interrupt is raised interrupt stub function (implemented in HAL) is called and stores the
current thread context (registers and other data) on the top of the kernel stack before it passes control to the
interrupt dispatching function and finally to the registered interrupt service routine. After interrupt dispatching and
service routine execution control is returned to the interrupt stub which restores the saved context.

The last register stored on the kernel stack is the current stack pointer, and it can be changed by interrupt service
routine to another one. This happens if interrupt routine executes the scheduler and context switch appears. In such
case the control is passed to the new thread. If the next thread is executing in the separate address space (belongs to
other process) before switching to the new thread scheduler switches the address space using `pmap_switch()` function.

Context is described using `cpu_contex_t` structure.

## See also

1. [Kernel](../README.md)
2. [Kernel - HAL for ARMv7 Cortex-M based targets](armv7m.md)
3. [Kernel - HAL for ARMv7 Cortex-A based targets](armv7a.md)
4. [Kernel - HAL for IA32 targets](ia32.md)
5. [Kernel - HAL for RISC-V 64 based targets](riscv64.md)
6. [Kernel - HAL for SPARCv8 LEON3 based targets](sparcv8leon3.md)
7. [Table of Contents](../README.md)
