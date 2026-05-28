# Memory mapper

The mapper owns virtual address ranges. It stores every mapped range as a `map_entry_t` in a red-black tree attached to
`vm_map_t`. The tree is ordered by virtual address and stores gap sizes, so the mapper can find free ranges without
linear scans.

## Main structures

`vm_map_t` describes one address space. It contains:

| Field | Meaning |
| --- | --- |
| `pmap` | Architecture page-map state used by the HAL. |
| `start`, `stop` | Valid virtual address range. |
| `tree` | Red-black tree of mapped ranges. |
| `lock` | Map lock. |

`map_entry_t` describes one mapped range. Important fields are:

| Field | Meaning |
| --- | --- |
| `vaddr`, `size` | Range start and size. |
| `lmaxgap`, `rmaxgap` | Largest free gaps in the left and right subtrees. |
| `flags`, `prot`, `protOrig` | Mapping flags and current/original protection. |
| `object`, `offs` | Backing object and object offset. |
| `amap`, `aoffs` | Anonymous memory backing used by private writable mappings. |
| `map` | Owning map. |

On MMU targets each process has its own user map and the kernel has a separate map. On NOMMU targets mappings are kept
in shared maps because processes do not have separate hardware address spaces.

## Address selection

The internal search code finds the first gap that can hold the requested size at or above the requested address. The
`lmaxgap` and `rmaxgap` fields let the search skip subtrees that cannot contain a large enough gap. After insertion or
removal, the mapper updates these gap values on the affected tree path.

When a new mapping is adjacent to an entry with compatible flags, protection, object, and offset, the mapper can merge
entries instead of adding another tree node.

## Mapping API

```{function} void *vm_mapFind(vm_map_t *map, void *vaddr, size_t size, vm_flags_t flags, vm_prot_t prot)

Finds a free address range in `map`.

:param map: Address-space map.
:param vaddr: Preferred start address.
:param size: Requested mapping size.
:param flags: Mapping flags.
:param prot: Requested protection.
:returns: Selected virtual address, or `NULL` when no suitable range exists.
```

```{function} void *vm_mmap(map, vaddr, p, size, prot, o, offs, flags)

Creates a mapping in `map`.

:param map: Address-space map.
:param vaddr: Requested address. With `MAP_FIXED`, the address must be available.
:param p: Optional page backing for direct page mappings.
:param size: Mapping size in bytes.
:param prot: Requested protection.
:param o: Optional backing memory object.
:param offs: Offset in the backing object.
:param flags: Mapping flags.
:returns: Mapped virtual address, or `MAP_FAILED` on error.
```

```{function} int vm_munmap(vm_map_t *map, void *vaddr, size_t size)

Removes mappings from an address range.

:param map: Address-space map.
:param vaddr: Start of the range.
:param size: Range size in bytes.
:returns: `EOK` on success or a negative error code.
```

```{function} int vm_mprotect(vm_map_t *map, void *vaddr, size_t len, vm_prot_t prot)

Changes protection attributes for an existing range.

:param map: Address-space map.
:param vaddr: Start of the range.
:param len: Range size in bytes.
:param prot: New protection flags.
:returns: `EOK` on success or a negative error code.
```

```{function} int vm_mapCreate(vm_map_t *map, void *start, void *stop)

Initializes a memory map.

:param map: Map object to initialize.
:param start: First address managed by the map.
:param stop: End address managed by the map.
:returns: `EOK` on success or a negative error code.
```

```{function} void vm_mapDestroy(process_t *p, vm_map_t *map)

Destroys a map and releases its entries.

:param p: Process owning the map.
:param map: Map to destroy.
```

## Hardware boundary

The mapper decides which ranges exist and which protections apply. The HAL `pmap` layer installs and removes the
architecture-specific page-table entries. `vm_flagsToAttr()` converts VM flags such as `MAP_UNCACHED` or `MAP_DEVICE`
into page-map attributes used by the HAL.
