# Core Libraries Documentation — Outdated Points

## 1. libswdg.md Typo

**Documentation:** Example code shows `swdg_reaload(0)`.

**Current code:** The function is `swdg_reload(0)`.

**Recommendation:** Fix the typo in the example.

---

## 2. libcache.md Unresolved TODOs

**Documentation contains unresolved TODOs:**
- Whether the library is static and precompiled
- Whether `errno` is set on callback failures
- Additional error codes for `deinit` (mentions `EBUSY` as example)
- Whether `invalidate` clears validity bit or just marks invalid

**Recommendation:** Resolve the TODOs based on current implementation.

---

## 3. libvga API Coverage

**Documentation:** Mentions register access functions but doesn't fully document all register fields or the complete API.

**Current code:** Full register access for CRT controller, sequencer, graphics controller, and attribute controller.

**Recommendation:** Complete the API reference or note which functions are internal.

---

## 4. Documentation Coverage Ratio

**Documentation covers:** 7 out of 15 libraries (47%).

**Current code has:** 15 libraries total. The 8 undocumented libraries include critical infrastructure (storage, encryption, partitioning) that have been added between 2017–2025.

**Recommendation:** Prioritize documenting `libptable`, `libstorage`, `libmtd`, and `libtinyaes` as these are critical for embedded system operation.
