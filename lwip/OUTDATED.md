# LwIP (Networking) Documentation — Outdated Points

## 1. PPPoU Emphasis vs Ethernet Reality

**Documentation:** Focuses primarily on PPPoU (PPP over UART) for IoT connectivity.

**Current code:** Ethernet is the primary interface. Multiple Ethernet drivers exist: RTL8139C+, iMX ENET, GR740 (greth). PHY handling includes detailed GPIO reset/IRQ configurations.

**Recommendation:** Rebalance the documentation to reflect Ethernet as the primary use case, with PPPoU as a secondary/specialized scenario.

---

## 2. PHY Configuration Complexity Missing

**Documentation:** Does not mention PHY management.

**Current code:** Sophisticated PHY driver support:
- PHY chips: KSZ8081, KSZ9031, RTL8201, RTL8211
- GPIO reset pin configuration
- IRQ mapping patterns
- Uses `/dev/gpioX` naming for hardware-agnostic control

**Recommendation:** Document PHY configuration requirements for Ethernet-based targets.

---

## 3. Missing Driver Directories

**Current code shows additional capabilities:**
- `ipsec/` — IPsec support
- `wi-fi/` — Wi-Fi driver
- `modem/` — Modem driver
- `g3/` — Possibly G3-PLC powerline communication

None of these are mentioned in documentation.

**Recommendation:** At minimum, list available network interface types and their status.
