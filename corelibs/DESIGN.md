# Core Libraries — Design Observations

## Architecture Tiers

The 15 libraries organize into three tiers:

### High-level (User-facing)
- **libgraph**: 2D graphics with hardware acceleration
- **libcgi**: HTTP/CGI request handling
- **libswdg**: Software multichannel watchdog

### Mid-level (Device abstraction)
- **libvirtio**: VirtIO device management
- **libvga**: VGA display hardware
- **libuuid**: UUID generation (RFC 4122)
- **libcache**: N-way set-associative cache
- **libmodbus**: Modbus RTU industrial protocol
- **libtrace**: Performance/debug tracing

### Low-level (Infrastructure)
- **libstorage**: Storage device abstraction
- **libmtd**: Flash memory (MTD) interface
- **libptable**: Partition table management
- **libmbr**: Master Boot Record handling
- **libtinyaes**: AES encryption
- **libalgo**: Lock-free data structures

## Concurrency Design Patterns

- **Mutex-based**: `libcache` uses traditional mutex locking
- **Lock-free**: `libalgo` uses C11 atomics with cache-line alignment
- **Callback-driven**: `libswdg`, `libmodbus` invoke user-provided callbacks
- **Thread-safe by contract**: `libvirtio` documents thread-safety guarantees

## Storage Stack Composition

```
libmbr        → MBR partition table parsing
  ↓
libptable     → Phoenix-RTOS partition table format (v2)
  ↓
libmtd        → Flash memory device abstraction (NOR/NAND)
  ↓
libstorage    → Storage device registration + filesystem mounting
```

This stack supports the full path from boot sector to mounted filesystem.

## Standards Compliance

- **libuuid**: RFC 4122, DCE 1.1, Linux libuuid compatible
- **libmtd**: Based on Linux MTD interface
- **libmodbus**: Modbus RTU specification
- **libtinyaes**: NIST AES standard (multiple AEAD modes)
- **libmbr**: Standard PC MBR layout

## Hardware Acceleration

`libtinyaes` provides both:
- Generic software implementation
- STM32L4 hardware-accelerated variant (`aes_hw_stm32l4`)

This pattern could extend to other libraries where hardware acceleration is available.

## Development Timeline

```
2017–2020: libmbr, libptable (foundational)
2021–2022: libstorage, libmtd (storage infrastructure)
2024:      libtinyaes (security)
2025:      libtrace, libmodbus, libalgo (new capabilities)
```

Active development continues to add new capabilities, outpacing documentation.
