<!-- Phoenix-RTOS documentation master file -->

# Phoenix-RTOS Documentation

Phoenix-RTOS is a scalable real-time operating system for IoT. It is based on its own microkernel and can be used
either on small devices based on microcontrollers and on advanced computer systems based on multiple processors and
equipped with gigabytes of RAM.

The system supports multiple architectures, including ARM Cortex-M, ARM Cortex-A, Intel x86, RISC-V, LEON3/4 (SPARC)
and some popular microcontrollers and reference boards. Phoenix-RTOS is constantly under development, but it was
implemented in numerous Smart Utility appliances e.g. in smart gas meters, smart energy meters, data concentrators
(DCU).

The POSIX application environment can be emulated to enable the execution of regular UN*X applications.
The ARINC653 execution environment (APEX) is under development.

## Table of Contents

1. [Introduction](introduction/index.md)
2. [Architecture](architecture/index.md)
3. [Project repository](project/index.md)
4. [Building](building/index.md)
    1. [Linux](building/linux.md)
    2. [Windows](building/windows.md)
5. [Running system on targets](quickstart/index.md)
    1. [Running system on `armv7m4-stm32l4x6-nucleo` (ST STM32L4x)](quickstart/armv7m4-stm32l4x6-nucleo.md)
    2. [Running system on `armv7m7-imxrt105x-evk` (NXP i.MX RT105x)](quickstart/armv7m7-imxrt105x-evk.md)
    3. [Running system on `armv7m7-imxrt106x-evk` (NXP i.MX RT106x)](quickstart/armv7m7-imxrt106x-evk.md)
    4. [Running system on `armv7m7-imxrt117x-evk` (NXP i.MX RT117x)](quickstart/armv7m7-imxrt117x-evk.md)
    5. [Running system on `armv8m33-mcxn94x-frdm` (NXP MCX N94x)](quickstart/armv8m33-mcxn94x-frdm.md)
    6. [Running system on `armv7a7-imx6ull-evk` (NXP i.MX 6ULL)](quickstart/armv7a7-imx6ull-evk.md)
    7. [Running system on `armv7a9-zynq7000` (Xilinx Zynq 7000)](quickstart/armv7a9-zynq7000/index.md)
        1. [Running system on `armv7a9-zynq7000-zedboard`](quickstart/armv7a9-zynq7000/armv7a9-zynq7000-zedboard.md)
        2. [Running system on `armv7a9-zynq7000-zturn`](quickstart/armv7a9-zynq7000/armv7a9-zynq7000-zturn.md)
        3. [Running system on `armv7a9-zynq7000-qemu`](quickstart/armv7a9-zynq7000/armv7a9-zynq7000-qemu.md)
    8. [Running system on `armv8r52-mps3an536-qemu`](quickstart/armv8r52-mps3an536-qemu.md)
    9. [Running system on `ia32-generic-qemu`](quickstart/ia32-generic-qemu.md)
    10. [Running system on `riscv64-generic-qemu`](quickstart/riscv64-generic-qemu.md)
    11. [Running system on `riscv64-generic-spike`](quickstart/riscv64-generic-spike.md)
    12. [Running system on `riscv64-noelv-fpga`](quickstart/riscv64-noelv-fpga.md)
    13. [Running system on `sparcv8leon-gr716-mini`](quickstart/sparcv8leon-gr716-mini.md)
    14. [Running system on `sparcv8leon-gr712rc-board`](quickstart/sparcv8leon-gr712rc-board)
    15. [Running system on `sparcv8leon-gr716-mimas`](quickstart/sparcv8leon-gr716-mimas)
    16. [Running system on `sparcv8leon-generic-qemu`](quickstart/sparcv8leon-generic-qemu)
    17. [Running system on `sparcv8leon-gr740-mini`](quickstart/sparcv8leon-gr740-mini)
6. [Loader](loader/index.md)
    1. [Architecture](loader/architecture.md)
    2. [Command-line interface](loader/cli.md)
