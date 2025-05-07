# Running system on <nobr>armv7a9-zynq7000</nobr>

This version is designed for Xilinx Zynq-7000 SoC (System on Chip) with ARM Cortex-A9 core. To launch this version the
final disk image should be provided. The image is created as the final artifact of the `phoenix-rtos-project` building
and is located in the `_boot` directory. The disk image consists of the bootloader (plo), kernel, UART driver (tty),
dummyfs filesystem server (RAM disk), flash driver with jffs file system and psh (shell). Necessary tools to carry out
the flashing process are located in the `_boot` directory as well.

## Development board and emulator

The easiest way to start programming hardware targets using Phoenix-RTOS is to get some evaluation
boards with a specified target processor or microcontroller. There are 2 supported boards
[Zedboard](https://www.xilinx.com/products/boards-and-kits/1-8dyf-11.html)
and [Zturn](https://www.myirtech.com/list.asp?id=502) with the `zynq7000` SoC, where the default
configuration of peripherals allows running Phoenix-RTOS.
The next steps for particular development board are described below.

```{toctree}
:maxdepth: 1

armv7a9-zynq7000-zedboard.md
```

```{toctree}
:maxdepth: 1

armv7a9-zynq7000-zturn.md
```

If you don't have one, you can check the running system for this target architecture on an emulator and follow the steps
from the site below.

```{toctree}
:maxdepth: 1

armv7a9-zynq7000-qemu.md
```

## Common problems on zynq7000 boards

- Phoenix-RTOS loader does not appear:
  - When booting using SD card: Make sure that a proper `BOOT.bin` file
  is placed on the card, and that it's in a binary format (right click → properties):

  ```{image} ../../_static/images/quickstart/armv7a9-zynq7000/zynq7000-problems-file-type.png
  :align: center
  :width: 60%
  ```

  - Try to open picocom for a second time (it could get stuck).

  - Power down a board and try once again (changing boot modes needs restart by power off).

  - When booting using SD card: Make sure that SD card is not broken, you can try to format it by yourself.
