# Loader (PLO) Documentation — Outdated Points

## 1. Device Type Count

**Documentation says:** 4 device major types: UART, USB, STORAGE, TTY.

**Current code implements:** 9 device major types in `plo/devices/devs.h` (lines 21–29):
- 0: `DEV_UART`
- 1: `DEV_USB`
- 2: `DEV_STORAGE`
- 3: `DEV_TTY`
- 4: `DEV_RAM` (undocumented)
- 5: `DEV_NAND_DATA` (undocumented)
- 6: `DEV_NAND_META` (undocumented)
- 7: `DEV_NAND_RAW` (undocumented)
- 8: `DEV_PIPE` (undocumented)

Device array dimensioned as `SIZE_MAJOR=9` × `SIZE_MINOR=16` (`plo/devices/devs.c` lines 20–21).

**Recommendation:** Update device type documentation to reflect all 9 types.

---

## 2. Command Count

**Documentation lists:** ~20 CLI commands.

**Current code implements:** 36 command source files in `plo/cmds/`:
alias, app, bankswitch, bitstream, blob, bootcm4, bootrom, bridge, call, cmd, console, copy, devices, dump, echo, erase, go, help, jffs2, kernel, kernelimg, lspci, map, mem, mpu, otp, phfs, ptable, reboot, script, stop, test-ddr, test-dev, vbe, wait, watchdog.

**Recommendation:** Document all implemented commands, especially newer ones (bridge, devices, stop, bitstream, bootcm4, call, mpu, test-ddr).

---

## 3. Architecture Subsystem Count

**Documentation lists:** 5 subsystems: Cmds, Devices, HAL, Lib, PHFS.

**Current code:** 6 subsystems — the `riscv-sbi` module (`plo/riscv-sbi/`) for RISC-V Supervisor Binary Interface is completely absent from architecture documentation. Contains `entry.c`, core/, devices/, include/, ld/, platform/ subdirectories.

**Recommendation:** Add riscv-sbi to the architecture overview.

---

## 4. PHFS Internal Limits Undocumented

**Current code shows hardcoded limits:**
- `SIZE_PHFS_ALIASES = 32` file aliases — `plo/phfs/phfs.c` line 22
- `SIZE_CMD_ARG_LINE = 256` command argument line — `plo/cmds/cmd.h` line 23
- `SIZE_CMD_ARGV = 10 + 1` arguments per command — `plo/cmds/cmd.h` line 28
- `SIZE_HIST = 8` history entries — `plo/cmds/cmd.c` line 23
- Device limit: 9 major × 16 minor (`SIZE_MAJOR=9`, `SIZE_MINOR=16`) — `plo/devices/devs.c` lines 20–21

**Recommendation:** Document these limits for users who need to work within them.
