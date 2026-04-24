# Core Libraries Documentation — Outdated Points

## 1. libswdg.md Typo

**Documentation:** Example code at `corelibs/libswdg.md` line 78 shows `swdg_reaload(0)`.

**Current code:** The function is `swdg_reload(0)` — see `phoenix-rtos-corelibs/libswdg/swdg.h` line 22 and `swdg.c` line 94.

**Recommendation:** Fix the typo on line 78 from `swdg_reaload(0)` to `swdg_reload(0)`.

---

## 2. libcache.md Unresolved TODOs

**Documentation contains unresolved TODOs at specific lines:**
- Line 5: Whether the library is static and precompiled
- Line 30: Whether `errno` is set on callback failures
- Line 54: Whether `errno` is set on write callback failure
- Line 81: Additional error codes for `deinit` (mentions `EBUSY` as example)

**Source evidence:** `phoenix-rtos-corelibs/libcache/` contains the implementation that can resolve these questions.

**Recommendation:** Resolve the TODOs based on current implementation.

---

## 3. libvga API Coverage

**Documentation (`corelibs/libvga.md`):** Mentions register access functions but doesn't fully document all register fields or the complete API.

**Current code:** `phoenix-rtos-corelibs/libvga/` includes full register access for CRT controller, sequencer, graphics controller, and attribute controller.

**Recommendation:** Complete the API reference or note which functions are internal.

---

## 4. Documentation Coverage Ratio

**Documentation covers:** 7 out of 15 libraries (47%): libcache, libcgi, libgraph, libswdg, libuuid, libvga, libvirtio.

**Current code has:** 15 libraries total in `phoenix-rtos-corelibs/`:
- **Documented:** libcache, libcgi, libgraph, libswdg, libuuid, libvga, libvirtio
- **Undocumented:** libalgo, libmbr, libmodbus, libmtd, libptable, libstorage, libtinyaes, libtrace

The 8 undocumented libraries include critical infrastructure (storage, encryption, partitioning).

**Recommendation:** Prioritize documenting `libptable`, `libstorage`, `libmtd`, and `libtinyaes` as these are critical for embedded system operation.
