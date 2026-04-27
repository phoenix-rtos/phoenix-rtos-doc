# Host utilities

This chapter describes tools that run on the host computer to build, flash, and debug Phoenix-RTOS systems. After
reading this chapter, you will know how to use each host utility for firmware upload, disk image management, and
system debugging.

The source code of host utilities is in the
[phoenix-rtos-hostutils](https://github.com/phoenix-rtos/phoenix-rtos-hostutils) GitHub repository.

The following host utilities are available:

| Tool | Purpose |
|---|---|
| `phoenixd` | Host daemon for serial/USB/network communication with targets |
| `psu` | Serial uploader for flashing firmware via SDP/MCUBoot |
| `psdisk` | Disk image and partition table creator |
| `metaelf` | ELF metadata and CRC32 checksum embedder |
| `mcxisp` | MCX N94x series ISP (In-System Programming) tool |
| `mkrofs` | Read-Only File System image creator |
| `syspagen` | System page generator from PLO scripts |
| `trace` | RTT trace collection and conversion utilities |

> **Note:** `phoenixd` supports up to 8 concurrent device instances across all transport modes (serial, UDP, TCP, USB).

```{toctree}
:maxdepth: 1

psdisk.md
psu.md
phoenixd.md
hosttools.md
```
