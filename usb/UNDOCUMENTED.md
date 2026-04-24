# USB Documentation — Undocumented Areas

## 1. Procdriver API (2024)

Thread-pool based event handling system (`libusb/include/usbprocdriver.h` line 26):
```c
__attribute__((noreturn)) void usb_driverProcRun(usb_driver_t *driver, unsigned int prio, unsigned int nthreads, void *args);
```
- Spawns thread pool for concurrent message handling
- Handles insertion/deletion/completion events in parallel
- `noreturn` semantics
- Replaces manual `msgRecv()` loops in drivers
- Uses `usb_hostLookup()` internally (`libusb/procdriver.c` line 124)

## 2. Device Info Query API (2025)

Query device descriptor information via `/dev/usb` (`libusb/include/usbdevinfo.h` line 22):
```c
int usb_devinfoGet(oid_t oid, usb_devinfo_desc_t *desc);
```
- `usb_hostLookup(oid_t*)` (`libusb/internal.c` line 17) — blocks until `/dev/usb` is available
- Used by `libusb/devinfo.c` (line 29) and `libusb/procdriver.c` (line 124)
- Returns full device descriptor data

## 3. URB Control Commands (2024)

New message type `usb_msg_urbcmd` with three operations:
- `urbcmd_submit` — submit URB for processing
- `urbcmd_cancel` — cancel pending URB
- `urbcmd_free` — free URB resources

## 4. Hub Interrupt Handling

- `hub_interrupt()` function for status change detection
- Status change endpoint polling mechanism
- Debounce state machine (`usb/hub.c` lines 36–39): 1.5s timeout (`HUB_DEBOUNCE_TIMEOUT`), 100ms stability (`HUB_DEBOUNCE_STABLE`), 25ms sampling (`HUB_DEBOUNCE_PERIOD`), 3 enumeration retries (`HUB_ENUM_RETRIES`)
- Reset polling: 5 retries × 100ms (lines 207–208)

## 5. Driver Binding Algorithm

"Most specific match wins" with precedence order:
1. PID/VID match (most specific)
2. Device class match
3. Subclass match
4. Protocol match (least specific)

Algorithm details and tie-breaking rules are not documented.

## 6. Device Address Allocation

Bitmap-based address pool using `uint32_t addrmask[4]` (`usb/hcd.h` line 58, 128 addresses):
- O(1) allocation via `__builtin_ffsl()` (`usb/hcd.c` line 49)
- Bit set on allocation (line 57), cleared on release (line 65)
- Initial mask `0x1` reserves address 0 (line 125)
- USB 2.0 limit: 127 device addresses

## 7. Port Status Flags

16 port status/change flags defined in `hub.h`:
- Connection, enable, suspend, overcurrent, reset, power status
- Corresponding change bits for each status
- Feature codes for port operations

## 8. Device Speed Detection

```c
enum usb_speed { full_speed, low_speed, high_speed };
```
Bus enumeration detects and stores device speed. Not mentioned in documentation.

## 9. String Descriptor Language Support

Devices cache language ID (`uint16_t langId`) for multilingual string fetches. Separate `usb_lenStr_t` wrapper structure for manufacturer, product, and serial number strings.

## 10. HCD Callback Interface

```c
typedef struct hcd_ops {
    const char type[HCD_TYPE_LEN];
    int (*init)(struct hcd*);
    int (*transferEnqueue)(struct hcd*, usb_transfer_t*, usb_pipe_t*);
    void (*transferDequeue)(struct hcd*, usb_transfer_t*);
    void (*pipeDestroy)(struct hcd*, usb_pipe_t*);
    uint32_t (*getRoothubStatus)(usb_dev_t*);
} hcd_ops_t;
```
Interface is used but not documented. HCD implementers need this reference.

## 11. Configuration Limitations

Code allocates a single `usb_configuration_desc_t` per device. Multi-configuration devices may not be fully supported.

## 12. Hub Tree Structure

Parent-child relationship for USB device tree:
```c
struct _usb_dev {
    struct _usb_dev *hub;    // Parent hub
    struct _usb_dev **devs;  // Children (for hubs)
    int port;                // Port on parent
    int nports;              // Total ports (if hub)
};
```
