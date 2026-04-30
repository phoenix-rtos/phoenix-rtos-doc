# Kernel launch and memory layout

This page describes the contract between the build system, PLO, the kernel entry code, and the process loader.

## Kernel image type

The kernel is linked as a position-dependent executable. The kernel Makefile generates a target linker script from the
compiler driver, then links with `-e _start` and `--section-start,.init=$(VADDR_KERNEL_INIT)`. PLO does not apply ELF
relocation records for the kernel. It loads `PT_LOAD` segments and jumps to the entry address selected from the ELF
header or from the target image format.

For MMU targets, `VADDR_KERNEL_INIT` is a virtual address selected by the target Makefile. For example, ARMv7-A and
SPARC MMU targets use `0xc0000000`, AArch64 uses `0xffffffffc0000000`, IA32 uses `VADDR_KERNEL_BASE + 0x110000`, and
RISC-V 64 uses `0x0000003fc0000000`. PLO target code translates the kernel virtual address to the physical load
address when the target requires that. On Zynq-7000 and ZynqMP, `hal_kernelGetAddress()` subtracts
`VADDR_KERNEL_INIT` and adds the DDR base address.

For NOMMU targets, `VADDR_KERNEL_INIT` is set to `KERNEL_PHADDR`. The link address is therefore also the physical
execution address. Some NOMMU targets place writable kernel sections in a separate RAM window with `-Tdata` and
`-Tbss`.

## Loading through PLO

PLO has two kernel-loading commands.

### `kernel`

The `kernel <dev> [name]` command opens an ELF file through PHFS. The default file name is `PATH_KERNEL` when no name is
passed. The loader validates the ELF magic, iterates program headers, and handles each `PT_LOAD` segment:

1. It calls `syspage_entryAdd(NULL, hal_kernelGetAddress(p_vaddr), p_memsz, p_align)` to reserve the physical memory
   range for the segment.
2. It records the executable segment start as `kernelPAddr` when `p_flags` contains `PF_X`.
3. It copies `p_filesz` bytes from the file to the reserved range.
4. After all segments are processed, it sets the kernel entry point with
   `hal_kernelEntryPoint(hal_kernelGetAddress(e_entry))`.
5. It stores `kernelPAddr` in `syspage_t.pkernel` with `syspage_kernelPAddrAdd()`.

This path is an ELF segment loader, not a relocating ELF loader. It does not process dynamic relocation sections.

### `kernelimg`

The `kernelimg <dev> [name] <text begin> <text size> <data begin> <data size>` command is used for binary or XIP kernel
images. The build script derives the text and data ranges from the kernel ELF with `readelf -l`, writes a binary image,
and emits a `kernelimg` command in the PLO script.

At run time, `kernelimg` verifies that the image is mappable from the selected device, adds the text and data ranges to
the syspage, and sets the kernel entry point from the HAL-defined entry offset. It does not copy the text image when the
device map is used for XIP.

### `go!`

The `go!` command is the handoff point. PLO restores the console state, finishes devices and HAL state with
`devs_done()` and `hal_done()`, then calls `hal_cpuJump()`. Target HAL code disables interrupts and caches as needed,
passes the syspage address in the target ABI register, and branches to the stored entry point.

## Direct launch without PLO

The direct path is target-specific. It is used by targets that embed a syspage into the kernel image instead of running
the full PLO command interpreter before the kernel.

The `syspagen` host utility builds a 32-bit or 64-bit syspage from PLO-style scripts and writes it into a target image:

- it accepts preinit and user scripts;
- it supports `alias`, `map`, `app`, and `console` commands;
- it records the physical image address as `pkernel`;
- it writes the syspage at the offset passed with `-s <pimg:offs:sz>`.

The ARMv7-A i.MX 6ULL path shows this mode. When `KERNEL_PLO_BOOT` is not defined, startup code uses the embedded
`syspage_data` area, copies preloaded applications to `ADDR_PROGS_BEGIN`, updates their `syspage_prog_t.start` and
`syspage_prog_t.end` fields, sets the kernel `syspage` pointer, and initializes `relOffs` so kernel syspage pointers
relocate to the virtual address range.

