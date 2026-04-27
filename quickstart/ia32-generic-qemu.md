# Running system on <nobr>ia32-generic-qemu</nobr>

This page covers running Phoenix-RTOS on a generic IA32 (x86) PC using QEMU. The disk image is built to `_boot/`
and includes the bootloader (plo), kernel, TTY VGA driver, ATA driver, and ext2 filesystem.

See [Building](../building/index.md) chapter.

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
  qemu-system-i386 --version
  ```

  ```shell
  ~$ qemu-system-i386 --version
  QEMU emulator version 4.2.1 (Debian 1:4.2-3ubuntu6.24)
  Copyright (c) 2003-2019 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

Run from the project root:

```shell
./scripts/ia32-generic-qemu.sh
```

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal.

```
Phoenix-RTOS microkernel v. 2.97 rev: 400c40d
hal: GenuineIntel Family 6 Model 6 Stepping 3 (4/4), cores=1
hal: +fpu+de+pse+tsc+msr+pae+apic+pge+cmov+pat
hal: Using i8259 interrupt controller
vm: Initializing page allocator (1332+452)/131008KB, page_t=16
vm: KCYPPS[128H]PP[20,]PPPB[80x][16B][14,]P[192K]P[32272,][32B][1015744x][64B]
vm: Initializing memory mapper: (8046*60) 482760
vm: Initializing kernel memory allocator: (64*48) 3072
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [101]
main: Decoding programs from data segment
main: Starting syspage programs: 'pc-ata', 'pc-tty', 'psh'
(psh)%
```

See [Shell basics](psh-basics.md) for an introduction to the available shell commands, process inspection,
and running programs.

To run one of the user applications, type its path:

```shell
/usr/bin/voxeldemo
```

<!-- REVIEW: filler - remove or rephrase -->
The result is presented below.

```{only} html
![Output sample](../_static/gifs/voxeldemo.gif)
```

```{only} latex
![Output sample](../_static/images/pdf/voxeldemo.png)
```

You can press `ctrl + c` to quit the voxeldemo app.

The `ash` shell (BusyBox) is also available:

```shell
/bin/ash
```

```
(psh)% /bin/ash

BusyBox v1.27.2 (2021-10-28 15:31:03 CEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

~ #
```

To run on multiple cores, pass `-smp` to QEMU:

```shell
qemu-system-i386 -hda _boot/phoenix-ia32-generic.disk -smp 4
```

The kernel reports the detected core count during boot:

```
Phoenix-RTOS microkernel v. 2.97 rev: 400c40d
hal: GenuineIntel Family 6 Model 6 Stepping 3 (4/4), cores=4
hal: +fpu+de+pse+tsc+msr+pae+apic+pge+cmov+pat
hal: Using i8259 interrupt controller
...
main: Starting syspage programs: 'pc-ata', 'pc-tty', 'psh'
(psh)%
```

## Network setup on ia32-generic-qemu

```{note}
This guide was tested on `Ubuntu 24.04 LTS` host OS.
```

Follow these steps:

### 1. Create and set up `vibr0` bridge on a host using `qemu-bridge-helper`

Install the required package and ensure that `libvirtd` is running:

```shell
sudo apt update
sudo apt install qemu-system-common libvirt-clients libvirt-daemon
systemctl enable libvirtd.service
systemctl start libvirtd.service
```

Start the default network bridge, and configure it to run on startup.

```shell
sudo virsh net-autostart --network default
sudo virsh net-start --network default
```

After that verify that the IP range `192.168.122.1/24` is reported by the `vibr0` bridge:

```shell
ip addr show virbr0
```

The expected output:

```shell
virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
  link/ether xx:xx:xx:xx:xx:xx brd ff:ff:ff:ff:ff:ff
  inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
    valid_lft forever preferred_lft forever
```

If `/etc/qemu` directory does not exist, create it and provide required privileges:

```shell
sudo mkdir /etc/qemu
sudo chmod 755 /etc/qemu
```

Provide bridge configuration for QEMU:

```shell
echo "allow virbr0" | sudo tee -a /etc/qemu/bridge.conf > /dev/null
sudo chmod 644 /etc/qemu/bridge.conf
```

Set permissions on `qemu-bridge-helper` to allow running QEMU without root privileges.

```{warning}
Mind that setting this permission is not fully secure.
See this [discussion](https://bugs.launchpad.net/ubuntu/+source/qemu/+bug/1882420).
```

```shell
sudo chmod u+s /usr/lib/qemu/qemu-bridge-helper
```

Sources used: <https://apiraino.github.io/qemu-bridge-networking/>,
<https://mike42.me/blog/2019-08-how-to-use-the-qemu-bridge-helper-on-debian-10>

### 2. If IPv6 is needed, change the configuration of `virbr0`

```shell
sudo virsh net-destroy default
sudo virsh net-edit default
```

The commands above open the editor of the configuration file of `virbr0`. There are two necessary changes:

- Add IPv6 address to the bridge interface:

  ```XML
  <ip family='ipv6' address='2001:db8:dead:beef:fe::2' prefix='64'/>
  ```

- Enable NAT for IPv6:

  ```XML
  <forward mode='nat'>
    <nat ipv6='yes'/>
  </forward>
  ```

The overall config should look something like this:

```XML
<network>
  <name>default</name>
  <uuid>a9e032b7-e32f-4f91-a273-e6c6f15b8904</uuid>
  <forward mode='nat'>
    <nat ipv6='yes'/>
  </forward>
  <bridge name='virbr0' stp='on' delay='0'>
  <mac address='52:54:00:99:4d:c3'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
    </dhcp>
  </ip>
  <ip family='ipv6' address='2001:db8:dead:beef:fe::2' prefix='64'/>
</network>
```

Save the config file and start the bridge by running:

```shell
sudo virsh net-start default
```

### 3. Launch QEMU using a starting script with `net` suffix

```shell
./scripts/ia32-generic-qemu-net.sh
```

### 4. Configure network on the target

This configuration can be done in two ways: using `psh` tools or `Busybox`.

```{note}
For now IPv6 configuration is possible only using `Busybox`.
```

#### Network configuration using `psh`

Enable dynamic IP address assignment and set default gateway:

```shell
ifconfig en1 dynamic
route add default gw 192.168.122.1 en1
```

Here `192.168.122.1` is the address of the virtual bridge interface on the host.
Adjust the address if your bridge uses a different subnet.

#### Network configuration using `Busybox` and `rc` script

```{note}
By default `IP` is assigned using `DHCP`. For other options, see
`_projects/ia32-generic-qemu/rootfs-overlay/etc/rc.conf.d/network`
```

```{note}
Other programs are also started by this script. For details, see
`_projects/ia32-generic-qemu/rootfs-overlay/etc/rc`
```

Run the script by calling:

```shell
/linuxrc
```

The full system with POSIX shell starts:

```
BusyBox v1.27.2 (2022-06-30 17:42:15 CEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

         Welcome to Phoenix-RTOS

root@?:~ #
```

```{note}
Some applications may require accurate datetime to be set. See how it is done in case of [Azure IoT SDK](../ports/azure_sdk.md).
```

## Running image on regular hardware

To run on regular hardware, ensure the target has an ATA disk with PATA interface support. The image should be copied to the boot disk using the `dd` command (it is assumed that the target
disk is represented by /dev/sda block device).

```shell
dd if=_boot/ia32-generic-pc/phoenix.disk of=/dev/sda
```