7. [Kernel](kernel/index.md)
    1. [HAL](kernel/hal/index.md)
        1. [HAL layer for ARMv7 Cortex-M based based targets](kernel/hal/armv7m.md)
        2. [HAL layer for ARMv7 Cortex-A based based targets](kernel/hal/armv7a.md)
        3. [HAL layer for IA32 based targets](kernel/hal/ia32.md)
        4. [HAL layer for RISC-V 64 based targets](kernel/hal/riscv64.md)
        5. [HAL layer for SPARCv8 LEON based targets](kernel/hal/sparcv8leon.md)
    2. [Processes and threads](kernel/proc/index.md)
        1. [Process and thread overview](kernel/proc/overview.md)
        2. [Scheduler](kernel/proc/scheduler.md)
        3. [Management](kernel/proc/forking.md)
        4. [Synchronization primitives](kernel/proc/sync.md)
        5. [Message passing](kernel/proc/msg.md)
        6. [Namespace](kernel/proc/namespace.md)
    3. [Memory management](kernel/vm/index.md)
        1. [Paging technique and Memory Management Unit](kernel/vm/page.md)
        2. [Memory mapper](kernel/vm/mapper.md)
        3. [Zone allocator](kernel/vm/zalloc.md)
        4. [Fine-grained allocator](kernel/vm/kmalloc.md)
        5. [Memory objects](kernel/vm/objects.md)
        6. [Memory management subsystem](kernel/vm/subsystem.md)
        7. [Other memory protection mechanisms](kernel/vm/protection.md)
    4. [System calls](kernel/syscalls/index.md)
        1. [Prototypes and definition](kernel/syscalls/prototypes.md)
        2. [Adding syscall](kernel/syscalls/add.md)
        3. [Debug](kernel/syscalls/debug.md)
        4. [Memory management](kernel/syscalls/mem.md)
        5. [Processes management](kernel/syscalls/proc.md)
        6. [Threads management](kernel/syscalls/threads.md)
        7. [Threads synchronization](kernel/syscalls/sync.md)
        8. [Inter-process communication](kernel/syscalls/ipc.md)
        9. [File operations](kernel/syscalls/file.md)
        10. [Socket operations](kernel/syscalls/socket.md)
        11. [Interrupts management](kernel/syscalls/interrupts.md)
        12. [Performance monitoring](kernel/syscalls/perf.md)
        13. [Time management](kernel/syscalls/time.md)
        14. [Platform management](kernel/syscalls/platform.md)
        15. [RISC-V specific](kernel/syscalls/riscv.md)
    5. [Common routines](kernel/lib.md)
8. [Standard library](libc/index.md)
    1. [Functions](libc/functions/index.md)
    2. [POSIX emulation server](libc/posix.md)
9. [Device drivers](devices/index.md)
    1. [Interface](devices/interface.md)
    2. [Accessing hardware](devices/hwaccess.md)
    3. [Handling interrupts](devices/interrupts.md)
    4. [Libsdio](devices/libsdio.md)
    5. [Simsensors (Simulating sensors)](devices/simsensors.md)
10. [Filesystems](filesystems/index.md)
11. [Network stack](lwip/index.md)
    1. [PPPoU driver](lwip/lwip-pppou.md)
12. [USB stack](usb/index.md)
    1. [USB Host stack](usb/usbhost.md)
    2. [Libusb](usb/libusb.md)
13. [Utilities](utils/index.md)
    1. [Phoenix Shell (psh)](utils/psh/index.md)
    2. [Phoenix Downloader (psd)](utils/psd.md)
14. [Host utilities](hostutils/index.md)
    1. [Phoenix disk tool (psdisk)](hostutils/psdisk.md)
    2. [Phoenix Serial Uploader (psu)](hostutils/psu.md)
    3. [Phoenix Server (phoenixd)](hostutils/phoenixd.md)
15. [Libraries](corelibs/index.md)
    1. [Common Gateway Interface library (libcgi)](corelibs/libcgi.md)
    2. [VirtIO library (libvirtio)](corelibs/libvirtio.md)
    3. [VGA library (libvga)](corelibs/libvga.md)
    4. [Graphics library (libgraph)](corelibs/libgraph.md)
    5. [Universally Unique identifiers library (libuuid)](corelibs/libuuid.md)
    6. [Cache library (libcache)](corelibs/libcache.md)
    7. [Software watchdog library (libswdg)](corelibs/libswdg.md)
16. [Ports](ports/index.md)
17. [Tests and testing process](tests/index.md)
18. [Coding convention](coding/index.md)

```{toctree}
:hidden:
:maxdepth: 3
:caption: Contents

introduction/index.md
architecture/index.md
project/index.md
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
