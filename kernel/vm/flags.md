# Mapping flags

Mapping flags describe virtual memory allocation, inheritance, and cache behavior.
The public definitions are in `phoenix-rtos-kernel/include/mman.h`, and the kernel stores them as `vm_flags_t`.

## Public flags

| Flag | Value | Source behavior |
| --- | --- | --- |
| `MAP_NONE` | `0x0U` | No extra mapping flags. |
| `MAP_NEEDSCOPY` | `0x1U << 0` | Marks mappings that need copy handling during VM operations. |
| `MAP_UNCACHED` | `0x1U << 1` | Adds the architecture `PGHD_NOT_CACHED` page attribute. |
| `MAP_DEVICE` | `0x1U << 2` | Adds the architecture `PGHD_DEV` page attribute. |
| `MAP_NOINHERIT` | `0x1U << 3` | Excludes a mapping from inheritance paths that honor this flag. |
| `MAP_PHYSMEM` | `0x1U << 4` | Requests physical-memory object handling in `mmap()`. |
| `MAP_CONTIGUOUS` | `0x1U << 5` | Requests contiguous allocation in `mmap()` when used with anonymous memory. |
| `MAP_ANONYMOUS` | `0x1U << 6` | Requests anonymous memory. |
| `MAP_FIXED` | `0x1U << 7` | Requests the caller-provided virtual address. |
| `MAP_SHARED` | `0x0U` | Compatibility definition with no extra flag bits. |
| `MAP_PRIVATE` | `0x0U` | Compatibility definition with no extra flag bits. |

`mman.h` notes that the VM layer uses an 8-bit type for mapping flags.
Adding new flag bits requires changing that storage type.

## Attribute conversion

`vm_flagsToAttr()` converts the flag subset that affects page-table attributes:

| Flag | Page attribute |
| --- | --- |
| `MAP_UNCACHED` | `PGHD_NOT_CACHED` |
| `MAP_DEVICE` | `PGHD_DEV` |

Architecture headers define the `PGHD_*` bit values.
For example, AArch64 and ARMv7-A define `PGHD_NOT_CACHED`, `PGHD_USER`, `PGHD_WRITE`, `PGHD_EXEC`, `PGHD_DEV`, and
`PGHD_PRESENT`, while RISC-V defines its own page-table attribute values.

## IPC mapping use

The message passing implementation calls `vm_mapFlags()` for buffers mapped between sender and receiver address spaces.
It then calls `vm_flagsToAttr()` so that wrapper pages and mapped pages preserve device and cache attributes where the
source mapping reports them.

## mmap path

`syscalls_sys_mmap()` reads protection and flag values from the user stack.
When `MAP_ANONYMOUS` is set, it selects a VM object according to `MAP_PHYSMEM` and `MAP_CONTIGUOUS`.
Before calling `vm_mmap()`, it removes allocation-selection bits from the flags so that the map entry keeps only the
attributes that remain relevant after object selection.
