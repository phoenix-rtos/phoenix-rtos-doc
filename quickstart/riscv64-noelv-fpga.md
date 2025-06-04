# Running system on <nobr>riscv64-noelv-fpga</nobr>

These instructions describe how to run Phoenix-RTOS on the NOEL-V processor configured on the Digilent Arty A7-100T
FPGA - `riscv64-noelv-fpga` target. Note that the build artifacts, including the system image should be provided in the
`_boot` directory. If you have not built the system image yet, please refer to the
[Building Phoenix-RTOS image](../building/index.md) section.

## Connecting the board

Connect the board to the computer using 1 micro USB cable that provides power and UART communication and 1 additional
USB-UART converter.

## Loading the Phoenix-RTOS system image

### Uploading the Phoenix-RTOS Loader (PLO) image to RAM

To load the PLO image to the board, you will need to use the `GRMON` debug monitor.

<details>
<summary>How to get GRMON</summary>

- Download the GRMON software from the [official website](https://www.gaisler.com/products/grmon4).
- After downloading the archive, extract it and optionally add the `grmon` binary to the `PATH` variable.
- Install Digilent Adept Runtime for debug link connection as described in the
[GRMON User's Manual](https://download.gaisler.com/products/GRMON4/doc/grmon4.pdf).

</details>
</br>

Launch the `GRMON` monitor using the following command:

```console
grmon -digilent
```

The `-digilent` parameter specifies the Digilent JTAG adapter.

Load the PLO image to the RAM by running the following command in the `GRMON`:

```console
load _boot/riscv64-noelv-fpga/sbi-ram-noelv.elf
```

Check on which port the board is connected to the computer. To do this, run the following command:

```console
ls -l /dev/serial/by-id
```

![Image](_images/noelv-ls.png)


In this case, the serial port to use is `/dev/ttyUSB2`. Open the terminal emulator and connect to the board using the
following command:

```console
picocom -b 115200 --imap lfcrlf /dev/ttyUSB2
```

Start the bootloader execution through the `GRMON` monitor by executing the following command in its interface:

```console
run
```

The PLO interface will be visible in the terminal emulator.

### Formatting the rootfs JFFS2 partition

To format the rootfs JFFS2 partition, execute the command that is printed out during the build process of Phoenix-RTOS. The
command should look like this:

```console
jffs2 -d 2.0 -c 80:80:65536:16 -e
```

This will erase the root filesystem partition and write the JFFS2 clean markers to the flash memory. The parameters will
change depending on the partition configuration in the `nvm.yaml` file. The example above is for the default
configuration of the `riscv64-noelv` target located in `_targets/riscv64/noelv/nvm.yaml`.

### Copying the Phoenix-RTOS image to the flash memory

To copy the Phoenix-RTOS image to the flash memory, `phoenixd` has to be launched in the `_boot/riscv64-noelv-fpga/`
directory. To do so, execute the following command, choosing appropriate serial port (in this case `/dev/ttyUSB0`):

```console
sudo ./phoenixd -p /dev/ttyUSB0 -b 115200 -s .
```

You may now copy the Phoenix-RTOS image files to the flash memory using the `copy` command.
To copy the kernel partition, use the following command (if you only want to reflash the root filesystem, you can skip
this):

```console
copy uart1 part_kernel.img flash0 0x440000 0x0
```

To copy the root filesystem partition, use the following command:

```console
copy uart1 part_rootfs.img flash0 0x500000 0x0
```

To copy the flash partition table, use the following command:

```console
copy uart1 part_flash0_ptable.img flash0 0xff0000 0x0
```

Note that the offsets used in the commands must match the offsets defined in the `nvm.yaml` file for the `riscv64-noelv`
target. Flash partition table should be copied to the last sector of the flash memory, which is why the offset is
`0xff0000`. The `plo` partition is not copied to the flash memory, as this target does not yet support booting from
flash - `plo` is loaded by GRMON to the RAM and executed from there.

### Booting Phoenix-RTOS

To launch the Phoenix-RTOS image uploaded to the flash memory, interrupt the `GRMON` execution by `^C`, and load the
second bootloader image:

```console
load _boot/riscv64-noelv-fpga/sbi-noelv.elf
```

Then, start the bootloader execution through the `GRMON` monitor by executing the following command in its interface:

```console
run
```

The Phoenix-RTOS shell should appear in the terminal shortly after.

## Using the Phoenix-RTOS

After executing the `run` command, Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the
terminal.

![Image](_images/noelv-start.png)

## See also

1. [Running system on targets](index.md)
2. [Table of Contents](../index.md)
