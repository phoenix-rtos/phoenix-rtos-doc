# Core Libraries Documentation — Undocumented Areas

## 1. libtrace (2025, Adam Greloch)

Performance/debug trace library. Source: `phoenix-rtos-corelibs/libtrace/`.

Header `libtrace/include/trace.h` (line 20) defines trace channel struct with `name[16]`, configurable buffer size, and file output. Supports RTT (Real-Time Transfer) and rolling window modes. Multiple trace channels with background gathering at configurable sleep intervals.

## 2. libtinyaes (Aleksander Kaminski)

AES encryption library based on tiny-AES-c. Source: `phoenix-rtos-corelibs/libtinyaes/`.

Base modes in `aes.c` (ECB, CBC, CTR). Extended modes in separate files:
- **CCM\***: `aes_ccm_s.c` — Counter with CBC-MAC star mode (RFC 3610, AES-128 only)
- **EAX**: `aes_eax.c` — Encrypt-then-Authenticate-then-Translate (authenticated encryption)
- **GCM**: `aes_gcm.c` — Galois/Counter Mode (authenticated encryption)
- **KW**: `aes_kw.c` — Key Wrap
- **CMAC**: `cmac.c` — Cipher-based Message Authentication Code

STM32L4 hardware-accelerated variant: `aes_hw_stm32l4.c` / `aes_hw_stm32l4.h`.

Configuration in `include/aes.h` selects key size: `AES128`, `AES192`, or `AES256`.

## 3. libptable (Partition Table Management, v2)

Partition table management library. Source: `phoenix-rtos-corelibs/libptable/`.

`ptable.h` line 23: `#define PTABLE_VERSION 2`. Supports partition types: raw, jffs2, meterfs, futurefs. CRC checksum validation via `ptable_verify()` (`ptable.c` line 112). Little-endian serialization format. Partition entries with offset/size/type/CRC.

Used by `psdisk` host utility and bootloader.

## 4. libmtd (2022, Hubert Buczynski)

Memory Technology Device interface for flash memory (NOR/NAND). Source: `phoenix-rtos-corelibs/libmtd/`.

Erase operations with state tracking, out-of-band (OOB) data handling. Device flags: writeable, bit-writeable. Depends on `libstorage`.

## 5. libstorage (2021–2022, Lukasz Kosinski, Hubert Buczynski)

Storage device abstraction layer. Source: `phoenix-rtos-corelibs/libstorage/`.

Filesystem mounting/unmounting, device registration and management. Message-based I/O handling with configurable thread counts and queue sizes.

## 6. libmodbus (2025, Mateusz Kobak)

Modbus RTU master (client) library for industrial protocols. Source: `phoenix-rtos-corelibs/libmodbus/`.

Functions: read/write holding registers, read input registers. CRC error checking. Exception handling. Serial communication via user-provided read/write callbacks.

## 7. libalgo (2025, Ziemowit Leszczynski)

Lock-free single-producer single-consumer FIFO using C11 atomics. Source: `phoenix-rtos-corelibs/libalgo/lf-fifo.h`.

`_Static_assert` checks `ATOMIC_UINT_LOCK_FREE` and `ATOMIC_INT_LOCK_FREE` (lines 24–27). Uses `memory_order_acquire`/`memory_order_release` for lock-free operation. Cache-line aligned head/tail pointers. Power-of-2 buffer sizing. Both overwriting and non-overwriting modes. Header-only implementation.

## 8. libmbr (2017, 2020, Kamil Amanowicz, Lukasz Kosinski)

Master Boot Record parsing and management. Source: `phoenix-rtos-corelibs/libmbr/`.

Standard MBR layout (446-byte bootstrap code + 4 partition entries). CHS and LBA addressing. Partition type support: empty, Linux, protective GPT.

## 9. Missing Cross-Library Documentation

- No documentation for the storage hierarchy: `libmbr` → `libptable` → `libmtd` → `libstorage`
- No documentation for how these libraries compose to support device partitioning, filesystem mounting, and flash memory management
- No guidance on which libraries are needed for common embedded scenarios (boot image creation, flash programming, data logging)
