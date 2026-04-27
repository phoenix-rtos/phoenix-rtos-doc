# Running system on <nobr>sparcv8leon-generic-qemu</nobr>

These instructions describe how to run a Phoenix-RTOS system image for the `sparcv8leon-generic-qemu` target
architecture.

Note that the build artifacts, including the system image, should be first provided in the `_boot` directory.

If you haven't run the `build.sh` script yet, run it for `sparcv8leon-generic-qemu` target.

See [Building](../building/index.md) chapter.

## Running the system image

Support for the `leon3_generic` machine in QEMU has been greatly improved in QEMU 9.0.0. It is recommended to use QEMU
version 9.0.0 or later to run the Phoenix-RTOS system image for the `sparcv8leon-generic-qemu` target architecture.
To obtain QEMU in this version on Ubuntu 22.04, you must build it from source.

  <details>
  <summary>How to build QEMU on Ubuntu</summary>

- Download QEMU 9.0.2 (or later) source code from the official repository and build for the `sparc-softmmu` target:

  ```shell
  sudo apt update && \  
  sudo apt install -y ninja-build \  
  libglib2.0-dev && \
  git clone https://gitlab.com/qemu-project/qemu.git -b v9.0.2 && \
  cd qemu && \
  git submodule update --init --recursive && \
  ./configure --target-list=sparc-softmmu && \
  make && \
  sudo make install
  ```

- Check if QEMU is properly installed:

  ```shell
  qemu-system-sparc --version
  ```

  ```shell
  QEMU emulator version 9.0.2 (v9.0.2)
  Copyright (c) 2003-2024 Fabrice Bellard and the QEMU Project developers
  ```

  </details>

To run the image under QEMU, use the following script provided in the `phoenix-rtos-project` repository:

  ```shell
  ./scripts/sparcv8leon-generic-qemu.sh
  ```

## Using Phoenix-RTOS

Once booted, the `psh` shell prompt appears. See [Shell basics](psh-basics.md) for an introduction to
the available shell commands, process inspection, and running programs.

To quit QEMU, press `ctrl+a` then `x`.  
