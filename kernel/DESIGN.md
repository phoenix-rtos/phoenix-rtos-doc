# Kernel — Design Observations

## True Microkernel (~20K LoC)

The kernel delegates file I/O and sockets to external POSIX server. All inter-process communication flows through ports. A single syscall dispatcher routes all 107 syscalls via function pointer table (verified in `phoenix-rtos-kernel/syscalls.c`). Clean separation: `proc/`, `vm/`, `hal/`.

## Dual-Path Architecture (MMU vs Non-MMU)

```c
#ifndef NOMMU
    msg_t msg;    // Inline message structure (MMU: virtual addressing, COW)
#else
    msg_t *msg;   // Pointer to message (Non-MMU: physical addressing, simplified)
#endif
```

Same API but different internal implementation. Conditional compilation is scattered throughout `proc/` and `vm/`.

## Priority Scheduling

- 8 priority levels (0–7, lower = higher priority)
- Preemptive round-robin within each level
- No priority inheritance mechanism observed — risk of unbounded priority inversion with nested locks

## Process Lifecycle with Reaper Pattern

```
Process exit → GHOST thread state → Reaper thread cleanup → SIGCHLD to parent
```

Dedicated reaper thread handles zombie cleanup. Parent must reap children via signal handling.

## Copy-on-Write (BSD UVM Model)

- `amap`/`anon` structures for per-page tracking (not shadow object chains)
- Fork creates shared amaps with reference counts
- Write fault creates new anon, increments refcount
- Collapse merges when refcount drops to 1

## Synchronization Hierarchy

```
Spinlocks (active waiting, HAL-level)
  → Locks (passive waiting, scheduler-based)
    → Mutexes/Condition Variables (resource handles)
      → Message Passing (blocking, serialized IPC)
```

## Resource Handle Model

Unified handle namespace: mutexes, conditions, and ports share `idtree_t`. Per-process tracking via `process_t.resources`. Automatic cleanup on process exit destroys all handles.

## Hardware Context Switching

- Full `cpu_context_t` saved on kernel stack during interrupt/exception
- Scheduler picks new thread; `pmap_switch()` updates MMU on process switch
- No assembly in scheduler itself — context switching is entirely within HAL

## Message Buffer Optimization

- First ~64 bytes inline in `msg_t` header
- Larger messages: buffers mapped into receiver's address space
- Partial-page handling: wrapper pages prevent interference
- Copy-only for unaligned boundary data

## Multi-core Support

- RISC-V multi-hart: per-hart data structures (`hal_riscvHartData`)
- Boot hart centralized; other harts wait for initialization
- Inter-processor interrupts (IPI) for scheduling synchronization
- Spinlock coordination via test-and-set

## Two-Level Signal Handling

- Process-level: `sighandler` function pointer, process-wide `sigpend`/`sigmask`
- Thread-level: per-thread `sigmask` and `sigpend`
- `sys_tkill` can deliver signals to specific threads
- Signal delivery is not preemptive — checked from pending mask

## Kernel Stack Per-Thread

- Separate kernel stacks per thread (`SIZE_KSTACK`)
- Initial bootstrap stack (`SIZE_INITIAL_KSTACK`)
- Stack canaries for overflow detection
- vfork: `parentkstack`/`execkstack` support parent suspension
