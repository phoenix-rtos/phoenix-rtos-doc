# Kernel undocumented areas

This status file has no open undocumented items after the current source audit.

| Former item | Resolution |
| --- | --- |
| Kernel launch and memory layout | Documented in `kernel/launch.md`. |
| Syspage handoff and build placement variables | Documented in `kernel/launch.md`. |
| Application ELF loading and heap mapping | Documented in `kernel/launch.md`. |
| Thread-specific kill | Documented in `kernel/syscalls/signals.md`. |
| Complete signal subsystem | Documented in `kernel/syscalls/signals.md`. |
| Thread-local storage | Documented in `kernel/proc/tls.md`. |
| Process address-space flags | Documented in `kernel/vm/flags.md`. |
| IPC buffer optimization | Documented in `kernel/proc/msg.md`. |
| Port unregistration | Documented in `kernel/syscalls/ipc.md`. |
| Kernel stack management | Documented in `kernel/proc/stacks.md`. |
| RISC-V SBI syscalls | Documented in `kernel/syscalls/riscv.md` and `kernel/hal/multicore.md`. |
| Device Tree Blob processing | Documented in `kernel/hal/dtb.md`. |
| Exception reporting | Documented in `kernel/proc/exceptions.md`. |
| Memory ordering and multicore | Documented in `kernel/hal/multicore.md`. |
| Additional file syscalls | Documented in `kernel/syscalls/file.md`. |
| Common routine API contracts | Documented in `kernel/lib.md`. |

Reopen this file when source exploration finds a kernel topic with no reader-facing documentation home.
