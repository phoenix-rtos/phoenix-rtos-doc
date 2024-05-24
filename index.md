<!-- Phoenix-RTOS documentation master file -->

# Phoenix-RTOS Documentation

Phoenix-RTOS is a scalable real-time operating system for IoT. It is based on its own microkernel and can be used
either on small devices based on microcontrollers and on advanced computer systems based on multiple processors and
equipped with gigabytes of RAM.

The system supports multiple architectures, including ARM Cortex-M, ARM Cortex-A, Intel x86, RISC-V, LEON3 (SPARC)
and some popular microcontrollers and reference boards. Phoenix-RTOS is constantly under development, but it was
implemented in numerous Smart Utility appliances e.g. in smart gas meters, smart energy meters, data concentrators
(DCU).

The POSIX application environment can be emulated to enable the execution of regular UN*X applications.
The ARINC653 execution environment (APEX) is under development.

## Table of Contents

1. [Introduction](introduction/index.md)
2. [Architecture](architecture/index.md)
3. [Building](building/index.md)
    1. [Toolchain](building/toolchain.md)
    2. [Building script](building/script.md)
    3. [Reference project repository](building/project.md)
4. [Running system on targets](quickstart/index.md)
    1. [Running system on `armv7m4-stm32l4x6-nucleo` (ST STM32L4x)](quickstart/armv7m4-stm32l4x6-nucleo.md)
    2. [Running system on `armv7m7-imxrt105x-evk` (NXP i.MX RT105x)](quickstart/armv7m7-imxrt105x-evk.md)
    3. [Running system on `armv7m7-imxrt106x-evk` (NXP i.MX RT106x)](quickstart/armv7m7-imxrt106x-evk.md)
    4. [Running system on `armv7m7-imxrt117x-evk` (NXP i.MX RT117x)](quickstart/armv7m7-imxrt117x-evk.md)
    5. [Running system on `armv7a7-imx6ull-evk` (NXP i.MX 6ULL)](quickstart/armv7a7-imx6ull-evk.md)
    6. [Running system on `armv7a9-zynq7000` (Xilinx Zynq 7000)](quickstart/armv7a9-zynq7000.md)
    7. [Running system on `ia32-generic-qemu`](quickstart/ia32-generic-qemu.md)
    8. [Running system on `riscv64-generic-qemu`](quickstart/riscv64-generic-qemu.md)
    9. [Running system on `riscv64-generic-spike`](quickstart/riscv64-generic-spike.md)
    10. [Running system on `sparcv8leon3-gr716-mini`](quickstart/sparcv8leon3-gr716-mini.md)
5. [Loader](loader/index.md)
    1. [Architecture](loader/architecture.md)
    2. [Command-line interface](loader/cli.md)
6. [Kernel](kernel/index.md)
    1. [HAL](kernel/hal/index.md)
        1. [HAL layer for ARMv7 Cortex-M based based targets](kernel/hal/armv7m.md)
        2. [HAL layer for ARMv7 Cortex-A based based targets](kernel/hal/armv7a.md)
        3. [HAL layer for IA32 based targets](kernel/hal/ia32.md)
        4. [HAL layer for RISC-V 64 based targets](kernel/hal/riscv64.md)
        5. [HAL layer for SPARCv8 LEON3 based targets](kernel/hal/sparcv8leon3.md)
    2. [Processes and threads](kernel/proc/index.md)
        1. [Processes creation](kernel/proc/forking.md)
        2. [Synchronization primitives](kernel/proc/sync.md)
        3. [Message passing](kernel/proc/msg.md)
        4. [Namespace](kernel/proc/namespace.md)
    3. [Memory management](kernel/vm/index.md)
        1. [Page allocator](kernel/vm/page.md)
        2. [Memory mapper](kernel/vm/mapper.md)
        3. [Zone allocator](kernel/vm/zalloc.md)
        4. [Fine-grained allocator](kernel/vm/kmalloc.md)
        5. [Memory objects](kernel/vm/objects.md)
    4. [System calls](kernel/syscalls/index.md)
        1. [Debug (1)](kernel/syscalls/debug.md)
        2. [Memory management (5)](kernel/syscalls/mem.md)
        3. [Processes management (13)](kernel/syscalls/proc.md)
        4. [Threads management (7)](kernel/syscalls/threads.md)
        5. [Threads synchronization (8)](kernel/syscalls/sync.md)
        6. [Inter-process communication (12)](kernel/syscalls/ipc.md)
        7. [File operations (23)](kernel/syscalls/file.md (32))
        8. [Socket operations (13)](kernel/syscalls/socket.md)
        9. [Interrupts management (1)](kernel/syscalls/interrupts.md)
        10. [Performance monitoring (3)](kernel/syscalls/perf.md)
        11. [Time management (2)](kernel/syscalls/time.md)
        12. [Platform management (4)](kernel/syscalls/platform.md)
        13. [RISC-V specific (2)](kernel/syscalls/riscv.md)
    5. [Common routines](kernel/lib.md)
7. [Standard library](libc/index.md)
    1. [Functions](libc/functions/index.md)
    2. [POSIX emulation server](libc/posix.md)
8. [Device drivers](devices/index.md)
    1. [Device server interface](devices/interface.md)
    2. [Accessing hardware](devices/hwaccess.md)
    3. [Handling interrupts](devices/interrupts.md)
    4. [libsdio](devices/libsdio.md)
    5. [Simsensors (Simulating sensors)](devices/sensors/simsensors.md)
9. [Filesystem servers](filesystems/index.md)
10. [Network stack](lwip/index.md)
11. [USB stack](usb/index.md)
    1. [USB Host stack](usb/usbhost.md)
    2. [libusb](usb/libusb.md)
12. [Utilities](utils/index.md)
    1. [psh](utils/psh/index.md)
    2. [psd](utils/psd.md)
13. [Host utilities](hostutils/index.md)
    1. [psdisk](hostutils/psdisk.md)
    2. [psu](hostutils/psu.md)
    3. [phoenixd](hostutils/phoenixd.md)
14. [Libraries](corelibs/index.md)
    1. [libcgi](corelibs/libcgi.md)
    2. [libvirtio](corelibs/libvirtio.md)
    3. [libvga](corelibs/libvga.md)
    4. [libgraph](corelibs/libgraph.md)
    5. [libuuid](corelibs/libuuid.md)
    6. [libcache](corelibs/libcache.md)
15. [Ports](ports/index.md)
16. [Tests and testing process](tests/index.md)
17. [Coding convention](coding/index.md)

```{toctree}
:hidden:
:maxdepth: 1
:caption: Contents

introduction/index.md
architecture/index.md
building/index.md
quickstart/index.md
loader/index.md
kernel/index.md
libc/index.md
devices/index.md
filesystems/index.md
lwip/index.md
usb/index.md
utils/index.md
hostutils/index.md
corelibs/index.md
ports/index.md
tests/index.md
coding/index.md
```
