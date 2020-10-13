# HAL subsystem

HAL (Hardware Abstraction Layer) is the kernel hardware dependent subsystem which hides hardware architecture differences and provides unified interface for other hardware independent subsystems. HAL layer is the only one layer which should be changed to port kernel to the new hardware architecture.

HAL implements following functionalities:

>
* Kernel initialization,
* Basic type definitions,
* Definition of syspage structure,
* Basic synchronization (spinlocks),
* Kernel console,
* String functions (memcpy, memset),
* Exception and interrupt handling,
* MMU or MPU management,
* Timer device support,
* Context switching.

Theses functionalities are briefly discussed in this chapter.

## Kernel initialization

After loading kernel into memory HAL initializaiton is started. Typically code responsible for this task is located in `_init.S` file and it is written in assembly language. Initialization function sets specific processor registers (e.g. segment registers, MMU registers), prepares address space for executing main function and finally passes control to it.

## Basic types

Phoenix-RTOS 3 microkernel uses basic C types and assumes some types defined in HAL. Type definitions for sample 32-bit architecture has been presented below.

>
    typedef unsigned char u8;             /* 8-bit unsigned integer */
    typedef unsigned short u16;           /* 16-bit unsigned integer */
    typedef unsigned int u32;             /* 32-bit unsigned integer */
    typedef unsigned long long u64;       /* 64-bit unsigned integer */
>
    typedef char s8;                      /* 8-bit signed integer */
    typedef short s16;                    /* 16-bit signed integer */
    typedef int s32;                      /* 32-bit signed integer */
    typedef long long s64;                /* 64-bit signed integer */
>
    typedef u32 addr_t;                   /* Physical address */
    typedef u64 cycles_t;                 /* Type for processor cycles counter */
>
    typedef s64 offs_t;                   /* Object offset */
>
    typedef unsigned int size_t;          /* Data size */
    typedef unsigned long long time_t;    /* Time representation (microseconds) */

## Syspage
The low-level kernel initialization is based on `syspage_t` structure. This structure is prepared during the boot by operating system loader and stored in physical memory at predefined or dynamic address chosen by the loader.

The `syspage_t` definition and its location depends on the hardware architecture and developer choice. It can provide the lot of information to the kernel e.g. locations of interrupts tables, physical memory map etc. The minimum set of attributes which should be defined (which is assumed by upper layers) is presented below.

>
    typedef struct _syspage_t {
        ..
        addr_t stack;
        u32 stacksz;
>
        addr_t kernel;
        u32 kernelsize; 
>
        u16 progssz;
        syspage_program_t progs[0];
        ..
    } syspage_t;

Attributes `stack` and `stacksz` define the location and size of the initial kernel stack used during the kernel initialization until first process is started. Attributes `kernel` and `kernelsz` define the physical memory location of the kernel. Array `progs[]` defines  programs available in physical memory which should be started by the first operating system process during the boot. Attribute `progsz` defines the size of the `progs[]` array. The size of the array could be zero if no programs are loaded into the memory. In such case only kernel is executed and boot process is stopped when first process is launched.

Each entry of `progs[]` array is defined in the following way.

>
    typedef struct syspage_program_t {
        void *entry;
        u32 hdrssz;
        struct {
            addr_t addr;
            u32 memsz;
            u32 flags;
            void *vaddr;
            u32 filesz;
            u32 align;
        } hdrs[1];
    } syspage_program_t;

It defines the program starting address (`entry`) and program segments (`hdrs`). The definition of the segment practically corresponds to ELF program header definition. Each segment is defined by providing its physical and virtual address, physical and virtual size, alignment and attributes (readable, writable, executable). The minimal number of segments defined for the program is 1.

## Spinlocks

Spinlocks are basic primitives uses for process synchronization. They prevent to execute the same code by multiple processors at the same time. They are implemented using special processor instruction (called test-and-set) used for atomic exchange of the value stored in the processor register with the value stored in the memory. From programmer point of view spinlock behaves like binary semaphore but the main difference is the active waiting. If spinlock is locked on the one processor and code running on other processor tries to lock it again the execution of the the locking operation fails and is repeated until it will be succeeded. To check the spinlock state in the memory the test-and-set instruction is used. In one operation the value indicating the lock is stored in the memory and previous value is retrieved into the register. If the value from memory indicates the lock the operation is repeated.

There are few  functions used for operating on spinlocks.

>
    void hal_spinlockSet(spinlock_t *spinlock);
    void hal_spinlockClear(spinlock_t *spinlock);

These functions are used for locking/unlocking spinlocks.

>
    void hal_spinlockCreate(spinlock_t *spinlock, const char *name);
    void hal_spinlockDestroy(spinlock_t *spinlock);

These functions are used for creating new spinlock. It is assumed that spinlock provided in as argument resides in memory. Created spinlock are added to the common spinlock list. The argument name identifies the spinlock in the system and it is used only for evaluation purposes.

Upper layers assume that `spinlock_t` structure defines some mandatory attirbutes presented below.

