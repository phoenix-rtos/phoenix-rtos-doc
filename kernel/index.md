# Kernel

## Synopsis

After reading this chapter, you will know:

- How the Phoenix-RTOS microkernel is structured into HAL, VM, proc, lib, and test subsystems
- How processes and threads are managed, including `fork()`, `vfork()`, and thread lifecycle
- How message passing works with inline, page-mapped, and boundary-copy optimizations
- How the signal subsystem delivers signals to processes and threads
- How the system calls are organized across categories

For a high-level overview of where the kernel fits in the system, see [Architecture](../architecture/index.md).

Phoenix-RTOS is based on a written-from-scratch dedicated microkernel consisting of about 20K lines of code (LoC).
The microkernel is responsible for:

- Memory management (virtual memory, page allocation, kernel heap)
- Thread and process management (scheduling, forking, signals, process groups)
- Inter-thread communication and synchronization (message passing, mutexes, condition variables, semaphores)
- System call interface (107 syscalls across 14 categories)

The kernel is divided into five subsystems:

| Subsystem | Purpose |
|-----------|---------|
| `hal`  | Hardware abstraction layer  -  architecture-specific CPU, MMU, timer, interrupt, and console code |
| `lib`  | Common routines  -  string operations, printf, binary buddy allocator, red-black trees |
| `vm`   | Virtual memory management  -  page allocator, kernel allocator, memory mapper, object cache |
| `proc` | Process and thread management  -  scheduler, IPC, synchronization, namespace, signals |
| `test` | Internal tests for kernel subsystems |

```{toctree}
:maxdepth: 1

hal/index.md
proc/index.md
vm/index.md
syscalls/index.md
lib.md
```
