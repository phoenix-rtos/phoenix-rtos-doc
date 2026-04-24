# Devices Documentation — Outdated Points

## 1. Only 2 Specific Drivers Documented

**Documentation:** Only `libsdio` and `simsensors` have dedicated documentation pages in `devices/`.

**Current code:** `phoenix-rtos-devices/` contains 21 driver categories: adc, can, display, dma, gpio, i2c, libklog, libpseudodev, librtt, mag, multi, otp, pcie, rtc, sdio, sensors, spacewire, spi, storage, temp, tty, usb, watchdog. Plus 4 consolidated multi-function servers in `multi/`: grlib-multi, imxrt-multi, mcxn94x-multi, stm32l4-multi. Over 60 individual driver implementations total.

**Recommendation:** At minimum, add an inventory of all driver categories and drivers to the index page.

---

## 2. Hardware Access Examples Omit Modern Platforms

**Documentation (`hwaccess.md`):** Examples focus on older platforms.

**Current code:** RISC-V (Spike) drivers in `tty/spike-tty/`, ARM CMSDK UART in `tty/cmsdk-apbuart/`, GRLIB drivers in `multi/grlib-multi/`, and MCXn94x multi-function server in `multi/mcxn94x-multi/` demonstrate modern platform patterns not covered in examples.

**Recommendation:** Update `hwaccess.md` with examples from RISC-V and ARMv8 platforms.

---

## 3. libsdio Limitation Statement

**Documentation (`devices/libsdio.md`, line 19):** States "only one library instance per system" and line 21: "no support for multiple SDIO devices."

**Current code:** This is an implementation limitation in `phoenix-rtos-devices/sdio/`, not an architectural constraint. The documentation should distinguish between current limitations and design limitations.

**Recommendation:** Clarify this as a current implementation limitation.

---

## 4. Port Registration Example Oversimplified

**Documentation (`interface.md`):** Shows basic single-port registration.

**Current code:** Modern drivers use complex patterns:
- Multi-port servers with device folder hierarchies (e.g., GPIO creates `/dev/gpioN/port` + `/dev/gpioN/dir` — see `phoenix-rtos-devices/gpio/imx6ull-gpio/`)
- Consolidated multi-function servers routing via `mtDevCtl` with union messages (see `phoenix-rtos-devices/multi/stm32l4-multi/`)
- Device driver libraries shared across platforms (e.g., `libtty/` used by all UART drivers)

**Recommendation:** Add examples showing multi-port registration, device folder hierarchies, and the multi-function server pattern.
