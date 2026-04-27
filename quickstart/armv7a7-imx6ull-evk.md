# Running system on <nobr>armv7a7-imx6ull-evk</nobr>

This version is designed for NXP i.MX 6ULL processors with ARM Cortex-A7 core. To launch this version the final disk
image and loader image should be provided. Images are created as the final artifacts of the `phoenix-rtos-project`
building and are located in the `_boot` directory. The disk image consists of bootloader (plo), kernel, UART driver
(tty), dummyfs filesystem server (RAM disk), and psh (shell). Necessary tools to carry out the uploading process are
located in the `_boot` directory as well.
See [Building](../building/index.md) chapter.

## Development board

The easiest way to start programming hardware targets using Phoenix-RTOS is to get some evaluation boards with a
specified target processor or microcontroller. In this case
<!-- markdownlint-disable -->
[i. MX 6ULL - EVK](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/evaluation-kit-for-the-i-mx-6ull-and-6ulz-applications-processor:MCIMX6ULL-EVK)
<!-- markdownlint-restore -->
Is the example of a board with the `imx6ull` processor, where the default configuration of peripherals allows running
Phoenix-RTOS.

## Connecting the board

- To provide a power supply for the board, you should connect AC Adapter to the DC socket on the board. For now, leave
the `SW2001` switch in the `1` position.

- To communicate with the board you will need to connect the USB cable to the `DEBUG USB` port (`J1901`). The onboard
UART-USB converter is used here.

- You should also connect another micro USB cable to the `USB OTG` port (`J1102`). As a result two available USB ports
in `i. MX 6ULL - EVK` will be connected to your host-pc.

- Now you can power up the board by changing the `SW2001` position to `2`. The `D2003` LED should turn green.

- Now you should verify what USB device on your host-pc is connected with the `DEBUG USB` (console). To check that run:

  ```shell
  ls -l /dev/serial/by-id
  ```

  ```
  ~$ ls -l /dev/serial/by-id/
  total 0
  lrwxrwxrwx 1 root root 13 lis  8 13:07 usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0 -> ../../ttyUSB0
  ~$
  ```

  If your output is like in the screenshot above, the console (`DEBUG USB` in the evaluation board) is on the `USB0`
  port.

- When the board is connected to your host-pc, open serial port in terminal using picocom and type the console port
(in this case USB0)

  ```shell
  picocom -b 115200 --imap lfcrlf /dev/ttyUSB0
  ```

  <details>
  <summary>How to get picocom (Ubuntu 20.04)</summary>

  ```shell
  sudo apt-get update && \
  sudo apt-get install picocom
  ```

  </details>

You can leave the terminal with the serial port open, and follow the next steps.

## Flashing the Phoenix-RTOS system image

The process comes down to a few steps, described below.

### Uploading Phoenix-RTOS loader (plo) to the RAM memory

To flash the disk image to the board, the bootloader (plo) image located in the `_boot` directory should be uploaded to
the RAM using `psu` (Phoenix Serial Uploader) via `SDP` (Serial Download Protocol).

- Make sure, that the SW602 switch is in the following configuration (serial downloader mode):

  | D1/MODE1 | D2/MODE0 |
  |----------|----------|
  | OFF      | ON       |

  If it was in a different position you have to restart the board after the change and connect to the serial port a
  second time.

- Change directory to `_boot` and run `psu` as follows:

  ```shell
  cd _boot/armv7a7-imx6ull-evk
  ```

  ```shell
  sudo ./psu plo-ram.sdp
  ```

```
~/phoenix-rtos-project/_boot/armv7a7-imx6ull-evk$ sudo ./psu plo-ram.sdp
WAIT 0x15a2 0x80
ERROR_STATUS
WRITE_FILE F "plo-ram.img" 0x00907000
 - Sending to the device: plo-ram.img
 - Sent (54920/54920) 100%
 - File has been written correctly.
JUMP_ADDRESS 0x00908000
 - To the address: 0x908000
~/phoenix-rtos-project/_boot/armv7a7-imx6ull-evk$
```

- The plo user interface should appear in the console.

```
Phoenix-RTOS loader v. 1.21 rev: a8408b1
hal: Cortex-A7 i.MX 6ULL
dev/uart: Initializing uart(0.0)
dev/uart: Initializing uart(0.1)
dev/uart: Initializing uart(0.2)
dev/uart: Initializing uart(0.3)
dev/uart: Initializing uart(0.4)
dev/uart: Initializing uart(0.5)
dev/uart: Initializing uart(0.6)
dev/uart: Initializing uart(0.7)
dev/usb: Initializing usb-cdc(1.2)
dev/flash/nor: Configured Micron MT25QL256 32MB nor flash(2.0)
cmd: Executing pre-init script
console: Setting console to 0.0

(plo)%
```

