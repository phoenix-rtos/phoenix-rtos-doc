# Utilities Documentation — Outdated Points

## 1. nandtool — Mentioned But Not Documented

**Documentation:** Listed in `index.md` with a brief sentence. No dedicated documentation page exists.

**Current code:** Full implementation in `phoenix-rtos-utils/nandtool/`.

**Recommendation:** Create a documentation page for nandtool with usage, options, and examples.

---

## 2. cm4-tool — Mentioned But Not Documented

**Documentation:** Listed in `index.md` with a brief sentence. No dedicated documentation page.

**Current code:** Full implementation for imxrt117x-cm4 communication.

**Recommendation:** Create a documentation page for cm4-tool.

---

## 3. psd.md Is a Stub

**Documentation:** Contains only a placeholder `<!-- #TODO: add more information -->`.

**Current code:** Full Phoenix Serial Downloader implementation.

**Recommendation:** Expand psd.md with protocol description, usage guide, and supported platforms.

---

## 4. Missing PSH Applets from Documentation

**Documentation lists:** 48 applets.

**Current code (Makefile `PSH_ALLCOMMANDS`):** Missing from docs:
- `chmod` — file permission changes
- `hd` — hex dump
- `route` — routing table management

**Recommendation:** Add documentation pages for chmod, hd, and route applets.

---

## 5. PSH Applet List Inconsistency

**Documentation (`psh/index.md`):** Lists `clear`, `exit`, `reset`, `history`, `export`, `unset`, `pshlogin` as applets.

**Current code:** `clear`, `exit`, `reset`, `history` are internal shell commands in `pshapp.c`, not separate applet directories. `export` and `unset` are in `env.c`.

**Recommendation:** Clarify which are standalone applets and which are built-in shell commands.
