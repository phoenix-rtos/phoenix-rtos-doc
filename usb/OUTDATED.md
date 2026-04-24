# USB Documentation — Outdated Points

## 1. Procdriver Architecture Missing (2024 Addition)

**Documentation:** Assumes single-threaded `msgRecv()` dispatch in drivers.

**Current code:** `libusb/include/usbprocdriver.h` (line 26) provides:
```c
__attribute__((noreturn)) void usb_driverProcRun(usb_driver_t *driver, unsigned int prio, unsigned int nthreads, void *args);
```
Thread-pool based event handling for concurrent insertion/deletion/completion handling. Used by `libusb/procdriver.c` (line 124, calls `usb_hostLookup`).

**Recommendation:** Add a section documenting the procdriver API and threading model.

---

## 2. Message Protocol Outdated

**Documentation:** Documents 5 message types: `connect`, `insertion`, `deletion`, `urb`, `open`.

**Current code (`libusb/include/usbdriver.h` lines 130–137):** 8 message types:
```c
enum { usb_msg_connect, usb_msg_insertion, usb_msg_deletion,
       usb_msg_urb, usb_msg_open, usb_msg_urbcmd,
       usb_msg_completion, usb_msg_devdesc } type;
```
Adds `urbcmd` (URB control: submit/cancel/free), `completion`, and `devdesc` (device descriptor query).

**Recommendation:** Update the message type specification.

---

## 3. Device Info Query API Missing (2025 Addition)

**Documentation:** No mention.

**Current code:** `libusb/include/usbdevinfo.h` (line 22):
```c
int usb_devinfoGet(oid_t oid, usb_devinfo_desc_t *desc);
```
Allows querying device descriptor information via `/dev/usb`. `usb_hostLookup()` (defined in `libusb/internal.c` line 17) provides blocking host discovery, used by both `libusb/devinfo.c` (line 29) and `libusb/procdriver.c` (line 124).

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

**Current code (`usb/hub.c` lines 36–39):**
```c
#define HUB_ENUM_RETRIES     3
#define HUB_DEBOUNCE_STABLE  100000   // 100ms
#define HUB_DEBOUNCE_PERIOD  25000    // 25ms
#define HUB_DEBOUNCE_TIMEOUT 1500000  // 1.5s
```
Reset polling uses 5 retries with 100ms intervals (`hub.c` lines 207–208). Enumeration retries at line 267.

**Recommendation:** Document hub timing behavior for driver developers.

---

## 7. Transfer Completion Oversimplified

**Documentation says:** "synchronous (msgRespond) or asynchronous (event message)."

**Current code:** Full state machine with reference counting, mutex-protected states (idle/ongoing/completed), and condition variables.

**Recommendation:** Document the transfer lifecycle and state management.
