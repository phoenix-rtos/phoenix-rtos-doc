# Running system on targets

## Synopsis

After reading this chapter, you will know:

- How to boot Phoenix-RTOS on supported hardware and emulators
- How to use launch scripts for QEMU targets
- What components are included in a typical boot image

This chapter presents how to run Phoenix-RTOS on supported targets. It is assumed that `phoenix-rtos-project` is built,
and system artifacts are available in the `_boot` directory. The building process has been described in
[Building](../building/index.md) chapter.

## Launch scripts

QEMU and simulator targets include launch scripts in the `scripts/` directory:

```shell
./scripts/ia32-generic-qemu.sh
```

Script naming follows two patterns:
- `scripts/<target>.sh`  -  standard launch
- `scripts/<target>-test.sh`  -  launch with test configuration (e.g., serial console for automated testing)

Some targets have additional variants (e.g., `ia32-generic-qemu-net.sh` for networking, `ia32-generic-qemu-virt.sh`
for VirtIO).

## Boot image contents

A typical boot image in `_boot/<target>/` contains the bootloader (plo), kernel, device drivers, filesystem servers,
and the shell (psh). The exact set of components varies per target and is defined in the target's `build.project`.

## User applications

The `_user/` directory contains example applications that are included in the root filesystem. These can be
run directly from the psh shell prompt after boot.

```{note}
The following targets have project configurations in `_projects/` but do not yet have quickstart pages:
`aarch64a53-zynqmp-qemu`, `aarch64a53-zynqmp-som`, `armv7r5f-zynqmp-qemu`, `armv7r5f-zynqmp-som`,
`armv8m33-mcxn94x-frdm_cpu1`, `armv8m55-stm32n6-nucleo`, `host-generic-pc`, `ia32-generic-pc`.
```

```{toctree}
:maxdepth: 1

aarch64a53-zynqmp-zcu104.md
armv7m4-stm32l4x6-nucleo.md
armv7m7-imxrt105x-evk.md
armv7m7-imxrt106x-evk.md
armv7m7-imxrt117x-evk.md
armv8m33-mcxn94x-frdm.md
armv7a7-imx6ull-evk.md
armv7a9-zynq7000/index.md
armv8r52-mps3an536-qemu.md
ia32-generic-qemu.md
riscv64-generic-qemu.md
riscv64-generic-spike.md
riscv64-grfpga-artya7.md
riscv64-gr765-vcu118.md
sparcv8leon-gr716-mini.md
sparcv8leon-gr712rc-board.md
sparcv8leon-gr716-mimas.md
sparcv8leon-generic-qemu.md
sparcv8leon-gr740-mini.md
```
