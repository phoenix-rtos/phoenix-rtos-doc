# Phoenix Serial Uploader (psu)

`psu` is a tool designed to load firmware onto Phoenix-RTOS devices using the SDP (Script Download Protocol) protocol.
This tool allows users to execute various commands on Phoenix-RTOS devices by executing scripts containing
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
[host-utils/psu](https://github.com/phoenix-rtos/phoenix-rtos-hostutils/tree/master/psu)
