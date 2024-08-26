# Running system on <nobr>sparcv8leon3-generic-qemu</nobr>

These instructions describe how to run a Phoenix-RTOS system image for the `sparcv8leon3-generic-qemu` target
architecture.

Note that the build artifacts, including the system image, should be first provided in the `_boot` directory.

If you haven't run the `build.sh` script yet, run it for `sparcv8leon3-generic-qemu` target.

See [how to build the Phoenix-RTOS system image](../building/index.md).

## Running the system image

Support for the `leon3_generic` machine in QEMU has been greatly improved in QEMU 9.0.0. It is recommended to use QEMU
version 9.0.0 or later to run the Phoenix-RTOS system image for the `sparcv8leon3-generic-qemu` target architecture.
To obtain QEMU in this version on Ubuntu 22.04, you must build it from source.

  <details>
  <summary>How to build QEMU (Ubuntu 22.04)</summary>

- Download QEMU 9.0.2 (or later) source code from the official repository and build for the `sparc-softmmu` target:

  ```console
  git clone https://gitlab.com/qemu-project/qemu.git -b v9.0.2 && \
  cd qemu && \
  git submodule update --init --recursive && \
  ./configure --target-list=sparc-softmmu && \
  make && \
  sudo make install
  ```

- Check if QEMU is properly installed:

  ```console
  qemu-system-sparc --version
  ```

  ```console
  ~$ qemu-system-arm --version
  QEMU emulator version 9.0.2 (v9.0.2)
  Copyright (c) 2003-2024 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

To run the image under QEMU, use the following script provided in the `phoenix-rtos-project` repository:

  ```console
  ./scripts/sparcv8leon3-generic-qemu.sh
  ```

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal.

![Image](_images/sparcv8leon3-qemu-psh.jpg)

To get the available command list use command:

```console
help
```

![Image](_images/sparcv8leon3-qemu-help.jpg)

To get the list of working processes use command:

```console
ps
```

![Image](_images/sparcv8leon3-qemu-ps.jpg)

## See also

1. [Running system on targets](index.md)
2. [Table of Contents](../index.md)
