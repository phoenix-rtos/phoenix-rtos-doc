# Architecture

The Phoenix-RTOS loader is a self-sufficient application which does not use any of the external libraries.

It only includes common syspage's header files from phoenix-rtos-kernel.

Plo is divided into five subsystems:
 - cmds - command-line interface
 - devices - platform's drivers
 - hal - hardware abstraction layer
 - lib - common routines
 - phfs - phoenix filesystem
 - syspage - system configuration structure


## Cmds
Each of the commands have to implement interface defined in `cmds/cmd.h` and be registered using constructor invocation.

There is a flexibility of defining command setups for each platform. The targets define their own set of commands in `PLO_COMMANDS` variable in a `Makefile` file.

All available commands are described in the [CLI chapter](cmds.md).

## Devices
Devices are the hardware dependent subsystem containing a collection of drivers with a unified interface for the other loader components. Each driver has to register itself using constructor invocation. During bootloader initialization, the registered devices are initialized and appropriate `major.minor` numbers are assigned to them. The other plo's components refer to specific devices using `major.minor` identification. The minor number indicates on the device instance and are assigned dynamically. However, the major numbers are static and refer to the following device types:
 - `0` - UART
 - `1` - USB
 - `2` - STORAGE
 - `3` - TTY

Each platform defines its own set of drivers in a `Makefile` file.

## HAL
HAL (Hardware Abstraction Layer) is the loader hardware dependent subsystem used for adopting it to the particular hardware platform. It provides the unified interface for the other plo components.
When loader is ported to the new architecture, only the common hal interface has to be implemented, the rest of the subsystems remain unchanged.

HAL implements the following functionalities:
 - platform initialization
 - types definition
 - basic console
 - string functions
 - timer controller
 - exceptions and interrupts handling
 - memory synchronization

### Platform initialization

Platform initialization is one of the most important part of the the loader. Typically, the majority of the code is written in assembly language and is placed in a `_init.S` file. It prepares the most low-level components of of the processor like cache invalidation, FlexRAM configuration, disabling MMU and FPU. After that, the loader moves to platform specific controller initializations. In this part, the loader is responsible for setting clocks, PLLs, external memory controllers like DDR and preparing other crucial components for dedicated platforms.


### Console

Console is used for presenting plo messages until the device driver for the console is initialized. It is typically based on UART but it can use other display devices (on IA32 there is a console based on VGA graphics adapter and keyboard). Initially the console should be kept as simple as possible so it works from the early boot stage. It does not use interrupts or other HAL mechanisms, nor allow the loader to read data.


### Strings

HAL provides a set of string functions used for data copying and string manipulation. They correspond to ANSI C functions provided by the compiler but the compiler`s functions are not intentionally used. The intention was to implement these functions from scratch to control the details of implementation and external references.


### Timer

The timer driver controller is a part of the common hal interface. It calculates uptime from booting in milliseconds.


### Interrupts & Exceptions

HAL handles interrupts, implements the interrupt and exception stubs for specific architectures and service routines invocations.

Furthermore, interrupts interface provides synchronization mechanisms, it allows to either disable or enable interrupts in other loader's subsystems.


## Common routines
Common routines contain the following units:
 - `circular buffer` - basic interface to push and pop data to buffer
 - `console` - unit sets console to specific device and print data on it
 - set of functions to handle `character types`
 - `error definition`
 - `circular doubly-linked list` - basic interface to operate on list
 - `logger` - log information with appropriate formatting
 - family of `printf functions`
 - `variable arguments handling`

## PHFS
PHFS (phoenix filesystem) is an abstraction for data access from different devices. This abstraction is used by CLI to copy data/files from different sources to physical memory maps. Currently, phfs supports two protocols for data access:
 - `raw` - direct access to storage devices
 - `phoenixd` - protocol to exchange data between host and target platform via interfaces like serial or USB, using [Phoenix Daemon](https://github.com/phoenix-rtos/phoenix-rtos-hostutils/tree/master/phoenixd).

In order to use a device in the phoenix filesystem, the user should assign an alias to a dedicated `major.minor` identification of the device with an appropriate protocol type, for example: `phfs usb0 1.0 phoenixd`.


## Syspage
Low-level kernel initialization is based on `syspage_t` structure. This structure is prepared during the bootstrap process by the loader. It is stored on the physical memory at the address above the stack memory. The `syspage_t` definition consists of the generic part which is common to all architectures and the hardware architecture dependent data. Syspage provides information like physical memory maps, interrupts tables, preloaded user applications and data for specific architecture. It should be treated as the main structure used for operating system configuration.

## See also

1. [Table of Contents](../README.md)
2. [Loader](README.md)
3. [CLI](cli.md)
