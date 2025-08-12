#!/bin/bash

STLINK_GDB_PATH="/opt/st/stm32cubeide_1.18.1/plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.2.100.202501151542/tools/bin"
STLINK_PROG_PATH="/opt/st/stm32cubeide_1.18.1/plugins/com.st.stm32cube.ide.mcu.externaltools.cubeprogrammer.linux64_2.2.100.202412061334/tools/bin"
BACKGROUND_CMD="$STLINK_GDB_PATH/ST-LINK_gdbserver -p 3333 -l 4 -v -d -s -cp $STLINK_PROG_PATH -m 1"
FOREGROUND_CMD="gdb-multiarch -x gdb_stm32n6.txt"

setsid bash -c "exec $BACKGROUND_CMD" &
gdbserver_pid=$!
# Prevent script from dying on Ctrl+C
trap '' SIGINT
$FOREGROUND_CMD

# Clean up gdbserver when gdb exits
echo "[INFO] GDB exited. Cleaning up gdbserver."
kill -9 $gdbserver_pid 2>/dev/null
wait $gdbserver_pid 2>/dev/null
