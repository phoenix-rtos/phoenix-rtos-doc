# Kernel Documentation — Undocumented Areas

## 1. Thread-Specific Kill

`syscalls_sys_tkill()` at `phoenix-rtos-kernel/syscalls.c` line 1853 — sends signal to individual thread by TID. Distinct from process-level `kill`. Ordering guarantees and behavior when targeting specific threads is not documented.

## 2. Complete Signal Subsystem

All signal syscalls present in `phoenix-rtos-kernel/syscalls.c`:
- `syscalls_signalHandle()` (line 1018) — register signal handler
- `syscalls_signalPost()` (line 1036) — send signal
- `syscalls_signalMask()` (line 1076) — modify signal mask
- `syscalls_signalSuspend()` (line 1093) — suspend until signal delivered
- `syscalls_sigreturn()` (line 1102) — return from signal handler

The signal delivery algorithm, mask/pending interaction, and thread selection logic are entirely absent from documentation.

## 3. Thread Local Storage (TLS)

HAL manages `hal_tls_t` for both process and thread level. Process stores GOT (Global Offset Table). TLS is copied during process forking. Architecture-specific TLS register management (e.g., TPIDR on ARM, `tp` on RISC-V). Configuration and usage are undocumented.

## 4. Process Address Space Flags

Address space entry fields control memory allocation behavior but are undocumented. These likely control address space layout for heap/stack gaps and lazy page fault handling.

## 5. IPC Buffer Optimization

`phoenix-rtos-kernel/proc/msg.c` implements buffer layout for partial-page handling:
- Inline for messages ≤ 64 bytes (data carried in `msg_t` structure — `include/msg.h` lines 151, 163)
- Mapped into receiver space for larger messages via `page_map()` calls
- Wrapper page allocation for unaligned boundaries
- See also `msg-nommu.c` for the simplified non-MMU variant

## 6. Port Unregistration

`sys_portUnregister` is the inverse of `sys_portRegister` but is completely undocumented. Its semantics (what happens to pending messages, when is it safe to call) are not specified. Implementation in `phoenix-rtos-kernel/proc/ports.c`.

## 7. Kernel Stack Management

- Per-thread kernel stacks — `SIZE_KSTACK` defined per architecture
- Initial bootstrap kernel stack — `SIZE_INITIAL_KSTACK`
- Stack canaries for overflow detection (`threads_canaryInit()`)
- vfork special case: `parentkstack`, `execkstack` for parent suspension — `phoenix-rtos-kernel/proc/process.c` lines 1401–1411

## 8. RISC-V SBI Syscalls

`sbi_putchar` and `sbi_getchar` — RISC-V Supervisor Binary Interface calls present in the kernel. `phoenix-rtos-kernel/hal/riscv64/sbi.c` implements SBI extensions including IPI (`SBI_EXT_IPI 0x735049` at line 38). These provide console I/O and inter-hart communication via SBI firmware.

## 9. Device Tree Blob (DTB) Processing

RISC-V targets process Device Tree data during bootstrap. Referenced in HAL initialization code but the DTB parsing interface is not documented.

## 10. Exception Reporting

`process_dumpException()` provides crash dump information for debugging. Output format and invocation conditions are not documented.

## 11. Memory Ordering and Multi-core

No documentation on multicore memory ordering guarantees. The kernel uses spinlocks with architecture-specific barriers:
- IA32: IPI via `hal_cpuBroadcastIPI()` / `hal_cpuSendIPI()` (`hal/ia32/cpu.c` lines 305–340)
- RISC-V: SBI-based IPI (`hal/riscv64/sbi.c`)

The memory model for application developers is not specified.

## 12. Additional Undocumented Syscalls

From `phoenix-rtos-kernel/syscalls.c`, beyond the documented set:
- `sys_poll` — file descriptor polling
- `sys_futimens` — file timestamp update
- `sys_statvfs` — filesystem statistics
- Process group syscalls: `sys_setpgid` (line 1867), `sys_getpgid` (line 1878), `sys_setpgrp` (line 1888), `sys_setsid` (line 1900)
- `sys_tkill` (line 1853) — thread-level signal delivery
