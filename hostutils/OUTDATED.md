# Host Utilities Documentation — Outdated Points

## 1. Missing `-t` (TCP) Option in phoenixd Synopsis

**Documentation (`hostutils/phoenixd.md`):** The synopsis line omits `-t tcp_ip_addr:port` from the usage.

**Current code:** `phoenix-rtos-hostutils/phoenixd/phoenixd.c` line 93 shows TCP option in usage string: `"\t\t-t tcp_ip_addr:port"`. Lines 219–222 handle the `-t` option identically to `-i` (UDP), setting `mode[i] = TCP`.

**Recommendation:** Add `-t tcp_ip_addr[:port]` to the documented synopsis and argument table.

---

## 2. psu Documentation Is Stub

**Documentation (`hostutils/psu.md`):** Contains only a placeholder `<!-- #TODO: add more information -->`.

**Current code:** Full SDP and MCUBoot protocol implementation with scripting support. `phoenix-rtos-hostutils/psu/README.md` contains detailed script syntax documentation including:
- `WAIT <vid> <pid>` — wait for HID device
- `WRITE_FILE F/S <path> [address] [format] [offset] [size]` — file transfer
- `WRITE_REGISTER <address> <value>` — register write

**Recommendation:** Expand `psu.md` incorporating content from the source's `psu/README.md`.

---

## 3. psdisk Implicit Modes Not Documented

**Documentation (`hostutils/psdisk.md`):** Describes `-m`, `-p`, `-r` options but does not explain the three implicit modes.

**Current code:** `phoenix-rtos-hostutils/psdisk/psdisk.c` lines 51–53 define three modes via preprocessor macros:
- **CREATE_IMG**: File doesn't exist + memory declared + partitions declared (line 555)
- **UPDATE_IMG**: File exists + memory declared + partitions/removals (line 565)
- **READ_IMG**: File exists + memory declared + no partition operations (line 574)

**Recommendation:** Document the three operational modes explicitly.

---

## 4. phoenixd Max Instance Limit

**Documentation:** Does not mention any limitation.

**Current code:** `phoenix-rtos-hostutils/phoenixd/phoenixd.c` lines 198–223 enforce a hard limit of 8 concurrent instances for all transport modes (serial `-p`, UDP `-i`, TCP `-t`, USB `-u`). Exceeding prints "Too many instances" and breaks.

**Recommendation:** Document the 8-instance limit.
