# Running system on `riscv64-generic-spike`
This version is designated for RISC-V 64 processor based spike machine implemented by the spike (riscv-isa-sim) emulator and `qemu-system-riscv64`. To launch this version two files should be provided - kernel file integrated with SBI firmware with embedded SBI console driver, dummyfs filesystem and `psh` shell, and disk image with ext2 filesystem.

The files are created as the final artifact of the `phoenix-rtos-project` building and are located in the `_boot` directory. See [how to build the Phoenix-RTOS system image](../building/README.md)

## Running image under the spike
Firstly, you need to install a spike simulator.

  <details>
  <summary>How to install spike simulator (Ubuntu 20.04)</summary>

  1. Clone the riscv-isa-sim Github repository in a `1.1.0` version.

  ```
  git clone https://github.com/riscv-software-src/riscv-isa-sim.git --branch v1.1.0 --single-branch
  ```

  2. Enter the downloaded repository

  ```
  cd riscv-isa-sim
  ```

  3. Install the device-tree-compiler

  ```
  sudo apt-get update && \
  sudo apt-get install device-tree-compiler
  ```

  4. Install the Spike RISC-V ISA Simulator

  ```
  mkdir build && \
  cd build && \
  ../configure --prefix=$RISCV && \
  make && \
  sudo make install
  ```

  </details>
  </br>

Then, to run the image under spike you should change the directory to `phoenix-rtos-project` and type:

```bash
spike _boot/riscv64-generic-spike/phoenix.bbl
```

<img src="_images/riscv64-generic-spike-spike.png" width="700px">


## Running image under qemu
Just like before, you first need to install the emulator.

  <details>
  <summary>How to get qemu (Ubuntu 20.04)</summary>

  - Install the required packages

  ```
  sudo apt-get update && \
  sudo apt-get install qemu-kvm \
  qemu virt-manager \
  virt-viewer libvirt-clients \
  libvirt-daemon-system \
  bridge-utils virtinst \
  libvirt-daemon \
  qemu-system-misc
  ```

  - Check if qemu is properly installed:

  ```
  qemu-system-riscv64 --version
  ```

  <img src="_images/qemu-version-riscv64.png" width="700px">

  </details> 

To run the system image under qemu you should type the following command from the `phoenix-rtos-project` directory.

```bash
./scripts/riscv64-generic-spike.sh
```

<img src="_images/riscv64-generic-spike-qemu.png" width="700px">

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal. To get the available command list please type:

```
help
```

<img src="_images/riscv64-generic-spike-help.png" width="700px">

To get the list of working processes please type:

```bash
ps
```

<img src="_images/riscv64-generic-spike-ps.png" width="700px">

## See also

1. [Running system on targets](README.md)
2. [Table of Contents](../README.md)
