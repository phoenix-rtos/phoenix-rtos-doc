# Loader (PLO) — Design Observations

## Flexible Subsystem Architecture

6 subsystems (Cmds, Devices, HAL, Lib, PHFS, riscv-sbi) with clean separation. New platforms only require HAL implementation. The approach mirrors the kernel's portability strategy.

## Dynamic Command Registration

No hardcoded command table. Uses custom linker section `.commands` with `__cmd_start`/`__cmd_end` anchors. Commands register via constructor attributes. This allows platform-specific commands to be included/excluded at link time.

## Device Major.Minor Identification

9 major device types (UART, USB, STORAGE, TTY, RAM, NAND_DATA, NAND_META, NAND_RAW, PIPE) with minor numbers for instances. This grew from the original 4-type design, indicating scope expansion over time.

## PHFS Protocol Abstraction

File access layer decouples bootloader logic from device/protocol details:
- "raw" protocol for direct device access
- "phoenixd" protocol for host communication
- Aliases map logical names to device+protocol pairs

## PLO Script Mechanism

Two-level configuration:
1. `preinit.plo.yaml` — target-level baseline configuration
2. `user.plo.yaml` — project-level overrides

Scripts are generated during build and embedded in the bootloader binary via `.data` section patching. This allows per-board boot sequences without recompiling the bootloader.

## Scope Evolution

PLO has expanded from a simple bootloader to include:
- **Diagnostics**: `mem`, `test-dev`, `devices`, `lspci`
- **Administration**: `otp`, `watchdog`, `erase`, `reboot`
- **Configuration**: `ptable`, `jffs2` cleanmarkers
- **Hardware setup**: `vbe` (graphics), `bridge` (serial mux), `bankswitch`

This scope creep is intentional for embedded systems that need hardware management capabilities before the OS boots.

## 33+ Platform-Specific Device Drivers

The PLO includes its own device driver collection (separate from the kernel's), covering UART, flash, storage, GPIO, and specialized interfaces. This duplication is necessary because PLO runs before the kernel and cannot use kernel drivers.

## RISC-V SBI Integration

The `riscv-sbi` module provides hardware abstraction specific to RISC-V platforms, bridging the bootloader to SBI firmware (OpenSBI or equivalent). This is architecturally significant but completely undocumented.
