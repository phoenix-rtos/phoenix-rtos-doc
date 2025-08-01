# Running system on <nobr>ia32-generic-qemu</nobr>

This version is designated for generic PC based on the IA32 processor. To launch this version the final disk image
should be provided. The image is created as the final artifact of the `phoenix-rtos-project` building and is located in
the `_boot` directory. The image consists of the bootloader (plo), kernel, TTY VGA driver, ATA driver with ext2
filesystem.

See [Building](../building/index.md) chapter.

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
  qemu-system-i386 --version
  ```

  ```console
  ~$ qemu-system-i386 --version
  QEMU emulator version 4.2.1 (Debian 1:4.2-3ubuntu6.24)
  Copyright (c) 2003-2019 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

To run the system image under QEMU you should type the following command
(launched from `phoenix-rtos-project` directory).

```console
./scripts/ia32-generic-qemu.sh
```

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal.

![Image](../_static/images/quickstart/qemu-ia32-generic.png)

To get the available command list please type:

```console
help
```

![Image](../_static/images/quickstart/qemu-ia32-generic-help.png)

In order to run one of the user applications you should type `/usr/bin/appname`, for example:

```console
/usr/bin/voxeldemo
```

The result is presented below.

```{only} html
![Output sample](../_static/gifs/voxeldemo.gif)
```

```{only} latex
![Output sample](../_static/images/pdf/voxeldemo.png)
```

You can press `ctrl + c` to quit the voxeldemo app.

To get the list of working processes please type:

```console
ps
```

![Image](../_static/images/quickstart/qemu-ia32-generic-ps.png)

There is a possibility to run the ash shell, it can be launched using the following command.

```console
/bin/ash
```

![Image](../_static/images/quickstart/qemu-ia32-generic-ash.png)

Phoenix-RTOS image can be also launched on multiple processor cores. To do this please define the number of cores
(e.g. 4) using the following command (launched from the `phoenix-rtos-project` directory).

```console
qemu-system-i386 -hda _boot/phoenix-ia32-generic.disk -smp 4
```

The number of detected cores is presented during kernel initialization.

![Image](../_static/images/quickstart/qemu-ia32-generic-smp.png)

## Running image on regular hardware

To run the image on regular hardware please be sure that a target system is equipped with an ATA disk supporting the
PATA interface. The image should be copied to the boot disk using the `dd` command (it is assumed that the target
disk is represented by /dev/sda block device).

```console
dd if=_boot/ia32-generic-pc/phoenix.disk of=/dev/sda
```
