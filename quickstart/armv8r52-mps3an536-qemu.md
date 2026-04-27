# Running system on <nobr>armv8r52-mps3an536-qemu</nobr>

These instructions describe how to run a Phoenix-RTOS system image for the `armv8r52-mps3an536-qemu` target
architecture.

Note that the build artifacts, including the system image, should be first provided in the `_boot` directory.

If you haven't run the `build.sh` script yet, run it for `armv8r52-mps3an536-qemu` target.

See [Building](../building/index.md) chapter.

## Running the system image

Support for the `mps3-an536` machine in QEMU has been added in QEMU 9.0.0. To run the Phoenix-RTOS system image for the
`armv8r52-mps3an536-qemu` target architecture, you must have QEMU version 9.0.0 or later installed. On Ubuntu 22.04, you
must build QEMU from source.

  <details>
  <summary>How to build QEMU (Ubuntu 22.04)</summary>

- Download QEMU 9.0.2 (or later) source code from the official repository and build for the `arm-softmmu` target:

  ```shell
  git clone https://gitlab.com/qemu-project/qemu.git -b v9.0.2 && \
  cd qemu && \
  git submodule update --init --recursive && \
  ./configure --target-list=arm-softmmu && \
  make && \
  sudo make install
  ```

- Check if QEMU is properly installed:

  ```shell
  qemu-system-arm --version
  ```

  ```shell
  ~$ qemu-system-arm --version
  QEMU emulator version 9.0.2 (v9.0.2)
  Copyright (c) 2003-2024 Fabrice Bellard and the QEMU Project developers
  ~$
  ```

  </details>

To run the image under QEMU, use the following script provided in the `phoenix-rtos-project` repository:

  ```shell
  ./scripts/armv8r52-mps3an536-qemu.sh
  ```

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal.

```
~/phoenix-rtos-project$ ./scripts/armv8r52-mps3an536-qemu.sh
VNC server running on 127.0.0.1:5900
Phoenix-RTOS loader v. 1.21 rev: 06a21e6
hal: Cortex-R52 MPS3-AN536
cmd: Executing pre-init script
console: Setting console to 0.2
Waiting for input,     0 [ms]
Phoenix-RTOS microkernel v. 3.2 rev: ec52ca2
hal: MPS3 AN536 ARMv8 Cortex-R52 r1p3 x1
hal: Jazelle, Thumb, ARM, Generic Timer, Virtualization
hal: Using GICv3 interrupt controller
hal: Using ARM Dual Timer
vm: Initializing page allocator 18/431 KB, page_t=12
vm: Initializing memory mapper: (199*80) 15920
vm: Initializing kernel memory allocator: (16*48) 768
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [100]
main: Starting syspage programs: 'dummyfs', 'cmsdk-apbuart', 'psh'
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
        0        0   4  ready  93.0      69ms    00:00:02    190K   2 [idle]
        1        0   4  sleep   0.3       3ms    00:00:00       0   1 init
        2        1   4  sleep   1.8       2ms    00:00:00   42.5K   1 dummyfs
        3        1   2  sleep   3.3       2ms    00:00:00     43K   4 cmsdk-apbuart
        4        1   4  ready   1.3       2ms    00:00:00   31.5K   1 psh
(psh)%
```
