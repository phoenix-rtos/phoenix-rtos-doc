# Running system on <nobr>riscv64-generic-qemu</nobr>

This version is designated for RISC-V 64 processors based virtual machine implemented by `qemu-system-riscv64`.
To launch this version two files should be provided - `phoenix.disk` file integrated with SBI firmware with embedded
PLO, kernel, UART16550 interface and virtio-blk drivers, dummyfs filesystem and the `psh` shell and `rootfs.disk` image
with the ext2 filesystem.

The files are created as the final artifact of the `phoenix-rtos-project` building and are located in the `_boot`
directory. See [Building](../building/index.md) chapter.

## Running image under QEMU

Install QEMU:
  <details>
  <summary>How to get QEMU (Ubuntu)</summary>

- Install the required packages

  ```shell
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

  ```shell
  qemu-system-riscv64 --version
  ```

  ```shell
  ~$ qemu-system-riscv64 --version
  QEMU emulator version 4.2.1 (Debian 1:4.2-3ubuntu6.24)
  Copyright (c) 2003-2019 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

To run the image under QEMU type:

```shell
./scripts/riscv64-generic-qemu.sh
```

OpenSBI will initialize first, followed by PLO and the kernel:

```
OpenSBI v1.4
Platform Name             : riscv-virtio,qemu
Platform HART Count       : 1
Runtime SBI Version       : 2.0
...
Phoenix-RTOS loader v. 1.21 rev: 8d0f6ec
hal: RISC-V 64-bit Generic
cmd: Executing pre-init script
console: Setting console to 0.0
Waiting for input,      0 [ms]
Phoenix-RTOS microkernel v. 3.0 rev: 290441b
hal: riscv-virtio,qemu (cfi-flash)
hal: riscv@3964MHz(rv64imafdcsu+riscv,sv48)
hal: Using PLIC interrupt controller
hal: Using hypervisor timer
vm: Initializing page allocator (1432+8)/129024KB, page_t=32
vm: [524800x][32H][35K][29H][71A][191H][7834.]BB[24062.]
vm: Initializing memory mapper: (7919*112) 886928
vm: Initializing kernel memory allocator: (32*88) 2816
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [100]
main: Starting syspage programs: 'dummyfs;-N;devfs;-D', 'uart16550', 'psh;-i;/etc/rc.psh', 'virtio-blk;-r;0:0'
dummyfs: initialized
virtio-blk: initialized
(psh)%
```

## Using Phoenix-RTOS

Once booted, the `psh` shell prompt appears. See [Shell basics](psh-basics.md) for an introduction to
the available shell commands, process inspection, and running programs.
