# System calls

System call (commonly abbreviated to syscall) is an entry point to execute a specific user program's request to a
service from the kernel. The operating system kernel runs in a privileged mode to protect sensitive software and
hardware parts from the other software components. A user application executing in an unprivileged mode does not have
access to the protected data. Performing a hardware interrupt or conducting a trap handled by the kernel, the user
application can obtain sensitive data from the kernel, e.g. information about all processes running in the system.

The kernel implements 107 system calls organized into the following categories:

| Category | Examples |
|----------|----------|
| Debug | `debug` |
| Memory | `mmap`, `munmap`, `mprotect` |
| Processes | `getpid`, `getppid`, `exit`, `waitpid`, `vforked` |
| Threads | `beginthreadex`, `endthread`, `gettid`, `priority` |
| Synchronization | `mutexCreate`, `condWait`, `semaphoreCreate` |
| IPC | `portCreate`, `portRegister`, `portUnregister`, `msgSend`, `msgRecv`, `msgRespond` |
| File I/O | `open`, `close`, `read`, `write`, `dup`, `dup2`, `link`, `unlink`, `fcntl`, `ftruncate`, `lseek`, `fstat`, `fsync`, `pipe`, `mkfifo`, `chmod`, `poll`, `futimens`, `statvfs` |
| Sockets | `socket`, `bind`, `listen`, `connect`, `accept`, `sendto`, `recvfrom`, `shutdown`, `socketpair` |
| Interrupts | `interrupt` |
| Performance | `perf_start`, `perf_read`, `perf_finish` |
| Time | `gettime`, `settime` |
| Platform | `platformctl` |
| Signals | `signalHandle`, `signalPost`, `signalMask`, `signalSuspend`, `sigreturn`, `tkill` |
| Process groups | `setpgid`, `getpgid`, `setpgrp`, `setsid` |
| RISC-V | `sbi_putchar`, `sbi_getchar` |

> **Note:** File I/O and socket syscalls have kernel-level entry points but are routed to user-space servers
> (e.g., filesystem servers, `lwip`) via message passing. The kernel provides the syscall interface; the actual
> implementation resides in the server process.

The documented pages below cover the most commonly used syscalls. Refer to the
[prototypes](prototypes.md) page for a complete list of all syscall signatures.

```{toctree}
:maxdepth: 1

prototypes.md
add.md
debug.md
mem.md
proc.md
threads.md
sync.md
ipc.md
file.md
socket.md
interrupts.md
perf.md
time.md
platform.md
riscv.md
```
