# Quickstart Documentation — Outdated Points

## 1. Missing Newer Targets

**Documentation:** Does not mention newer targets.

**Current code:** Targets like `armv8m33-mcxn94x-frdm`, `armv8r52-mps3an536-qemu`, `armv8m55-stm32n6-nucleo` exist in `_projects/` but may not have quickstart pages.

**Recommendation:** Verify all targets in `_projects/` have corresponding quickstart documentation.

---

## 2. Image Component Lists Incomplete

**Documentation (ia32-generic-qemu example):** Lists bootloader (plo), kernel, TTY VGA, ATA, ext2fs as components.

**Current code:** Modern builds may include additional components (posixsrv, LwIP, more device drivers) depending on the project configuration.

**Recommendation:** Update component lists per-target to reflect current build outputs.

---

## 3. Script Location Convention

**Documentation:** Infers script locations from examples but doesn't explicitly state the convention.

**Current code:** Scripts follow `./scripts/TARGET-VARIANT.sh` naming pattern.

**Recommendation:** Explicitly document the script naming and location convention.