When `KERNEL_PLO_BOOT=y`, the same startup file expects PLO to pass the syspage address. It copies the PLO syspage to
the kernel virtual syspage area and computes `relOffs` from the original physical address.

## Syspage interface

The syspage is the handoff data structure between the loader and the kernel. Its common layout is defined by
`syspage_t`:

| Field | Meaning |
| --- | --- |
| `hs` | Architecture-specific `hal_syspage_t` payload. |
| `size` | Total syspage size in bytes. |
| `pkernel` | Physical address of the executable kernel segment. |
| `maps` | Circular list of named `syspage_map_t` memory maps. |
| `progs` | Circular list of `syspage_prog_t` preloaded programs and blobs. |
| `console` | Loader-selected console identifier. |

PLO creates the syspage at `__heap_base`. `syspage_alloc()` grows syspage metadata up to `__heap_limit`, which is
defined by the PLO linker script. PLO marks the syspage and the remaining PLO heap as reserved in the memory map so
later allocations do not reuse it.

Each `syspage_map_t` has a name, an ID, a physical range, attributes, and a circular list of allocated entries.
Attributes are encoded with `mAttrRead`, `mAttrWrite`, `mAttrExec`, `mAttrShareable`, `mAttrCacheable`, and
`mAttrBufferable`. PLO scripts write the same attributes as letters: `r`, `w`, `x`, `s`, `c`, and `b`.

Each `syspage_prog_t` stores a physical `[start, end)` range, an argument string, and arrays of instruction-map and
data-map IDs. `app -x` marks a program for startup by prefixing the saved argument string with `X`. `app -xn` adds the
no-copy flag for devices that are not mappable by PHFS. The kernel strips the `X` prefix before spawning the process.

Early in `main()`, the kernel calls `syspage_init()`. That function obtains the syspage address from `hal_syspageAddr()`
and relocates all syspage pointers with `hal_syspageRelocate()`. After VM, process, and syscall initialization,
`main_initthr()` walks `syspage_progList()` and spawns only programs with the `X` prefix.

## Build variables that affect kernel placement

The placement variables are split between target `build.project` files and target Makefile fragments:

`HAVE_MMU`
: Target Makefile switch. MMU targets reject `KERNEL_PHADDR`; NOMMU targets require it.

`KERNEL_PHBASE`
: Target shell variable with the physical base used to compute the NOMMU kernel address.

`KERNEL_PHOFFS`
: Target shell variable with the offset added to `KERNEL_PHBASE`. Some targets read it from `nvm.yaml`.

`KERNEL_PHADDR`
: Exported shell variable containing `KERNEL_PHBASE + KERNEL_PHOFFS` as a formatted hexadecimal value. NOMMU target
   Makefiles use it as `VADDR_KERNEL_INIT`.

`KERNEL_DATA_PHADDR`
: Target shell or Make variable for kernel `.data` and `.bss` on selected NOMMU targets.

`VADDR_KERNEL_INIT`
: Make variable with the link address for `.init` and the kernel entry address base used by the linker.

`KERNEL_ELF`
: Shell variable with the kernel ELF file name. The default is
   `phoenix-${TARGET_FAMILY}-${TARGET_SUBFAMILY}.elf`.

`KERNEL_FILE`
: Derived shell variable naming the file written into an image and used in generated PLO aliases. It is an ELF file for
   `kernel` and a binary file for `kernelimg`.

`KERNEL_OFFS`
: Target image offset where the kernel file is placed in a flash or disk image. It is not a link address.

`KERNEL_PLO_BOOT`
: i.MX 6ULL target variable. When set to `y`, it selects the PLO handoff path; otherwise the direct syspage image path
   is used.

Current target fragments use these variables as follows:

| Target family | Kernel address rule | Writable kernel data rule |
| --- | --- | --- |
| `armv7m` | `VADDR_KERNEL_INIT := $(KERNEL_PHADDR)` | `-Tdata=20000000 -Tbss=20000000`. |
| `armv7r` | `VADDR_KERNEL_INIT := $(KERNEL_PHADDR)` | `KERNEL_DATA_PHADDR ?= 0x100000`. |
| `armv8m` | `VADDR_KERNEL_INIT := $(KERNEL_PHADDR)` | `KERNEL_DATA_PHADDR ?= 0x20000000`. |
| `armv8r` | `VADDR_KERNEL_INIT := $(KERNEL_PHADDR)` | `-Tdata=10014000 -Tbss=10014000`. |
| `sparcv8leon gr716` | `VADDR_KERNEL_INIT := $(KERNEL_PHADDR)` | Data at `40001a00`; `.rodata` at `40000000`. |
| MMU targets | Fixed virtual address selected by the target Makefile | Standard linker placement in the kernel ELF. |

