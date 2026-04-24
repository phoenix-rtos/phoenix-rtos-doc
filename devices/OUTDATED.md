# Devices Documentation — Outdated Points

## 1. Only 2 Specific Drivers Documented

**Documentation:** Only `libsdio` and `simsensors` have dedicated documentation pages.

**Current code:** 60+ device drivers/servers across 15+ categories (ADC, CAN, Display, DMA, GPIO, I2C, Magnetometer, RTC, SDIO, Sensors, SPI, Storage/Flash, TTY/UART, USB, Watchdog, SpaceWire, Temperature, PCIe, OTP, Multi-function).

**Recommendation:** At minimum, add an inventory of all driver categories and drivers to the index page.

---

## 2. Hardware Access Examples Omit Modern Platforms

**Documentation (`hwaccess.md`):** Examples focus on older platforms.

**Current code:** RISC-V (Spike), STM32, MCXn94x, and many other modern platforms have distinct hardware access patterns not covered in examples.

**Recommendation:** Update `hwaccess.md` with examples from RISC-V and ARMv8 platforms.

---

## 3. libsdio Limitation Statement

**Documentation:** States "only one library instance per system" and "no multiple SDIO device support."

**Current code:** This is an implementation limitation, not an architectural constraint. The documentation should distinguish between current limitations and design limitations.

**Recommendation:** Clarify this as a current implementation limitation.

---

## 4. Port Registration Example Oversimplified

**Documentation (`interface.md`):** Shows basic single-port registration.

**Current code:** Modern drivers use complex patterns — multi-port servers, device folder hierarchies (e.g., GPIO creates `/dev/gpioN/port` + `/dev/gpioN/dir`), and multi-function consolidated servers.

**Recommendation:** Add examples showing multi-port registration, device folder hierarchies, and the multi-function server pattern.
