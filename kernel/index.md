# Kernel

## Synopsis

The Phoenix-RTOS kernel provides process and thread management, virtual memory, message passing, synchronization,
system-call dispatch, hardware abstraction, tracing hooks, and bootstrap support.

The source tree is organized around the following areas:

| Area | Source paths | Documentation status |
| --- | --- | --- |
| Hardware abstraction layer | `hal/`, `include/arch/`, `syspage.c` | Covered by HAL overview and architecture pages. |
| Processes and threads | `proc/` | Covers scheduling, IPC, forking, synchronization, and namespace concepts. |
| Virtual memory | `vm/` | Covers paging, mapping, object handling, allocators, and protection topics. |
| System calls | `include/syscalls.h`, `syscalls.c` | `include/syscalls.h` declares 103 syscall IDs. |
| Common routines | `lib/` | Summarized in this chapter. Detailed API coverage remains limited. |
| POSIX boundary | `posix/`, file and socket syscall handlers | Kernel entry points route requests to servers. |
| Performance tracing | `perf/` | Syscall interface is documented. Buffer and event internals need more detail. |
| Internal tests | `test/` | Source-only coverage for kernel subsystem tests. |

The public syscall table is generated from the `SYSCALLS(ID)` macro in `include/syscalls.h`.
The dispatcher in `syscalls.c` traces syscall entry and exit, calls the selected handler, and prepares the user-mode
return path.

```{toctree}
:maxdepth: 1

hal/index.md
proc/index.md
vm/index.md
syscalls/index.md
lib.md
```