- To get the available bootloader command list please type `help`.

```
(plo)% help
  alias       - sets alias to file, usage: alias [-b <base> | [-r] <name> <offset> <size>]
  app         - loads app, usage: app [<dev> [-x | -xn] <name> <imap1;imap2...> <dmap1;dmap2...>]
  call        - calls user's script, usage: call <dev> <script name> <magic>
  console     - sets console to device, usage: console <major.minor>
  copy        - copies data between devices, usage:
                copy <src dev> <file/offs size> <dst dev> <file/offs size>
  dump        - dumps memory, usage: dump [-F|-r <phfs>] <addr> [<size>]
  echo        - command switch on/off information logs, usage: echo [on/off]
  erase       - erase sectors or all data from storage device using phfs interface, Usage: erase <d
  ev> [<offset> <size>]
  go!         - starts Phoenix-RTOS loaded into memory
  help        - prints this message
  jffs2       - writes jffs2 cleanmarkers, usage: jffs2 -d <major>.<minor> -c <start block>:<number
   of blocks>:<block size>:<clean marker size> [-e]
  kernel      - loads Phoenix-RTOS, usage: kernel [<dev> [name]]
  map         - defines multimap, usage: map [<name> <start> <end> <attributes>]
  mem         - Reads or writes values from/to a range of memory addresses
  phfs        - registers device in phfs, usage: phfs [<alias> <major.minor> [protocol]]
  script      - shows script, usage: script [<dev> <name> <magic>]
  test-dev    - performs simple dev read/write test, usage:test-dev [-e erase before] [-E erase aft
  er] -d <dev> [-s <addr> start(default 0)] -l length
  test-ddr    - perform test DDR, usage: test-ddr
  wait        - waits in milliseconds or in infinite loop, usage: wait [ms]
(plo)%
```

### Copying flash image using PHFS (phoenixd)

To flash the disk image, first, you need to verify on which port plo USB device has appeared. You can check that using
`ls` as follows:

```shell
ls -l /dev/serial/by-id
```

```
~$ ls -l /dev/serial/by-id
total 0
lrwxrwxrwx 1 root root 13 bře 19 16:46 usb-Phoenix_Systems_plo_CDC_ACM-if00 -> ../../ttyACM0
lrwxrwxrwx 1 root root 13 bře 19 16:06 usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0 -> ../../ttyUSB0
~$
```

To share disk image to the bootloader, `phoenixd` has to be launched with the following arguments
(choose suitable ttyACMx device, in this case, ttyACM0):

```shell
sudo ./phoenixd -p /dev/ttyACM0 -b 115200 -s .
```

```
~/phoenix-rtos-project/_boot/armv7a7-imx6ull-evk$ sudo ./phoenixd -p /dev/ttyACM0 -b 115200 -s .
-\- Phoenix server, ver. 1.5
(c) 2012 Phoenix Systems
(c) 2000, 2005 Pawel Pisarczyk

[126763] dispatch: Starting message dispatcher on [/dev/ttyACM0] (speed=115200)
```

To start copying a file, write the following command in the console with plo interface:

```shell
copy usb0 phoenix.disk nor0 0x0 0x0
```

The `nor0` is the flash memory.

### Booting Phoenix-RTOS from Flash

- Turn off the board.

- Change configuration of SW602 to the following configuration (internal boot mode):

  | D1/MODE1 | D2/MODE0 |
  | -------- | -------- |
  | ON       | OFF      |

- Change configuration of SW601 to the following configuration (boot from QSPI):
  | D1  | D2  | D3  | D4  |
  | --- | --- | --- | --- |
  | OFF | OFF | OFF | OFF |

- Turn on the board.

If everything has gone correctly, Phoenix-RTOS with the default configuration and the `psh` shell command prompt will
appear in the terminal after 2 seconds. If there is a need to enter the bootloader, the waiting for input should be
interrupted by pressing any key. Then you can exit plo by passing `go!` command.