## Kernel internal memory layout

The kernel initializes memory in this order:

1. `_pmap_init()` prepares architecture page-map state and returns the first free region through `bss` and `top`.
2. `_page_init()` builds the physical page allocator.
3. `_map_init()` creates the kernel map and the kernel VM object.
4. `_zone_init()` stores the kernel map and object for zone allocations.
5. `_kmalloc_init()` creates the fine-grained kernel allocator.
6. `_object_init()` and `_amap_init()` initialize object-backed and anonymous mappings.

On MMU targets, `_page_init()` places the `page_t` array at the beginning of the kernel heap, directly after the BSS and
architecture-reserved area. It discovers physical pages with `pmap_getPage()`, marks boot, kernel, syspage, page-table,
stack, and heap pages with page-owner flags, then builds a buddy-style free list indexed by block size. The number of
free buckets is `sizeof(void *) * CHAR_BIT`.

On NOMMU targets, `page-nommu.c` resolves the syspage map containing `__bss_start`. The memory from the current `bss`
pointer to the end of that map becomes the allocator arena. The `page_t` descriptors are placed at the beginning of
that arena, and the remaining pages are linked into a simple free queue.

The kernel fine-grained allocator is `vm_kmalloc()`:

- it has 24 size classes in `kmalloc_common.sizes`;
- requests smaller than 16 bytes are rounded up to 16 bytes;
- each request is rounded to the next power of two;
- indexes outside the 24-entry table fail;
- `vm_zone_t` zones provide the blocks for each size class;
- the first zone is a zone for `vm_zone_t` headers;
- `zonehdrs` is 16, so header zones reserve at least 16 header blocks;
- ordinary zones contain `max(1, SIZE_PAGE / block_size)` blocks, with the same 16-block minimum for header zones;
- empty zones are destroyed, except for the initial header zone.

Process resources do not use a fixed static pool. Each process owns an `idtree_t resources` tree. Resource IDs start at
1 and are bounded by `MAX_ID`, which is the positive range of `int`. A `resource_t` stores one of `rtLock`, `rtCond`, or
`rtInth`, and the object behind it is allocated separately. Ports use a global port ID tree, and each port has a
separate response-ID tree for pending messages. These structures are allocated with `vm_kmalloc()`, so their practical
limit is available kernel memory.

## Application launch and user memory layout

The kernel starts applications from two sources:

- `proc_syspageSpawn()` starts a preloaded syspage program from physical memory;
- `proc_fileSpawn()` and `proc_execve()` start a filesystem object returned by the POSIX lookup path.

### MMU targets

For a new executable image, `process_exec()` creates a process map from `VADDR_MIN + SIZE_PAGE` to `VADDR_USR_MAX`.
The first page is left unmapped. `process_load()` maps the ELF header into the kernel map, selects the 32-bit or 64-bit
loader by `e_ident[EI_CLASS]`, and then loads `PT_LOAD` segments.

For each non-zero `PT_LOAD` virtual address:

- `PF_R`, `PF_W`, and `PF_X` become `PROT_READ`, `PROT_WRITE`, and `PROT_EXEC`, always with `PROT_USER`;
- file-backed bytes are mapped from the executable object;
- writable file-backed mappings use `MAP_NEEDSCOPY`;
- if `p_memsz` is larger than `p_filesz`, the remaining pages are anonymous and the tail is zeroed with `hal_memset()`.

The result is the standard ELF layout: text and read-only data come from read and execute or read-only `PT_LOAD`
segments, initialized data comes from writable `PT_LOAD` bytes, and BSS is the zeroed tail of a segment whose memory
size is larger than its file size.

