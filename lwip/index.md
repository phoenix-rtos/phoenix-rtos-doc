# Network stack

This chapter describes the Phoenix-RTOS network stack. After reading this chapter, you will know:

- The available network interface types (Ethernet, PPP, Wi-Fi, cellular modem, G3-PLC).
- How to configure Ethernet interfaces and PHY drivers.
- How PPP over UART connectivity works for IoT scenarios.
- Which network interfaces are available per target platform.

The Phoenix-RTOS network stack is based on LwIP. Following the microkernel architecture philosophy, it runs as a
user-level server and provides a socket interface. Sockets are implemented using the native Phoenix-RTOS message passing
mechanism and are placed in the `libphoenix` library. The network stack communicates with hardware via
[Device Drivers](../devices/index.md) and uses kernel [Message passing](../kernel/proc/msg.md) for client requests.

## Network Interface Types

The network server supports several interface types:

| Interface | Directory | Description |
|---|---|---|
| Ethernet | `drivers/` | Wired Ethernet with MAC and PHY support |
| PPP over UART | `pppos/` | Point-to-point link over serial (IoT, embedded) |
| Wi-Fi | `wi-fi/` | Wireless LAN (Wireless Host Driver) |
| Cellular modem | `modem/` | Cellular connectivity (ESP8266, Huawei, Quectel) |
| IPsec | `ipsec/` | IPsec VPN support |
| G3-PLC | `g3/` | G3 Power Line Communication |

## Per-Platform Network Interfaces

| Target | Primary Interface | Driver |
|---|---|---|
| IA32 (PC/QEMU) | RTL8139C+ Ethernet | `drivers/rtl8139cp.c` |
| i.MX 6ULL | iMX ENET | `drivers/imx-enet.c` |
| SPARC (GRLIB) | GRLIB greth | `drivers/greth.c` |
| ARM Cortex-M | PPP over UART | `pppos/` |

```{toctree}
:maxdepth: 1

lwip-interfaces.md
lwip-pppou.md
```
