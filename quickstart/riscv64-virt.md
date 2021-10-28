# Running system on `riscv64-virt`
This version is designated for RISC-V 64 processor based virt machine implemented by `qemu-system-riscv64`. To launch this version two files should be downloaded - kernel file
integrated with SBI firmware with embedded UART16550 interface driver, dummyfs filesystem and `psh` shell and disk image with ext2 filesystems.

## Running image under qemu
To run image under qemu you should type:

```
  qemu-system-riscv64 -machine virt -serial stdio  -kernel ./phoenix-riscv64-virt.bbl
```

<img src="_images/qemu-riscv64-virt.png" width="700px">

Phoenix-RTOS will be launched and `psh` shell command prompt will appear in the terminal. To get the available command list please type `help`. To get the list of working threads and processes please type `ps -t`.

<img src="_images/qemu-riscv64-virt-ps-t.png" width="700px">

## See also

1. [Running system on targets](README.md)
2. [Table of Contents](../README.md)
