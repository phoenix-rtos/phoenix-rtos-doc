# Host Utilities Documentation — Outdated Points

## 1. Missing `-t` (TCP) Option in phoenixd Synopsis

**Documentation:** The synopsis line omits `-t tcp_ip_addr:port` from the usage.

**Current code:** `phoenixd.c` parses `-t` via `getopt_long` for TCP connection mode, identical to `-i` (UDP) handling.

**Recommendation:** Add `-t tcp_ip_addr[:port]` to the documented synopsis and argument table.

---

## 2. psu Documentation Is Stub

**Documentation:** Contains only a placeholder `<!-- #TODO: add more information -->`.

**Current code:** Full SDP and MCUBoot protocol implementation with scripting support:
- `WRITE_REGISTER`, `WRITE_FILE`, `WAIT` script commands
- HID device communication with 1024-byte max payload
- Progress reporting during file transfers
- Special register addresses for PSD control (-1 = CHANGE_PARTITION, -2 = ERASE, -5 = CONTROL_BLOCK, -6 = BLOW_FUSES, -100 = CLOSE_PSD)

**Recommendation:** Expand psu.md with full command reference. The source's `psu/README.md` already contains detailed information that should be reflected in the official docs.

---

## 3. psdisk Implicit Modes Not Documented

**Documentation:** Describes `-m`, `-p`, `-r` options but does not explain the three implicit modes.

**Current code:** `psdisk.c` selects mode based on option combination:
- **CREATE_IMG**: File doesn't exist + memory declared + partitions declared
- **UPDATE_IMG**: File exists + memory declared + partitions/removals
- **READ_IMG**: File exists + memory declared + no partition operations

**Recommendation:** Document the three operational modes explicitly.

---

## 4. phoenixd Max Instance Limit

**Documentation:** Does not mention any limitation.

**Current code:** Hard-limited to 8 concurrent instances (serial/pipe/UDP/TCP/USB).

**Recommendation:** Document the 8-instance limit.
