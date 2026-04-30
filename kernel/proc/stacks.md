# Kernel stacks

Each kernel thread owns a kernel stack recorded in `thread_t.kstack` and `thread_t.kstacksz`.
The stack is used for exception, interrupt, syscall, scheduling, signal, and thread-entry contexts.

## Stack allocation

`proc_threadCreate()` allocates the `thread_t` object and then allocates the kernel stack with `vm_kmalloc(kstacksz)`.
The stack memory is filled with `0xba`, the initial CPU context is created with `hal_cpuCreateContext()`, and the thread
is inserted into the scheduler data structures.

The syscall path uses `SIZE_KSTACK` when creating user threads.
Kernel helper threads also pass an architecture-specific kernel stack size to `proc_threadCreate()`.

## Architecture constants

The kernel stack size is defined by architecture headers:

| Architecture | `SIZE_INITIAL_KSTACK` | `SIZE_KSTACK` |
| --- | --- | --- |
| `aarch64` | `2U * SIZE_PAGE` | `2U * SIZE_PAGE` |
| `armv7a` | Source-specific bootstrap stack | `8U * 1024U` |
| `armv7m` | Source-specific bootstrap stack | `4U * SIZE_PAGE` |
| `armv7r` | `SIZE_PAGE` | `8U * 1024U` |
| `armv8m` | Source-specific bootstrap stack | `4U * SIZE_PAGE` |
| `armv8r` | `SIZE_PAGE` | `8U * 1024U` |
| `ia32` | Source-specific bootstrap stack | `2U * SIZE_PAGE` |
| `riscv64` | `4U * SIZE_PAGE` | `4U * SIZE_PAGE` |
| `sparcv8leon` with `NOMMU` | Source-specific bootstrap stack | `8U * SIZE_PAGE` |
| `sparcv8leon` with MMU | Source-specific bootstrap stack | `SIZE_PAGE` |

Some architectures use assembly bootstrap code for the initial kernel stack instead of exposing a
`SIZE_INITIAL_KSTACK` macro.

## Runtime checks

When `STACK_CANARY` is enabled or debug assertions are active, the scheduler checks the selected kernel context against
the top 90 percent of the kernel stack.
A failed check triggers `LIB_ASSERT_ALWAYS()` with the process ID, thread ID, stack base, and context pointer.

`threads_canaryInit()` writes a 16-byte `0x55, 0xaa` pattern to the user stack address stored in `thread_t.ustack`.
The scheduler verifies this pattern for process threads that have a user stack pointer.
This canary protects the user stack boundary tracked by the thread structure, while the kernel stack overflow check uses
the saved kernel context address.

## Release path

When a thread reaches the ghost cleanup path, the reaper releases its kernel stack with `vm_kfree(thread->kstack)`.
If the thread owns TLS storage, the reaper destroys it before freeing the thread object.

## vfork stack path

The `vfork()` implementation saves the active part of the parent kernel stack in `parentkstack` before the child runs in
the parent address space.
The child stores its original stack in `execkstack`, switches to the parent stack while executing the shared-address
phase, and restores the parent stack when the child exits or executes a new image.
