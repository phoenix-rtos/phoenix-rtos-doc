# Architecture Documentation — Undocumented Areas

## 1. Message Copy Minimization in Message Passing

The architecture uses a tiered strategy for IPC efficiency, implemented in `phoenix-rtos-kernel/include/msg.h` (lines 143–170) and `phoenix-rtos-kernel/proc/msg.c` (lines 36–200):
- **Inline**: Messages ≤ 64 bytes are carried in the `msg_t` structure's `raw[64]` union — no separate buffer allocation
- **Page mapping**: Larger buffers are mapped into the receiver's address space via `page_map()` calls in `msg_map()` — avoids copying entire pages
- **Boundary copy**: Only unaligned partial-page data at buffer boundaries requires actual copying, using wrapper page allocation

These optimizations are critical to the architecture's performance but not documented.

## 2. Virtual Memory Sharing Mechanism

How physical memory pages are shared between processes during message passing (`phoenix-rtos-kernel/proc/msg.c`):
- Page table entry sharing for mapped regions via `page_map(&dstmap->pmap, ...)`
- Copy-on-write for `fork()` via `vm_mapCopy()` in `phoenix-rtos-kernel/proc/process.c` (line 1534)
- Wrapper pages for partial-page transfers prevent interference between sender and receiver

## 3. System Call Instructions Per Architecture

Each architecture uses different privilege transition mechanisms, verified in source:
- **ARM Cortex-M**: SVC instruction — `phoenix-rtos-kernel/hal/armv7m/exceptions.c` (line 40: `"11 #SVC"`)
- **ARM Cortex-A**: SVC instruction — `phoenix-rtos-kernel/hal/armv7a/exceptions.S`
- **x86/IA32**: INT 0x80 — `phoenix-rtos-kernel/hal/ia32/arch/interrupts.h` (line 25: `#define SYSCALL_IRQ 0x80U`)
- **RISC-V**: ECALL — `phoenix-rtos-kernel/hal/riscv64/arch/cpu.h` (line 42: `#define SCAUSE_ECALL 8U`), handler in `_interrupts.S` (lines 276–280)
- **SPARC**: Trap instruction — `phoenix-rtos-kernel/hal/sparcv8leon/_traps.S` (lines 6–67: trap table)

The specific system call ABI (register conventions, return value handling) per architecture is not documented.

## 4. Namespace Structure

The port-based namespace and object identifier system is mentioned but not specified:
- Port registration via `portCreate()` + `portRegister()` syscalls
- Namespace resolution in `phoenix-rtos-kernel/proc/name.c`
- How ports map to filesystem paths
- Resolution order for overlapping registrations
- Namespace hierarchy and traversal

## 5. Memory Management Policies

MMU configuration, page table format, address space layout, and memory protection policies vary by architecture. Conditional compilation via `NOMMU` guards throughout `phoenix-rtos-kernel/proc/` and `phoenix-rtos-kernel/vm/` separates the MMU and non-MMU paths, but the dual-path design is not documented.

## 6. Thread Context Switching

Thread scheduling uses 8 priority levels (`ready[8]` array in `phoenix-rtos-kernel/proc/threads.c` line 42, with `MAX_PRIO` derived at line 70). Context switching saves/restores full `cpu_context_t` on kernel stack, `pmap_switch()` updates MMU on process switch. The mechanism is architecturally significant but not described.

## 7. POSIX Emulation Architecture

The `phoenix-rtos-posixsrv` provides POSIX-compatible interfaces (pipes, `/dev/null`, `/dev/zero`, `/dev/urandom`, pseudo-terminals) over the microkernel's message passing. Additionally, the kernel itself includes 16 file I/O syscalls and 18 socket syscalls (verified in `phoenix-rtos-kernel/syscalls.c` — 107 total `syscalls_*` functions) that are routed to servers. The boundary between kernel-level entry points and server-level handling is not documented.

## 8. Multi-core Architecture

Multi-core support is implemented:
- **IA32**: IPI via `hal_cpuBroadcastIPI()` and `hal_cpuSendIPI()` in `phoenix-rtos-kernel/hal/ia32/cpu.c` (lines 305–340), per-CPU tracking with `MAX_CPU_COUNT`
- **RISC-V**: Per-hart data structures (`hal_riscvHartData`), SBI-based IPI via `SBI_EXT_IPI (0x735049)` in `phoenix-rtos-kernel/hal/riscv64/sbi.c` (line 38)
- Boot hart centralized initialization; other harts wait
- Spinlock coordination via test-and-set

The multi-core architectural model (memory model, ordering guarantees, scheduling coordination) is not documented.