>
    typedef struct _spinlock_t {
        const char *name;
        cycles_t dmin;
        cycles_t dmax;
        struct _spinlock_t *next;
        struct _spinlock_t *prev;
        ..
    } spinlock_t;

Attributes `dmin` and `dmax` stores respectively the minimum and maximum number of CPU cycles wasted during the execution of the code protected by the spinlock. The `prev` and `next` attributes are used for purposes of the spinlock list which was mentioned above.

## Console
Console is used for presenting kernel messages until first process and terminal drivers are started. It is typically based on UART but it can use other display devices (on IA32 there is console based on VGA). Console should work from the early boot stage and therefore it should be kept as simple as possible and should use no interrupts and other HAL mechanisms.

## String functions
HAL provides set of string functions used for data copying and string manipulation. They correspond to ANSI C functions provided by compiler but compiler`s functions are not intentionally used. The intention was to implement these functions from scratch to control the details of implementation and external references.

>
    static inline void hal_memcpy(void *to, const void *from, unsigned int n);
>
    static inline void hal_memset(void *where, u8 v, unsigned int n);
>
    static inline void hal_memsetw(void *where, u16 v, unsigned int n);
>
    static inline unsigned int hal_strlen(const char *s);
>
    static inline int hal_strcmp(const char *s1, const char *s2);
>
    static inline int hal_strncmp(const char *s1, const char *s2, unsigned int count);
>
    static inline char *hal_strcpy(char *dest, const char *src);
>
    static inline char *hal_strncpy(char *dest, const char *src, size_t n);

These functions should be implemented as static inline in the header file. Some exceptions are allowed.

## MMU/MPU management

HAL is responsible for the lowest part of the memory managements subsystem - `pmap`. This layer provides functions used for controlling the MMU or MPU. When no memory control units are available these functions should emulate this functionality. 

>
    extern int pmap_create(pmap_t *pmap, pmap_t *kpmap);
>
    extern int pmap_destroy(pmap_t *pmap);

Above functions are responsible for creating and destroying the `pmap` object. When new object is created some entries are copied from kernel `pmap` to map kernel into the new address space.

>
    extern void pmap_switch(pmap_t *pmap);

Function switches address space to address space defined by `pmap` object.

>
    extern int pmap_enter(pmap_t *pmap, page_t *page, void *vaddr, int attrs, page_t *alloc);

Function enters new mapping into the address space defined by `pmap` object.

>
    extern int pmap_resolve(pmap_t *pmap, void *vaddr, addr_t *paddr);

Function returns the physical address associated with given virtual address.

>
    extern int pmap_get(page_t *page, addr_t *addr);

Function returns the page descriptor for given physical address. The next physical address is returned.


## Exception and interrupts

HAL plays very important role in exceptions and interrupts handling. It handles interrupts controller, implements the interrupt and exception stubs and interrupt and exception service routines invocations. Interrupts routines can reside in the kernel address space or in process address space. When interrupt handler is located in process address space the process `pmap` object is passed during the interrupt handler installation and before servicing interrupt the address space is switched.

Below are presented functions for interrupts and exceptions handling which should be implemented by HAL.

>
    int hal_interruptsSetHandler(unsigned int n, int (*handler)(unsigned int, cpu_context_t *, void *),
        void *data, pmap_t *pmap);
>
    void hal_exceptionsDumpContext(char *buff, exc_context_t *ctx);
>
    int hal_exceptionsSetHandler(unsigned int n, void (*handler)(unsigned int, exc_context_t *));


## Timer
Timer is the fundamental device for operating system kernel. It is used for preemptive scheduling and time management. HAL is responsible for implementation of two timers - scheduler timer and high precision timer. On some architectures they can be based on one hardware device but commonly the are based on two separated devices. The interface provided for upper layer unifies these devices and hides implementation details.

HAL implementsone functions for operating on timers and defines two interrupt numbers respectively for timer used for scheduling and for timer used for time management.

>
    #define INTERRUPT_SYSTIC        0
    #define INTERRUPT_TIMER         0
>
    int hal_timer(time_t time);

The defined function is used for defining the moment of next triggering of high precision timer used for time management. At this moment the `INTERRUPT_TIMER` interrupt will appear.

## Context switching

Context switching is the most exciting part of the HAL. In Phoenix-RTOS is assumed the context switching is based on thread kernel stack switching. When interrupt is raised interrupt stub function (implemented in HAL) is called and stores the current thread context (registers and other data) on the top of the kernel stack before it passes control to the interrupt dispatching function and finally to the registered interrupt service routine. After interrupt dispatching and service routine execution control is returned to the interrupt stub which restores the saved context.

The last register stored on the kernel stack is the current stack pointer and it can be changed by interrupt service routine to another one. This happens if interrupt routine executes the scheduler and context switch appears. In such case the control is passed to the new thread. If the next thread is executing in the separate address space (belongs to other process) before switching to the new thread scheduler switches the address space using `pmap_switch()` function.

Context is described using `cpu_contex_t` structure.


