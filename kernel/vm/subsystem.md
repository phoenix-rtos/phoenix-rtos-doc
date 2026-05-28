# Memory management subsystem

The VM subsystem coordinates five mechanisms:

* physical memory allocation,
* virtual address range allocation,
* page-table updates through the HAL `pmap` layer,
* fixed-size and variable-size kernel allocation,
* memory-object mapping and sharing.

## Control flow

The usual MMU mapping path is:

1. the mapper reserves a virtual address range in `vm_map_t`,
2. a memory object supplies pages for the range,
3. the page allocator returns physical pages tagged with owner flags,
4. the architecture `pmap` code installs page-table entries,
5. unmap or protection changes update both the VM map and page tables.

NOMMU targets keep the same VM interfaces where practical, but the mapping layer works with direct physical access and
shared maps instead of per-process page tables.

## Main data ownership

| Data | Owner | Notes |
| --- | --- | --- |
| Physical pages | Page allocator | Tracks free pages, boot pages, kernel pages, and application pages. |
| Virtual ranges | Mapper | Stored as `map_entry_t` objects in a `vm_map_t` red-black tree. |
| Mapped content | Memory objects | Objects own backing pages and references from maps. |
| Small kernel blocks | Zone and kmalloc allocators | Backed by pages tagged as kernel heap pages. |
| Hardware mappings | HAL `pmap` | Converts VM flags into architecture-specific MMU attributes. |

## Implementation files

| Area | Files |
| --- | --- |
| Page allocation | `vm/page.c`, `vm/page-nommu.c`, `vm/page.h` |
| Mapping | `vm/map.c`, `vm/map.h` |
| Objects and anonymous memory | `vm/object.c`, `vm/object.h`, `vm/amap.c`, `vm/amap.h` |
| Zone allocator | `vm/zone.c`, `vm/zone.h` |
| Kernel allocator | `vm/kmalloc.c`, `vm/kmalloc.h` |
| HAL page-map layer | `hal/<arch>/pmap.c`, `hal/<arch>/include/arch/pmap.h` |
