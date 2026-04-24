# LwIP (Networking) Documentation — Outdated Points

## 1. PPPoU Emphasis vs Ethernet Reality

**Documentation (`lwip/lwip-pppou.md`):** Focuses primarily on PPPoU (PPP over UART) for IoT connectivity.

**Current code:** Ethernet is the primary interface. Multiple Ethernet drivers exist in `phoenix-rtos-lwip/drivers/`:
- `rtl8139cp.c` — Realtek RTL8139C+ NIC (IA32/PC targets)
- `imx-enet.c` — i.MX 6ULL/RT Ethernet (with `imx-enet-regs.h`)
- `greth.c` — GRLIB Ethernet (SPARC targets, with `greth-regs.h`)

PHY handling includes dedicated driver code in `drivers/ephy.c` with KSZ8081 variants (RNA, RNB, RND) selected via `EPHY_KSZ8081` Makefile variable (drivers/Makefile lines 3–10).

**Recommendation:** Rebalance the documentation to reflect Ethernet as the primary use case, with PPPoU as a secondary/specialized scenario.

---

## 2. PHY Configuration Complexity Missing

**Documentation:** Does not mention PHY management.

**Current code:** `phoenix-rtos-lwip/drivers/ephy.c` implements sophisticated PHY support:
- KSZ8081-specific registers (line 50): Digital Reserved Control, AFE Control, RXER Counter
- GPIO reset pin configuration via `/dev/gpioX` naming
- IRQ mapping for link status changes

**Recommendation:** Document PHY configuration requirements for Ethernet-based targets.

---

## 3. Missing Driver Directories

**Current code shows additional directories in `phoenix-rtos-lwip/`:**
- `ipsec/` — IPsec support (contains `aes.c`, `ah.c` and more)
- `wi-fi/` — Wi-Fi driver (contains `hal/`, `lwip/`, `whd/` subdirectories)
- `modem/` — Cellular modem drivers (subdirectories: `esp8266/`, `huawei/`, `quectel/`)
- `g3/` — G3-PLC powerline communication (contains `g3_opts.h`, `g3plc.h`)

None of these are mentioned in documentation.

**Recommendation:** At minimum, list available network interface types and their status.
