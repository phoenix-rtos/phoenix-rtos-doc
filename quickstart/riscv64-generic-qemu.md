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

To run the image under QEMU you should type:

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

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal. To get the available
command list please type:

```shell
help
```

```
(psh)% help
Available commands:
 bind          - binds device to directory
 cat           - concatenate file(s) to standard output
 cd            - changes the working directory
 clear         - clear the terminal screen
 cp            - copy file
 date          - print/set the system date and time
 dd            - copy a file according to the operands
 df            - print filesystem statistics
 dmesg         - read kernel ring buffer
 echo          - display a line of text
 edit          - text editor
 exec          - replace shell with the given command
 exit          - exits shell
 export        - set and export variables list to environment
 help          - prints this help message
 history       - prints commands history
 hm            - health monitor, spawns apps and keeps them alive
 ifconfig      - configures network interfaces
 kill          - terminates process
 ln            - make links between files
 ls            - lists files in the namespace
 mem           - prints memory map
 mkdir         - creates directory
 mount         - mounts a filesystem
 nc            - TCP and UDP connections and listens
 nslookup      - queries domain name servers
 ntpclient     - set the system's date from a remote host
 perf          - track kernel performance events
 ping          - ICMP ECHO requests
 pm            - process monitor
 printenv      - print all or part of environment
 ps            - prints processes and threads
 pwd           - prints the name of current working directory
 reboot        - restarts the machine
 reset         - restore terminal from abnormal state
 rm            - unlink files or remove empty directories
 rmdir         - remove empty directories
 sync          - synchronizes device
 sysexec       - launch program from syspage using given map
 top           - top utility
 touch         - changes file timestamp
 tty           - print or replace interactive shell tty device
 umount        - unmount a filesystem
 unset         - unset list of environment variables
 uptime        - prints how long the system has been running
 wget          - downloads a file using http
(psh)%
```

To get the list of working processes please type:

```shell
ps
```

```
(psh)% ps
  PID  PPID PR STATE  %CPU   WAIT      TIME    VMEM THR CMD
    0     0  4 ready  79.7  324ms  00:00:02    2.2M   2 [idle]
    1     0  4 sleep   0.2    3ms  00:00:00       0   1 init
    3     1  1 sleep   4.3    6ms  00:00:00    128K   4 uart16550
    5     1  4 sleep   0.7    2ms  00:00:00    104K   1 dummyfs
    7     1  1 sleep  10.8    3ms  00:00:00    180K   4 virtio-blk
    9     1  4 sleep   1.1    4ms  00:00:00    136K   5 /bin/posixsrv
   10     1  4 ready   1.1    1ms  00:00:00    184K   1 /bin/psh
(psh)%
```
