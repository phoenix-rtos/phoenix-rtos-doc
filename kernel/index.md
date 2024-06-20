# Kernel

Phoenix-RTOS is based on the written from scratch dedicated microkernel and consists of about 20K lines of code (LoC).
Microkernel is responsible for:

* memory management
* thread and process management
* inter-thread communication and synchronization
* basic application interface implementation (syscalls)

Kernel is divided into five subsystems.

* Hal - hardware abstraction layer
* Lib - common routines
* Vm - virtual memory management
* Proc - process and thread management
* Test - internal tests for kernel subsystems

## Kernel source code

The source code of the kernel could be obtained using the following command

```console
    git clone http://github.com/phoenix-rtos.com/phoenix-rtos-kernel
```

## See also

1. [Kernel - HAL Subsystem](hal/index.md)
2. [Kernel - Processes and threads](proc/index.md)
3. [Kernel - Memory management](vm/index.md)
4. [Kernel - System calls](syscalls/index.md)
5. [Kernel - Common interface](lib.md)
6. [Table of Contents](../index.md)

```{toctree}
:hidden:
:glob:

*
hal/index.md
msg/index.md
proc/index.md
syscalls/index.md
vm/index.md
```
