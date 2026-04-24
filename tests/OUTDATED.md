# Tests Documentation — Outdated Points

## 1. "Only User Space Tests" Statement

**Documentation says:** "Currently, only user space tests are supported."

**Current state:** No clarity on kernel-space testing plans or timeline. This statement may still be accurate but lacks context about whether kernel tests are planned or not.

**Recommendation:** Either update with current plans or remove the ambiguity.

---

## 2. Example Build Commands

**Documentation:** Shows specific build commands for running tests.

**Current code:** Build commands may not reflect current best practices depending on the target. The YAML `targets` filtering capability is not mentioned.

**Recommendation:** Verify and update all example commands against the current build system.
