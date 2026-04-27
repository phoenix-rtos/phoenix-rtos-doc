# Running system on <nobr>riscv64-generic-spike</nobr>

This version is designated for RISC-V 64 processors based spike machine implemented by the Spike (`riscv-isa-sim`)
emulator. To launch this version `phoenix.osbi` file should be provided - system image with integrated OpenSBI
bootloader, containing PLO, kernel, console driver, dummyfs filesystem and the `psh` shell.

The file is created as the final artifact of the `phoenix-rtos-project` build and is located in the `_boot` directory.
See [Building](../building/index.md) chapter.

## Running image under the spike

Firstly, you need to install a spike simulator.

  <details>
  <summary>How to install spike simulator (Ubuntu 20.04)</summary>

  1. Clone the `riscv-isa-sim` GitHub repository. System was tested on commit `5fa1cd54` on `master` branch.

      ```shell
      git clone https://github.com/riscv-software-src/riscv-isa-sim.git --single-branch
      ```

  2. Enter the downloaded repository

      ```shell
      cd riscv-isa-sim
      ```

  3. Check out the commit `5fa1cd54`

      ```shell
      git checkout 5fa1cd54
      ```

  4. Install the device-tree-compiler

      ```shell
      sudo apt-get update && \
      sudo apt-get install device-tree-compiler
      ```

  5. Install the Spike RISC-V ISA Simulator

      ```shell
      mkdir build && \
      cd build && \
      ../configure --prefix=$RISCV && \
      make && \
      sudo make install
      ```

  </details>
  </br>

Then, to run the image under spike you should change the directory to `phoenix-rtos-project` and type:

```shell
./scripts/riscv64-generic-spike.sh
```

```
~/phoenix-rtos-project$ ./scripts/riscv64-generic-spike.sh

OpenSBI v1.4
   ____                    _____ ____ _____
  / __ \                  / ____|  _ \_   _|
 | |  | |_ __   ___ _ __ | (___ | |_) || |
 | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
 | |__| | |_) |  __/ | | |____) | |_) || |_
  \____/| .__/ \___|_| |_|_____/|____/_____|
        | |
        |_|

Platform Name             : ucbbar,spike-bare
Platform Features         : medeleg
Platform HART Count       : 1
Platform IPI Device       : aclint-mswi
Platform Timer Device     : aclint-mtimer @ 10000000Hz
Platform Console Device   : uart8250
Platform HSM Device       : ---
Platform PMU Device       : ---
Platform Reboot Device    : htif
Platform Shutdown Device  : htif
Platform Suspend Device   : ---
Platform CPPC Device      : ---
Firmware Base             : 0x80000000
Firmware Size             : 195 KB
Firmware RW Offset        : 0x20000
Firmware RW Size          : 67 KB
Firmware Heap Offset      : 0x28000
Firmware Heap Size        : 35 KB (total), 2 KB (reserved), 9 KB (used), 23 KB (free)
Firmware Scratch Size     : 4096 B (total), 328 B (used), 3768 B (free)
Runtime SBI Version       : 2.0

Domain0 Name              : root
Domain0 Boot HART         : 0
Domain0 HARTs             : 0*
Domain0 Region00          : 0x0000000010000000-0x0000000010000fff M: (I,R,W) S/U: (R,W)
Domain0 Region01          : 0x0000000080000000-0x000000008001ffff M: (R,X) S/U: ()
Domain0 Region02          : 0x0000000080020000-0x000000008003ffff M: (R,W) S/U: ()
Domain0 Region03          : 0x0000000002080000-0x00000000020bffff M: (I,R,W) S/U: ()
Domain0 Region04          : 0x0000000002000000-0x00000000020fffff M: (I,R,W) S/U: ()
Domain0 Region05          : 0x000000000c000000-0x000000000cffffff M: (I,R,W) S/U: (R,W)
Domain0 Region06          : 0x0000000000000000-0xffffffffffffffff M: () S/U: (R,W,X)
Domain0 Next Address      : 0x0000000080200000
Domain0 Next Arg1         : 0x0000000082200000
Domain0 Next Mode         : S-mode
Domain0 SysReset          : yes
...
Boot HART PMP Address Bits: 54
Boot HART MHPM Info       : 0 (0x00000000)
Boot HART MIDELEG         : 0x0000000000000222
Boot HART MEDELEG         : 0x000000000000b109
Phoenix-RTOS loader v. 1.21 rev: b4d8016
hal: RISC-V 64-bit Generic
cmd: Executing pre-init script
console: Setting console to 0.0
Waiting for input,     0 [ms]
Phoenix-RTOS microkernel v. 3.0 rev: 290441b
hal: ucbbar,spike-bare (ucbbar,spike-bare-dev)
hal: riscv@1000MHz(rv64imafdc_zicntr_zihpm+riscv,sv57)
hal: Using PLIC interrupt controller
hal: Using hypervisor timer
vm: Initializing page allocator (2396+4)/260096KB, page_t=32
vm: [524800x][32H][35K][444H]P[32H][3579.][55A][4014.]B[56831.]
vm: Initializing memory mapper: (15996*112) 1791552
vm: Initializing kernel memory allocator: (32*88) 2816
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [100]
main: Starting syspage programs: 'dummyfs', 'spike-tty', 'psh'
dummyfs: initialized
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
    bind       - binds device to directory
    cat        - concatenate file(s) to standard output
    cd         - changes the working directory
    clear      - clear the terminal screen
    cp         - copy file
    date       - print/set the system date and time
    dd         - copy a file according to the operands
    df         - print filesystem statistics
    dmesg      - read kernel ring buffer
    echo       - display a line of text
    edit       - text editor
    exec       - replace shell with the given command
    exit       - exits shell
    export     - set and export variables list to environment
    help       - prints this help message
    history    - prints commands history
    hm         - health monitor, spawns apps and keeps them alive
    ifconfig   - configures network interfaces
    kill       - terminates process
    ln         - make links between files
    ls         - lists files in the namespace
    mem        - prints memory map
    mkdir      - creates directory
    mount      - mounts a filesystem
    nc         - TCP and UDP connections and listens
    nslookup   - queries domain name servers
    ntpclient  - set the system's date from a remote host
    perf       - track kernel performance events
    ping       - ICMP ECHO requests
    pm         - process monitor
    printenv   - print all or part of environment
    ps         - prints processes and threads
    pwd        - prints the name of current working directory
    reboot     - restarts the machine
    reset      - restore terminal from abnormal state
    rm         - unlink files or remove empty directories
    rmdir      - remove empty directories
    sync       - synchronizes device
    sysexec    - launch program from syspage using given map
    top        - top utility
    touch      - changes file timestamp
    tty        - print or replace interactive shell tty device
    umount     - unmount a filesystem
    unset      - unset list of environment variables
    uptime     - prints how long the system has been running
    wget       - downloads a file using http
(psh)%
```

To get the list of working processes please type:

```shell
ps
```

```
(psh)% ps
ps
      PID     PPID  PR  STATE  %CPU     WAIT        TIME    VMEM THR CMD
        0        0   4  ready  90.7     106ms    00:00:02      4M   2 [idle]
        1        0   4  sleep   0.3       3ms    00:00:00       0   1 init
        2        1   4  sleep   3.7       2ms    00:00:00    320K   1 dummyfs
        3        1   4  sleep   3.1       2ms    00:00:00    120K   4 spike-tty
        4        1   4  ready   1.7       2ms    00:00:00    184K   1 psh
(psh)%
```
