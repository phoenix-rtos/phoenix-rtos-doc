# Tests Documentation — Outdated Points

## 1. "Only User Space Tests" Statement

**Documentation says:** "Currently, only user space tests are supported."

**Current state:** No clarity on kernel-space testing plans or timeline. This statement may still be accurate but lacks context about whether kernel tests are planned or not.

**Recommendation:** Either update with current plans or remove the ambiguity.

---

## 2. Example Build Commands

**Documentation:** Shows specific build commands for running tests.

**Current code:** The test repo has architecture-specific Makefiles (`Makefile.host`, `Makefile.riscv64`, `Makefile.sparcv8leon`) alongside the main `Makefile`. The YAML `targets` filtering capability (e.g., `psh/test.yaml` line 2: `targets:` with `include`/`exclude` lists) is not mentioned in the documentation.

**Recommendation:** Verify and update all example commands. Document target filtering in YAML configs.
