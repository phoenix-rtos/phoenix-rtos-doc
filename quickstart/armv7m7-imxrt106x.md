# Running system on `armv7m7-imxrt106x` (NXP i.MX RT106x)

This version is designated for NXP i.MX RT106x processors with ARM Cortex-M7 core. To launch this version the final disk image and loader image should be downloaded. The images are created as the final artifact of `phoenix-rtos-project` building and are located in `_boot` directory. The disk image consist of bootloader (plo), kernel, UART driver (tty), dummyfs filesystem server (RAM disk) and psh (shell). The necessary tools to carry out the flashing process are located in `_boot` directory as well.

Default configuration of peripherals allows to run Phoenix-RTOS on i. MX RT1064 - EVK:
https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/mimxrt1064-evk-i-mx-rt1064-evaluation-kit:MIMXRT1064-EVK

## Running loader (plo) using SDP

In order to flash the disk image to the board, the bootlader (plo) image located in `_boot` directory should be uploaded to the RAM memory using `psu` (Phoenix Serial Uploader) via SDP (Serial Download Protocol).

NOTE: i. MX RT1064 should be set in Serial Download mode. Set appropriate configuration of SW7 switch on i. MX RT1064 - EVK.

Run `psu` as follow:

```
$ sudo ./psu plo-ram-armv7m7-imxrt106x.sdp
```

The plo user interface should appear on UART1 - connector J41 on i. MX RT1064 - EVK. The default baudrate is set to 115200 bps.

<img src="_images/imxrt106x-plo.png" width="1000px">

To get the available bootloader command list please type `help`.

<img src="_images/imxrt106x-plo-help.png" width="1000px">

## Copying flash image using PHFS (phoenixd)

To flash the disk image, the another serial connection has to be established. For this purpose the UART3 located on arduino interface is used.
To share disk image to the bootloader, `phoenixd` has to be launched with the following arguments (choose suitable ttyUSBx device):

```
$ sudo ./phoenixd -k ../_build/armv7m7-imxrt106x/prog/phoenix-armv7m7-imxrt106x.elf -p /dev/ttyUSBx -b 115200 -s .
```

To start copying file, write following command:

```
(plo)% copy com1 phoenix-armv7m7-imxrt106x.disk flash0 0 0
```

<img src="_images/imxrt106x-plo-copy.png" width="1000px">

## Booting Phoenix-RTOS from internal Flash

To launch Phoenix-RTOS from flash memory, change SW7 switch to Internal Flash mode and restart the board.

If everything has gone correctly, the bootloader should launch Phoenix-RTOS with default configuration and `psh` shell command prompt will appear in the terminal.

<img src="_images/imxrt106x-start.png" width="1000px">


## Using Phoenix-RTOS


To get the list of working threads and processes please type `ps -t`.

<img src="_images/imxrt106x-ps-t.png" width="1000px">


To get the table of processes please type `top`.

<img src="_images/imxrt106x-top.png" width="1000px">

## See also

1. [Running system on targets](README.md)
2. [Table of Contents](../README.md)

