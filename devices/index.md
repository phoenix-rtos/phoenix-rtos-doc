# Device divers

This chapter describes the Phoenix-RTOS device driver architecture. After reading this chapter, you will know:

- How device drivers are structured as user-level servers.
- The available driver categories and their platforms.
- The multi-function consolidated server pattern.

Phoenix-RTOS implements device drivers as device servers running on the user level. The communication with drivers is
done via message passing using a well-defined interface for exchanging data between programs and drivers.

To control a device, two mechanisms are necessary and should be provided by the operating system kernel: access to
device hardware registers and a method of handling interrupts triggered by the device.

Each typical driver creates a communication port, registers it in the namespace, initializes the device, and starts
processing incoming messages using `msgRecv`/`msgRespond` syscalls.

The source code of Phoenix-RTOS device drivers can be obtained using the following command:

```shell
git clone https://github.com/phoenix-rtos/phoenix-rtos-devices.git
```

## Driver Categories

| Category | Directory | Description |
|---|---|---|
| ADC | `adc/` | Analog-to-digital converters (AD7779, ADE7913, MCP331) |
| CAN | `can/` | CAN bus (ZynqMP CAN) |
| Display | `display/` | Display drivers (OLED 128x64) |
| DMA | `dma/` | DMA controllers (GRDMAC2, i.MX SDMA, i.MX RT eDMA) |
| GPIO | `gpio/` | GPIO controllers (i.MX 6ULL, Zynq, RCPWM) |
| I2C | `i2c/` | I2C masters (GRLIB, i.MX 6ULL, Zynq) |
| Magnetometer | `mag/` | Magnetic sensors (ALS31300) |
| OTP | `otp/` | One-time programmable fuses (i.MX 6ULL, i.MX RT117x) |
| PCIe | `pcie/` | PCIe controllers (Xilinx AXI, Xilinx NWL) |
| RTC | `rtc/` | Real-time clocks (i.MX 6ULL, PCF85363) |
| SDIO | `sdio/` | SD/SDIO interface |
| Sensors | `sensors/` | Sensor framework (barometer, GPS, IMU, magnetometer) |
| SPI | `spi/` | SPI controllers (GRLIB, i.MX eCSPI/QSPI, Zynq) |
| SpaceWire | `spacewire/` | SpaceWire interfaces (GRLIB GRSPW2, router) |
| Storage | `storage/` | Flash/block storage (NOR, NAND, ATA, VirtIO, USB mass storage) |
| Temperature | `temp/` | Temperature sensors (NCT75, SHT3x) |
| TTY/UART | `tty/` | Serial terminals and UARTs (16550, CMSDK, GRLIB, i.MX, Zynq, USB ACM) |
| USB | `usb/` | USB host controllers and device controllers |
| Watchdog | `watchdog/` | Hardware watchdog timers |

## Multi-Function Consolidated Servers

On resource-constrained platforms, multiple device types are handled by a single consolidated server process. These
are in `multi/` and route operations via `mtDevCtl` messages with per-peripheral union structures:

| Server | Platform | Peripherals |
|---|---|---|
| `grlib-multi` | GRLIB (SPARC) | UART, GPIO, SPI, I2C |
| `imxrt-multi` | i.MX RT | UART, GPIO, SPI, I2C, ADC |
| `mcxn94x-multi` | NXP MCX N94x | UART, GPIO, SPI, I2C |
| `stm32l4-multi` | STM32L4/N6 | ADC, LCD, RTC, GPIO, UART, flash, SPI, I2C, DMA |

## Shared Driver Libraries

| Library | Purpose |
|---|---|
| `libtty` | TTY line discipline, FIFO, serial parameters. Shared by all UART drivers. |
| `libklog` | Kernel log interface |
| `libpseudodev` | Pseudo-device abstraction |
| `librtt` | Real-Time Transfer communication |

```{toctree}
:maxdepth: 1

interface.md
hwaccess.md
interrupts.md
libsdio.md
simsensors.md
```
