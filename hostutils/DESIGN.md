# Host Utilities — Design Observations

## Modular Tool Architecture

Each host utility is a standalone binary with a single responsibility:
- **phoenixd**: Communication dispatcher and session manager
- **psdisk**: Partition table utility (thin wrapper around `libptable`)
- **psu**: Complex protocol handler (SDP + MCUBoot)
- **metaelf**: ELF metadata and checksum management
- **mcxisp**: MCX-specific ISP programming
- **mkrofs**: ROFS image creation
- **syspagen**: System page generation from PLO scripts

## Common Library Dependency

All tools link against `libhostutils-common`, providing:
- Serial communication
- HID device access
- Dispatch mechanisms
- Shared type definitions

## Multi-Protocol Bus Architecture (phoenixd)

Acts as a dispatcher router mapping modes to backends:
- `-p` → SERIAL mode → `serial_open()`
- `-m` → PIPE mode → pipe file handling
- `-i`/`-t` → UDP/TCP modes → network dispatch
- `-u` → USB_VYBRID mode → USB dispatch

Each mode can run in parallel via `fork()` (max 8 instances).

## Two-Level Protocol Design (psu)

- **High-level**: SDP/MCUBoot script syntax (human-readable commands)
- **Low-level**: HID/serial binary protocol (device communication)

Script parsing translates human commands to device-specific binary protocol frames.

## Partition Table Abstraction (psdisk)

Uses dependency injection via external `libptable` library:
- State management across three modes (CREATE/UPDATE/READ)
- Pipeline: Parse → Serialize → Write → Verify → Display

## Tool Evolution Timeline

```
2001/2004  → phoenixd (oldest, mature, v1.5)
2012       → psu + psdisk initial versions
2020       → psdisk overhaul
2022       → metaelf + syspagen (image processing)
2024       → mcxisp + mkrofs (newest MCX + ROFS support)
```

Recent tools (2022–2024) indicate active expansion of the build infrastructure without corresponding documentation updates.
