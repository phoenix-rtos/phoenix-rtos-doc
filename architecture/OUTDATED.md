# Architecture Documentation — Outdated Points

## 1. ANSI C89 Reference

**Documentation says:** References ANSI C89 standard.

**Current code:** Uses modern C features (C11 atomics in libalgo, constructor attributes, etc.). The C89 reference is misleading.

**Recommendation:** Update to reflect actual C standard used in the codebase.

---

## 2. Message Passing Performance

**Documentation:** Acknowledges message passing overhead but does not quantify it.

**Current code:** Implements buffer optimizations (inline for small messages, shared page mapping for large messages, zero-copy for aligned data).

**Recommendation:** Document the optimization strategies and their performance implications.

---

## 3. Interrupt Redirection Mechanism

**Documentation says:** "Low-level I/O for redirecting interrupts" to threads.

**Current code:** Uses `interrupt()` syscall with callback returning condition variable signal. The mechanism is well-implemented but poorly explained in the architecture overview.

**Recommendation:** Provide clearer architectural description of the interrupt-to-thread mechanism.
