# Building

To create Phoenix-RTOS image for a specific target, the `phoenix-rtos-project` repository should be used. This
repository aggregates all operating system modules, including kernel, standard library, device drivers, filesystems,
utilities and loader. Read more about `phoenix-rtos-project` submodule repositories in
[Reference project](../project/index.md) chapter.

## Host operating system

Currently, the most supported development platform is Linux, particularly Ubuntu 24.04. Windows is also supported
but to a limited extent.

```{toctree}
:maxdepth: 1

linux.md
windows.md
```

## Building script

The Phoenix-RTOS reference project supports the following target platforms:

- aarch64a53-zynqmp-qemu
- aarch64a53-zynqmp-zcu104
- aarch64a53-zynqmp-som
- armv7a7-imx6ull-evk
- armv7a9-zynq7000-qemu
- armv7a9-zynq7000-zedboard
- armv7a9-zynq7000-zturn
- armv7m4-stm32l4x6-nucleo
- armv7m7-imxrt105x-evk
- armv7m7-imxrt106x-evk
- armv7m7-imxrt117x-evk
- armv7r5f-zynqmp-qemu
- armv8m33-mcxn94x-frdm
- armv8m55-stm32n6-nucleo
- armv8r52-mps3an536-qemu
- host-generic-pc
- ia32-generic-pc
- ia32-generic-qemu
- riscv64-generic-qemu
- riscv64-generic-spike
- riscv64-grfpga-artya7
- riscv64-gr765-vcu118
- sparcv8leon-generic-qemu
- sparcv8leon-gr712rc-board
- sparcv8leon-gr716-mimas
- sparcv8leon-gr716-mini
- sparcv8leon-gr740-mini

List of all valid targets can be seen using the `build.sh` script with `TARGET` variable not set.

To build Phoenix-RTOS system image build.sh script is used. The simplest way to build the image is the
following command.

```console
TARGET=ia32-generic-qemu phoenix-rtos-build/build.sh all
```

As you can see there can be other arguments like `all`.

You can also use the `clean` argument to clean the last build artifacts.

```console
TARGET=ia32-generic-qemu phoenix-rtos-build/build.sh clean all
```

When you want to compile only the new changes and save time you don't have to use it.

The `all` argument specifies that all system components for a given target should be compiled (excluding tests).
The available components are listed below:

- `fs` - filesystem image,

- `core` - Phoenix-RTOS core, i.e. kernel and other necessary components,

- `test` - tests,

- `ports` - phoenix-rtos-ports applications,

- `project` - project specific part (user applications),

- `image` - system image to be loaded to the target,

- `host` - host system utils.

For example, in ia32-generic-qemu target `all` means `core fs image project ports host`.</br>
For the other targets, `all` can be different components configurations. </br>
The `ports` component compiling process can take a while. If you need to build the system image quickly, you can use
the command above.

```console
TARGET=ia32-generic-qemu phoenix-rtos-build/build.sh core fs image project test
```

For ia32-generic-qemu target, running the system in a separate window isn't the only option. There is the possibility
to run it in a terminal, in that case, you have to set a few other variables.

```console
TARGET=ia32-generic-qemu CONSOLE=serial ./phoenix-rtos-build/build.sh all
```

After build completes, the disk image and all files needed to run system will be placed in the `_boot` directory.

## Launching Phoenix-RTOS

To start the created image on target architecture please see [Running system on targets](../quickstart/index.md).
