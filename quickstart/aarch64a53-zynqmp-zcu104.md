# Running system on <nobr>aarch64a53-zynqmp-zcu104</nobr>

These instructions describe how to run a Phoenix-RTOS system image for `aarch64a53-zynqmp-zcu104` target architecture.
The guide assumes that you have already built the system image and build artifacts are in the `_boot` directory.
If you haven't run the `build.sh` script yet, run it for `aarch64a53-zynqmp-zcu104` target.

See [how to build the Phoenix-RTOS system image](../building/index.md).

## Preparing the board

The first step of running Phoenix-RTOS is loading plo (Phoenix loader) into RAM. This can be done in two ways -
from the SD card or the on-board NOR flash. If you are flashing Phoenix-RTOS for the first time, or the image in
NOR flash is corrupt, you can load plo from the SD card. Using plo you can write the system image into NOR flash.
After this is done, you can run plo and then Phoenix-RTOS from NOR flash.

### Loading plo from SD card

1. Ensure the SD card is formatted using MBR scheme and the first partition is using FAT or FAT32 filesystem.

2. Copy the disk image `part_plo.img` from the `_boot/aarch64a53-zynqmp-zcu104` directory
to the FAT partition on the SD card and rename it to `BOOT.BIN` (case-insensitive).

3. Insert the SD card into the board.

4. Set boot mode to SD card. Set switches in the switch block `SW6` as follows:

    ```text
            ┌───────┐
            │  -->  │
    MODE0  =│1 --[] │=
    MODE1  =│2 []-- │=
    MODE2  =│3 []-- │=
    MODE3  =│4 []-- │=
            │       │
            └───────┘
    ```

    MODE pins[3:0]: 1110/0xE

    SW6 switch positions [4:1]: OFF,OFF,OFF,ON

### Loading plo from NOR flash

```{note}
If this is the first time you run Phoenix-RTOS on this board, use the SD card method to run plo first!
```

1. Set boot mode to QSPI32 flash. Set switches in the switch block `SW6` as follows:

    ```text
            ┌───────┐
            │  -->  │
    MODE0  =│1 --[] │=
    MODE1  =│2 []-- │=
    MODE2  =│3 --[] │=
    MODE3  =│4 --[] │=
            │       │
            └───────┘
    ```

    MODE pins[3:0]: 0010/0x2

    SW6 switch positions [4:1]: ON,ON,OFF,ON

### Loading plo - common steps

1. Plug in the dedicated power supply into the board using connector `J52`. For now leave the `SW1` switch
in the `OFF` position to turn off power to the board.

2. The board contains an FTDI FT4232HL chip that adapts JTAG and UART ports of the SoC into USB. Connect a
micro-USB cable from the host PC to connector `J164`.

3. Verify that the UART ports of FT4232HL are visible on host PC.
    - On Ubuntu:

      ```sh
      ls -l /dev/serial/by-id
      ```

      The result should be similar to:

      ```shell
      lrwxrwxrwx 1 root root 13 sty 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if00-port0 -> ../../ttyUSB0
      lrwxrwxrwx 1 root root 13 sty 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if01-port0 -> ../../ttyUSB1
      lrwxrwxrwx 1 root root 13 sty 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if02-port0 -> ../../ttyUSB2
      lrwxrwxrwx 1 root root 13 sty 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if03-port0 -> ../../ttyUSB3
      ```

      `ttyUSB1` is connected to `UART0` which is used for data transfer using `phoenixd`.

      `ttyUSB2` is connected to `UART1` which is used for serial console.

      `ttyUSB3` is connected to the FPGA part of the SoC, and it will not be used in this guide.

      `ttyUSB0` is not connected to UART but the corresponding port on FT4232HL is connected to JTAG. The device may
      disappear after connecting OpenOCD (described at the end of the guide).

4. Power up the board, changing the `SW1` position to `ON`. Two rows of green LEDs should turn on indicating
power rails - see "Power and Status LEDs" section of the ZCU104 Board User Guide (UG1267) for detailed descriptions.
    - If the `DS36` LED is turned on (red), the board is in reset. It should light up for a short time after turning on
    the board or pressing the `POR_B` button.

    - If the `DS35` LED is turned on (red), it indicates an error loading plo. Ensure that the boot mode is
    set correctly, and the boot image is written correctly to the chosen boot medium (SD card or NOR flash).

