# Host Utilities Documentation — Undocumented Areas

## 1. Completely Undocumented Tools

### metaelf (2022)
Checksum and metadata ELF embedder. Supports ELF signature verification via CRC32, byte-order swapping, ELF32/64 support. Two modes: `checkCRC` and `writeCRC`. Used in the build process for image preparation.

### mcxisp (2024)
MCX N94x series ISP (In-System Programming) tool. Serial TTY communication at 576000 baud with frame-based protocol and CRC16 checksums. Frame types: Ack, Nak, Command, Data, Ping, PingResponse. Handles flash page operations (128 bytes).

### mkrofs (2024)
Read-Only File System (ROFS) image creator. Creates 256-byte node structures with directory tree support. Includes CRC32 checksumming, big/little-endian support, metadata embedding (timestamps, UID/GID, permissions). Command-line options: `-m` (endianness), `-d` (max depth).

### syspagen (2022)
System page generator from PLO scripts. Produces syspage32/64 format. Processes commands: alias, map, app, console. Supports memory allocation in syspage buffer with alignment and PHFS alias handling.

## 2. Undocumented phoenixd Features

- Multi-instance management with fork-based parallelism (up to 8 devices)
- Port parsing from `IP:port` strings for UDP/TCP
- USB_VYBRID mode with separate load and jump addresses
- BSP session-based protocol handling (`phoenixd_session()` function)

## 3. Undocumented psu Features

- **Full SDP protocol**: `sdp_writeRegister()`, `sdp_writeFile()`, `sdp_jmpAddr()`, `sdp_errStatus()`
- **MCUBoot protocol**: Distinct from SDP, with frame types and properties
- **Byte string parsing** with escaped characters
- **Dual protocol support**: Both SDP and MCUBoot in a single binary
- **Progress reporting** during file transfers (percentage output)
- **Script blob handling** with dynamic memory allocation

## 4. Undocumented psdisk Features

- Partition verification after write (`psdisk_verifyPartsTable()`)
- Integration with `libptable` library for serialization/deserialization
- Block size validation against partition table size
- File-existence-based conditional behavior for mode selection

## 5. Common Library (libhostutils-common)

All host tools link against a common library containing:
- Serial communication (`serial.c`)
- HID device access (`hid.*`)
- Type definitions and error codes
- Dispatch mechanisms (`dispatch.c`, `dispatch.h`)

This shared library is not documented.
