# Filesystem Reference

This section describes each filesystem server in detail, including its features, limitations, and typical use cases.

## dummyfs - In-Memory Filesystem

Source: `phoenix-rtos-filesystems/dummyfs/`

The `dummyfs` filesystem provides a volatile, RAM-backed file storage. All data is lost on reboot. It serves a similar
role to `tmpfs` on Linux.

**Features:**

- In-memory storage with lazy allocation (memory allocated on first write)
- Symlink support
- Object caching
- Mount/unmount support

**Use cases:** Temporary files, development and testing, `/tmp` equivalent on embedded targets.

## ext2 - Second Extended Filesystem

Source: `phoenix-rtos-filesystems/ext2/`

The `ext2` server implements the second extended filesystem format. It provides full read-write access to ext2-formatted
block devices.

**Features:**

- Inode-based file organization with block group structure
- Symlinks (short symlinks ≤60 bytes stored inline in the inode, longer ones in data blocks)
- Multiple inode types: regular file, directory, symlink, block device, character device
- Inode and block buffer caching

**Limitations:**

- The ext2 header (`sb.h`) defines fields for ext3/compression/encryption for format compatibility, but only base
  ext2 is implemented.
- No extended attributes
- No large file support beyond ext2 format limits

## FAT - File Allocation Table

Source: `phoenix-rtos-filesystems/fat/`

The FAT server provides **read-only** access to FAT12, FAT16, and FAT32 formatted media.

**Features:**

- FAT12, FAT16, and FAT32 format support
- Directory cache using red-black tree
- FAT chain caching
- Block device access via `libstorage` interface

**Limitations:**

- **Read-only.** All write operations (`write`, `truncate`, `link`, `unlink`) return `EROFS`. This is an
  implementation limitation, not a format constraint.

**Use cases:** Reading data from SD cards and USB mass storage devices formatted with FAT.

## JFFS2 - Journalling Flash File System 2

Source: `phoenix-rtos-filesystems/jffs2/`

The `jffs2` server implements a log-structured filesystem designed for NOR and NAND flash memory. It provides
wear leveling through garbage collection and crash resilience through its journaling design.

**Features:**

- NOR and NAND flash support (with write buffer for NAND)
- Compression: JFFS2 native, LZO, Rubin, and zlib algorithms
- Garbage collection with wear leveling
- ACL and extended attribute (xattr) support
- Symlink support

**Known limitations** (from the project's own `TODO` file):

- Asynchronous operations not fully implemented
- Compression tuning incomplete
- Checkpointing not implemented (scan-based mount is used instead; the developers note scan is "quite fast")
- Per-inode compression tuning via `chattr` not implemented
- NAND bad block checking incomplete

## LittleFS - Little File System

Source: `phoenix-rtos-filesystems/littlefs/`

The `littlefs` server implements a small filesystem designed for microcontrollers and embedded NOR flash. It provides
crash resilience using copy-on-write metadata pairs.

**Features:**

- Metadata pairs for crash resilience (power-loss safe)
- Block-level wear leveling with configurable cycle threshold
- Symlink support
- LRU object caching
- Read-only partition option
- Mount point and device file support

**Use cases:** Small NOR flash on Cortex-M and similar constrained targets.

## MeterFS - Meter/Logging Filesystem

Source: `phoenix-rtos-filesystems/meterfs/`

The `meterfs` server implements a fixed-structure filesystem for data logging. It is designed for reliability in metering
and industrial data acquisition applications.

**Features:**

- Fixed-size files with pre-allocated sectors
- Fixed-size records within files
- Log-style (FIFO) writing - when a file is full, oldest records are overwritten
- Write-verify for reliability
- Power control hooks
- Partial erase journal for crash recovery
- Debug facilities: unreliable write simulation and reboot trigger

**Limits:**

- Maximum file count is computed dynamically based on sector size: `MAX_FILE_CNT(ssz)` (defined in `files.h`)

**Use cases:** Energy metering, data logging, industrial sensor recording.

## ROFS - Read-Only File System

Source: `phoenix-rtos-filesystems/rofs/`

The `rofs` server provides read-only access to a pre-built filesystem image, typically placed in AHB-addressable
flash. It supports both direct memory mapping and indirect access via a device read callback.

**Features:**

- Direct memory mapping or indirect device read access
- Tree-based file index
- Checksum validation
- Minimal buffer (256 bytes)

**Use cases:** XIP (Execute-in-Place) firmware images, factory data, embedded resource storage. Images are created using
the `mkrofs` host utility.

## Pseudo-Filesystems

In addition to the disk-based filesystems above, the POSIX compatibility server (`phoenix-rtos-posixsrv`) provides
several pseudo-devices:

| Path | Description |
|---|---|
| `/dev/null` | Discards all data written to it |
| `/dev/zero` | Returns zero bytes on read |
| `/dev/urandom` | Returns random data |
| `/dev/full` | Returns `ENOSPC` on write |

The POSIX server also implements:

- **Named pipes** - FIFO communication channels with circular buffers and event notifications.
- **Pseudo-terminals (PTY)** - terminal emulation for remote access and serial console redirection.