```
(plo)% Phoenix-RTOS loader v. 1.21 rev: a8408b1
hal: Cortex-A7 i.MX 6ULL
dev/uart: Initializing uart(0.0)
dev/uart: Initializing uart(0.1)
dev/uart: Initializing uart(0.2)
dev/uart: Initializing uart(0.3)
dev/uart: Initializing uart(0.4)
dev/uart: Initializing uart(0.5)
dev/uart: Initializing uart(0.6)
dev/uart: Initializing uart(0.7)
dev/usb: Initializing usb-cdc(1.2)
dev/flash/nor: Configured Micron MT25QL256 32MB nor flash(2.0)
cmd: Executing pre-init script
console: Setting console to 0.0
Waiting for input,    0 [ms]
Phoenix-RTOS microkernel v. 3.0 rev: 0890d1b
hal: NXP i.MX 6ULL ARMv7 Cortex-A7 r0p5
hal: ThumbEE, Jazelle, Thumb, ARM, Generic Timer, Virtualization, Security
hal: Using GIC interrupt controller
hal: Using EPIT and GPT timers
vm: Initializing page allocator (1092+0)/131072KB, page_t=16
vm: [524288x][24K][6P]H[24K][127H]PP[832.]P...PPPS[31248.][83A]P[412.]
vm: Initializing memory mapper: (8091*64) 517824
vm: Initializing kernel memory allocator: (64*48) 3072
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [100]
main: Starting syspage programs: 'dummyfs;-N;devfs;-D', 'imx6ull-uart', 'imx6ull-flashnor;-q;1;-r;0;1048576;32505856;jffs2', 'psh;-i;/etc/rc.psh'
dummyfs: initialized
dev/flash/nor: Probing flash id   0x19ba20
imx6ull-flashnor: Configured Micron MT25QL256 32MB nor flash
version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.

imx6ull-flashnor: initialized
dummyfs: initialized
lwip: enet@02188000 Resetting device...
lwip: enet@02188000 Reset done.
lwip: enet@02188000 MDIO bus 0
lwip: enet@02188000 initialized, MAC=00:04:9f:05:b9:e9
lwip: enet@02188000 mdio: speed 13 (2357 kHz), hold 0 (15 ns), with preamble
lwip: ephy0.2 link is DOWN 10Mbps/Full (ctl 0500, status 7849, adv 8061, lpa 0000, pctl 000f,8180)
lwip: enet@020b4000 Resetting device...
lwip: enet@020b4000 Reset done.
lwip: enet@020b4000 initialized, MAC=00:04:9f:05:b9:ea
lwip: ephy0.1 link is DOWN 10Mbps/Half (ctl 0100, status 7849, adv 8061, lpa 0000, pctl 0003,8180)
(psh)%
```

## Using Phoenix-RTOS

To get the available command list please type:

```shell
help
```

```
(psh)% help
Available commands:
  bind      - binds device to directory
  cat       - concatenate file(s) to standard output
  edit      - text editor
  exec      - replace shell with the given command
  exit      - exits shell
  help      - prints this help message
  history   - prints commands history
  kill      - terminates process
  ls        - lists files in the namespace
  mem       - prints memory map
  mkdir     - creates directory
  mount     - mounts a filesystem
  nc        - TCP and UDP connections and listens
  nslookup  - queries domain name servers
  perf      - track kernel performance events
  ping      - ICMP ECHO requests
  ps        - prints processes and threads
  reboot    - restarts the machine
  sync      - synchronizes device
  sysexec   - launch program from syspage using given map
  top       - top utility
  touch     - changes file timestamp
  uptime    - prints how long the system has been running
(psh)%
```

If you want to get the list of working processes please type:

```shell
ps
```

```
(psh)% ps
  PID  PPID PR STATE  %CPU  WAIT      TIME  VMEM THR CMD
    0     0  7 ready  99.9 100.s     14:42  1.3M   1 [idle]
    1     0  4 sleep   0.0 233us      0:00     0   1 init
    2     1  4 sleep   0.0  12us      0:00  1.4M   1 dummyfs
    3     1  3 sleep   0.0 288us      0:00  100K   3 imx6ull-uart
    4     1  4 ready   0.0 154us      0:00  140K   1 psh
(psh)%
```

To get the table of processes please type:

```shell
top
```

```
Tasks:    5 total, running: 3, sleeping: 2
  PID  PPID PR STATE  %CPU  WAIT      TIME  VMEM CMD
    0     0  7 ready  99.8 100.s   9:25.81  1.3M [idle]
    2     1  4 sleep   0.0  12us   0:00.00  1.4M dummyfs
    1     0  4 sleep   0.0 233us   0:00.06     0 init
    4     1  4 ready   0.0 154us   0:00.03  148K psh
    3     1  3 ready   0.0 466us   0:00.03  100K imx6ull-uart
    4     1  4 ready   0.0 154us   0:00.01  148K psh
    3     1  3 ready   0.0 428us   0:00.01  100K imx6ull-uart
```
