# Ports Documentation — Outdated Points

## 1. Port List Generation Timing

**Documentation says:** Port list is "automatically generated."

**Current state:** Update frequency and timing of generation is not specified. Users cannot determine if the list reflects the latest available ports.

**Recommendation:** Add a timestamp or version reference to the generated port list.

---

## 2. OpenSSL Version Conflict Not Documented

**Current code:** `openssl` and `openssl3` exist as separate ports with conflicts declared between `openssl` and `openssl111`.

**Documentation:** Does not mention the OpenSSL version situation or migration path.

**Recommendation:** Document OpenSSL version choices and conflict implications.

---

## 3. Actual Port Count Not Mentioned

**Current code:** 30+ ports available (azure_sdk, busybox, coreMQTT, curl, dropbear, lua, micropython, openssl, zlib, libpng, etc.).

**Documentation:** Does not state the total number of available ports.

**Recommendation:** Include a count or summary of available port categories.
