# LwIP (Networking) Documentation — Undocumented Areas

## 1. Ethernet Interface Configuration

Multiple Ethernet interface drivers in `phoenix-rtos-lwip/drivers/` are not documented:
- **RTL8139C+**: `rtl8139cp.c` + `rtl8139cp-regs.h` — Realtek NIC (for IA32/PC targets)
- **iMX ENET**: `imx-enet.c` + `imx-enet-regs.h` — i.MX 6ULL/RT Ethernet
- **GRLIB greth**: `greth.c` + `greth-regs.h` — GRLIB Ethernet (SPARC targets)
- Physical memory mapping support: `physmmap.c` / `physmmap.h`

Configuration, initialization, and usage of each interface is undocumented.

## 2. PHY Driver Layer

PHY chip drivers in `phoenix-rtos-lwip/drivers/ephy.c`:
- **KSZ8081**: Microchip/Micrel PHY — variants RNA, RNB, RND (selected via `EPHY_KSZ8081` build variable, `drivers/Makefile` lines 3–10). Registers at line 50.
- **KSZ9031MNX**: Microchip Gigabit PHY — registers at line 113, link speed detection at line 319
- **RTL8201**: Realtek 10/100 PHY — registers at line 69, page-based register access
- **RTL8211**: Realtek Gigabit PHY — registers at line 89, extended page selection

Each requires specific GPIO reset pin and IRQ configuration via `/dev/gpioX` filesystem interface.

## 3. Wi-Fi Driver

`phoenix-rtos-lwip/wi-fi/` directory contains Wi-Fi interface implementation with subdirectories:
- `hal/` — hardware abstraction
- `lwip/` — LwIP integration
- `whd/` — Wireless Host Driver

No documentation on supported chips, configuration, AP vs station mode, or power management.

## 4. IPsec Support

`phoenix-rtos-lwip/ipsec/` directory contains IPsec implementation files including `aes.c`, `ah.c`. No documentation on supported algorithms, configuration, SA management, or tunnel vs transport mode.

## 5. Modem Driver

`phoenix-rtos-lwip/modem/` directory with three modem vendor subdirectories:
- `esp8266/` — Espressif ESP8266 Wi-Fi module
- `huawei/` — Huawei cellular modem
- `quectel/` — Quectel cellular modem

No documentation on AT command handling, PPP session establishment, or APN configuration.

## 6. G3-PLC Driver

`phoenix-rtos-lwip/g3/` directory — G3-PLC (Power Line Communication). Contains `g3_opts.h` and `g3plc.h`. Purpose, configuration, and usage completely undocumented.

## 7. Per-Platform Network Configuration

No matrix showing which network interfaces are available per target:
- IA32: RTL8139C+ Ethernet (`rtl8139cp.c`)
- i.MX 6ULL: iMX ENET (`imx-enet.c`)
- SPARC: GRLIB Ethernet (`greth.c`)
- ARM Cortex-M: Typically PPPoU over UART

Target-specific configuration in `phoenix-rtos-lwip/_targets/`.

## 8. IPv6 Configuration Details

Documentation mentions `LWIP_IPV6=1` for dual-stack support but provides no details on IPv6 address assignment, neighbor discovery, router advertisement handling, or supported IPv6 features vs limitations.

## 9. Socket API Implementation

How LwIP socket API is exposed via the Phoenix-RTOS message passing system is not documented. The bridge between kernel socket syscalls (in `phoenix-rtos-kernel/syscalls.c`) and user-level LwIP implementation is unexplained.

## 10. Network Configuration at Runtime

Beyond PLO scripts, runtime network configuration (ifconfig applet in PSH, DHCP, static IP) workflows are not documented.
