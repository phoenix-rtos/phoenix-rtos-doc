# USB Documentation — Outdated Points

## 1. Procdriver Architecture Missing (2024 Addition)

**Documentation:** Assumes single-threaded `msgRecv()` dispatch in drivers.

**Current code (2024):** New `usbprocdriver.h` provides thread-pool based event handling via `usb_driverProcRun(driver, prio, nthreads, args)`. This supports concurrent insertion/deletion/completion handling.

**Recommendation:** Add a section documenting the procdriver API and threading model.

---

## 2. Message Protocol Outdated

**Documentation:** Documents 5 message types: `connect`, `insertion`, `deletion`, `urb`, `open`.

**Current code:** 8 message types — adds `urbcmd` (URB control: submit/cancel/free), `completion`, and `devdesc` (device descriptor query).

**Recommendation:** Update the message type specification.

---

## 3. Device Info Query API Missing (2025 Addition)

**Documentation:** No mention.

**Current code:** `usb_devinfoGet(oid_t, usb_devinfo_desc_t*)` allows querying device descriptor information via `/dev/usb`. Includes `usb_hostLookup()` for blocking host discovery.

**Recommendation:** Document the device info query API.

---

## 4. Hybrid Driver Architecture Not Explained

**Documentation:** Describes a single driver registration method via `usb_connect()`.

**Current code:** Two distinct paths:
- **Linked library drivers**: `usb_internalDriverInit()` + `usb_libDrvInit()` — synchronous, direct function calls
- **Process drivers**: `usb_connect()` via IPC — asynchronous with thread pools

**Recommendation:** Clarify both driver initialization paths.

---

## 5. HCD Device Tree Still Not Implemented

**Documentation says:** "future: device tree" for HCD enumeration.

**Current code:** Still uses `hcd_getInfo()` function with static per-platform registration via GCC constructors. No device tree support.

**Recommendation:** Update the status of device tree support.

---

## 6. Hub Timing Constants Undocumented

**Current code reveals critical timing:**
- Debounce stable: 100ms
- Debounce sampling: 25ms
- Debounce timeout: 1.5s
- Enumeration retries: 3

**Recommendation:** Document hub timing behavior for driver developers.

---

## 7. Transfer Completion Oversimplified

**Documentation says:** "synchronous (msgRespond) or asynchronous (event message)."

**Current code:** Full state machine with reference counting, mutex-protected states (idle/ongoing/completed), and condition variables.

**Recommendation:** Document the transfer lifecycle and state management.
