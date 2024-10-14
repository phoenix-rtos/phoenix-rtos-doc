# Running system on <nobr>ia32-generic-qemu</nobr>

This version is designated for generic PC based on the IA32 processor. To launch this version the final disk image
should be provided. The image is created as the final artifact of the `phoenix-rtos-project` building and is located in
the `_boot` directory. The image consists of the bootloader (plo), kernel, TTY VGA driver, ATA driver with ext2
filesystem.

See [how to build the Phoenix-RTOS system image](../building/index.md).

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

<details>
  <summary>How to get QEMU (macOS)</summary>

- Install the required packages

  ```zsh
  brew update && \
  brew install qemu
  ```

- Check if QEMU is properly installed:

  ```zsh
  qemu-system-i386 --version
  ```

  ```zsh
  ~$ qemu-system-i386 --version
  QEMU emulator version 8.0.0
  Copyright (c) 2003-2022 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

To run the system image under QEMU you should type the following command
(launched from `phoenix-rtos-project` directory).

```console
./scripts/ia32-generic-qemu.sh
```

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal.

![Image](_images/qemu-ia32-generic.png)

To get the available command list please type:

```console
help
```

![Image](_images/qemu-ia32-generic-help.png)

In order to run one of the user applications you should type `/usr/bin/appname`, for example:

```console
/usr/bin/voxeldemo
```

The result is presented below.

![Image](_gifs/voxeldemo.gif)

You can press `ctrl + c` to quit the voxeldemo app.

To get the list of working processes please type:

```console
ps
```

![Image](_images/qemu-ia32-generic-ps.png)

There is a possibility to run the ash shell, it can be launched using the following command.

```console
/bin/ash
```

![Image](_images/qemu-ia32-generic-ash.png)

Phoenix-RTOS image can be also launched on multiple processor cores. To do this please define the number of cores
(e.g. 4) using the following command (launched from the `phoenix-rtos-project` directory).

```console
qemu-system-i386 -hda _boot/phoenix-ia32-generic.disk -smp 4
```

The number of detected cores is presented during kernel initialization.

![Image](_images/qemu-ia32-generic-smp.png)

## Network setup on `ia32-generic-qemu`

- Note: This guide was tested on `Ubuntu 20.04 LTS` host OS.

There are few steps to follow:

 1. Create and set up `vibr0` bridge on a host using `qemu-bridge-helper`:

    - Install the required package and ensure that `libvirtd` is running:

      ```bash
      sudo apt-get update
      sudo apt-get install qemu-system-common
      systemctl enable libvirtd.service
      systemctl start libvirtd.service
      ```

    - Start the default network bridge, and configure it to run on startup.

      ```bash
      sudo virsh net-autostart --network default
      sudo virsh net-start --network default
      ```

    - After that verify that the IP range `192.168.122.1/24` is reported by the `vibr0` bridge:

      ```bash
      ip addr show virbr0
      ```

    - The expected output:

      ```bash
       virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
          link/ether xx:xx:xx:xx:xx:xx brd ff:ff:ff:ff:ff:ff
          inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
             valid_lft forever preferred_lft forever
      ```

    - Set up `qemu-bridge-helper` (`chmod` is used here to allow running QEMU without root privileges)

      ```bash
      echo "allow virbr0" > /etc/qemu/bridge.conf
      sudo chmod a+rw /etc/qemu/bridge.conf
      ```

    - If `/etc/qemu` directory does not exist, create it and provide required privileges:

      ```bash
      sudo mkdir /etc/qemu
      sudo chmod a+rw /etc/qemu
      echo "allow virbr0" > /etc/qemu/bridge.conf
      sudo chmod a+rw /etc/qemu/bridge.conf
      ```

      ![Image](_images/ia32_sdk_vibr_setup.png)

    - Sources: <https://apiraino.github.io/qemu-bridge-networking/>,
     <https://mike42.me/blog/2019-08-how-to-use-the-qemu-bridge-helper-on-debian-10>

 2. Launch `qemu` using a starting script with `net` suffix:

      ```bash
      ./scripts/ia32-generic-qemu-net.sh
      ```

 3. Configure network and run `ash` (Busybox applet) using `rc` script:

      - Note: By default `IP` is assigned using `DHCP`. For other possibilities please check the configuration file
       located in `_projects/ia32-generic-qemu/rootfs-overlay/etc/rc.conf.d/network`

      - Note: There are other programs executed by the script. For more information please check the content of the `rc`
       file for `ia32-generic-qemu` in `_projects/ia32-generic-qemu/rootfs-overlay/etc/rc`

        ```bash
        /linuxrc
        ```

      - As you can see, the advanced version of `Phoenix-RTOS` with `POSIX` shell has been started:

        ![Image](_images/ia32_linuxrc.png)

      - Now you can check the internet connection using the `ping` applet.

## Running image on regular hardware

To run the image on regular hardware please be sure that a target system is equipped with an ATA disk supporting the
PATA interface. The image should be copied to the boot disk using the `dd` command (it is assumed that the target
disk is represented by /dev/sda block device).

```console
  dd if=_boot/ia32-generic-pc/phoenix.disk of=/dev/sda
```

## See also

1. [Running system on targets](index.md)
2. [Table of Contents](../index.md)
