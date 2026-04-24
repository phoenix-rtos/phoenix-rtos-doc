# Loader (PLO) Documentation — Outdated Points

## 1. Device Type Count

**Documentation says:** 4 device major types: UART, USB, STORAGE, TTY.

**Current code implements:** 9 device major types:
- 0: UART
- 1: USB
- 2: STORAGE
- 3: TTY
- 4: RAM (undocumented)
- 5: NAND_DATA (undocumented)
- 6: NAND_META (undocumented)
- 7: NAND_RAW (undocumented)
- 8: PIPE (undocumented)

**Recommendation:** Update device type documentation to reflect all 9 types.

---

## 2. Command Count

**Documentation lists:** ~20 CLI commands.

**Current code implements:** 24+ commands. Commands added since documentation freeze:
- `bridge` (2024): Serial device multiplexing
- `devices` (2024): Device enumeration
- `stop` (2024): Script control flow
- `bankswitch` (2022): Flash dual-bank switching
- `bootrom` (2023): ROM bootloader access
- `blob`: Embedded data loading
- `erase`: Flash erase
- `mem`: Memory access/inspection
- `watchdog`: Watchdog control
- `test-dev`: Device testing
- `jffs2`: JFFS2 cleanmarker writing
- `ptable`: Partition table parsing
- `kernelimg`: XIP kernel loading
- `vbe`: VGA modesetting (IA32)
- `lspci`: PCI enumeration (IA32)
- `otp`: OTP fuse programming (iMX RT/STM32N6)
- `reboot`: System reboot

**Recommendation:** Document all implemented commands.

---

## 3. Architecture Subsystem Count

**Documentation lists:** 5 subsystems: Cmds, Devices, HAL, Lib, PHFS.

**Current code:** 6 subsystems — the `riscv-sbi` module for RISC-V Supervisor Binary Interface is completely absent from architecture documentation.

**Recommendation:** Add riscv-sbi to the architecture overview.

---

## 4. PHFS Internal Limits Undocumented

**Current code shows hardcoded limits:**
- 8 device handlers maximum
- 32 file aliases maximum
- 256-byte command argument line
- 10 arguments per command
- 8 history entries

**Recommendation:** Document these limits for users who need to work within them.
