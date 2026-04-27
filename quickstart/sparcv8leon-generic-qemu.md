# Running system on <nobr>sparcv8leon-generic-qemu</nobr>

These instructions describe how to run a Phoenix-RTOS system image for the `sparcv8leon-generic-qemu` target
architecture.

Note that the build artifacts, including the system image, should be first provided in the `_boot` directory.

If you haven't run the `build.sh` script yet, run it for `sparcv8leon-generic-qemu` target.

See [Building](../building/index.md) chapter.

## Running the system image

Support for the `leon3_generic` machine in QEMU has been greatly improved in QEMU 9.0.0. It is recommended to use QEMU
version 9.0.0 or later to run the Phoenix-RTOS system image for the `sparcv8leon-generic-qemu` target architecture.
To obtain QEMU in this version on Ubuntu 22.04, you must build it from source.

  <details>
  <summary>How to build QEMU on Ubuntu</summary>

- Download QEMU 9.0.2 (or later) source code from the official repository and build for the `sparc-softmmu` target:

  ```shell
  sudo apt update && \  
  sudo apt install -y ninja-build \  
  libglib2.0-dev && \
  git clone https://gitlab.com/qemu-project/qemu.git -b v9.0.2 && \
  cd qemu && \
  git submodule update --init --recursive && \
  ./configure --target-list=sparc-softmmu && \
  make && \
  sudo make install
  ```

- Check if QEMU is properly installed:

  ```shell
  qemu-system-sparc --version
  ```

  ```shell
  QEMU emulator version 9.0.2 (v9.0.2)
  Copyright (c) 2003-2024 Fabrice Bellard and the QEMU Project developers
  ```

  </details>

To run the image under QEMU, use the following script provided in the `phoenix-rtos-project` repository:

  ```shell
  ./scripts/sparcv8leon-generic-qemu.sh
  ```

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal.

```
~/phoenix-rtos-project$ ./scripts/sparcv8leon-generic-qemu.sh
Phoenix-RTOS loader v. 1.21 rev: ffe21a4
hal: Generic LEON3
cmd: Executing pre-init script
console: Setting console to 0.0
alias: Setting relative base address to 0x0000f000
Waiting for input,     0 [ms]
Phoenix-RTOS microkernel v. 3.2 rev: 50deba9
hal: SPARCv8 LEON3-Generic
hal: No FPU, 8 windows
hal: Using IRQMP interrupt controller
hal: Using General Purpose Timer
vm: Initializing page allocator (924+0)/114688KB, page_t=16
vm: [262144x][44K][71A][112H]PPPP[28441.]
vm: Initializing memory mapper: (9430*64) 603520
vm: Initializing kernel memory allocator: (64*48) 3072
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [100]
main: Starting syspage programs: 'dummyfs', 'grlib-uart', 'psh'
dummyfs: initialized
(psh)%
```

To get the available command list use command:

```shell
help
```

```
(psh)% help
Available commands:
    bind       - binds device to directory
    cat        - concatenate file(s) to standard output
    cd         - changes the working directory
    chmod      - changes file mode, chmod [-R] <mode> <file>...
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
    hd         - dumps file contents in hexadecimal and ascii representation
    help       - prints this help message
    history    - prints commands history
    hm         - health monitor, spawns apps and keeps them alive
    ifconfig   - configures network interfaces
    kill       - sends a signal to a process
    ln         - make links between files
```

To get the list of working processes use command:

```shell
ps
```

```
(psh)% ps
      PID     PPID  PR  STATE  %CPU     WAIT        TIME    VMEM THR CMD
        0        0   4  ready  99.2      50ms    00:00:23    1.3M   2 [idle]
        1        0   4  sleep   0.0       2ms    00:00:00       0   1 init
        2        1   4  sleep   0.1       2ms    00:00:00    364K   1 dummyfs
        3        1   2  sleep   0.1       2ms    00:00:00    124K   4 grlib-uart
        4        1   4  ready   0.2       2ms    00:00:00    220K   1 psh
(psh)%
```

If you want to quit, you should click on the terminal window, press ctrl + a, release it, and next press the x key.  