5. When the board is connected to your host PC, open serial port in terminal using picocom and type the console port
(in this case `ttyUSB2`)

    ```sh
    picocom -b 115200 --imap lfcrlf /dev/[port]
    ```

<details>

<summary>How to get picocom and run it without privileges (Ubuntu 22.04)</summary>

```sh
sudo apt-get update && \
sudo apt-get install picocom
```

To use picocom without sudo privileges run this command and then restart:

```sh
sudo usermod -a -G tty <yourname>
```

</details>
</br>

You can leave the terminal with the serial port open, and follow the next steps.

## Flashing the Phoenix-RTOS system image

At first before any flashing, you need to enter Phoenix-RTOS loader (plo), which should have been already loaded.

If there wasn't an older system image in the NOR flash the following output should appear:

```console
Phoenix-RTOS loader v. 1.21 rev: 66720bf
hal: Cortex-A53 ZynqMP
dev/uart: Initializing uart(0.0)
dev/uart: Initializing uart(0.1)
dev/flash: Configured Micron MT25QU512 64MB nor flash(2.0)
cmd: Executing pre-init script
console: Setting console to 0.0
alias: Setting relative base address to 0x0000000000020000
Magic number for user.plo is wrong.
(plo)%
```

If you don't see it, please press the `POR_B` button (`SW4`) to reset the chip.

Providing that Phoenix-RTOS is present in the flash memory you will probably see the system startup:

```console
Phoenix-RTOS loader v. 1.21 rev: b3bf39c
hal: Cortex-A53 ZynqMP
dev/uart: Initializing uart(0.0)
dev/uart: Initializing uart(0.1)
dev/flash: Configured Micron n25q512 64MB nor flash(2.0)
cmd: Executing pre-init script
console: Setting console to 0.1
alias: Setting relative base address to 0x0000000000020000
Waiting for input,     0 [ms]
Phoenix-RTOS microkernel v. 3.3 rev: 80df916
hal: Xilinx Zynq Ultrascale ARMv8 Cortex-A53 r0p4 x4
hal: EL3, EL2, FP, AdvSIMD, AES, SHA1, SHA256, CRC32
hal: Using GIC interrupt controller
hal: Using Triple Timer Counter
vm: Initializing page allocator (18168+0)/2096128KB, page_t=32
vm: [56K][456H][129A]P[512H]P[512H]P[512H]P[512H]P[512H]P[512H]P[512H]P[54H]
vm: [255P][519490.]
vm: Initializing memory mapper: (171598*112) 19218976
vm: Initializing kernel memory allocator: (32*88) 2816
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [100]
main: Starting syspage programs: 'system.dtb', 'dummyfs;-N;devfs;-D', 'zynq7000-uart', 'psh;-i;/etc/rc.psh', 'zynq7000-flash;-r;/dev/mtd0:8388608:8388608:jffs2'
dummyfs: initialized
version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.

dummyfs: initialized
(psh)%
```

You want to press the `POR_B` button (`SW4`) again and interrupt `Waiting for input` by pressing any key to enter plo:

```console
Type [C-a] [C-h] to see available commands
Terminal ready
Phoenix-RTOS loader v. 1.21 rev: b3bf39c
hal: Cortex-A53 ZynqMP
dev/uart: Initializing uart(0.0)
dev/uart: Initializing uart(0.1)
dev/flash: Configured Micron n25q512 64MB nor flash(2.0)
cmd: Executing pre-init script
console: Setting console to 0.1
alias: Setting relative base address to 0x0000000000020000
Waiting for input,   700 [ms]
(plo)%
```

### Erasing the area intended for file system

It's needed to erase sectors that will be used by `jffs2` file system as we place in the `phoenix.disk`
 only the necessary file system content, not the whole area intended for it.
Without erasure `jffs2` may encounter data from the previous flash operation and errors
 during the system startup may occur.
That's why we have to run erase using plo command specific to `jffs2` file system:

```shell
jffs2 -d 2.0 -e -c 0x80:0x100:0x10000:16
```

Quick description of used arguments:

