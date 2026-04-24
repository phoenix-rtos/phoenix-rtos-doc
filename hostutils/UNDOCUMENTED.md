# Host Utilities Documentation — Undocumented Areas

## 1. Completely Undocumented Tools

### metaelf (2022) — `phoenix-rtos-hostutils/metaelf/`
Checksum and metadata ELF embedder. Supports ELF signature verification via CRC32, byte-order swapping, ELF32/64 support. Two modes: `checkCRC` and `writeCRC`. Used in the build process for image preparation.

### mcxisp (2024) — `phoenix-rtos-hostutils/mcxisp/`
MCX N94x series ISP (In-System Programming) tool. Serial TTY communication at 576000 baud with frame-based protocol and CRC16 checksums. Frame types: Ack, Nak, Command, Data, Ping, PingResponse. Handles flash page operations (128 bytes).

### mkrofs (2024) — `phoenix-rtos-hostutils/mkrofs/`
Read-Only File System (ROFS) image creator. Creates 256-byte node structures with directory tree support. Includes CRC32 checksumming, big/little-endian support, metadata embedding (timestamps, UID/GID, permissions). Command-line options: `-m` (endianness), `-d` (max depth).

### syspagen (2022) — `phoenix-rtos-hostutils/syspagen/`
System page generator from PLO scripts. Produces syspage32/64 format. Processes commands: alias, map, app, console. Supports memory allocation in syspage buffer with alignment and PHFS alias handling.

### trace (host-side) — `phoenix-rtos-hostutils/trace/`
RTT trace collection and conversion utilities. Python scripts for:
- `collect_rtt_trace.py` — collects RTT trace data from target
- `convert.sh` / `rootfs_convert.sh` — conversion pipelines
- `ctf_to_proto/` — CTF (Common Trace Format) to protocol buffer conversion
- `get_rootfs_offset.sh` — finds rootfs offset in image

## 2. Undocumented phoenixd Features

- Multi-instance management with fork-based parallelism (up to 8 devices) — `phoenixd.c` lines 198–291
- Port parsing from `IP:port` strings for UDP/TCP
- USB_VYBRID mode with separate load and jump addresses
- BSP session-based protocol handling (`phoenixd_session()` function)
- TCP mode (`-t` option) — `phoenixd.c` lines 219–222, 321–329

## 3. Undocumented psu Features

- **Full SDP protocol**: implemented in `psu/` with `sdp_writeRegister()`, `sdp_writeFile()`, `sdp_jmpAddr()`, `sdp_errStatus()`
- **MCUBoot protocol**: separate from SDP, with frame types and properties
- **Script syntax**: documented in `phoenix-rtos-hostutils/psu/README.md` but not in official docs
- **Progress reporting** during file transfers (percentage output)

## 4. Undocumented psdisk Features

- Partition verification after write (`psdisk_verifyPartsTable()`)
- Integration with `libptable` library for serialization/deserialization
- Three implicit operational modes: CREATE_IMG, UPDATE_IMG, READ_IMG (`psdisk.c` lines 51–53, 555–574)

## 5. Common Library (`phoenix-rtos-hostutils/common/`)

All host tools link against a common library containing:
- Serial communication (`common/serial.c`)
- HID device access (`common/hid.c`)
- Script parsing (`common/script.c`)
- USB communication (`common/usb_imx.c`, `common/usb_vybrid.c`)
- Shared type definitions (`common/include/hostutils-common/`)

This shared library is not documented.
