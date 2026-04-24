# LwIP (Networking) — Design Observations

## User-Level Network Server

The network stack runs as a user-level server based on LwIP (Lightweight IP). Socket operations from applications are forwarded via kernel message passing to the LwIP server process. This follows the microkernel philosophy.

## Layered Interface Architecture

```
Application layer (sockets)
  ↓ (message passing)
LwIP server
  ↓
Interface drivers (Ethernet, PPPoU, Wi-Fi, Modem, G3)
  ↓
PHY drivers (KSZ8081, KSZ9031, RTL8201, RTL8211)
  ↓
Hardware
```

Interface drivers are separated from higher-level networking features. PHY management is an independent layer with GPIO-based hardware control.

## Hardware-Aware PHY Management

PHY drivers go beyond simple register access:
- GPIO reset pin control via `/dev/gpioX` filesystem
- IRQ mapping for link status changes
- Platform-specific initialization sequences
- Auto-negotiation support

## Multiple Interface Types

The code supports diverse connectivity:
- **Wired**: Ethernet (RTL8139, iMX ENET, GRLIB)
- **Wireless**: Wi-Fi
- **Serial**: PPPoU (UART-based PPP), Modem (cellular)
- **Specialized**: G3-PLC (potentially powerline)
- **Security**: IPsec

## Per-Target Configuration

`_targets/` directory contains per-SoC optimizations. Network configuration is target-specific, reflecting the different hardware capabilities of each platform:
- MMU targets: full Ethernet + sockets
- Non-MMU targets: typically PPPoU or specialized

## POSIX Socket Bridge

Socket syscalls in the kernel are routed to the LwIP server via message passing. This bridge layer implements the POSIX socket API on top of LwIP's callback-based architecture.
