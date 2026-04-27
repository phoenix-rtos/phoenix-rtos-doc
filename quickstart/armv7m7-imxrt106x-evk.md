# Running system on <nobr>armv7m7-imxrt106x-evk</nobr>

This version is designed for NXP i.MX RT106x processors with ARM Cortex-M7 core. To launch this version the final disk
image and loader image should be provided. The images are created as the final artifacts of the `phoenix-rtos-project`
building and are located in the `_boot` directory. The disk image consists of the bootloader (plo), kernel, UART driver
(tty), dummyfs filesystem server (RAM disk), and psh (shell). Necessary tools to carry out the flashing process are
located in the `_boot` directory as well.

See [Building](../building/index.md) chapter.

## Development board

The easiest way to start programming hardware targets using Phoenix-RTOS is to get some evaluation boards with a
specified target processor or microcontroller.

<!-- markdownlint-disable -->
In this case [i. MX RT1064 - EVK](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/mimxrt1064-evk-i-mx-rt1064-evaluation-kit:MIMXRT1064-EVK)
<!-- markdownlint-restore -->

Is the example of a board with the `imxrt106x` processor, where the default configuration of peripherals allows running
Phoenix-RTOS.

## Connecting the board

- Firstly make sure, that the `J1` jumper is in a `3-4` position so that the power will be supplied from the `USB OTG`
port. This is the simplest way, but the good practice is using a USB hub. You can provide power using an AC adapter and
DC connector too (1-2 jumper position).

- To provide a power supply for the board and make flashing possible, connect a USB to micro USB cable
between your host pc and `USB OTG` (`J9`) of the development board. Do it first.

- To communicate with the board connect another USB cable, but to `DEBUG USB` port (`J14`). The onboard
UART-USB converter is used here.

  Board connections:

  ![Image](../_static/images/quickstart/imxrt106x-connections.jpg)

- Verify what USB device on your host-pc is connected with the `DEBUG USB` (console). To check that run:

  - On Ubuntu:

  ```shell
  ls -l /dev/serial/by-id
  ```

  ```
  ~$ ls -l /dev/serial/by-id/
  total 0
  lrwxrwxrwx 1 root root 13 lis 16 15:26 usb-ARM_DAPLink_CMSIS-DAP_0232000007b01b88000000000000000000000097969905-if01 -> ../../ttyACM0
  ~$
  ```

  If the output matches, the console (`DEBUG USB` in the evaluation board) is on the `ACM0`
  port.

- When the board is connected to your host-pc, open serial port in terminal using picocom and type the console port
(in this case ACM0)

  ```shell
  picocom -b 115200 --imap lfcrlf /dev/tty[port]
  ```

  <details>
  <summary>How to get picocom and run it without privileges (Ubuntu 22.04)</summary>

  ```shell
  sudo apt-get update && \
  sudo apt-get install picocom
  ```

  To use picocom without sudo privileges run this command and then restart:

  ```shell
  sudo usermod -a -G tty <yourname>
  ```

  </details>
  </br>

You can leave the terminal with the serial port open, and follow the next steps.

## Flashing the Phoenix-RTOS system image

The process comes down to a few steps, described below.

### Uploading Phoenix-RTOS loader (PLO) to the RAM

In order to flash the disk image to the board, the bootloader (plo) image located in the `_boot` directory should be
uploaded to the RAM using `psu` (Phoenix Serial Uploader) via SDP (Serial Download Protocol).

NOTE: i. MX RT1064 should be set in Serial Download mode. Set the appropriate configuration of SW7 switch on
i.MX RT1064 - EVK, which is `0001` as it is shown below. If the configuration was different restart
the board after the change and open the serial port using picocom once again.

  ![Image](../_static/images/quickstart/imxrt106x-serial-download.jpg)

Change directory to `_boot/armv7m7-imxrt106x-evk` and run `psu` as follows:

```shell
cd _boot/armv7m7-imxrt106x-evk
```

```shell
sudo ./psu plo-ram.sdp
```

The plo user interface should appear in the console.

```
Phoenix-RTOS loader v. 1.21 rev: 53e52e2
hal: Cortex-M i.MX RT106x
uart: Initializing uart(0.0)
uartsb/usb-cdc: Initializing uartsb/usb-cdc(1.2)
flash: Initializing flash(2.0)
flash: Initializing flash(2.1)
pre-init script
console 0.0
(plo)%
```

Type `help`.

```
(plo)% help
available commands:
  alias     - defines or displays aliases
  app       - loads app to memory and registers in syspage
  call      - calls user script
  console   - sets console to device
  copy      - copies data between devices
  dump      - dumps memory
  echo      - displays text
  go!       - starts Phoenix-RTOS loaded into memory
  help      - prints this message
  kernel    - loads phoenix-rtos-kernel
  map       - defines a memory map entry in the syspage
  mpu       - displays or modifies the MPU table from syspage
  phfs      - registers phfs server
  script    - roles script from devices
  syspage   - shows syspage contents
  wait      - waits for data on device or for a number of milliseconds
(plo)%
```

### Copying flash image using PHFS (phoenixd)

To flash the disk image, first, verify on which port plo USB device has been appeared. You can check that
using `ls` as follows:

- On Ubuntu:

```shell
ls -l /dev/serial/by-id
```

```
~$ ls -l /dev/serial/by-id/
total 0
lrwxrwxrwx 1 root root 13 lis 16 15:26 usb-ARM_DAPLink_CMSIS-DAP_0232000007b01b88000000000000000000000097969905-if01 -> ../../ttyACM0
lrwxrwxrwx 1 root root 13 lis 16 15:27 usb-Phoenix_Systems_plo_CDC_ACM-if00 -> ../../ttyACM1
~$
```

Launch `phoenixd` to share the disk image with the bootloader
(choose suitable ttyACMx device, in this case, ttyACM1):

```shell
sudo ./phoenixd -p /dev/tty[port] -b 115200 -s .
```

```
~$ sudo ./phoenixd -p /dev/ttyACM1 -b 115200 -s .
[roles/phoenixd] Phoenix server ver. 1.5
[roles/phoenixd] Starting roles server [/dev/ttyACM1] - speed: 115200
[roles/phoenixd] Roles daemon is waiting...
```

To start copying a file, write the following command in the console with plo interface:

```shell
copy usb0 phoenix.disk flash1 0x0 0x0
```

The `flash1` is the internal flash memory. The alternative option is to copy the system image to external
flash memory - `flash0`.

### Booting Phoenix-RTOS from internal Flash

To launch Phoenix-RTOS from flash memory, change SW7 switch to Internal Flash mode (`0010` configuration as presented
in the photo below) and restart the board (you can do it by pushing the `SW3` button).

  ![Image](../_static/images/quickstart/imxrt106x-internal-flash.jpg)

If everything has gone correctly, Phoenix-RTOS with the default configuration and the `psh` shell command prompt will
appear in the terminal after 2 seconds. If there is a need to enter the bootloader, the waiting for input should be
interrupted by pressing any key. Then you can exit plo by passing `go!` command.

```
Phoenix-RTOS microkernel v. 2.97 rev: 10b7a77
hal: NXP i.MX RT10xx ARMv7 Cortex-M7
dummyfs: initialized
(psh)%
```

## Using Phoenix-RTOS

Once booted, the `psh` shell prompt appears. See [Shell basics](psh-basics.md) for an introduction to
the available shell commands, process inspection, and running programs.
