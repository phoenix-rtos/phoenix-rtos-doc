# Ports Documentation — Outdated Points

## 1. Port List Generation Timing

**Documentation says:** Port list is "automatically generated."

**Current state:** Update frequency and timing of generation is not specified. Users cannot determine if the list reflects the latest available ports.

**Recommendation:** Add a timestamp or version reference to the generated port list.

---

## 2. OpenSSL Version Conflict

**Current code:** `phoenix-rtos-ports/openssl111/port.def.sh` line 21 declares `conflicts="openssl3>=0.0"`. An `openssl/` directory exists containing only a tarball (`openssl-1.1.1a.tar.gz`) with no `port.def.sh`. No `openssl3` port directory exists yet.

**Documentation:** Does not mention the OpenSSL version situation.

**Recommendation:** Document the openssl111 port and its declared conflict with the future openssl3. Clarify that the `openssl/` directory is a legacy artifact without a proper port definition.

---

## 3. Actual Port Count

**Current code:** 25 ports have `port.def.sh` files in `phoenix-rtos-ports/`: azure_sdk, busybox, coremark, coremark_pro, coreMQTT, curl, dropbear, fs_mark, heatshrink, jansson, libevent, lighttpd, lua, lzo, mbedtls, micropython, openiked, openssl111, openvpn, pcre, picocom, smolrtsp, sscep, wpa_supplicant, zlib. Additional directories without port definitions: joe, libpng, lsb_vsx, openssl, x11.

**Documentation:** Does not state the total number of available ports.

**Recommendation:** Include a count or summary of available port categories.
