# Running system on <nobr>armv7m4-stm32l4x6-nucleo</nobr>

This version is designated for STM32L4x6 processors with Cortex-M4 core. To launch this version the final flash image
should be provided. The image is created as the final artifact of the `phoenix-rtos-project` building and is located in
the `_boot` directory. The image consists of a kernel, TTY UART driver, RAM disk filesystem, and psh (shell).

See [Building](../building/index.md) chapter.

## Development board

The easiest way to start programming hardware targets using Phoenix-RTOS is to get some of the evaluation boards with a
specified target processor or microcontroller.

In this case [NUCLEO-L4A6ZG](https://www.st.com/en/evaluation-tools/nucleo-l4a6zg.html#overview) is the example of a
board with `stm32l4x6` microcontroller.

## Connecting the board

To provide a power supply for the board and make flashing possible, you have to connect a USB to micro USB cable between
your host pc and the development board (`USB PWR` port, also called `CN1`).

To communicate with the board you will need to use a UART-USB converter, like `PL2303 TA`.

- Connect TX, RX, and GND wires to the USART2 (called also USART_B) in the Nucleo board.
  For example, using PL2303 TA:
  - PL2303 TX (green) - Nucleo USART_B_RX
  - PL2303 RX (white) - Nucleo USART_B_TX
  - PL2303 GND (black) - Nucleo GND

  <!-- adjust size and position in pdf -->
  ```{image} ../_static/images/quickstart/nucleo-pinout.png
  :align: center
  :width: 50%
  ```

  Source: The Nucleo board's schematic, available on
  <https://www.st.com/en/evaluation-tools/nucleo-l4a6zg.html#cad-resources>

- Put the converter into your host PC's USB port

  The picture below presents how the board should be connected:

  <!-- use image directive due to poor render in pdf -->
  ```{image} ../_static/images/quickstart/stm32l4x6-connections.png
  :align: center
  :width: 50%
  ```

- Now you should verify, what USB device on your host-pc is connected with the `UART` (console). To check that run:

  - On Ubuntu:

  ```shell
    ls -l /dev/serial/by-id
  ```

  ```
  total 0
  lrwxrwxrwx 1 root root 13 lip 25 14:55 usb-STMicroelectronics_STM32_STLink_066FFF393430533457035332-if02 -> ../../ttyACM0
  ```

- Open serial port in terminal using picocom

  ```shell
  picocom -b 115200 --imap lfcrlf /dev/tty[port]
  ```

  <details>
  <summary>How to get picocom and run it without privileges (Ubuntu 22.04)</summary>

  ```shell
  sudo apt update && \
  sudo apt install -y picocom
  ```

  To use picocom without sudo privileges run this command and then restart:

  ```shell
  sudo usermod -a -G tty <yourname>
  ```

  </details>

You can leave the terminal with the serial port open, and follow the next steps.

## Flashing the Phoenix-RTOS system image

To flash the image to the board you will need `openocd` in version 0.11 or 0.12. You can check it using

```shell
openocd -v
```

  <details>
  <summary>How to get openocd on Ubuntu</summary>

To install from the default repositoriy:

- use `apt`

  ```shell
  sudo apt install -y openocd
  ```

- check if the version is correct

  ```shell
  openocd -v
  ```

If you encounter errors install manually from sources (v0.12.0):

- download, build and install `openocd-0.12.0-1` from sources

  ```shell
  wget -O- https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/openocd/0.12.0-1build2/openocd_0.12.0.orig.tar.bz2 | \
  sudo tar xjvf - -C /usr/local/src && \
  cd /usr/local/src/openocd-0.12.0 && \
  sudo apt install -y pkg-config \
  libusb-1.0-0-dev && \
  ./configure --enable-stlink && \
  make && \
  sudo make install
  ```

- check if the version is correct

  ```shell
  openocd -v
  ```

  ```
  Open On-Chip Debugger 0.11.0-rc2
  Licensed under GNU GPL v2
  For bug reports, read
          http://openocd.org/doc/doxygen/bugs.html
  ```

  </details>

If you have openocd, next you can use the following script:

```shell
sudo phoenix-rtos-build/scripts/program-stm32l4x6.sh _boot/armv7m4-stm32l4x6-nucleo/phoenix.disk
```

or use openocd directly:

```shell
openocd -f interface/stlink.cfg \
-f target/stm32l4x.cfg -c "reset_config srst_only srst_nogate connect_assert_srst" \
-c "program _boot/armv7m4-stm32l4x6-nucleo/phoenix.disk 0x08000000 verify reset exit"
```

```
~/phoenix-rtos-project$ openocd -f interface/stlink.cfg -f target/stm32l4x.cfg -c "reset_config srst_only srst_nogate connect_assert_srst" -c "program _boot/armv7m4-stm32l4x6-nucleo/phoenix.disk 0x08000000 verify reset exit"
Open On-Chip Debugger 0.11.0-rc2
Licensed under GNU GPL v2
For bug reports, read
        http://openocd.org/doc/doxygen/bugs.html
Info : auto-selecting first available session transport "hla_swd". To override use 'transport select
  <transport>'.
Info : The selected transport took over low-level target control. The results might differ compared
to plain JTAG/SWD
srst_only separate srst_nogate srst_open_drain connect_assert_srst

Info : clock speed 500 kHz
Info : STLINK V2J30M19 (API v2) VID:PID 0483:374B
Info : Target voltage: 3.248358
Info : stm32l4x.cpu: hardware has 6 breakpoints, 4 watchpoints
Info : starting gdb server for stm32l4x.cpu on 3333
Info : Listening on port 3333 for gdb connections
Info : Unable to match requested speed 500 kHz, using 480 kHz
Info : Unable to match requested speed 500 kHz, using 480 kHz
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x080003a4 msp: 0x20013a00
** Programming Started **
Info : device idcode = 0x20006461 (STM32L49/L4Axx - Rev B : 0x2000)
Info : flash size = 1024kbytes
Info : flash mode : dual-bank
Info : Padding image section 0 at 0x0803bf9c with 4 bytes (bank write end alignment)
Warn : Adding extra erase range, 0x0803bfa0 .. 0x0803bfff
** Programming Finished **
** Verify Started **
** Verified OK **
** Resetting Target **
Info : Unable to match requested speed 500 kHz, using 480 kHz
Info : Unable to match requested speed 500 kHz, using 480 kHz
shutdown command invoked
~/phoenix-rtos-project$
```

The script can be modified to accommodate other SWD interfaces.

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal with the serial port
opened.

```
Phoenix-RTOS microkernel v. 2.97 rev: 10b7a77
hal: STM32 ARMv7 Cortex-M4 r0 p1
hal: softfp, MPU, Thumb
hal: Using NVIC interrupt controller
vm: Initializing page allocator 11/320 KB, page_t=12
vm: Initializing memory mapper: (149*72) 10728
vm: Initializing kernel memory allocator: (16*48) 768
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [102]
main: Starting syspage programs: 'stm32l4-multi', 'psh'
multidrv: Started
(psh)%
```

- Note: You can also enter plo (Phoenix-RTOS loader) by pressing any button, for example, `enter` within some time after
reset (using `RESET B2`).

To get the available command list please type:

```shell
help
```

```
(psh)% help
Available commands:
  bind      - binds device to directory
  cat       - concatenate file(s) to standard output
  date      - print/set the system date and time
  df        - print filesystem statistics
  dmesg     - read kernel ring buffer
  echo      - display a line of text
  edit      - text editor
  exec      - replace shell with the given command
  exit      - exits shell
  help      - prints this help message
  history   - prints commands history
  hm        - health monitor, spawns apps and keeps them alive
  kill      - terminates process
  ls        - lists files in the namespace
  mem       - prints memory map
  mkdir     - creates directory
  mount     - mounts a filesystem
  nc        - TCP and UDP connections and listens
  nslookup  - queries domain name servers
  perf      - track kernel performance events
  ping      - ICMP ECHO requests
  pm        - process monitor
  ps        - prints processes and threads
  reboot    - restarts the machine
  sync      - synchronizes device
  sysexec   - launch program from syspage using given map
  top       - top utility
  touch     - changes file timestamp
  uptime    - prints how long the system has been running
  wget      - downloads a file using http
(psh)%
```

To get the list of working processes please type:

```shell
ps
```

```
(psh)% ps
  PID   PPID  PR  STATE  %CPU    WAIT       TIME    VMEM THR CMD
    0      0   7  ready  99.5  934.8s   00:04:31    112K   1 [idle]
    1      0   4  sleep   0.0  733us    00:00:00       0   1 init
    2      1   1  sleep   0.1   11ms    00:00:01     21K   9 stm32l4-multi
    3      1   4  ready   0.1  18.8ms   00:00:00   28.5K   1 psh
(psh)%
```
