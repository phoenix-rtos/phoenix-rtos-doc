# Kernel

Phoenix-RTOS is based on the written from scratch dedicated microkernel and consists of about 20K lines of code (LoC). Microkernel is responsible for:

- memory management,
- thread and process management,
- inter-thread communication and synchronization,
- basic application interface implementation (syscalls).

Kernel is divided into five subsystems.

- hal - hardware abstraction layer
- lib - common routines
- vm - virtual memory management
- proc - process and thread management
- test - internal tests for kernel subsystems

## Kernel source code

The source code of the kernel could be obtained using the following command

>
    git clone http://github.com/phoenix-rtos.com/phoenix-rtos-kernel

## See also

1. [Kernel - HAL Subsystem](hal/README.md)
2. [Kernel - Processes and threads](proc/README.md)
3. [Kernel - Memory management](vm/README.md)
4. [Kernel - System calls](syscalls/README.md)
5. [Kernel - Common interface](lib.md)
6. [Table of Contents](../README.md)
