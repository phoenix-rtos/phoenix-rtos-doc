# Reference project repository

The main repository of Feniks-RTOS is the
[feniks-rtos-project](https://github.com/feniks-rtos/feniks-rtos-project.git).
The project consists of the following GitHub submodule repositories.

- [libfeniks](https://github.com/feniks-rtos/libfeniks.git)

    Standard C library. Written from scratch for Feniks-RTOS.

- [feniks-rtos-build](https://github.com/feniks-rtos/feniks-rtos-build.git)

    Building scripts, makefile templates, rules, flags definitions, target selection and
    toolchain.
- [feniks-rtos-corelibs](https://github.com/feniks-rtos/feniks-rtos-corelibs.git)

    Libraries for use in user space.

- [feniks-rtos-devices](https://github.com/feniks-rtos/feniks-rtos-devices.git)

    Hardware drivers.

- [feniks-rtos-doc](https://github.com/feniks-rtos/feniks-rtos-doc.git)

    Documentation.

- [feniks-rtos-filesystems](https://github.com/feniks-rtos/feniks-rtos-filesystems.git)

    Filesystem drivers.

- [feniks-rtos-hostutils](https://github.com/feniks-rtos/feniks-rtos-hostutils.git)

    Utilities for development PC (e.g. a tool for transferring system binary image to the
    target).
- [feniks-rtos-kernel](https://github.com/feniks-rtos/feniks-rtos-kernel.git)

    Microkernel repository.

- [feniks-rtos-lwip](https://github.com/feniks-rtos/feniks-rtos-lwip.git)

    LwIP network stack.

- [feniks-rtos-ports](https://github.com/feniks-rtos/feniks-rtos-ports.git)

    Linux (and potentially other OSes) applications ported to Feniks-RTOS.

- [feniks-rtos-posixsrv](https://github.com/feniks-rtos/feniks-rtos-posixsrv.git)

    POSIX server; user space server that is providing additional POSIX features not
    provided by the kernel itself (e.g.
    pipes).
- [feniks-rtos-tests](https://github.com/feniks-rtos/feniks-rtos-tests.git)

    Tests based on our own framework.

- [feniks-rtos-usb](https://github.com/feniks-rtos/feniks-rtos-usb.git)

    USB stack (both host and device).

- [feniks-rtos-utils](https://github.com/feniks-rtos/feniks-rtos-utils.git)

    System utilities (e.g. native shell psh).

- [plo](https://github.com/feniks-rtos/plo.git)

    Feniks-RTOS bootloader.

There are other directories and files directly in `feniks-rtos-project`.

- `_fs/` - rootfs template,

- `_targets/` - rules for building the system for each hardware target,

- `_user/` - user applications are placed here. Some demos are available from the box - e.g. hello world, voxeldemo,

- `mtd-utils` - outside tool for creating jffs2 partitions,

- `riscv` - bootloader for RISC-V CPU,

- `scripts` - bash scripts for running Feniks-RTOS on simulators (e.g. QEMU),

- `build.project` - bash include file, defines how to build the whole system, it is included by
feniks-rtos-build/build.sh,

- `busybox-config` - configuration for busybox (baseline Linux based toolkit and shell),

- `docker-build.sh` - script for building using docker (docker allows user to not have toolchain on his or
her development PC).

## See also

1. [Building Feniks-RTOS image](index.md)
2. [Building script](script.md)
3. [Toolchain](toolchain.md)
4. [Table of Contents](../index.md)
