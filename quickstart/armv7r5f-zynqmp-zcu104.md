# Running system on <nobr>armv7r5f-zynqmp-zcu104</nobr>

These instructions describe how to run a Phoenix-RTOS system image for `armv7r5f-zynqmp-zcu104` target architecture.
The guide assumes that you have already built the system image and build artifacts are in the `_boot` directory.
If you haven't run the `build.sh` script yet, run it for `armv7r5f-zynqmp-zcu104` target.

See [how to build the Phoenix-RTOS system image](../building/index.md).

## Preparing the board

The first step of running Phoenix-RTOS is loading plo (Phoenix loader) into RAM. This can be done in two ways -
from the SD card or the on-board NOR flash. If you are flashing Phoenix-RTOS for the first time, or the image in
NOR flash is corrupt, you can load plo from the SD card. Using plo you can write the system image into NOR flash.
After this is done, you can run plo and then Phoenix-RTOS from NOR flash.

The ZCU104 board is presented in figure below. `SW6` switch (boot mode) and `SW_RST` button
(software reset) are highlighted, as well as power switch, SD card slot and JTAG USB header.
As presented in the attached the `SW6` is configured for SD CARD boot mode.

![Image](../_static/images/quickstart/zynqmp-rpu-ram_start-2.png)

### Loading plo from SD card

1. Ensure the SD card is formatted using MBR scheme and the first partition is using FAT or FAT32 filesystem.

2. Copy the disk image `part_plo.img` from the `_boot/armv7r5f-zynqmp-zcu104` directory
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
      lrwxrwxrwx 1 root root 13 Jan 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if00-port0 -> ../../ttyUSB0
      lrwxrwxrwx 1 root root 13 Jan 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if01-port0 -> ../../ttyUSB1
      lrwxrwxrwx 1 root root 13 Jan 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if02-port0 -> ../../ttyUSB2
      lrwxrwxrwx 1 root root 13 Jan 31 11:48 usb-Xilinx_JTAG+3Serial_90805-if03-port0 -> ../../ttyUSB3
      ```

      `ttyUSB0` is not connected to UART but the corresponding port on FT4232HL is connected to JTAG. The device may
      disappear after connecting OpenOCD (described at the end of the guide).

      `ttyUSB1` is connected to `UART0` which is used for data transfer using `phoenixd` (not used in this guide).

      `ttyUSB2` is connected to `UART1` which is used for serial console.

      `ttyUSB3` is connected to the FPGA part of the SoC, and it will not be used in this guide.


4. Power up the board, changing the `SW1` position to `ON`. Two rows of green LEDs should turn on indicating
power rails - see "Power and Status LEDs" section of the ZCU104 Board User Guide (UG1267) for detailed descriptions.
    - If the `DS36` LED is turned on (red), the board is in reset. It should light up for a short time after turning on
    the board or pressing the `POR_B` button.

    - If the `DS35` LED is turned on (red), it indicates an error loading plo. Ensure that the boot mode is
    set correctly, and the boot image is written correctly to the chosen boot medium (SD card or NOR flash).

5. When the board is connected to your host PC, open serial port in terminal using picocom and type the console port
(in this case `ttyUSB2`)

    ```sh
    picocom -b 115200 --imap lfcrlf /dev/tty[port]
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

If there wasn't an older system image in the NOR flash the `plo` welcome screen will appear.
If you don't see it, please press the `POR_B` button (`SW4`) to reset the chip.

Providing that Phoenix-RTOS is present in the flash memory you will probably see the system startup:

![Image](../_static/images/quickstart/zynqmp-rpu-ram_start-2.png)

You want to press the `POR_B` button (`SW4`) again and interrupt `Waiting for input` by pressing any key to enter plo:

![Image](../_static/images/quickstart/zynqmp-rpu-sd-plo.png)

### Erasing the area intended for file system

It's needed to erase sectors that will be used by `jffs2` file system as we place in the `flash0.disk`
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

![Image](../_static/images/quickstart/zynqmp-plo-erase.png)

Please wait until erasing is finished.

### Copying flash image using RAM disk and OpenOCD

On ZynqMP plo is configured with a RAM disk at address 0x08000000. The flash image can be written to it
using OpenOCD over JTAG which is a lot faster than over UART.

