# Kernel Documentation — Undocumented Areas

## 1. Thread-Specific Kill

`sys_tkill` — Kill individual thread by TID. This is distinct from process-level `kill`. Ordering guarantees and behavior when targeting specific threads is not documented.

## 2. Complete Signal Subsystem

Syscalls (`signalHandle`, `signalPost`, `signalMask`, `signalSuspend`, `sigreturn`) are present in the kernel but entirely absent from documentation. The signal delivery algorithm, mask/pending interaction, and thread selection logic are undocumented.

## 3. Thread Local Storage (TLS)

HAL manages `hal_tls_t` for both process and thread level:
- Process stores GOT (Global Offset Table)
- TLS copied during process forking
- Architecture-specific TLS register management (e.g., TPIDR on ARM)

Zero documentation on TLS initialization, usage, or per-architecture behavior.

## 4. Process Address Space Flags

```c
unsigned int lazy : 1;  // Likely demand paging / lazy allocation
unsigned int lgap : 1;  // Left gap in address space
unsigned int rgap : 1;  // Right gap in address space
```

These flags affect memory allocation logic but are undocumented. They likely control address space layout for heap/stack gaps and lazy page fault handling.

## 5. IPC Buffer Optimization

`kmsg_layout_t` tracks buffer layout for partial-page handling:
- Inline for small messages (< page size)
- Mapped into receiver space for larger messages
- Partial page handling at unaligned boundaries
- Zero-copy potential for aligned page-sized transfers

## 6. Port Unregistration

`sys_portUnregister` is the inverse of `sys_portRegister` but is completely undocumented. Its semantics (what happens to pending messages, when is it safe to call) are not specified.

## 7. Kernel Stack Management

- Per-thread kernel stacks (`SIZE_KSTACK`)
- Initial bootstrap kernel stack (`SIZE_INITIAL_KSTACK`)
- Stack canaries for overflow detection (`threads_canaryInit()`)
- vfork special case: `parentkstack`, `execkstack` for parent suspension

## 8. RISC-V SBI Syscalls

`sbi_putchar` and `sbi_getchar` — RISC-V Supervisor Binary Interface calls present in the kernel syscall table. These provide console I/O via SBI firmware on RISC-V targets.

## 9. Device Tree Blob (DTB) Processing

RISC-V targets process Device Tree data during bootstrap. Referenced in HAL initialization code but not documented.

## 10. Exception Reporting

`process_dumpException()` provides crash dump information. `process_getName()` assists with debugging. Neither function's output format nor invocation conditions are documented.

## 11. Memory Ordering

No documentation on multicore memory ordering guarantees. The kernel uses spinlocks with architecture-specific barriers, but the memory model is not specified for application developers.

## 12. Device I/O Control

`sys_ioctl` present in kernel syscall table but marked as delegated to POSIX server. The boundary between kernel-level and server-level handling is unclear.

## 13. Additional Undocumented Syscalls

- `sys_poll` — file descriptor polling
- `sys_futimens` — file timestamp update
- `sys_statvfs` — filesystem statistics
- `keepidle` — connection keepalive
- `release` — resource release
