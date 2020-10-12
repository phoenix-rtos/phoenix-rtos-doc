# Kernel

Phoenix-RTOS is based on the written from scratch dedicated microkernel. Microkernel is effectively implemented and consists of about 20K lines of code (LoC). Microkernel is responsible for:

   - memory management,
   - thread and process management,
   - inter-thread communication and synchronization.

Kernel is divided into five subsystems.

   - hal - hardware abstraction layer
   - lib - common routines
   - vm - virtual memory management
   - proc - process and thread management
   - test - test for other subsystems


## Kernel source code

The source code of the kernel could be obtained using the following command

>
    git clone http://github.com/phoenix-rtos.com/phoenix-rtos-kernel

Kernel source code is structured into following subdirectories.

>
    include/
    scripts/
    src/
      hal/
         ia32/
         arm/
         armv7/
         riscv64/
         ..
      lib/
      vm/
      proc/
      tests/

The `include/` subdirectory consist of header files defining constants and structures used for communication with userland.

The `scripts/` subdirectory consist of set of scripts used for creating OS images (kernel with set of drivers and applications) for specific targets. build-toolchain.sh script is used for simplifying the compilation GNU CC for Phoenix-RTOS and specific target.

The `src/` directory consist of the kernel source code. Subdirectories corresponds to microkernel subsystems mentioned above. Subdirectory `hal/` consist of subdirectories for each supported platform.

## Compilation

For compilation of the microkernel traditional make system is used. To compile you should define the `TARGET` variable in the main `Makefile` located in `src/` directory. The list of available targets is defined inside the file. The structure of target consist of three parts: `<cpu>-<platform>-<board>`.

After defining the `TARGET` variable the set of command should be used.

>
    make clean
Removes all intermediate files (e.g. object files).
>
    make depend
Analyses dependencies between files and stores it in `.depend` files.
>
    make
Compiles kernel and creates the ELF and BIN files in `../src/` directory.




