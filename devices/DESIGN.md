# Devices — Design Observations

## User-Level Driver Architecture

All device drivers run in user space as servers. Communication happens via message passing (`portCreate()`, `portRegister()`, `msgRecv()`, `msgRespond()`). This follows the microkernel philosophy — faults in drivers do not crash the kernel.

## Two Driver Patterns: Modular vs Consolidated

### Modular (per-device server)
Separate servers for UART, GPIO, SPI, etc. Typical for i.MX 6ULL platform. Each driver is an independent process.

### Consolidated (multi-function server)
Single server handles multiple device types. Used by `stm32l4-multi`, `imxrt-multi`, `grlib-multi`, `mcxn94x-multi`. Routes via `mtDevCtl` with union message structures. Reduces context switch overhead and centralizes hardware init.

**Trade-off:** Modularity and fault isolation vs. initialization complexity and resource overhead.

## Device Type Message Union

Multi-function servers define message unions covering all supported peripherals:
```
adc_get, rtc_get, rtc_set, lcd_get, lcd_set, i2c_get, i2c_set,
gpio_def, gpio_get, gpio_set, uart_def, uart_get, uart_set,
flash_get, flash_set, spi_get, spi_set, spi_def
```

## Library-Backed Drivers

Complex driver logic lives in static libraries linked into thin server wrappers:
- `libzynqmp-can-if`: CAN frame formatting
- `libsensors`: Pluggable sensor framework with per-driver operations
- `libtty`: TTY line discipline, FIFO, terminal parameter management
- `libecspi`, `libzynq-spi`: SPI hardware abstraction

## Sensor Plugin Architecture

Sensorhub framework with pluggable drivers:
- Registration: `sensors_register(sensor_info_t*)`
- Driver ops: `alloc`, `dealloc`, `start`, `read`
- Event delivery: `sensors_publish()`
- Supported types: barometer, GPS (NMEA/UBX), IMU, magnetometer, power supply
- Simulated sensors from CSV files for testing

## GPIO Filesystem Interface

GPIO drivers expose dual-mode filesystem interface:
```
/dev/gpioN/port    # Binary: read/write pin states
/dev/gpioN/dir     # Text: echo +28 (output) or -28 (input)
```

## Interrupt Handling Contract

All major peripherals register interrupt handlers via `interrupt()` syscall:
- Handler executes in kernel context with interrupts globally disabled
- Returns ≥ 0 to trigger `condBroadcast()` for user-space notification
- Used for: UART RX/TX, SPI transfer completion, ADC sampling, GPIO events, DMA completion, RTC alarms

## Platform Coverage Matrix

| Peripheral | i.MX 6ULL | i.MX RT | STM32L4 | Zynq | GRLIB | MCXn94x | PC/x86 | RISC-V |
|-----------|:---------:|:-------:|:-------:|:----:|:-----:|:-------:|:------:|:------:|
| UART      | ✓         | (multi) | (multi) | ✓    | ✓     | (multi) | ✓      | ✓      |
| SPI       | ✓         | (multi) | (multi) | ✓    | ✓     | (multi) | —      | —      |
| I2C       | ✓         | (multi) | (multi) | ✓    | ✓     | (multi) | —      | —      |
| GPIO      | ✓         | (multi) | (multi) | ✓    | —     | (multi) | —      | —      |
| Flash     | ✓         | ✓       | (multi) | ✓    | ✓     | —       | —      | —      |
| ADC       | —         | —       | (multi) | —    | —     | —       | —      | —      |
| RTC       | ✓         | —       | (multi) | —    | —     | —       | —      | —      |
| Watchdog  | ✓         | —       | —       | —    | —     | —       | —      | —      |
| DMA       | ✓         | ✓       | —       | —    | ✓     | —       | —      | —      |
| CAN       | —         | —       | —       | ✓*   | —     | —       | —      | —      |
| PCIe      | —         | —       | —       | ✓    | —     | —       | —      | —      |
| SpaceWire | —         | —       | —       | —    | ✓     | —       | —      | —      |
| OTP       | ✓         | ✓       | —       | —    | —     | —       | —      | —      |

*(multi) = covered by consolidated multi-function server*
*✓* = ZynqMP*
