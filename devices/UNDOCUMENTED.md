# Devices Documentation — Undocumented Areas

## 1. Completely Undocumented Driver Categories

### ADC (Analog-to-Digital Conversion)
- **ad7779**: Multi-channel ADC with SPI interface, uses DMA
- **ade7913**: Energy metering IC
- **mcp331**: Precision ADC

### CAN Bus
- **zynqmp-can**: Xilinx ZynqMP CAN peripheral (CAN0/CAN1) with custom `libzynqmp-can-if` static library interface

### Display
- **oled-128O064B0**: 128×64 OLED display driver

### DMA (Direct Memory Access)
- **grdmac2**: GRLIB DMA controller
- **imx6ull-sdma**: i.MX 6ULL Smart DMA
- **imxrt-edma**: i.MX RT eDMA

### GPIO
- **imx6ull-gpio**: Port + dir file interface with binary/text modes
- **rcpwm**: Reversible PWM controller
- **zynq-pwm**: Zynq PWM
- **zynq7000-gpio**: Zynq 7000 GPIO
- **zynq7000-xgpio**: Xilinx GPIO (AXI)

### I2C
- **gri2cmst**: GRLIB I2C master
- **imx6ull**: i.MX 6ULL I2C
- **zynq**: Xilinx Zynq I2C
- Common I2C library with `i2c-msg.h` (`bus_write`, `bus_read`, `reg_read` operations)

### Magnetometer
- **mag-als31300**: ALS31300 magnetometer via I2C

### RTC (Real-Time Clock)
- **imx6ull-rtc**: i.MX 6ULL RTC
- **pcf85363a**: PCF85363 RTC via I2C

### SPI
- **grspictrl**: GRLIB SPI controller
- **imx6ull-ecspi**: i.MX 6ULL eSPI (256-byte max burst, 4-channel)
- **imx6ull-qspi**: Quad SPI
- **zynq-spi**: Xilinx Zynq SPI
- **zynq7000-xspi**: Xilinx Zynq 7000 SPI

### Storage/Flash
- **flashdrv**: Generic flash MTD interface
- **gr716-flash**: GRLIB flash controller
- **grlib-nandfctrl2**: NAND flash GRLIB
- **host-flash**: Emulated flash for host PC
- **imx6ull-flash**: i.MX 6ULL internal flash
- **imx6ull-flashnor**: i.MX 6ULL NOR flash
- **imxrt-flash**: i.MX RT flash
- **pc-ata**: IBM PC ATA hard disk controller
- **umass**: USB mass storage
- **virtio-blk**: Virtual block device
- **zynq-flash**: Xilinx Zynq flash
- **zynq7000-sdcard**: Xilinx Zynq SD card/MMC

### TTY/UART
- **cmsdk-apbuart**: ARM CMSDK UART
- **grlib-uart**: GRLIB UART
- **imx6ull-uart**: i.MX 6ULL UART
- **libtty**: TTY library with FIFO, line discipline, serial parameters
- **pc-tty**: PC serial port
- **spike-tty**: RISC-V Spike simulator UART
- **uart16550**: Intel 16550 UART
- **usbacm**: USB CDC ACM modem
- **pl2303**: Prolific PL2303 USB-to-serial
- **zynq-uart**: Xilinx Zynq UART

### USB
- **cdc-demo**: USB CDC demo
- **ehci**: USB EHCI host controller
- **libusbclient**: USB device controller library (STM32N6 implementation)

### Watchdog
- **imx6ull-watchdog**: i.MX 6ULL watchdog timer

### SpaceWire
- **grspw2**: GRLIB SpaceWire interface
- **grspwrtr**: GRLIB SpaceWire router
- **libgrspw**: SpaceWire library

### Temperature Sensors
- **nct75**: Nuvoton NCT75 via I2C
- **sht3x**: Sensirion SHT3x humidity/temperature via I2C

### PCIe
- **pcie-xilinx-axi**: Xilinx AXI PCIe Gen1/Gen2
- **pcie-xilinx-nwl**: Xilinx NWL PCIe Gen3
- PCIe server (platform-agnostic)
- **tebf0808**: TEBF0808 baseboard PCIe support

### OTP (One-Time Programmable)
- **imx6ull-otp**: i.MX 6ULL OTP/fuse controller
- **imxrt117x-otp**: i.MX RT117x OTP

### Multi-function Consolidated Servers
- **grlib-multi**: GRLIB multi-function server
- **imxrt-multi**: i.MX RT consolidated device server
- **mcxn94x-multi**: MCXn94x multi-function server
- **stm32l4-multi**: STM32L4x6 consolidated driver (ADC, flash, GPIO, I2C, LCD, RTC, SPI, UART)

### Support Libraries
- **libklog**: Kernel logging
- **libpseudodev**: Pseudo device library
- **librtt**: RTT (Real-Time Transfer) library

## 2. Undocumented Architectural Patterns

### Multi-Function Consolidated Servers
Single server handling multiple device types (e.g., `stm32l4-multi` supports ADC, EEPROM, GPIO, I2C, LCD, RTC, SPI, UART). Uses `mtDevCtl` messages with union structures for type switching. Reduces process overhead and centralizes hardware initialization.

### Custom Library Interfaces
Beyond standard message passing: `libzynqmp-can-if`, `libsensors`, `libtty`. Static linking of complex driver logic allows thin server wrappers with logic in the library.

### Sensor Plugin Architecture
`sensor_info_t` structures registered with `sensors_register()`. Each driver provides: `alloc`, `dealloc`, `start`, `read` operations. `sensors_publish()` for event delivery. Framework supports: barometer, GPS, IMU, magnetometer, power supply.

### GPIO Text Mode Interface
GPIO drivers create folder hierarchies with text-mode access:
```
echo +28 > /dev/gpio2/dir   # Set pin 28 as output
```

### Device Instance Patterns
- Named instances: `uart1`, `uart2`, `uart3` (UART drivers)
- Numbered instances: `ecspi1-4`, `spi0-1` (SPI)
- CAN peripherals: `CAN0`, `CAN1`
