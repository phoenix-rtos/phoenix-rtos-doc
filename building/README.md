# Building Phoenix-RTOS image

To create Phoenix-RTOS image for selected target the `phoenix-rtos-project` repository should be used. This repository aggregates all operating system modules. This chapter contains instruction how to build reference project and how to create the final system image.

## Available target platforms

The reference Phoenix-RTOS project supports following target platforms:

* armv7m4-stm32l4x6
* armv7m7-imxrt105x
* armv7m7-imxrt106x
* armv7m7-imxrt117x
* armv7a7-imx6ull
* ia32-generic
* riscv64-spike
* riscv64-virt

## Cloning and initializing repository

The first step of preparation of the final system image is the repository cloning. The repository should be cloned and entered using following commands.

````bash
git clone https://github.com/phoenix-rtos/phoenix-rtos-project.git
cd phoenix-rtos-project/
````

The next step is the initialization and update of git submodules:
````bash
git submodule update --init --recursive
````

## Building and installing toolchains

Build the toolchain:

````bash
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh i386-pc-phoenix ~/toolchains/i386-pc-phoenix)
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh arm-phoenix ~/toolchains/arm-phoenix)
(cd phoenix-rtos-build/toolchain/ && ./build-toolchain.sh riscv64-phoenix-elf ~/toolchains/riscv64-phoenix-elf)
````

Add toolchain binaries to PATH variable:

````bash
export PATH=$PATH:~/toolchains/i386-pc-phoenix/i386-pc-phoenix/bin/
export PATH=$PATH:~/toolchains/arm-phoenix/arm-phoenix/bin/
export PATH=$PATH:~/toolchains/riscv64-phoenix-elf/riscv64-phoenix-elf/bin/
````

## Define the build target

To build Phoenix-RTOS for selected platform you should edit build.project file and set TARGET variable to define target processor architecture and target board.






## Running build.sh script

```
	./phoenix-rtos-build/build.sh clean all
```
After the build successfully completes, kernel and disk images will be created and placed in the *_boot* directory.
