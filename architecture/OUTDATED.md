# Architecture Documentation — Outdated Points

## 1. ANSI C89 Reference

**Documentation says:** `libphoenix` is "compatible with ANSI C89" (`architecture/index.md`, line ~48).

**Current code:** The C library targets C89 API compatibility, but the wider codebase uses modern C features. For example, `phoenix-rtos-corelibs/libalgo/lf-fifo.h` (lines 24–27, 37–206) uses C11 `_Static_assert`, `atomic_load_explicit()`, `atomic_store_explicit()` with `memory_order_acquire`/`memory_order_release`. GCC `__attribute__((constructor))` is used throughout (e.g., PLO command registration, PSH applet registration).

**Recommendation:** Clarify that the C89 reference applies to `libphoenix` API compatibility, not the codebase as a whole. Note that internal code uses C11 features.

---

## 2. Message Passing Performance

**Documentation:** Acknowledges message passing overhead but does not quantify it or explain optimizations.

**Current code:** `phoenix-rtos-kernel/include/msg.h` (lines 143–170) defines inline data buffers of exactly 64 bytes (`unsigned char raw[64]` in both input and output parts). `phoenix-rtos-kernel/proc/msg.c` (lines 36–200) implements page-level sharing via `page_map()` for larger buffers and wrapper page allocation for partial-page transfers at unaligned boundaries.

**Recommendation:** Document the three-tier optimization: (1) inline for ≤64 bytes, (2) page mapping for larger aligned buffers, (3) copy-only for unaligned boundary data.

---

## 3. Interrupt Redirection Mechanism

**Documentation says:** "Low-level I/O for redirecting interrupts" to threads.

**Current code:** `phoenix-rtos-kernel/syscalls.c` (lines 698–725) implements the `interrupt()` syscall, extracting a handler function, data pointer, and **condition variable handle**. `phoenix-rtos-kernel/proc/userintr.c` (lines 83–85) shows the callback returning ≥ 0 triggers `proc_threadBroadcast(&ui->cond->queue)` to wake user-space threads.

**Recommendation:** Document the complete interrupt-to-thread pipeline: handler registered via `interrupt()` syscall runs in kernel context → returns ≥ 0 → condition variable broadcast → user-space thread wakes via `condWait()`.
