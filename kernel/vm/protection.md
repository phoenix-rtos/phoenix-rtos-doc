# Memory protection

Phoenix-RTOS supports targets with and without MMUs. The VM layer exposes one mapping interface, while the HAL selects
the hardware mechanism used to protect or describe memory.

## MMU targets

On MMU targets every process has its own user address map. The mapper stores ranges in `vm_map_t`, and the HAL `pmap`
layer installs page-table entries. Protection flags are stored in `map_entry_t.prot` and translated to architecture page
attributes when a mapping is created or changed.

Use `vm_mprotect()` to change protection for an existing range. The valid public protection flags are declared in
`include/mman.h`:

| Flag | Meaning |
| --- | --- |
| `PROT_NONE` | No access. |
| `PROT_READ` | Read access. |
| `PROT_WRITE` | Write access. |
| `PROT_EXEC` | Execute access. |
| `PROT_USER` | User-mode access. |

## MPU and NOMMU targets

Microcontroller targets often use direct physical addressing and, when available, an MPU. An MPU usually exposes a small
number of regions with hardware-specific alignment and size limits. Phoenix-RTOS represents these regions as shared
maps selected during system startup and process creation.

This model avoids reprogramming an entire MPU layout on each context switch. Instead, a process receives a set of
predefined regions and the architecture layer enables the relevant access permissions.

## Mapping attributes

Mapping flags affect cache and device attributes independently from read/write/execute protection. `vm_flagsToAttr()`
converts supported flags into HAL page-map attributes:

| VM flag | Effect |
| --- | --- |
| `MAP_UNCACHED` | Requests non-cached access. |
| `MAP_DEVICE` | Requests device-memory attributes. |

For the complete flag list, see [Mapping flags](flags.md).
