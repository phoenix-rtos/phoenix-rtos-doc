# Prototypes and definitions

System call wrappers are generated in the C library from the kernel syscall inventory.
The source inventory is the `SYSCALLS(ID)` macro in `phoenix-rtos-kernel/include/syscalls.h`.
The current macro declares 103 IDs, numbered from `0` to `102`.

Kernel handlers are implemented in `phoenix-rtos-kernel/syscalls.c`.
The dispatch table is generated from the same `SYSCALLS(ID)` macro, so the ID list and the kernel table share one
source of truth.
Handlers take the user stack pointer and read arguments with `GETFROMSTACK(stack_ptr, arg_type, var, id)`.

## Current syscall ID list

- 0-15: `debug`, `sys_mmap`, `sys_munmap`, `sys_fork`, `vforksvc`, `exec`, `spawnSyspage`,
  `sys_exit`, `sys_waitpid`, `threadJoin`, `getpid`, `getppid`, `gettid`, `beginthreadex`, `endthread`, `nsleep`.
- 16-33: `phMutexCreate`, `phMutexLock`, `mutexTry`, `mutexUnlock`, `phCondCreate`, `phCondWait`,
  `condSignal`, `condBroadcast`, `resourceDestroy`, `interrupt`, `portCreate`, `portDestroy`,
  `sys_portRegister`, `sys_portUnregister`, `msgSend`, `msgRecv`, `msgRespond`, `lookup`.
- 34-51: `gettime`, `settime`, `keepidle`, `platformctl`, `wdgreload`, `threadsinfo`, `meminfo`,
  `sys_perf_start`, `sys_perf_read`, `sys_perf_finish`, `sys_perf_stop`, `syspageprog`, `va2pa`,
  `signalHandle`, `signalPost`, `signalMask`, `signalSuspend`, `priority`.
- 52-67: `sys_read`, `sys_write`, `sys_open`, `sys_close`, `sys_link`, `sys_unlink`, `sys_fcntl`,
  `sys_ftruncate`, `sys_lseek`, `sys_dup`, `sys_dup2`, `sys_pipe`, `sys_mkfifo`, `sys_chmod`,
  `sys_fstat`, `sys_fsync`.
- 68-85: `sys_accept`, `sys_accept4`, `sys_bind`, `sys_connect`, `sys_gethostname`, `sys_getpeername`,
  `sys_getsockname`, `sys_getsockopt`, `sys_listen`, `sys_recvfrom`, `sys_sendto`, `sys_recvmsg`,
  `sys_sendmsg`, `sys_socket`, `sys_socketpair`, `sys_shutdown`, `sys_sethostname`, `sys_setsockopt`.
- 86-102: `sys_ioctl`, `sys_futimens`, `sys_poll`, `sys_tkill`, `sys_setpgid`, `sys_getpgid`,
  `sys_setpgrp`, `sys_getpgrp`, `sys_setsid`, `sys_spawn`, `release`, `sbi_putchar`, `sbi_getchar`,
  `sigreturn`, `sys_mprotect`, `sys_statvfs`, `sys_uname`.

## Wrapper and handler boundary

User-mode wrappers pass arguments according to the target application binary interface.
The syscall instruction transfers control to the kernel, where the dispatcher selects a handler by ID.

Kernel handlers validate user pointers where required before calling process, POSIX, VM, IPC, or HAL helper code.
Examples include `syscalls_sys_poll()`, which checks the `pollfd` array with `vm_mapBelongs()`, and
`syscalls_sys_futimens()`, which validates an optional `timespec` pointer before calling `posix_futimens()`.
