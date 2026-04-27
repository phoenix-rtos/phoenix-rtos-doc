# Network Interfaces

This section describes the Ethernet and other network interface drivers available in the Phoenix-RTOS network stack.

## Ethernet Drivers

Three Ethernet MAC drivers are included in `phoenix-rtos-lwip/drivers/`:

### RTL8139C+ (IA32)

Source: `drivers/rtl8139cp.c`, `drivers/rtl8139cp-regs.h`

Realtek RTL8139C+ PCI Ethernet NIC driver. Used on IA32 targets (PC hardware and QEMU).

### i.MX ENET (ARM)

Source: `drivers/imx-enet.c`, `drivers/imx-enet-regs.h`

NXP i.MX Ethernet controller driver. Used on i.MX 6ULL and i.MX RT targets.

### GRLIB Ethernet (SPARC)

Source: `drivers/greth.c`, `drivers/greth-regs.h`

GRLIB Ethernet MAC driver. Used on SPARC targets (GR716, GR712RC, GR740, GR765).

## PHY Driver Layer

PHY management is handled by `drivers/ephy.c`, which supports the following Ethernet PHY chips:

| PHY Chip | Type | Selection |
|---|---|---|
| KSZ8081 (RNA, RNB, RND) | 10/100 | `EPHY_KSZ8081` Makefile variable |
| KSZ9031MNX | Gigabit | Link speed detection |
| RTL8201 | 10/100 | Page-based register access |
| RTL8211 | Gigabit | Extended page selection |

Each PHY requires:

- A GPIO reset pin configured via the `/dev/gpioX` filesystem interface
- An IRQ mapping for link status change notifications

The PHY variant is selected at build time via the `EPHY_KSZ8081` variable in `drivers/Makefile`.

## Wi-Fi

Source: `wi-fi/`

The Wi-Fi interface driver uses the Wireless Host Driver (WHD) architecture:

- `wi-fi/hal/`  -  hardware abstraction
- `wi-fi/lwip/`  -  LwIP integration
- `wi-fi/whd/`  -  Wireless Host Driver

## Cellular Modem

Source: `modem/`

Three cellular modem vendor drivers are available:

- `modem/esp8266/`  -  Espressif ESP8266 Wi-Fi module
- `modem/huawei/`  -  Huawei cellular modem
- `modem/quectel/`  -  Quectel cellular modem

Modem drivers typically establish PPP sessions over AT command interfaces.

## IPsec

Source: `ipsec/`

IPsec support includes AES encryption and Authentication Header (AH) processing.

## G3-PLC

Source: `g3/`

G3-PLC (Power Line Communication) support for communication over electrical wiring. Configuration options are defined
in `g3_opts.h`.
