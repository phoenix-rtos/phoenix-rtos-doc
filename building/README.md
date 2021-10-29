# Building Phoenix-RTOS image

To create Phoenix-RTOS image for selected target the `phoenix-rtos-project` repository should be used. This repository aggregates all operating system modules - kernel, standard library, device drivers, filesystems, utilities and loader.

This chapter contains instruction how to build reference project and how to create the final system image.

## Obtaining the sources

The first step of preparation of the final system image is the repository cloning. The repository should be cloned and **recursively** (to get the submodules):

```bash
git clone --recursive https://github.com/phoenix-rtos/phoenix-rtos-project.git
```

## Supported target platforms

The reference Phoenix-RTOS project supports following target platforms:

* armv7m4-stm32l4x6
* armv7m7-imxrt105x
* armv7m7-imxrt106x
* armv7m7-imxrt117x
* armv7a7-imx6ull
* ia32-generic
* riscv64-spike
* riscv64-virt

To get the list of valid targets the `build.sh` script should be launched with empty `TARGET` variable , eg:

```bash
$ ./phoenix-rtos-build/build.sh
TARGET variable not set
Please specify a valid traget by setting TARGET variable to one of:
armv7a7-imx6ull
armv7m4-stm32l4x6
armv7m7-imxrt105x
armv7m7-imxrt106x
ia32-generic
riscv64-spike
riscv64-virt
```

## Building using docker

This is the quickest way to start development - all necessary tools are distributed in docker image.

To build - provide a `TARGET` via ENV variable:

```bash
cd phoenix-rtos-project/
TARGET=ia32-generic ./docker-build.sh clean all
```

After the build successfully completes, kernel and disk images will be created and placed in the `_boot` directory.

## Building using native toolchain

This is the method preferred when you plan to develop Phoenix-RTOS.

Firstly, you need to install some tools required for compiling toolchain and finally creating Phoenix-RTOS system image.
There is a list of commands you can use to get them on the Ubuntu 20.04 host operating system
```bash
sudo apt-get update && \
sudo apt-get upgrade && \
sudo apt-get install build-essential \
autoconf \
texinfo \
genext2fs \
libtool \
libhidapi-dev
```

Next, you need to compile the toolchains for all required target architectures:

```bash
cd phoenix-rtos-project
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh i386-pc-phoenix ~/toolchains/i386-pc-phoenix)
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh arm-phoenix ~/toolchains/arm-phoenix)
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh riscv64-phoenix ~/toolchains/riscv64-phoenix)
```

Toolchain binaries should be added to PATH variable:

```bash
export PATH=$PATH:~/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/
export PATH=$PATH:~/toolchains/arm-phoenix/arm-phoenix/bin/
export PATH=$PATH:~/toolchains/riscv64-phoenix/riscv64-phoenix/bin/
```

To build a project - provide a `TARGET` via ENV variable:

```bash
TARGET=ia32-generic ./phoenix-rtos-build/build.sh clean all
```

After the build successfully completes, kernel and disk images will be created and placed in the `_boot` directory.

## Launching Phoenix-RTOS

To start the created image on target architecture please see [phoenix-rtos-doc/quickstart](../quickstart/README.md) guide.

## See also

1. [Phoenix-RTOS toolchain](toolchain.md)
2. [Phoenix-RTOS building script](script.md)
3. [Phoenix-RTOS reference project repository](project.md)
4. [Table of Contents](../README.md)
