# Quickstart Documentation — Outdated Points

## 1. Missing Newer Targets

**Documentation:** Covers many targets but 11 targets in `_projects/` lack quickstart pages:
- `aarch64a53-zynqmp-qemu`
- `aarch64a53-zynqmp-som`
- `armv7a9-zynq7000-qemu`
- `armv7a9-zynq7000-zedboard`
- `armv7a9-zynq7000-zturn`
- `armv7r5f-zynqmp-qemu`
- `armv7r5f-zynqmp-som`
- `armv8m33-mcxn94x-frdm_cpu1`
- `armv8m55-stm32n6-nucleo`
- `host-generic-pc`
- `ia32-generic-pc`

**Current code:** 29 targets exist in `_projects/`, 18 have quickstart pages.

**Recommendation:** Add quickstart pages for all supported targets, especially QEMU ones that can be tried without hardware.

---

## 2. Image Component Lists Incomplete

**Documentation (ia32-generic-qemu example):** Lists bootloader (plo), kernel, TTY VGA, ATA, ext2fs as components.

**Current code:** Modern builds may include additional components (posixsrv, LwIP, more device drivers) depending on the project configuration.

**Recommendation:** Update component lists per-target to reflect current build outputs.

---

## 3. Script Location Convention

**Documentation:** Infers script locations from examples but doesn't explicitly state the convention.

**Current code:** 15 launch scripts in `scripts/` follow two naming patterns:
- `scripts/TARGET.sh` (e.g., `ia32-generic-qemu.sh`, `riscv64-generic-qemu.sh`)
- `scripts/run-TARGET.sh` (e.g., `run-armv7a7-imx6ull-evk.sh`)
- Some targets have variants: `ia32-generic-qemu-net.sh`, `ia32-generic-qemu-virt.sh`, `*-test.sh`

**Recommendation:** Explicitly document the script naming convention and the test/variant suffixes.