- `-d 2.0` - regards to the device with the following ID: 2.0, which means it's a flash memory (2) instance nr 0 (0),

- `-e` - erase,

- `-c 0x80:0x100:0x10000:16` - set clean markers
  - start block: `0x80` (`FS_OFFS`/`BLOCK_SIZE`),
  - number of blocks: `0x100` (`FS_SZ`/`BLOCK_SIZE`),
  - block size: `0x10000` (`erase_size`)
  - clean marker size: `16` (value specific for `jffs2` on `NOR` flash)

```console
(plo)% jffs2 -d 2.0 -e -c 0x80:0x100:0x10000:16
jffs2: block 255/256
(plo)%
```

Please wait until erasing is finished.

### Copying flash image using PHFS (phoenixd)

To share disk image to the bootloader, `phoenixd` has to be launched with the following arguments
 (choose suitable `ttyUSBx` device, in this case, `ttyUSB1`):

```sh
cd _boot/aarch64a53-zynqmp-zcu104
./phoenixd -p /dev/tty[port] -b 921600 -s .
```

```console
~/Documents/repos/phoenix-rtos-project/_boot/aarch64a53-zynqmp-zcu104$ ./phoenixd -p /dev/ttyUSB1 -b 921600 -s .
-\- Phoenix server, ver. 1.5
(c) 2012 Phoenix Systems
(c) 2000, 2005 Pawel Pisarczyk

[2149830] dispatch: Starting message dispatcher on [/dev/ttyUSB1] (speed=921600)
```

To start copying the file, write the following command in the console with plo interface:

```shell
copy uart0 flash0.disk flash0 0x0 0x0
```

```console
Phoenix-RTOS loader v. 1.21 rev: b3bf39c
hal: Cortex-A53 ZynqMP
dev/uart: Initializing uart(0.0)
dev/uart: Initializing uart(0.1)
dev/flash: Configured Micron n25q512 64MB nor flash(2.0)
cmd: Executing pre-init script
console: Setting console to 0.1
alias: Setting relative base address to 0x0000000000020000
Waiting for input,  1400 [ms]
(plo)%
(plo)%
(plo)% copy uart0 flash0.disk flash0 0x0 0x0
(plo)%
```

### Copying flash image using RAM disk and OpenOCD

On ZynqMP plo is configured with a RAM disk at address 0x08000000. The flash image can be written to it
using OpenOCD over JTAG which is a lot faster than over UART.

