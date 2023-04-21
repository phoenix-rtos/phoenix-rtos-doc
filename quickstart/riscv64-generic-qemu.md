# Running system on `riscv64-generic-qemu`
This version is designated for RISC-V 64 processor based virt machine implemented by `qemu-system-riscv64`. To launch this version two files should be provided - kernel file integrated with SBI firmware with embedded UART16550 interface driver, dummyfs filesystem and the`psh` shell and disk image with ext2 filesystem.

The files are created as the final artifact of the `phoenix-rtos-project` building and are located in the `_boot` directory. See [how to build the Phoenix-RTOS system image](../building/README.md).

## Running image under qemu
Firstly, you need to install qemu emulator.
  <details>
  <summary>How to get qemu (Ubuntu)</summary>

  - Install the required packages

  ```
  sudo apt-get update && \
  sudo apt-get install qemu-kvm \
  qemu virt-manager \
  virt-viewer libvirt-clients \
  libvirt-daemon-system \
  bridge-utils virtinst \
  libvirt-daemon \
  qemu-system-misc
  ```

  - Check if qemu is properly installed:

  ```
  qemu-system-riscv64 --version
  ```

  ```bash
  ~$ qemu-system-riscv64 --version
  QEMU emulator version 4.2.1 (Debian 1:4.2-3ubuntu6.24)
  Copyright (c) 2003-2019 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

  <details>
  <summary>How to get qemu (Mac OS)</summary>

  - Install the required packages

  ```
  brew update && \
  brew install qemu
  ```

  - Check if qemu is properly installed:

  ```
  qemu-system-riscv64 --version
  ```

  ```bash
  ~$ qemu-system-riscv64 --version
  QEMU emulator version 8.0.0
  Copyright (c) 2003-2022 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

To run the image under qemu you should type:

```bash
./scripts/riscv64-generic-qemu.sh
```

<img src="_images/riscv64-generic-qemu1.png" width="700px">
</br>
<img src="_images/riscv64-generic-qemu2.png" width="700px">

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal. To get the available command list please type:

```
help
```

<img src="_images/riscv64-generic-qemu-help.png" width="700px">

To get the list of working processes please type:

```bash
ps
```

<img src="_images/riscv64-generic-qemu-ps.png" width="700px">

## See also

1. [Running system on targets](README.md)
2. [Table of Contents](../README.md)
