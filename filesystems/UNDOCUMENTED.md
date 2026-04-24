# Filesystems Documentation — Undocumented Areas

## 1. All Disk-Based Filesystems (7 total)

### dummyfs — In-Memory Filesystem
- Source: `phoenix-rtos-filesystems/dummyfs/`
- Pure in-memory storage (no backing device)
- Lazy allocation (memory allocated on first write)
- Symlinks support
- Mounting/unmounting, object caching
- Used as tmpfs replacement and for development/testing

### ext2 — Extended Filesystem 2
- Source: `phoenix-rtos-filesystems/ext2/`
- Full ext2 format support with inode-based organization
- Block groups, symlinks (short ≤60 bytes in inode, long as blocks)
- Multiple inode types: regular, directory, symlink, block device, char device
- Compression, encryption, journal fields defined but not implemented

### fat — FAT12/FAT16/FAT32
- Source: `phoenix-rtos-filesystems/fat/`
- **Read-only** (`libfat_write()` returns `-EROFS` — `fat/libfat.c` lines 95–115)
- Directory cache with red-black tree, FAT chain cache
- `libstorage` interface for device access

### jffs2 — Journalling Flash File System 2
- Source: `phoenix-rtos-filesystems/jffs2/`
- Full JFFS2 implementation with compression (JFFS2, LZO, Rubin, Zlib algorithms)
- Garbage collection with wear leveling
- NAND flash support with write-buffer
- ACL support, extended attributes (xattr), symlinks
- Known incomplete: async operations, compression tuning, checkpointing

### littlefs — Small Embedded Filesystem
- Source: `phoenix-rtos-filesystems/littlefs/`
- Metadata pairs for crash resilience
- Block-level wear leveling with configurable cycles threshold
- Symlinks support, LRU object caching
- Read-only partition option
- Mount point and device file support

### meterfs — Meter/Logging Filesystem
- Source: `phoenix-rtos-filesystems/meterfs/`
- Fixed-size files with pre-allocated sectors
- Maximum file count computed dynamically: `MAX_FILE_CNT(ssz)` in `meterfs/files.h` line 23
- Fixed-size records within files, log-style writes (FIFO when full)
- Circular buffer semantics
- Write-verify for reliability, power control hooks
- Partial erase journal for crash recovery
- Unreliable write simulation and debug reboot trigger

### rofs — Read-Only File System (2024, Gerard Swiderski)
- Source: `phoenix-rtos-filesystems/rofs/`
- Read-only filesystem in AHB address space
- Direct memory mapping or indirect access via device read callback
- Tree-based file index, checksum validation
- Minimal buffer (256 bytes)

## 2. Pseudo-Filesystems in POSIX Server

Implemented in `phoenix-rtos-posixsrv/special.c` (lines 233–249):
- `/dev/null` — memory sink (line 233)
- `/dev/zero` — zero source (line 238)
- `/dev/urandom` — random data source (line 244)
- `/dev/full` — full disk simulator, returns ENOSPC on write (line 249)

Additional pseudo-device support:
- **Pipes** — `phoenix-rtos-posixsrv/pipe.c` — named pipes with circular buffer, link/unlink, event notifications
- **PTY** — `phoenix-rtos-posixsrv/pty.c` — pseudo-terminal support

## 3. Missing Architectural Documentation

- How filesystem servers interact with mount points and namespace management
- The serialization protocol for file server communication
- How to mount block devices to filesystems
- Lock mechanisms (JFFS2 complex locking, littlefs LRU, meterfs power hooks)
- Cache behavior (dummyfs object cache, FAT red-black tree, littlefs LRU, ext2 inode/block buffers)
- Error handling semantics across different filesystems
- Performance characteristics (GC overhead, memory overhead, access patterns)
- Mount point traversal across filesystem boundaries ("." and ".." handling)
- ROFS image format specification (binary layout, tree structure, checksum algorithm)

## 4. Missing Feature Comparison Matrix

No documentation compares filesystem features:
- Read/write support
- Wear leveling
- Compression
- Crash resilience
- Flash type requirements (NOR vs NAND)
- Maximum file count/size
- Recommended use cases
