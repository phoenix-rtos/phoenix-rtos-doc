# Core Libraries Documentation — Undocumented Areas

## 1. libtrace (2025, Adam Greloch)

Performance/debug trace library with RTT and rolling window mode. Multiple trace channels with file output. Configurable buffer size and sleep intervals for background gathering.

## 2. libtinyaes (2024, Aleksander Kaminski)

Full-featured AES encryption library. Modes:
- **CBC**: Cipher Block Chaining
- **CTR**: Counter mode
- **ECB**: Electronic Codebook
- **CCM**: Counter with CBC-MAC (authenticated encryption)
- **EAX**: Encrypt-then-Authenticate-then-Translate
- **GCM**: Galois/Counter Mode (authenticated encryption)
- **KW**: Key Wrap
- **CMAC**: Cipher-based Message Authentication Code

Includes a generic software implementation and an STM32L4 hardware-accelerated variant (`aes_hw_stm32l4`).

## 3. libptable (Partition Table Management, v2)

Partition table management library supporting:
- Partition types: raw, jffs2, meterfs, futurefs
- CRC checksum validation
- Little-endian serialization format
- Partition entries with offset/size/type/CRC

Used by `psdisk` host utility and bootloader.

## 4. libmtd (2022, Hubert Buczynski)

Memory Technology Device interface for flash memory (NOR/NAND):
- Erase operations with state tracking
- Out-of-band (OOB) data handling
- Device flags: writeable, bit-writeable
- Depends on `libstorage`

## 5. libstorage (2021–2022, Lukasz Kosinski, Hubert Buczynski)

Storage device abstraction layer:
- Filesystem mounting/unmounting
- Device registration and management
- Message-based I/O handling with configurable thread counts and queue sizes

## 6. libmodbus (2025, Mateusz Kobak)

Modbus RTU master (client) library for industrial protocols:
- Functions: read/write holding registers, read input registers
- CRC error checking
- Exception handling
- Serial communication via user-provided read/write callbacks

## 7. libalgo (2025, Ziemowit Leszczynski)

Lock-free single-producer single-consumer FIFO using C11 atomics:
- Cache-line aligned head/tail pointers
- Power-of-2 buffer sizing
- Both overwriting and non-overwriting modes
- Header-only implementation

## 8. libmbr (2017, 2020, Kamil Amanowicz, Lukasz Kosinski)

Master Boot Record parsing and management:
- Standard MBR layout (446-byte bootstrap code + 4 partition entries)
- CHS and LBA addressing
- Partition type support: empty, Linux, protective GPT

## 9. Missing Cross-Library Documentation

- No documentation for the storage hierarchy: `libmbr` → `libptable` → `libmtd` → `libstorage`
- No documentation for how these libraries compose to support device partitioning, filesystem mounting, and flash memory management
- No guidance on which libraries are needed for common embedded scenarios (boot image creation, flash programming, data logging)
