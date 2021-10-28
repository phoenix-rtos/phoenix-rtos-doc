# Running system on `riscv64-spike`
This version is designated for RISC-V 64 processor based spike machine implemented by spike (riscv-isa-sim) emulator and `qemu-system-riscv64`. To launch this version two files should be provided - kernel file integrated with SBI firmware with embedded SBI console driver, dummyfs filesystem and `psh` shell and disk image with ext2 filesystem.

The files are created as the final artifact of `phoenix-rtos-project` building and is located in `_boot` directory. See [how to build the Phoenix-RTOS system image](../building/README.md)

## Running image under spike
To run image under spike you should type:

````bash
spike _boot/phoenix-riscv64-spike.bbl
````

<img src="_images/spike-riscv64-spike.png" width="700px">

## Running image under qemu
To run image under qemu you should type:

```
  qemu-system-riscv64 -machine spike_v1.10 -serial stdio  -kernel _boot/phoenix-riscv64-spike.bbl
```

<img src="_images/qemu-riscv64-spike.png" width="700px">

Phoenix-RTOS will be launched and `psh` shell command prompt will appear in the terminal. To get the available command list please type `help`. To get the list of working threads and processes please type `ps -t`.

<img src="_images/qemu-riscv64-spike-ps-t.png" width="700px">

## See also

1. [Running system on targets](README.md)
2. [Table of Contents](../README.md)
