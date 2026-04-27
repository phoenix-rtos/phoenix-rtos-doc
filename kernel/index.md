# Kernel

## Synopsis

This chapter covers the kernel's internal structure (HAL, VM, proc, lib, test subsystems), process and thread management, message-passing optimizations, signal delivery, and system call organization.

Phoenix-RTOS is based on a written-from-scratch dedicated microkernel consisting of about 20K lines of code (LoC).
The microkernel is responsible for:

- Memory management (virtual memory, page allocation, kernel heap)
- Thread and process management (scheduling, forking, signals, process groups)
- Inter-thread communication and synchronization (message passing, mutexes, condition variables, semaphores)
- System call interface (107 syscalls across 14 categories)

The kernel is divided into five subsystems:

| Subsystem | Purpose |
|-----------|---------|
| `hal`  | Hardware abstraction layer - architecture-specific CPU, MMU, timer, interrupt, and console code |
| `lib`  | Common routines - string operations, printf, binary buddy allocator, red-black trees |
| `vm`   | Virtual memory management - page allocator, kernel allocator, memory mapper, object cache |
| `proc` | Process and thread management - scheduler, IPC, synchronization, namespace, signals |
| `test` | Internal tests for kernel subsystems |

```{toctree}
:maxdepth: 1

hal/index.md
proc/index.md
vm/index.md
syscalls/index.md
lib.md
```
