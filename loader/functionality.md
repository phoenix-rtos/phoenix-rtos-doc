# Functionality

The loader can be used as a first-stage or second-stage bootloader.
It can be loaded to RAM with JLink or vendor tools, or booted from supported devices such as NOR flash, NAND flash, and
SD card.

Acting as a first-stage, plo configures the memory controllers and a variety of supported devices on a dedicated
platform. It is also responsible for setting the initial processor's clocks values and preparing the board for the
kernel. The loader runs in a supervisor mode and doesn't support FPU and MMU on all architectures.

During the second-stage of booting, it loads the operating system and selected applications from storage devices or via
interfaces like serial or USB (acting as USB client) to the memory. For more complex platforms, additional work can
be performed like loading bit stream to FPGA or testing specific components.

The command-line interface controls the boot process on a serial port or another configured console.
The loader requires explicit device aliases and physical memory maps as destinations for data and file copies.
This makes hardware setup visible before the operating system starts.
All available commands are described in the [CLI chapter](cli.md).

## Script system

PLO executes a pre-init script embedded in the loader binary.
The command subsystem exposes this script through the `script[]` linker symbol, and `cmd_run()` passes it to
`cmd_parse()`.

Scripts are command streams parsed with the same limits as interactive input:

| Limit | Value |
| --- | --- |
| Command line buffer | 256 bytes |
| Arguments per command | 10 arguments plus a terminating `NULL` entry |
| Interactive history | 8 entries |

The `script` command displays the embedded script or reads a script from a PHFS device.
The `call` command loads and executes a script from a PHFS file after checking the supplied magic value.
The `stop` command halts script execution.

Examples of booting scripts are located in the building files of the supported targets in
[phoenix-rtos-project/_targets](https://github.com/phoenix-rtos/phoenix-rtos-project/tree/master/_targets).
