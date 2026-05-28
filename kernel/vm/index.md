# Memory management

Phoenix-RTOS memory management provides physical-page allocation, address-space mapping, kernel heap allocation,
memory objects, and protection attributes for MMU and NOMMU targets.

The implementation lives in `phoenix-rtos-kernel/vm/`. Architecture-specific page-map code lives under
`phoenix-rtos-kernel/hal/<arch>/`.

## Main layers

| Layer | Main source files | Responsibility |
| --- | --- | --- |
| Page allocator | `vm/page.c`, `vm/page-nommu.c`, `vm/page.h` | Allocate and free physical pages or descriptors. |
| Memory mapper | `vm/map.c`, `vm/map.h` | Track virtual address ranges and create or remove mappings. |
| Memory objects | `vm/object.c`, `vm/object.h`, `vm/amap.c`, `vm/amap.h` | Back mappings with object and COW pages. |
| Zone allocator | `vm/zone.c`, `vm/zone.h` | Allocate fixed-size blocks from page-backed zones. |
| Kernel allocator | `vm/kmalloc.c`, `vm/kmalloc.h` | Allocate variable-size kernel objects through size-class zones. |

## Target model

MMU targets keep separate process maps and use `pmap_t` to install page-table entries. NOMMU targets use shared memory
maps and still keep VM metadata so higher layers can use the same mapping and object interfaces.

```{toctree}
:maxdepth: 1

page.md
mapper.md
zalloc.md
kmalloc.md
objects.md
protection.md
flags.md
subsystem.md
```
