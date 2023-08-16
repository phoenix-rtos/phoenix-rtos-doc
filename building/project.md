# Reference project

The main repository of Phoenix-RTOS is the
[phoenix-rtos-project](https://github.com/phoenix-rtos/phoenix-rtos-project.git).
The project consists of the following GitHub submodule repositories.

- [libphoenix](https://github.com/phoenix-rtos/libphoenix.git)

    Standard C library. Written from scratch for Phoenix-RTOS

- [phoenix-rtos-build](https://github.com/phoenix-rtos/phoenix-rtos-build.git)

    Building scripts, makefile templates, rules, flags definitions, target selection and
    toolchain
- [phoenix-rtos-corelibs](https://github.com/phoenix-rtos/phoenix-rtos-corelibs.git)

    Libraries for use in user space.

- [Phoenix-rtos-devices](https://github.com/phoenix-rtos/phoenix-rtos-devices.git)

    Hardware drivers

- [phoenix-rtos-doc](https://github.com/phoenix-rtos/phoenix-rtos-doc.git)

    Documentation

- [phoenix-rtos-filesystems](https://github.com/phoenix-rtos/phoenix-rtos-filesystems.git)

    Filesystem drivers.

- [Phoenix-rtos-hostutils](https://github.com/phoenix-rtos/phoenix-rtos-hostutils.git)

    Utilities for development PC (e.g. a tool for transferring system binary image to the
    target)
- [phoenix-rtos-kernel](https://github.com/phoenix-rtos/phoenix-rtos-kernel.git)

    Microkernel repository

- [phoenix-rtos-lwip](https://github.com/phoenix-rtos/phoenix-rtos-lwip.git)

    LwIP network stack

- [phoenix-rtos-ports](https://github.com/phoenix-rtos/phoenix-rtos-ports.git)

    Linux (and potentially other OSes) applications ported to Phoenix-RTOS

- [phoenix-rtos-posixsrv](https://github.com/phoenix-rtos/phoenix-rtos-posixsrv.git)

    POSIX server; user space server that is providing additional POSIX features not
    provided by the kernel itself (e.g.
    pipes)
- [phoenix-rtos-tests](https://github.com/phoenix-rtos/phoenix-rtos-tests.git)

    Tests based on our own framework

- [phoenix-rtos-usb](https://github.com/phoenix-rtos/phoenix-rtos-usb.git)

    USB stack (both host and device)

- [phoenix-rtos-utils](https://github.com/phoenix-rtos/phoenix-rtos-utils.git)

    System utilities (e.g. native shell psh)

- [plo](https://github.com/phoenix-rtos/plo.git)

    Phoenix-RTOS bootloader

There are other directories and files directly in `phoenix-rtos-project`.

- `_fs/` - rootfs template,

- `_targets/` - rules for building the system for each hardware target,

- `_user/` - user applications are placed here. Some demos are available from the box - e.g. hello world, voxeldemo,

- `mtd-utils` - outside tool for creating jffs2 partitions,

- `riscv` - bootloader for RISC-V CPU,

- `scripts` - bash scripts for running Phoenix-RTOS on simulators (e.g. QEMU),

- `build.project` - bash include file, defines how to build the whole system, it is included by
phoenix-rtos-build/build.sh,

- `busybox-config` - configuration for busybox (baseline Linux based toolkit and shell),

- `docker-build.sh` - script for building using docker (docker allows user to not have toolchain on his or
her development PC).

## See also

1. [Building Phoenix-RTOS image](README.md)
2. [Building script](script.md)
3. [Toolchain](toolchain.md)
4. [Table of Contents](../README.md)