See [Debugging](#debugging) for details on how to launch OpenOCD.

Run the following commands (Note: this assumes the `ftdi_zcu104.cfg` file is in your home directory):

```sh
cd _boot/aarch64a53-zynqmp-zcu104
openocd -f "$(realpath ~/ftdi_zcu104.cfg)" -f "target/xilinx_zynqmp.cfg" \
  -c "init" \
  -c "halt" \
  -c "load_image flash0.disk 0x08000000 bin" \
  -c "resume" \
  -c "exit"
```

```console
~/Documents/repos/phoenix-rtos-project/_boot/aarch64a53-zynqmp-zcu104$ openocd -f "$(realpath ~/ftdi_zcu104.cfg)" -f "target/xilinx_zynqmp.cfg" \
  -c "init" \
  -c "halt" \
  -c "load_image flash0.disk 0x08000000 bin" \
  -c "resume" \
  -c "exit"
Open On-Chip Debugger 0.12.0+dev-01590-g437dde701 (2024-06-07-11:06)
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
adapter speed: 12000 kHz
Info : Hardware thread awareness created
boot_apu
Info : ftdi: if you experience problems at higher adapter clocks, try the command "ftdi tdo_sample_edge falling"
Info : clock speed 12000 kHz
Info : JTAG tap: uscale.tap tap/device found: 0x5ba00477 (mfg: 0x23b (ARM Ltd), part: 0xba00, ver: 0x5)
Info : JTAG tap: uscale.ps tap/device found: 0x14730093 (mfg: 0x049 (Xilinx), part: 0x4730, ver: 0x1)
Info : JTAG tap: uscale.tap tap/device found: 0x5ba00477 (mfg: 0x23b (ARM Ltd), part: 0xba00, ver: 0x5)
Info : JTAG tap: uscale.ps tap/device found: 0x14730093 (mfg: 0x049 (Xilinx), part: 0x4730, ver: 0x1)
Info : uscale.a53.0: hardware has 6 breakpoints, 4 watchpoints
Info : [uscale.a53.0] Examination succeed
Info : [uscale.axi] Examination succeed
Info : starting gdb server for uscale.a53.0 on 3333
Info : Listening on port 3333 for gdb connections
Info : gdb port disabled
Info : uscale.a53.0 cluster 0 core 0 multi core
uscale.a53.0 halted in AArch64 state due to debug-request, current mode: EL3H
cpsr: 0x8000020d pc: 0xffffc1bb8
MMU: enabled, D-Cache: enabled, I-Cache: enabled
65448436 bytes written at address 0x08000000
downloaded 65448436 bytes in 126.627167s (504.745 KiB/s)
~/Documents/repos/phoenix-rtos-project/_boot/aarch64a53-zynqmp-zcu104$
```

Once the flash image is in RAM disk you can copy it to flash0 in PLO:

```shell
copy ramdisk 0x0 0x4000000 flash0 0x0 0x4000000
```

### Booting Phoenix-RTOS from NOR flash memory

Now, the image is located in the NOR Quad SPI Flash memory.
To run it you should follow the steps below:

1. Power off the board using `SW1`

2. Switch boot mode to QSPI32 as described in section [Loading plo from NOR flash](#loading-plo-from-nor-flash)

3. Power on the board using `SW1`

4. Connect to the serial console port (in this case `ttyUSB2`).

    ```shell
    picocom -b 115200 --imap lfcrlf /dev/tty[port]
    ```

5. Restart the chip using the `POR_B` button to print initialization logs:

    ```console
    Phoenix-RTOS loader v. 1.21 rev: 66720bf
    hal: Cortex-A53 ZynqMP
    dev/uart: Initializing uart(0.0)
    dev/uart: Initializing uart(0.1)
    dev/flash: Configured Micron MT25QU512 64MB nor flash(2.0)
    cmd: Executing pre-init script
    console: Setting console to 0.0
    alias: Setting relative base address to 0x0000000000020000
    Waiting for input,     0 [ms]
    Phoenix-RTOS microkernel v. 3.3 rev: 60a5a76
    hal: Xilinx Zynq Ultrascale+ ARMv8 Cortex-A53 r0p4 x4
    hal: EL3, EL2, FP, AdvSIMD, AES, SHA1, SHA256, CRC32
    hal: Using GIC interrupt controller
    hal: Using Triple Timer Counter
    vm: Initializing page allocator (18172+0)/2096128KB, page_t=32
    vm: [57K][455H][129A]P[512H]P[512H]P[512H]P[512H]P[512H]P[512H]P[512H]P[55H]
    vm: [255P][519489.]
    vm: Initializing memory mapper: (171598*112) 19218976
    vm: Initializing kernel memory allocator: (32*88) 2816
    vm: Initializing memory objects
    proc: Initializing thread scheduler, priorities=8
    syscalls: Initializing syscall table [100]
    main: Starting syspage programs: 'system.dtb', 'dummyfs;-N;devfs;-D', 'zynq7000-uart', 'psh;-i;/etc/rc.psh', 'zynq7000-flash;-r;/dev/mtd0:2097152:8388608:jffs2'
    dummyfs: initialized
    version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.

    dummyfs: initialized
    (psh)%
    ```

## Using Phoenix-RTOS

To get the available command list please type:

```shell
help
```

```console
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
  ls         - lists files in the namespace
  mem        - prints memory map
  mkdir      - creates directory
  mount      - mounts a filesystem
  nc         - TCP and UDP connections and listens
  nslookup   - queries domain name servers
  ntpclient  - set the system's date from a remote host
  perf       - track kernel performance events
```

If you want to get the list of working processes please type:

```shell
ps
```

```console
(psh)% ps
  PID   PPID  PR  STATE  %CPU    WAIT       TIME   VMEM  THR  CMD
    0      0   4  ready  395.2   1.5ms   00:08:47  34.9M    5  [idle]
    1      0   4  sleep    0.0  413us    00:00:00      0    1  init
    3      1   4  ready    0.2  246us    00:00:00   148K    4  zynq7000-uart
    5      1   4  sleep    0.0  223us    00:00:00   124K    1  dummyfs
    7      1   1  sleep    4.1  690us    00:00:06   460K    7  zynq7000-flash
   10      1   4  sleep    0.0   60us    00:00:00   116K    1  /sbin/dummyfs
   11      1   4  sleep    0.0  182us    00:00:00   152K    5  /bin/posixsrv
   12      1   4  ready    0.0  119us    00:00:00   228K    1  /bin/psh
(psh)%
```

To get the table of processes please type:

```shell
top
```

```console
Tasks:     8 total, running: 3, sleeping: 5
  PID   PPID  PR  STATE  %CPU    WAIT       TIME   VMEM  CMD
    0      0   4  ready  396.2   1.7ms   13:11.99  34.9M  [idle]
    3      1   4  ready    2.4  472us     0:00.94   148K  zynq7000-uart
    7      1   1  sleep    0.8  690us     0:06.39   468K  zynq7000-flash
   12      1   4  ready    0.2  224us     0:00.08   236K  /bin/psh
   11      1   4  sleep    0.0  182us     0:00.00   152K  /bin/posixsrv
    1      0   4  sleep    0.0  413us     0:00.00     0   init
    5      1   4  sleep    0.0  223us     0:00.00   124K  dummyfs
   10      1   4  sleep    0.0   60us     0:00.00   116K  /sbin/dummyfs
```

## Debugging

The FT4232HL chip can be used to communicate with the SoC over JTAG. Below are instructions how to connect OpenOCD
to the board:

First create a file named `ftdi_zcu104.cfg` with the following contents:

```tcl
adapter driver ftdi
ftdi vid_pid 0x0403 0x6011
ftdi channel 0
ftdi layout_init 0x00c8 0x000b
ftdi layout_signal POR_RST -data 0x0040 -oe 0x0040
ftdi layout_signal nSRST -data 0x0080 -oe 0x0080
transport select jtag
adapter speed 8000
```

Then run OpenOCD with the following command:

```sh
openocd -f "ftdi_zcu104.cfg" -f "target/xilinx_zynqmp.cfg" -c "reset_config srst_only"
```

You may get an error `LIBUSB_ERROR_ACCESS`. If this happens, try running `openocd` with `sudo` - if this fixes
the problem, you need to configure [udev rules](https://github.com/arduino/OpenOCD/blob/master/contrib/60-openocd.rules)
for `openocd` and add your user account to group `plugdev`.

If the connection was successful, this result should appear:

```console
Open On-Chip Debugger 0.12.0+dev-01590-g437dde701 (2024-06-07-11:06)
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
jtag
adapter speed: 8000 kHz
Info : Hardware thread awareness created
boot_apu
srst_only separate srst_gates_jtag srst_open_drain connect_deassert_srst
Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
Info : clock speed 8000 kHz
Info : JTAG tap: uscale.tap tap/device found: 0x5ba00477 (mfg: 0x23b (ARM Ltd), part: 0xba00, ver: 0x5)
Info : JTAG tap: uscale.ps tap/device found: 0x14730093 (mfg: 0x049 (Xilinx), part: 0x4730, ver: 0x1)
Info : JTAG tap: uscale.tap tap/device found: 0x5ba00477 (mfg: 0x23b (ARM Ltd), part: 0xba00, ver: 0x5)
Info : JTAG tap: uscale.ps tap/device found: 0x14730093 (mfg: 0x049 (Xilinx), part: 0x4730, ver: 0x1)
Info : uscale.a53.0: hardware has 6 breakpoints, 4 watchpoints
Info : [uscale.a53.0] Examination succeed
Info : [uscale.axi] Examination succeed
Info : starting gdb server for uscale.a53.0 on 3333
Info : Listening on port 3333 for gdb connections
Info : gdb port disabled
```

Now GDB can be connected to port 3333 on local machine.

For debugging the kernel or userspace you will need to examine all cores before starting GDB.
To do this you need to run OpenOCD with command:

```sh
openocd -f "ftdi_zcu104.cfg" -f "target/xilinx_zynqmp.cfg" -c "reset_config srst_only" -c "init" -c "core_up 1 2 3"
```
