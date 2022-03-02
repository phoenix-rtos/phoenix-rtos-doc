# Running system on `ia32-generic` (PC based on IA32 processor)
This version is designated for generic PC based on the IA32 processor. To launch this version the final disk image should be provided. The image is created as the final artifact of the `phoenix-rtos-project` building and is located in the `_boot` directory. The image consists of the bootloader (plo), kernel, TTY VGA driver, ATA driver with ext2 filesystem.

See [how to build the Phoenix-RTOS system image](../building/README.md).

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
  qemu-system-i386 --version
  ```

  <img src="_images/qemu-version-i386.png" width="600px">

  </details> 

To run the system image under qemu you should type the following command (launched from `phoenix-rtos-project` directory).

```bash
./scripts/ia32-generic.sh
```

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal.

<img src="_images/qemu-ia32-generic.png" width="600px">

To get the available command list please type:

```
help
```

<img src="_images/qemu-ia32-generic-help.png" width="600px">

In order to run one of the user applications you should type `/usr/bin/appname`, for example:
```bash
/usr/bin/voxeldemo
```
The result is presented below.

<img src="_gifs/voxeldemo.gif" width="600px">

You can press `ctrl + c` to quit the voxeldemo app.

To get the list of working processes please type:

```bash
ps
```

<img src="_images/qemu-ia32-generic-ps.png" width="600px">

There is a possibility to run the ash shell, it can be launched using the following command.

```bash
/bin/ash
```

<img src="_images/qemu-ia32-generic-ash.png" width="600px">

Phoenix-RTOS image can be also launched on multiple processor cores. To do this please define the number of cores (e.g. 4) using the following command (launched from the `phoenix-rtos-project` directory).

```bash
qemu-system-i386 -hda _boot/phoenix-ia32-generic.disk -smp 4
```
The number of detected cores is presented during kernel initialization.

<img src="_images/qemu-ia32-generic-smp.png" width="600px">


## Running image on regular hardware
To run the image on regular hardware please be sure that a target system is equipped with an ATA disk supporting the PATA interface. The image should be copied to the boot disk using the `dd` command (it is assumed that the target disk is represented by /dev/sda block device).

```
  dd if=_boot/phoenix-ia32-generic.disk of=/dev/sda
```

## See also

1. [Running system on targets](README.md)
2. [Table of Contents](../README.md)