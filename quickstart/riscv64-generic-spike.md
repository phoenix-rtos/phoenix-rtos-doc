# Running system on `riscv64-generic-spike`

This version is designated for RISC-V 64 processors based spike machine implemented by the Spike (`riscv-isa-sim`)
emulator. To launch this version `phoenix.osbi` file should be provided - system image with integrated OpenSBI
bootloader, containing PLO, kernel, console driver, dummyfs filesystem and the `psh` shell.

The file is created as the final artifact of the `phoenix-rtos-project` build and is located in the `_boot` directory.
See [how to build the Phoenix-RTOS system image](../building/README.md)

## Running image under the spike

Firstly, you need to install a spike simulator.

  <details>
  <summary>How to install spike simulator (Ubuntu 20.04)</summary>

  1. Clone the `riscv-isa-sim` GitHub repository. System was tested on commit `5fa1cd54` on `master` branch.

      ```bash
      git clone https://github.com/riscv-software-src/riscv-isa-sim.git --single-branch
      ```

  2. Enter the downloaded repository

      ```bash
      cd riscv-isa-sim
      ```

  3. Check out the commit `5fa1cd54`

      ```bash
      git checkout 5fa1cd54
      ```

  4. Install the device-tree-compiler

      ```bash
      sudo apt-get update && \
      sudo apt-get install device-tree-compiler
      ```

  5. Install the Spike RISC-V ISA Simulator

      ```bash
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
./scripts/riscv64-generic-spike.sh
```

<img src="_images/riscv64-generic-spike1.png" width="700px">
</br>
<img src="_images/riscv64-generic-spike2.png" width="700px">

## Using Phoenix-RTOS

Phoenix-RTOS will be launched and the `psh` shell command prompt will appear in the terminal. To get the available
command list please type:

```bash
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
