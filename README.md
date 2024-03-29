# Table of Contents

1. [Introduction](introduction.md)
2. [Architecture](architecture.md)
3. [Building](building/README.md)
    1. [Toolchain](building/toolchain.md)
    2. [Building script](building/script.md)
    3. [Reference project repository](building/project.md)
4. [Running system on targets](quickstart/README.md)
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
5. [Loader](loader/README.md)
    1. [Architecture](loader/architecture.md)
    2. [Command-line interface](loader/cli.md)
6. [Kernel](kernel/README.md)
    1. [HAL](kernel/hal/README.md)
        1. [HAL layer for ARMv7 Cortex-M based based targets](kernel/hal/armv7m.md)
        2. [HAL layer for ARMv7 Cortex-A based based targets](kernel/hal/armv7a.md)
        3. [HAL layer for IA32 based targets](kernel/hal/ia32.md)
        4. [HAL layer for RISC-V 64 based targets](kernel/hal/riscv64.md)
        5. [HAL layer for SPARCv8 LEON3 based targets](kernel/hal/sparcv8leon3.md)
    2. [Processes and threads](kernel/proc/README.md)
        1. [Processes creation](kernel/proc/forking.md)
        2. [Synchronization primitives](kernel/proc/sync.md)
        3. [Message passing](kernel/proc/msg.md)
        4. [Namespace](kernel/proc/namespace.md)
    3. [Memory management](kernel/vm/README.md)
        1. [Page allocator](kernel/vm/page.md)
        2. [Memory mapper](kernel/vm/mapper.md)
        3. [Zone allocator](kernel/vm/zalloc.md)
        4. [Fine-grained allocator](kernel/vm/kmalloc.md)
        5. [Memory objects](kernel/vm/objects.md)
    4. [System calls](kernel/syscalls/README.md)
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
7. [Standard library](libc/README.md)
    1. [Functions](libc/functions/README.md)
    2. [POSIX emulation server](libc/posix.md)
8. [Device drivers](devices/README.md)
    1. [Device server interface](devices/interface.md)
    2. [Accessing hardware](devices/hwaccess.md)
    3. [Handling interrupts](devices/interrupts.md)
    4. [libsdio](devices/libsdio/README.md)
    5. [Simsensors (Simulating sensors)](devices/sensors/simsensors.md)
9. [Filesystem servers](filesystems/README.md)
10. [Network stack](lwip/README.md)
11. [USB stack](usb/README.md)
    1. [USB Host stack](usb/usbhost.md)
    2. [libusb](usb/libusb.md)
12. [Utilities](utils/README.md)
    1. [psh](utils/psh.md)
    2. [psd](utils/psd.md)
13. [Host utilities](hostutils/README.md)
    1. [psdisk](hostutils/psdisk.md)
    2. [psu](hostutils/psu.md)
    3. [phoenixd](hostutils/phoenixd.md)
14. [Libraries](corelibs/README.md)
    1. [libcgi](corelibs/libcgi.md)
    2. [libvirtio](corelibs/libvirtio.md)
    3. [libvga](corelibs/libvga.md)
    4. [libgraph](corelibs/libgraph.md)
    5. [libuuid](corelibs/libuuid.md)
    6. [libcache](corelibs/libcache.md)
15. [Ports](ports/README.md)
16. [Tests and testing process](tests/README.md)
17. [Coding convention](coding.md)
