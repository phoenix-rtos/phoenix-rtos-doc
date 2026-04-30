# System calls

System calls, also called syscalls, are kernel entry points for requests from user-space programs.
The kernel runs the syscall dispatcher in privileged mode, validates user-space arguments where needed, calls the
selected handler, and prepares the return to user mode.

The current syscall inventory is generated from the `SYSCALLS(ID)` macro in
`phoenix-rtos-kernel/include/syscalls.h`.
The macro declares 103 syscall IDs, and `phoenix-rtos-kernel/syscalls.c` creates the dispatch table from it.

| Category | Syscall IDs |
| --- | --- |
| Debug | `debug` |
| Memory | `sys_mmap`, `sys_munmap`, `sys_mprotect`, `va2pa`, `meminfo` |
| Processes and programs | `sys_fork`, `vforksvc`, `exec`, `sys_spawn`, `sys_exit`, `sys_waitpid` |
| Process information | `getpid`, `getppid`, `syspageprog`, `spawnSyspage`, `release`, `sys_uname` |
| Threads | `gettid`, `beginthreadex`, `endthread`, `threadJoin`, `nsleep`, `priority`, `threadsinfo` |
| Synchronization | `phMutexCreate`, `phMutexLock`, `mutexTry`, `phCondWait`, `condSignal` |
| Resources and IPC | `resourceDestroy`, `portCreate`, `sys_portRegister`, `msgSend`, `msgRecv`, `lookup` |
| File I/O | `sys_open`, `sys_close`, `sys_read`, `sys_write`, `sys_poll`, `sys_futimens`, `sys_statvfs` |
| Sockets | `sys_socket`, `sys_bind`, `sys_listen`, `sys_accept4`, `sys_recvmsg`, `sys_sendmsg` |
| Signals | `signalHandle`, `signalPost`, `signalMask`, `signalSuspend`, `sigreturn`, `sys_tkill` |
| Process groups | `sys_setpgid`, `sys_getpgid`, `sys_setpgrp`, `sys_getpgrp`, `sys_setsid` |
| Time, power, and platform | `gettime`, `settime`, `keepidle`, `platformctl`, `wdgreload` |
| Interrupts and performance | `interrupt`, `sys_perf_start`, `sys_perf_read`, `sys_perf_finish`, `sys_perf_stop` |
| RISC-V SBI | `sbi_putchar`, `sbi_getchar` |

```{note}
File I/O and socket syscalls have kernel-level entry points, but most operations are routed through the POSIX
compatibility layer to user-space servers, such as filesystem servers and `lwip`.
```

The C library wrappers for these system calls are documented in [Standard library](../../libc/index.md).

The pages below cover common syscall groups. For the complete source inventory, see
`phoenix-rtos-kernel/include/syscalls.h` and `phoenix-rtos-kernel/syscalls.c`.

```{toctree}
:maxdepth: 1

prototypes.md
add.md
debug.md
mem.md
proc.md
threads.md
sync.md
signals.md
ipc.md
file.md
socket.md
interrupts.md
perf.md
time.md
platform.md
riscv.md
```
