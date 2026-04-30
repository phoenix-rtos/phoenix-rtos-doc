# Device Tree Blob processing

Device Tree Blob (DTB) processing is implemented in the HAL for architectures that pass hardware description data to
the kernel at boot.
The current DTB parsers are under `phoenix-rtos-kernel/hal/aarch64/` and `phoenix-rtos-kernel/hal/riscv64/`.

## AArch64 path

The AArch64 HAL looks up a syspage program named `system.dtb` during early initialization.
If the entry exists, `_pmap_preinit()` maps the DTB area and `_dtb_init()` parses the flattened device tree.
`VADDR_DTB` reserves the last 1 MiB of virtual address space for this mapping.

The AArch64 parser exposes these accessors:

| Function | Data returned |
| --- | --- |
| `dtb_getSystem()` | Model and compatible strings. |
| `dtb_getCPU()` | CPU compatible string and clock value for a CPU index. |
| `dtb_getMemory()` | Up to 8 memory banks with start and end addresses. |
| `dtb_getGIC()` | GIC distributor and CPU interface addresses. |
| `dtb_getSerials()` | Up to 4 serial device base addresses and interrupt numbers. |

The parser validates the FDT magic value `0xd00dfeed` before walking the structure block.
It currently assumes two cells per memory address or size when parsing memory bank `reg` properties.

## RISC-V path

The RISC-V HAL stores and parses DTB data through `dtb_save()`, `dtb_parse()`, and `_dtb_init()`.
The RISC-V accessors expose system strings, CPU details, memory regions, Platform-Level Interrupt Controller (PLIC)
information, reserved memory, and the DTB storage area.

| Function | Data returned |
| --- | --- |
| `dtb_getSystem()` | Model and compatible strings. |
| `dtb_getCPU()` | Compatible string, clock, ISA string, and MMU string for a CPU index. |
| `dtb_getMemory()` | Memory `reg` data and entry count. |
| `dtb_getPLIC()` | PLIC information. |
| `dtb_getReservedMemory()` | Reserved memory `reg` data. |
| `dtb_getDTBArea()` | DTB physical area and size. |

## Constraints

DTB parsing is an early HAL service, not a runtime device manager.
The parsed data feeds low-level CPU, memory, interrupt-controller, and serial initialization paths.
Driver discovery outside these HAL paths still depends on the platform code and server configuration.