`PT_GNU_STACK` overrides the default user-stack size when `p_memsz` is non-zero. Otherwise the default is
`SIZE_USTACK`, defined by the architecture. The stack is mapped at the top of the process address range:
`map->pmap.end - ustacksz`.

Thread-local storage is driven by section names. The loader records `.tdata`, `.tbss`, and `armtls` section addresses.
`process_tlsInit()` allocates a per-thread TLS block, copies `.tdata`, zeroes `.tbss`, and stores the self pointer
required by the ABI.

There is no static ELF `.heap` section used by the kernel. `malloc()` in `libphoenix` uses a Doug Lea-style allocator.
When it needs another heap, it calls `mmap(NULL, heapSize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0)`.
The `sys_mmap` handler turns that into an anonymous `vm_mmap()` region in the current process map.

### NOMMU targets

On NOMMU targets, `process_load()` accepts only `VM_OBJ_PHYSMEM`. It executes from syspage-backed physical ranges and
uses the maps selected in the syspage program record:

- instruction maps from `syspage_prog_t.imaps` are added to the process `pmap`;
- data and I/O maps from `syspage_prog_t.dmaps` are also added;
- executable segments are copied to the instruction map when the original image range is outside that map;
- writable segments are allocated in the data map, copied from `p_filesz`, and zero-filled for alignment and BSS;
- `.got` entries and supported `.rel.*` or `.rela.*` relative relocations are adjusted to the physical locations;
- `.tdata`, `.tbss`, and `armtls` addresses are relocated in the same way.

The NOMMU user stack is allocated from the data map with `vm_mmap()`. The source comment in the loader states that the
build produces a position-dependent binary, while the kernel treats it as a PIE by relocating the GOT and relative
relocation entries.

## ELF headers and Phoenix-specific data

The kernel ELF loader uses standard ELF32 and ELF64 headers. The program-header constants recognized by the kernel are
`PT_LOAD`, `PT_DYNAMIC`, `PT_INTERP`, `PT_GNU_STACK`, `PT_LOPROC`, and `PT_HIPROC`. The source tree does not define a
Phoenix-specific `PT_*` program header for normal process loading.

Phoenix-specific behavior is carried outside custom program headers:

- the loader and kernel exchange boot data through `syspage_t`, not through an ELF program header;
- preloaded syspage programs use `syspage_prog_t` records with instruction-map and data-map IDs;
- NOMMU process loading relies on conventional section names such as `.got`, `.rel.*`, and `.rela.*`;
- TLS detection relies on `.tdata`, `.tbss`, and the ARM-specific `armtls` section name.

## Section initialization summary

PLO `.fastram.text.rel`
: `_startc()` copies it from `__ramtext_load` to `__ramtext_start` when load and run addresses differ.

PLO `.data`
: `_startc()` copies it from `__data_load` to `__data_start` when the addresses differ.

PLO `.rodata`
: `_startc()` copies it from `__rodata_load` to `__rodata_start` when the addresses differ.

PLO `.bss`
: `_startc()` clears `__bss_start` through `__bss_end` with `hal_memset()`.

PLO `.heap`
: Linker-reserved `NOLOAD` region. `syspage_init()` places `syspage_t` at `__heap_base`.

PLO `.stack`
: Linker-reserved `NOLOAD` region bounded by `__stack_limit` and `__stack_top`.

Kernel `PT_LOAD` bytes via PLO `kernel`
: PLO copies exactly `p_filesz` bytes for each loadable segment.

Kernel `p_memsz - p_filesz` tail via PLO `kernel`
: No generic zero-fill is present in `cmds/kernel.c`; target startup or image preparation must account for this.

Kernel syspage copy
: Kernel startup copies or relocates the syspage before `main()` on targets that use a copied virtual syspage.

Application file bytes on MMU
: `process_load32()` and `process_load64()` map them from the executable object.

Application BSS on MMU
: `process_load32()` and `process_load64()` map anonymous pages and zero the segment tail with `hal_memset()`.

Application writable segment on NOMMU
: `process_load()` allocates data-map memory, copies `p_filesz`, and zero-fills the rest.

Application TLS `.tdata`
: `process_tlsInit()` copies it to each thread TLS block.

Application TLS `.tbss`
: `process_tlsInit()` zeroes it in each thread TLS block.
