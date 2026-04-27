# Filesystems

This chapter describes the filesystem servers available in Phoenix-RTOS. After reading this chapter, you will know:

- The available filesystem types and their use cases.
- Which filesystems support read-write and which are read-only.
- The flash memory requirements and crash resilience features of each filesystem.
- How pseudo-filesystems provide special device files.

Filesystems in Phoenix-RTOS are implemented as user-space file servers. Each file server is a separate process that
implements a specific filesystem protocol and registers its port in the namespace during startup.
Filesystems register in the kernel namespace; see [Namespace](../kernel/proc/namespace.md). File servers
communicate with the kernel and other processes using the standard Phoenix-RTOS message passing interface.

## Filesystem Comparison

| Filesystem | Read | Write | Flash Type | Wear Leveling | Crash Resilience | Use Case |
|---|---|---|---|---|---|---|
| dummyfs | Yes | Yes | RAM only | N/A | No | tmpfs, testing |
| ext2 | Yes | Yes | Block device | No | No | General purpose storage |
| FAT | Yes | **No** | Block device | No | No | SD card interchange |
| JFFS2 | Yes | Yes | NOR/NAND | Yes (GC) | Yes (journal) | NOR flash storage |
| LittleFS | Yes | Yes | NOR flash | Yes | Yes (metadata pairs) | Small embedded flash |
| MeterFS | Yes | Yes | NOR flash | Yes (circular) | Yes (write-verify) | Data logging, metering |
| ROFS | Yes | **No** | AHB address space | N/A | N/A | XIP read-only images |

```{toctree}
:maxdepth: 1

filesystems.md
```
