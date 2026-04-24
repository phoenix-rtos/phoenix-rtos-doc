# Filesystems — Design Observations

## Server-Based Microservice Architecture

Each filesystem runs as a separate user-level server. Communication via message-passing protocol. Mount points register in namespace. Device detection via OID port comparison. Enables independent evolution of filesystems.

## Use-Case Specialization

Filesystems are highly specialized for different embedded scenarios:

| Filesystem | Use Case | Storage Type | Read/Write |
|-----------|----------|-------------|------------|
| dummyfs   | tmpfs / development | RAM | R/W |
| ext2      | General Unix compatibility | Block device | R/W |
| fat       | Removable media | Block device | Read-only |
| jffs2     | NOR flash with wear leveling | NOR flash | R/W |
| littlefs  | Small embedded with resilience | Flash | R/W |
| meterfs   | IoT telemetry / fixed-record logging | Flash | R/W (append) |
| rofs      | Immutable XIP images | Memory-mapped | Read-only |

## Crash Resilience Strategies

Each filesystem handles crash recovery differently:
- **ext2**: Journal fields defined but unused (potential future optimization)
- **jffs2**: Garbage collector + atomic operations
- **littlefs**: Metadata pairs provide automatic recovery
- **meterfs**: Sector redundancy + write-verify + partial erase journal
- **dummyfs**: No persistence needed (in-memory)

## Compression Support

Only JFFS2 supports transparent compression:
- JFFS2-specific algorithm
- LZO (fast compression)
- Rubin (embedded-optimized)
- Zlib (standard deflate)

Compression is transparent to callers.

## Wear Leveling Distribution

- **littlefs**: Block-level with configurable cycle threshold
- **jffs2**: Garbage collector provides wear distribution
- **meterfs**: Sector granulation + spare sectors
- **rofs**: Not needed (read-only)

## API Contract Consistency

Standard operations are consistent across all filesystems:
- open, close, read, write, truncate
- create, destroy, link, unlink
- lookup (path traversal)
- getattr, setattr (metadata)
- readdir (directory listing)
- mount, unmount

But semantics vary: FAT silently fails writes, meterfs pads partial records, littlefs supports per-mount read-only flag.

## Memory Model Diversity

- **dummyfs**: All in-memory, lazy allocation
- **littlefs**: LRU cache + per-object tracking
- **ext2**: Inode cache + block buffer
- **fat**: Red-black tree cache for open objects + chain cache
- **jffs2**: Node fragment lists + DC table
- **meterfs**: Minimal memory (headers + current file state)

## Symlink Optimization

All filesystems except FAT and ROFS support symlinks. EXT2 optimizes short symlinks (≤60 bytes) by storing them directly in the inode, avoiding separate block allocation.