See [Debugging](#debugging) for details on how to launch OpenOCD.

```sh
cd _boot/armv7r5f-zynqmp-zcu104
openocd -f "$(realpath ../../scripts/openocd/zynqmp/)" -f "../../scripts/openocd/zynqmp/xilinx_zynqmp.cfg" \
  -c "targets uscale.r5.0" \
  -c "init" \
  -c "halt" \
  -c "load_image flash0.disk 0x08000000 bin" \
  -c "resume" \
  -c "exit"
```

```sh
Open On-Chip Debugger 0.12.0-01005-g7a92ec0a6 (2026-02-18-16:06)
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
jtag
adapter speed: 12000 kHz

Info : Hardware thread awareness created
boot_apu
Info : J-Link V9 compiled Sep  1 2016 18:29:50
Info : Hardware version: 9.60
Info : VTarget = 3.209 V
Info : clock speed 12000 kHz
Info : JTAG tap: uscale.tap tap/device found: 0x5ba00477 (mfg: 0x23b (ARM Ltd), part: 0xba00, ver: 0x5)
Info : JTAG tap: uscale.ps tap/device found: 0x14730093 (mfg: 0x049 (Xilinx), part: 0x4730, ver: 0x1)
Info : JTAG tap: uscale.tap tap/device found: 0x5ba00477 (mfg: 0x23b (ARM Ltd), part: 0xba00, ver: 0x5)
Info : JTAG tap: uscale.ps tap/device found: 0x14730093 (mfg: 0x049 (Xilinx), part: 0x4730, ver: 0x1)
Error: JTAG-DP STICKY ERROR
Warn : target uscale.a53.0 examination failed
Info : uscale.r5.0: hardware has 8 breakpoints, 8 watchpoints
Error: target->coreid 1 powered down!
Warn : target uscale.r5.1 examination failed
Info : starting gdb server for uscale.a53.0 on 3333
Info : Listening on port 3333 for gdb connections
Info : gdb port disabled
Info : starting gdb server for uscale.r5.0 on 3334
Info : Listening on port 3334 for gdb connections
Info : starting gdb server for uscale.r5.1 on 3335
Info : Listening on port 3335 for gdb connections
Info : uscale.r5.0: MPIDR level2 0, cluster 1, core 0, mono core, no SMT
target halted in Thumb state due to debug-request, current mode: System
cpsr: 0x0000013f pc: 0xfffc0b4a
D-Cache: enabled, I-Cache: enabled
8388608 bytes written at address 0x08000000
downloaded 8388608 bytes in 139.805527s (58.596 KiB/s)
```

Once the flash image is in RAM disk (it can take 60-120s) you can copy it to flash0 in PLO:

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

## Using Phoenix-RTOS

To get the available command list please type:

```shell
help
```

![Image](../_static/images/quickstart/zynqmp-help.png)

If you want to get the list of working processes please type:

```shell
ps
```

![Image](../_static/images/quickstart/zynqmp-ps.png)

To get the table of processes please type:

```shell
top
```

![Image](../_static/images/quickstart/zynqmp-top.png)

## Debugging

The FT4232HL chip can be used to communicate with the SoC over JTAG.
Below are instructions how to connect OpenOCD to the board:

First run OpenOCD with the following command:

```sh
openocd -f "../../scripts/openocd/zynqmp/ftdi_zcu104.cfg" -f "../../scripts/openocd/zynqmp/xilinx_zynqmp.cfg" -c "reset_config srst_only"
```

You may get an error `LIBUSB_ERROR_ACCESS`. If this happens, try running `openocd` with `sudo` - if this fixes
the problem, you need to configure [udev rules](https://github.com/arduino/OpenOCD/blob/master/contrib/60-openocd.rules)
for `openocd` and add your user account to group `plugdev`.

If the connection was successful, this result should appear:

![Image](../_static/images/quickstart/zynqmp-openocd.png)

Now GDB can be connected to port 3333 on local machine.

For debugging the kernel or userspace you will need to examine all cores before starting GDB.
To do this you need to run OpenOCD with command:

```sh
openocd -f "../../scripts/openocd/zynqmp/ftdi_zcu104.cfg" -f "../../scripts/openocd/zynqmp/xilinx_zynqmp.cfg" -c "reset_config srst_only" -c "init" -c "core_up 1 2 3"
```
