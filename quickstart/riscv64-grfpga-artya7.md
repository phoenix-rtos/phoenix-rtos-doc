# Running system on <nobr>riscv64-grfpga-artya7</nobr>

These instructions describe how to run Phoenix-RTOS on the NOEL-V processor configured on the Digilent Arty A7-100T
FPGA - `riscv64-grfpga-artya7` target. Note that the build artifacts, including the system image should be provided in
the `_boot` directory. If you have not built the system image yet, please refer to the
[Building Phoenix-RTOS image](../building/index.md) section.

## Connecting the board

Connect the board to the computer using 1 micro USB cable that provides power and UART communication.

## Loading the Phoenix-RTOS system image

To load the Phoenix-RTOS system image to the board, you will need to use the `GRMON` debug monitor.

<details>
<summary>How to get GRMON</summary>

- Download the GRMON software from the [official website](https://www.gaisler.com/products/grmon4).
- After downloading the archive, extract it and optionally add the `grmon` binary to the `PATH` variable.
- Install Digilent Adept Runtime for debug link connection as described in the
[GRMON User's Manual](https://download.gaisler.com/products/GRMON4/doc/grmon4.pdf).

</details>
</br>

Launch the `GRMON` monitor using the following command:

```shell
grmon -digilent
```

The `-digilent` parameter specifies the Digilent JTAG adapter.

Load the Phoenix-RTOS system image to the RAM by running the following commands in the `GRMON`:

```shell
load _boot/riscv64-grfpga-artya7/sbi-grfpga.elf
```

```shell
load -binary _boot/riscv64-grfpga-artya7/phoenix.disk 0x08000000
```

Set entry point of the program:

```shell
ep 0x0
```

Check on which port the board is connected to the computer. To do this, run the following command:

```shell
ls -l /dev/serial/by-id
```

```
total 0
lrwxrwxrwx 1 root root 13 sie 14 10:37 usb-Digilent_Digilent_USB_Device_210319B7CF39-if01-port0 -> ../../ttyUSB1
```

In this case, the serial port to use is `/dev/ttyUSB1`. Open the terminal emulator and connect to the board using the
following command:

```shell
picocom -b 115200 --imap lfcrlf /dev/ttyUSB1
```

To start the Phoenix-RTOS system, execute the following command in the `GRMON` monitor:

```shell
run
```

## Using the Phoenix-RTOS

After executing the `run` command, Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the
terminal.

```
Phoenix SBI
Phoenix-RTOS loader v. 1.21 rev: 8326603
hal: RISC-V 64-bit NOEL-V
cmd: Executing pre-init script
console: Setting console to 0.0
Waiting for input,     0 [ms]
Phoenix-RTOS microkernel v. 3.2 rev: fa2cb46
hal: RISC-V NOEL-V 64 bit (fixed-clock) - 1 core
hal: riscv@MHz(rv64ima_zicbom+riscv,sv39)
hal: Using PLIC interrupt controller
hal: Using hypervisor timer
vm: Initializing page allocator (2544+0)/260096KB, page_t=32
vm: [512x]P[31H][68K][156H][58A][238H]P[83H][64388.]
vm: Initializing memory mapper: (15987*112) 1790544
vm: Initializing kernel memory allocator: (32*88) 2816
vm: Initializing memory objects
proc: Initializing thread scheduler, priorities=8
syscalls: Initializing syscall table [100]
main: Starting syspage programs: 'dummyfs', 'grlib-uart', 'psh'
dummyfs: initialized
(psh)%
```
