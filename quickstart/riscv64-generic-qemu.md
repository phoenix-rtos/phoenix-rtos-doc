# Running system on <nobr>riscv64-generic-qemu</nobr>

This version is designated for RISC-V 64 processors based virtual machine implemented by `qemu-system-riscv64`.
To launch this version two files should be provided - `phoenix.disk` file integrated with SBI firmware with embedded
PLO, kernel, UART16550 interface and virtio-blk drivers, dummyfs filesystem and the `psh` shell and `rootfs.disk` image
with the ext2 filesystem.

The files are created as the final artifact of the `phoenix-rtos-project` building and are located in the `_boot`
directory. See [Building](../building/index.md) chapter.

## Running image under QEMU

Firstly, you need to install QEMU emulator.
  <details>
  <summary>How to get QEMU (Ubuntu)</summary>

- Install the required packages

  ```console
  sudo apt update && \
  sudo apt install -y \
  qemu-system \
  virt-manager \
  virt-viewer \
  libvirt-clients \
  libvirt-daemon-system \
  bridge-utils \
  virtinst \
  libvirt-daemon
  ```

- Check if QEMU is properly installed:

  ```console
  qemu-system-riscv64 --version
  ```

  ```console
  ~$ qemu-system-riscv64 --version
  QEMU emulator version 4.2.1 (Debian 1:4.2-3ubuntu6.24)
  Copyright (c) 2003-2019 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

To run the image under QEMU you should type:

```console
./scripts/riscv64-generic-qemu.sh
```

![Image](../_static/images/quickstart/riscv64-generic-qemu1.png)
</br>
![Image](../_static/images/quickstart/riscv64-generic-qemu2.png)

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal. To get the available
command list please type:

```console
help
```

![Image](../_static/images/quickstart/riscv64-generic-qemu-help.png)

To get the list of working processes please type:

```console
ps
```

![Image](../_static/images/quickstart/riscv64-generic-qemu-ps.png)
