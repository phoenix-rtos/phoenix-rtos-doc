# Running system on `riscv64-virt`
This version is designated for RISC-V 64 processor based virt machine implemented by `qemu-system-riscv64`. To launch this version two files should be provided - kernel file integrated with SBI firmware with embedded UART16550 interface driver, dummyfs filesystem and the`psh` shell and disk image with ext2 filesystem.

The files are created as the final artifact of the `phoenix-rtos-project` building and are located in the `_boot` directory. See [how to build the Phoenix-RTOS system image](../building/README.md).

## Running image under qemu
Firstly, you need to install qemu emulator.
  <details>
  <summary>How to get qemu (Ubuntu 20.04)</summary>

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

  <img src="_images/qemu-version-riscv64.png" width="600px">

  </details> 

To run the image under qemu you should type:

```bash
./scripts/riscv64-virt.sh
```

<img src="_images/qemu-riscv64-virt1.png" width="600px">
</br>
<img src="_images/qemu-riscv64-virt2.png" width="600px">

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal. To get the available command list please type:

```
help
```

<img src="_images/qemu-riscv64-virt-help.png" width="600px">

To get the list of working processes please type:

```bash
ps
```

<img src="_images/qemu-riscv64-virt-ps.png" width="600px">

## See also

1. [Running system on targets](README.md)
2. [Table of Contents](../README.md)
