# Loader design observations

## Flexible subsystem architecture

The loader is organized around `cmds`, `devices`, `hal`, `lib`, `phfs`, `riscv-sbi`, and `syspage`.
New platforms primarily add HAL and device implementations while reusing the command and PHFS layers.

## Dynamic command registration

Commands live in the `.commands` linker section and are bounded by `__cmd_start` and `__cmd_end`.
The target `PLO_COMMANDS` selection controls which command objects are linked.

## Device major and minor identification

PLO uses 9 major device types and 16 minor slots per major.
The major identifies the device class, and the minor identifies the instance assigned at initialization.

## PHFS protocol abstraction

File access layer decouples bootloader logic from device/protocol details:
- `raw` protocol for direct device access
- `phoenixd` protocol for host communication
- Aliases map logical names to device+protocol pairs

## PLO script mechanism

Two-level configuration:
1. `preinit.plo.yaml`: target-level baseline configuration
2. `user.plo.yaml`: project-level overrides

Scripts are generated during build and embedded in the bootloader binary through `.data` section patching.
This allows per-board boot sequences without recompiling the bootloader.

## Loader scope

PLO includes boot preparation, diagnostics, storage maintenance, and hardware setup commands:
- **Diagnostics**: `mem`, `test-dev`, `devices`, `lspci`
- **Administration**: `otp`, `watchdog`, `erase`, `reboot`
- **Configuration**: `ptable`, `jffs2` cleanmarkers
- **Hardware setup**: `vbe` (graphics), `bridge` (serial mux), `bankswitch`

These capabilities are used before the operating system starts.

## Platform-specific device drivers

PLO includes its own device driver collection for UART, flash, storage, GPIO, USB CDC, and specialized interfaces.
The loader runs before the kernel, so it cannot use kernel drivers.

## RISC-V SBI integration

The `riscv-sbi` module provides RISC-V firmware services, HART coordination, exceptions, interrupts, timer support,
FDT parsing, and console drivers for RISC-V loader targets.
