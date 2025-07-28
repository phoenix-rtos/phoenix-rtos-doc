# Kernel

Phoenix-RTOS is based on the written from scratch dedicated microkernel and consists of about 20K lines of code (LoC).
Microkernel is responsible for:

* memory management
* thread and process management
* inter-thread communication and synchronization
* basic application interface implementation (syscalls)

Kernel is divided into five subsystems.

* hal - hardware abstraction layer
* lib - common routines
* vm - virtual memory management
* proc - process and thread management
* test - internal tests for kernel subsystems

## Kernel source code

The source code of the kernel could be obtained using the following command

```console
git clone https://github.com/phoenix-rtos/phoenix-rtos-kernel.git
```

```{toctree}
:hidden:
:glob:

hal/index.md
proc/index.md
vm/index.md
syscalls/index.md
lib.md
```
