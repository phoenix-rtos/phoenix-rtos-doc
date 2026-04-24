# LwIP (Networking) Documentation — Undocumented Areas

## 1. Ethernet Interface Configuration

Multiple Ethernet interface drivers exist but are not documented:
- **RTL8139C+**: Realtek NIC (for IA32/PC targets)
- **iMX ENET**: i.MX 6ULL/RT Ethernet (multiple variants)
- **GR740 (greth)**: GRLIB Ethernet (SPARC targets)

Configuration, initialization, and usage of each interface is undocumented.

## 2. PHY Driver Layer

PHY chip drivers with GPIO management:
- **KSZ8081**: Microchip/Micrel PHY
- **KSZ9031**: Gigabit PHY
- **RTL8201**: Realtek 10/100 PHY
- **RTL8211**: Realtek Gigabit PHY

Each requires specific GPIO reset pin and IRQ configuration. Patterns use `/dev/gpioX` filesystem interface.

## 3. Wi-Fi Driver

`wi-fi/` directory contains Wi-Fi interface implementation. No documentation on:
- Supported Wi-Fi chips/modules
- Configuration (SSID, authentication)
- AP vs station mode
- Power management

## 4. IPsec Support

`ipsec/` directory indicates IPsec capability. No documentation on:
- Supported algorithms
- Configuration
- SA (Security Association) management
- Tunnel vs transport mode

## 5. Modem Driver

`modem/` directory for cellular modem connectivity. No documentation on:
- Supported modem types
- AT command handling
- PPP session establishment
- APN configuration

## 6. G3 Driver

`g3/` directory — possibly G3-PLC (Power Line Communication). Purpose and usage completely undocumented.

## 7. Per-Platform Network Configuration

No matrix showing which network interfaces are available per target:
- IA32: RTL8139 Ethernet
- i.MX 6ULL: iMX ENET
- SPARC: GRLIB Ethernet
- ARM Cortex-M: PPPoU over UART (typical)

## 8. IPv6 Configuration Details

Documentation mentions `LWIP_IPV6=1` for dual-stack support but provides no details on:
- IPv6 address assignment
- Neighbor discovery
- Router advertisement handling
- Supported IPv6 features vs limitations

## 9. Socket API Implementation

How LwIP socket API is exposed via the Phoenix-RTOS message passing system is not documented. The bridge between kernel socket syscalls and user-level LwIP implementation is unexplained.

## 10. Network Configuration at Runtime

Beyond `sysexec` and PLO scripts, runtime network configuration (ifconfig applet, DHCP, static IP) workflows are not documented.
