# Libraries

Phoenix-RTOS core libraries provide reusable APIs for graphics, CGI helpers, VirtIO devices, software watchdogs,
cache frontends, UUID generation, and low-level VGA access.

The current source tree stores these libraries in `phoenix-rtos-corelibs/`. Example applications live under `_user/`.

## Library overview

The `phoenix-rtos-corelibs` repository contains 15 libraries. The following 7 have dedicated documentation.

| Library | Description |
| --- | --- |
| `libgraph` | Graphics library with graphic adapter drivers |
| `libcgi` | Common Gateway Interface library |
| `libvga` | Video Graphics Array access for graphic adapter implementations |
| `libvirtio` | Virtual I/O Device library for device emulation |
| `libuuid` | Universally Unique Identifier generation |
| `libcache` | N-way set-associative cache |
| `libswdg` | Multi-channel software watchdog |

The following 8 libraries do not yet have dedicated documentation pages.

| Library | Description |
| --- | --- |
| `libtinyaes` | AES encryption (ECB, CBC, CTR, CCM*, EAX, GCM, KW, CMAC). STM32L4 HW-accelerated variant. |
| `libptable` | Partition table management (v2). CRC checksum validation. |
| `libmtd` | Memory Technology Device interface for NOR/NAND flash |
| `libstorage` | Storage device abstraction (mount/unmount, device registration, message I/O) |
| `libmodbus` | Modbus RTU master (client) library for industrial protocols |
| `libalgo` | Lock-free SPSC FIFO using C11 atomics. Header-only. |
| `libmbr` | Master Boot Record parsing (standard MBR layout, CHS/LBA addressing) |
| `libtrace` | Trace data collection and formatting |

```{toctree}
:maxdepth: 1

libcgi.md
libvirtio.md
libvga.md
libgraph.md
libuuid.md
libcache.md
libswdg.md
```
