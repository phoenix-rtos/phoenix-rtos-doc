# Command-Line interface

The command-line interface allows the user to control the booting process.

## Usage

After successful booting by Boot ROM, the loader switches to interactive mode and the prompt `(plo)%`
is printed on the console.

```{note}
If the user defines a script which ends with the `go!` command, the loader jumps immediately
to the kernel and interactive mode is skipped.
```

### Limits

The following limits apply to CLI usage:

| Parameter | Value | Description |
|---|---|---|
| `SIZE_CMD_ARG_LINE` | 256 bytes | Maximum length of a command argument line |
| `SIZE_CMD_ARGV` | 11 | Maximum number of arguments per command (10 + terminator) |
| `SIZE_HIST` | 8 | Number of command history entries |

## Commands

The following commands are available in PLO. Some commands are available only on specific target platforms.

### Core Boot Commands

* `alias` — sets alias to file, usage: `alias [<name> <offset> <size>]`
* `app` — loads app, usage: `app [<dev> [-x] <name> <imap1;imap2...> <dmap1;dmap2...>]`
* `console` — sets console to device, usage: `console <major.minor>`
* `copy` — copies data between devices, usage: `copy <src dev> <file/offs size> <dst dev> <file/offs size>`
* `go!` — starts Phoenix-RTOS loaded into memory
* `kernel` — loads Phoenix-RTOS, usage: `kernel [<dev> [name]]`
* `kernelimg` — loads XIP (Execute-in-Place) kernel image
* `map` — defines memory map, usage: `map [<name> <start> <end> <attributes>]`
* `phfs` — registers device in PHFS, usage: `phfs [<alias> <major.minor> [protocol]]`
* `script` — shows script, usage: `script [<dev> <name> <magic>]`
* `wait` — waits in milliseconds or loops forever, usage: `wait [ms]`

### Diagnostic Commands

* `devices` — enumerates available devices
* `dump` — dumps memory, usage: `dump <addr>`
* `echo` — turns information logs on/off, usage: `echo [on/off]`
* `help` — prints the list of available commands
* `mem` — reads/writes memory directly
* `lspci` — enumerates PCI bus devices (IA32 only)
* `test-dev` — tests device functionality
* `test-ddr` — tests DDR memory
* `reboot` — reboots the system
* `stop` — halts script execution

### Flash/Storage Commands

* `blob` — loads embedded data blob
* `erase` — erases flash memory regions
* `jffs2` — writes JFFS2 cleanmarkers on flash
* `otp` — programs OTP (One-Time Programmable) fuses
* `ptable` — parses and displays partition table

### Hardware Control Commands

* `bitstream` — loads bitstream into FPGA PL, usage: `bitstream <dev> <name>`
* `bootcm4` — boots Cortex-M4 core on dual-core i.MX RT
* `bootrom` — accesses ROM bootloader
* `bridge` — serial device multiplexing
* `call` — calls user script from PHFS, usage: `call <dev> <script name> <magic>`
* `mpu` — prints MPU region usage, usage: `mpu [all]`
* `vbe` — VGA BIOS Extension modesetting (IA32 only)
* `watchdog` — configures hardware watchdog

### Commands registered via constructor

Commands use a linker-section-based plugin system. Each command registers itself at load time using
`__attribute__((constructor))` and is placed in the `.commands` section, bounded by `__cmd_start`/`__cmd_end` anchors.
Each platform selects its command set via the `PLO_COMMANDS` variable in its `Makefile`.
