# Additional Host Tools

This section describes host utilities beyond the three primary tools (phoenixd, psu, psdisk).

## metaelf - ELF Metadata Embedder

Source: `phoenix-rtos-hostutils/metaelf/`

Embeds checksums and metadata into ELF files. Used in the build process for image preparation and integrity
verification.

**Features:**

- CRC32 checksum computation and embedding
- ELF signature verification
- Byte-order swapping for cross-platform support
- ELF32 and ELF64 format support

**Modes:**

- `checkCRC` - verify the CRC of an existing ELF
- `writeCRC` - compute and embed CRC into the ELF

## mcxisp - MCX ISP Tool

Source: `phoenix-rtos-hostutils/mcxisp/`

In-System Programming tool for the NXP MCX N94x series microcontrollers. Communicates over serial TTY at 576000 baud
using a frame-based protocol with CRC16 checksums.

**Protocol frame types:**

| Frame | Purpose |
|---|---|
| Ack | Acknowledgment |
| Nak | Negative acknowledgment |
| Command | Command frame |
| Data | Data payload |
| Ping | Connection test |
| PingResponse | Connection test reply |

Flash page operations use 128-byte pages.

## mkrofs - ROFS image creator

Source: `phoenix-rtos-hostutils/mkrofs/`

Creates Read-Only File System images for use with the `rofs` filesystem server. The resulting image can be placed
in flash and accessed via direct memory mapping.

**Usage:**

```shell
mkrofs [OPTIONS] <source_directory> <output_image>
```

**Options:**

- `-m` - select endianness (big or little)
- `-d` - set maximum directory depth

**Image format:**

- 256-byte node structures
- Directory tree with CRC32 checksums
- Metadata: timestamps, UID/GID, permissions

## syspagen - System page generator

Source: `phoenix-rtos-hostutils/syspagen/`

Generates system page structures from PLO loader scripts. The system page contains the hardware configuration data
that the kernel reads during startup.

**Supported commands:**

- `alias` - define file aliases
- `map` - define memory maps
- `app` - register applications
- `console` - set console device

**Output formats:** syspage32 (32-bit) and syspage64 (64-bit).

## trace - Tracing utilities

Source: `phoenix-rtos-hostutils/trace/`

Collection of Python scripts for collecting and converting trace data from target devices.

**Components:**

- `collect_rtt_trace.py` - captures RTT (Real-Time Transfer) trace data from the target through OpenOCD
- `convert.sh` / `rootfs_convert.sh` - conversion pipelines
- `ctf_to_proto/` - converts Common Trace Format (CTF) to protocol buffers
- `get_rootfs_offset.sh` - finds the rootfs offset in a firmware image

## Common Library

Source: `phoenix-rtos-hostutils/common/`

All host tools share a common library that provides:

- **Serial communication** (`serial.c`) - platform-independent serial port access
- **HID device access** (`hid.c`) - USB HID communication for SDP protocol
- **Script parsing** (`script.c`) - SDP/MCUBoot script file parsing
- **USB communication** (`usb_imx.c`, `usb_vybrid.c`) - platform-specific USB transports
