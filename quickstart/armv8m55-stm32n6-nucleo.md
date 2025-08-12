# Phoenix-RTOS startup on STM32N6

Currently the project is set up to launch the system from a RAM disk. The RAM disk is 512 KB in size and applications are set up for execute-in-place. To start the system you need to load the PLO binary and the RAM disk image into memory.

## Set up GDB server and GDB

### OpenOCD (not recommended)
You can use OpenOCD to connect to the board and load the PLO and RAM disk. However, this setup is not useful for debugging, because all of RAM reads back as 0. I haven't investigated the cause.

To run OpenOCD you can copy the files `stm32n6_openocd.cfg` and `stm32n6x.cfg` to the current directory and run the command:
```sh
openocd -f stm32n6_openocd.cfg
```

### STLink GDB server
STLink GDB server works without problems and allows for both writing the image and debugging. It is part of STM32CubeIDE - it can be downloaded from https://www.st.com/en/development-tools/stm32cubeide.html .
Detailed instructions for use are in User Manual UM2576.

The GDB server can be stated using the following commands. Remember to set `STLINK_GDB_PATH` and `STLINK_PROG_PATH` variables accordingly on your machine after installing STM32CubeIDE.
```sh
STLINK_GDB_PATH="/opt/st/stm32cubeide_1.18.1/plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.2.100.202501151542/tools/bin"
STLINK_PROG_PATH="/opt/st/stm32cubeide_1.18.1/plugins/com.st.stm32cube.ide.mcu.externaltools.cubeprogrammer.linux64_2.2.100.202412061334/tools/bin"
$STLINK_GDB_PATH/ST-LINK_gdbserver -p 3333 -l 4 -v -d -s -cp "$STLINK_PROG_PATH" -m 1
```

### GDB script
Create the following script named `gdb_stm32n6.txt`:

```
set architecture arm
target extended-remote :3333

# Load PLO into memory
load <path_to_project>/_boot/armv8m55-stm32n6-nucleo/plo.elf

# Load symbol files for PLO, kernel, other applications (apps require relocation)
add-symbol-file <path_to_project>/_build/armv8m55-stm32n6-nucleo/prog/plo-armv8m55-stm32n6.elf
add-symbol-file <path_to_project>/_build/armv8m55-stm32n6-nucleo/prog/phoenix-armv8m55-stm32n6.elf
add-symbol-file <path_to_project>/_build/armv8m55-stm32n6-nucleo/prog/stm32l4-multi 0x341352C0

# Load ramdisk image
restore <path_to_project>/_boot/armv8m55-stm32n6-nucleo/phoenix.disk binary 0x34100000
```

Additionally, a script `run_gdbserver_and_gdb.sh` is attached. The script will run STLink GDB server in the background and GDB in the foreground. Before you run the script ensure all paths within it are set correctly.

## Run Phoenix image
1. Checkout `jmaksmyowicz/stm32n6` branch in phoenix-rtos-project and compile for `armv8m55-stm32n6-nucleo` target.
2. Ensure that the board is set up for DEV boot - BOOT0 jumper set in low position (closer to STM32N6), BOOT1 in high position (closer to ST-LINK).
3. Plug in a USB-C cable (pay attention to plug into the port closer to ST-LINK)
4. Start your chosen GDB server (either OpenOCD or STLink GDB server)
5. Run GDB with the following command:
    ```
    gdb-multiarch -x <path_to_dir>/gdb_stm32n6.txt
    ```
6. PLO and RAM disk image will be loaded. Continue program execution by typing `c` and pressing Enter.

The image will stop running if GDB is closed. It will have to be loaded again if the CPU is reset.
