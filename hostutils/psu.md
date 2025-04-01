# Feniks Serial Uploader (psu)

`psu` is a tool designed to load firmware onto Feniks-RTOS devices using the SDP (Script Download Protocol) protocol.
This tool allows users to execute various commands on Feniks-RTOS devices by executing scripts containing
specific instructions. This tool can be used to upload firmware to NXP devices,
specifically targeting devices like `imxrt106x`, `imxrt117x`, and `imx6ull`.

## Usage

To use `psu`, follow the syntax:

```bash
psu [OPTIONS] script_path
```

Options:

- -t: Set timeout for wait command (default is 10 seconds),
- -h: Display help

## Example Usage

```bash
psu -t 15 script.sdp
```

## SDP Script Syntax

For information about supported command visit
[host-utils/psu](https://github.com/feniks-rtos/feniks-rtos-hostutils/tree/master/psu)

## See also

1. [Feniks-RTOS disk tool](psdisk.md)
2. [Feniks-RTOS daemon](feniksd.md)
3. [Feniks-RTOS Host Utilities](index.md)
4. [Table of Contents](../index.md)
