# Phoenix-RTOS loader (plo)
The plo is an inherent part of Phoenix-RTOS used to prepare the system setup structure and load kernel and applications to selected memory areas defined as maps.
The loader configuration is flexible and allows the user to customize appropriate sets of functionality depending on hardware resources.

The Phoenix-RTOS loader supports the following target platforms:

 * armv7m4-stm32l4x6 (under development)
 * armv7m7-imxrt106x
 * armv7m7-imxrt117x
 * armv7a9-zynq7000 (under development)
 * armv7a7-imx6ull (under development)
 * ia32-generic

## Functionality
The loader can be treated as a first-stage and second-stage bootloader. It can be loaded to RAM via JLink or other tools specified by the platforms' vendors or booted from supported devices, such as a NOR flash (e.g. using FlexSPI, Quad SPI), NAND flash or SD card.

Acting as a first-stage, plo configures the memory controllers and a variety of supported devices on a dedicated platform. It is also responsible for setting the initial processor's clocks values and preparing the board for the kernel. The loader runs in a supervisor mode and doesn't support FPU and MMU on all architectures.

During the second-stage booting, it loads the operating system and selected applications from storage devices or via interfaces like serial or USB (acting as USB client) to the memory. For more complex platforms, additional work can be performed like loading bitstream to FPGA or testing specific components.

What is more, there is a command-line interface for users to control the boot process on a serial port. The loader requires an explicit list of available devices and available physical memory maps as destinations for copying data and files. Such an approach makes plo more flexible than other bootloaders and allows it to create solutions for demanding projects. However, providing access to low-level setup requires additional knowledge about hardware configuration. Using CLI, users can define their own booting sequences, save a script and run plo automatically during the booting phase. All available commands are described in the [CLI chapter](cmds.md).

Examples of booting scripts are located in the building files of the supported targets in [phoenix-rtos-project/_targets](https://github.com/phoenix-rtos/phoenix-rtos-project/tree/master/_targets).


## Source code

The source code of the loader can be obtained with the following command:

>
    git clone http://git.phoenix-rtos.com/plo

## See also

1. [Architecture](architecture.md)
2. [CLI](cli.md)
3. [Table of Contents](../README.md)
