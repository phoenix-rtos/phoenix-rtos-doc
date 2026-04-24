# Kernel Documentation — Outdated Points

## 1. Syscall Count Mismatch

**Documentation:** Syscall chapter documents ~15 pages covering selected syscalls across categories (debug, memory, processes, threads, sync, IPC, time, interrupts, performance, platform, file, socket, riscv).

**Current code:** `phoenix-rtos-kernel/syscalls.c` contains 107 `syscalls_*` functions — the vast majority are undocumented. The syscall documentation pages exist at `kernel/syscalls/` but cover only a fraction of the total.

**Recommendation:** The syscall documentation needs a comprehensive audit. At minimum, all categories should list their full syscall inventories with prototypes.

---

## 2. vfork() Semantics Incomplete

**Documentation says:** "Child will exec() another program, parent can block."

**Current code:** `phoenix-rtos-kernel/proc/process.c`:
- Line 1377: `process_vforkThread()` — vfork implementation
- Lines 1401–1411: Parent's kernel stack is saved (`parentkstack = vm_kmalloc(...)`) and copied
- Lines 1320–1321: On child exec/exit, parent's kernel stack is restored from `parentkstack`
- Lines 1325–1370: `proc_vforkedExit()` handles unwinding with `execkstack` management

Parent is SUSPENDED until child calls `exec()` or `_exit()`. This is a full synchronization primitive, not just an optimization hint.

**Recommendation:** Document the parent suspension behavior and the kernel stack swapping mechanism.

---

## 3. Process Groups Underspecified

**Documentation mentions:** Process groups exist.

**Current code:** `phoenix-rtos-kernel/syscalls.c`:
- Line 1867: `syscalls_sys_setpgid()` — set process group
- Line 1878: `syscalls_sys_getpgid()` — get process group
- Line 1888: `syscalls_sys_setpgrp()` — set process group to self (calls `posix_setpgid(0, 0)`)
- Line 1900: `syscalls_sys_setsid()` — create new session

These enable job control and session management via `posix_setpgid()`, `posix_getpgid()`, `posix_setsid()`.

**Recommendation:** Document process group and session management syscalls.

---

## 4. Signal Handling — Only SIGCHLD Documented

**Documentation mentions:** SIGCHLD for termination notification.

**Current code:** `phoenix-rtos-kernel/syscalls.c` implements full signal subsystem:
- Line 1018: `syscalls_signalHandle()` — register signal handler
- Line 1036: `syscalls_signalPost()` — send signal to process
- Line 1076: `syscalls_signalMask()` — modify signal mask
- Line 1093: `syscalls_signalSuspend()` — suspend until signal
- Line 1102: `syscalls_sigreturn()` — return from signal handler
- Line 1853: `syscalls_sys_tkill()` — send signal to specific thread

**Recommendation:** Document the complete signal subsystem including delivery algorithm and mask/pending interaction.

---

## 5. Thread States

**Documentation says:** READY, SLEEP, GHOST.

**Current code:** `phoenix-rtos-kernel/proc/threads.h`:
- Line 27: `THREAD_END 1U` — request thread termination
- Line 28: `THREAD_END_NOW 2U` — immediate termination request
- Line 31: `READY 0U` — thread is ready to run
- Line 32: `SLEEP 1U` — thread is sleeping
- Line 33: `GHOST 2U` — thread has terminated, awaiting cleanup

`THREAD_END` and `THREAD_END_NOW` are flags for termination requests, not run states. The three run states (READY, SLEEP, GHOST) are correct but the termination flags should also be documented.

**Recommendation:** Document all thread states and termination flags. Document the reaper thread lifecycle.

---

## 6. File I/O and Socket Syscalls Boundary

**Documentation:** Treats file I/O and sockets as external to the kernel.

**Current code:** `phoenix-rtos-kernel/syscalls.c` includes syscall entry points for file I/O (read, write, open, close, link, unlink, fcntl, ftruncate, lseek, dup, dup2, pipe, mkfifo, chmod, fstat, fsync, poll, futimens, statvfs) and socket operations (accept, bind, connect, listen, recvfrom, sendto, socket, socketpair, shutdown, etc.) — these are routed to servers but have kernel-level entry points.

**Recommendation:** Clarify the kernel/server boundary for file I/O and socket operations.
