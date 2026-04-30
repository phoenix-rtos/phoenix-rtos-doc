# PLO linker scripts

PLO linker scripts define the loader's own memory layout. They also create symbols used by PLO startup code, memory-map
discovery, and syspage allocation.

## Common structure

The common PLO scripts are architecture-specific files under `plo/ld/common/`:

| Script | Output format | Main difference |
| --- | --- | --- |
| `plo-arm.lds` | `elf32-littlearm` | Common ARM layout. |
| `plo-arm-hivecs.lds` | `elf32-littlearm` | Places `.init` in `INIT_VECTORS` for high vectors at `0xffff0000`. |
| `plo-aarch64.lds` | `elf64-littleaarch64` | AArch64 layout with 8-byte alignment and 16-byte stack alignment. |
| `plo-sparc.lds` | `elf32-sparc` | Uses separate `RODATA` and `RAM_TEXT` regions. |
| `plo-riscv64.lds` | `elf64-littleriscv` | Adds small-data sections and defines `__global_pointer$`. |
| `plo-ia32.lds` | `elf32-i386` | Defines `_plo_seg16` for the 16-bit IA32 entry path. |
| `plo-rtt.lds` | target-dependent | Adds `.rttmem` and the `__rttmem_rttcb` symbol for RTT tracing. |

All non-RTT common scripts use `ENTRY(_start)`. They set the initial location counter to `ORIGIN(PLO_IMAGE)` and place
code, read-only data, command descriptors, initialized data, BSS, heap, and stack into memory regions supplied by the
target-specific memory map.

## Sections and symbols

| Section | Purpose | Key symbols |
| --- | --- | --- |
| `.init` | Reset and early entry code. | `__init_start`, `__init_end`. |
| `.text` and `.fini` | Loader code. | `__text_start`, `__text_end`, `__etext`, `_etext`, `etext`. |
| `.rodata` | Read-only data. | `__rodata_load`, `__rodata_start`, `__rodata_end`. |
| `.commands` | Registered PLO commands. | `__cmd_start`, `__cmd_end`. |
| `.ARM.extab`, `.ARM.exidx` | ARM unwind metadata. | `__extab_start`, `__extab_end`, `__exidx_start`, `__exidx_end`. |
| `.eh_frame*` | Exception-frame metadata on SPARC, RISC-V, and IA32 scripts. | Format-defined symbols only. |
| `.init_array` | Static constructors. | `__init_array_start`, `__init_array_end`. |
| `.fini_array` | Static destructors. | `__fini_array_start`, `__fini_array_end`. |
| `.fastram.text.rel` | Functions copied to RAM. | `__ramtext_load`, `__ramtext_start`, `__ramtext_end`. |
| `.data` | Initialized writable data. | `__data_load`, `__data_start`, `__data_end`, `_edata`, `edata`. |
| `.bss` | Zero-initialized writable data. | `__bss_start`, `__bss_end`, `_end`, `end`. |
| `.heap` | Loader heap and syspage storage. | `__heap_base`, `__heap_limit`. |
| `.stack` | Loader stack. | `__stack_limit`, `__stack_top`, `_stacksz`, `_stack`. |

The `.commands` section is the command registry. Command implementations define `cmd_t` objects in a section named
`commands`; the linker script keeps and sorts that section so the CLI can enumerate registered commands between
`__cmd_start` and `__cmd_end`.

The `.fastram.text.rel` section is loaded from `PLO_IMAGE` and runs from a RAM-like region on scripts that use
`TCM_TEXT` or `RAM_TEXT`. PLO startup copies it before normal C code runs.

The `.heap` section is `NOLOAD`. PLO does not use a separate dynamic allocator for syspage metadata at startup.
`syspage_init()` places `syspage_t` at `__heap_base`, and `syspage_alloc()` advances through the same linker-reserved
range up to `__heap_limit`.

The `.stack` section is also `NOLOAD`. Startup code uses `_stack` or `__stack_top` as the initial stack top, depending
on the architecture.

The scripts compute loader image metadata:

- `_plo_load_addr = ORIGIN(PLO_IMAGE)`;
- `_plo_size = LOADADDR(.data) + SIZEOF(.data) - ORIGIN(PLO_IMAGE)`;
- IA32 additionally computes `_plo_seg16 = LOADADDR(.text) >> 4`.

## Startup initialization

The common C entry point `_startc()` consumes the linker symbols:

1. It copies `.fastram.text.rel` from `__ramtext_load` to `__ramtext_start` if the load and run addresses differ.
2. It copies `.data` from `__data_load` to `__data_start` if the load and run addresses differ.
3. It copies `.rodata` from `__rodata_load` to `__rodata_start` if the load and run addresses differ.
4. It clears `.bss` from `__bss_start` to `__bss_end` with `hal_memset()`.
5. It calls constructors from `__init_array_start` to `__init_array_end`.
6. It enters `main()`.
7. If `main()` returns, it calls destructors from `__fini_array_end` back to `__fini_array_start`.

This means PLO owns zero-initialization of its own `.bss`. The kernel and applications have separate initialization
paths described in the kernel launch page.

## Memory maps exposed to syspage

PLO HAL code reports loader-occupied ranges through `hal_memoryGetNextEntry()`. The common set is built from linker
symbols such as:

- `__init_start` to `__init_end`;
- `__text_start` to `__etext`;
- `__rodata_start` to `__rodata_end`;
- `__cmd_start` to `__cmd_end`;
- `__init_array_start` to `__init_array_end`;
- `__fini_array_start` to `__fini_array_end`;
- `__ramtext_start` to `__ramtext_end`;
- `__data_start` to `__data_end`;
- `__bss_start` to `__bss_end`;
- `__heap_base` to `__heap_limit`;
- `__stack_limit` to `__stack_top`.

Target HAL code also adds target-specific ranges, such as DDR, uncached DDR, bitstream storage, or device scratch
memory. The syspage range from the current syspage pointer to `__heap_limit` is reported as reserved.

## RTT script

`plo-rtt.lds` is an additive script for SEGGER RTT memory. It places `.rttmem` in the `RTTMEM` region, keeps input
sections named `.rttmem`, reserves the last 256 bytes for the RTT control block, and defines `__rttmem_rttcb`.

## RISC-V SBI linker script

`plo/riscv-sbi/ld/riscv-common.lds` is for Phoenix SBI, not for the PLO command interpreter. It uses `ENTRY(_start)`
and starts at `ORIGIN(SBI_IMAGE)`. Its notable sections are:

- `.extensions`, with `__ext_start` and `__ext_end`, for SBI extension descriptors;
- `.uart_drivers`, with `__uart_start` and `__uart_end`, for UART driver descriptors;
- `.payload`, aligned to 4 KiB, with `_payload_start` and `_payload_end`;
- `.stack`, bounded by `__stack_limit` and `__stack_top`.

It computes `_sbi_size` and `_sbi_load_addr` instead of `_plo_size` and `_plo_load_addr`.

## IA32 EFI linker script

`plo/hal/ia32/efi/plo.lds` is separate from the common IA32 script. It emits a PE/COFF image with
`OUTPUT_FORMAT("pei-i386")`, `OUTPUT_ARCH(i386)`, and `ENTRY(efi_main)`. The image contains page-aligned `.text`,
`.data`, and `.reloc` sections. Read-only data, writable data, GOT entries, BSS, and common symbols are grouped into
the PE/COFF `.data` section, and the `.reloc` section is kept for EFI relocation processing.
