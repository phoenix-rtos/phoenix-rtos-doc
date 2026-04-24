# Kernel Documentation — Outdated Points

## 1. Syscall Count Mismatch

**Documentation lists:** ~40 syscalls across categories (debug, memory, processes, threads, sync, IPC, time, interrupts, performance, platform).

**Current code implements:** ~106 syscalls total, including ~65 that are not documented.

**Recommendation:** The syscall documentation needs a comprehensive audit. At minimum, all categories should be listed with their full syscall inventories.

---

## 2. vfork() Semantics Incomplete

**Documentation says:** "Child will exec() another program, parent can block."

**Current code:** Parent is SUSPENDED (state set to blocked) until child calls `exec()` or `_exit()`. This is a full synchronization primitive with `parentkstack`/`execkstack` management, not just an optimization hint.

**Recommendation:** Document the parent suspension behavior and the kernel stack swapping mechanism used during vfork.

---

## 3. Process Groups Underspecified

**Documentation mentions:** Process groups exist.

**Current code implements:** Complete syscall interface — `setpgid`, `getpgid`, `setpgrp`, `getpgrp`, `setsid`. These enable job control and session management.

**Recommendation:** Document process group and session management syscalls.

---

## 4. Signal Handling — Only SIGCHLD Documented

**Documentation mentions:** SIGCHLD for termination notification.

**Current code implements:** Full signal subsystem with dual-level handling:
- Process-level: `sighandler`, `sigpend`, `sigmask`
- Thread-level: per-thread `sigmask` and `sigpend`
- Syscalls: `signalHandle`, `signalPost`, `signalMask`, `signalSuspend`, `sigreturn`

**Recommendation:** Document the complete signal subsystem including delivery algorithm and mask/pending interaction.

---

## 5. Thread States

**Documentation says:** READY, SLEEP, GHOST.

**Current code:** Additional states exist (`THREAD_END`, `THREAD_END_NOW`), plus the reaper trigger mechanism for ghost cleanup.

**Recommendation:** Document all thread states and the reaper thread lifecycle.

---

## 6. File I/O and Socket Syscalls Boundary

**Documentation:** Treats file I/O and sockets as external to the kernel.

**Current code:** The kernel implements 16 file I/O syscalls (read, write, open, close, link, unlink, fcntl, ftruncate, lseek, dup, dup2, pipe, mkfifo, chmod, fstat, fsync) and 18 socket syscalls (accept, bind, connect, listen, recvfrom, sendto, socket, socketpair, shutdown, etc.).

**Recommendation:** Clarify the kernel/server boundary for file I/O and socket operations. Even if delegated to servers, the syscall entry points exist in the kernel.
