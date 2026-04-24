# USB Documentation — Undocumented Areas

## 1. Procdriver API (2024)

Thread-pool based event handling system:
```c
void usb_driverProcRun(usb_driver_t *driver, int priority, int nthreads, void *args);
```
- Spawns thread pool for concurrent message handling
- Handles insertion/deletion/completion events in parallel
- Does not return (noreturn semantics)
- Replaces manual `msgRecv()` loops in drivers

## 2. Device Info Query API (2025)

Query device descriptor information via `/dev/usb`:
```c
int usb_devinfoGet(oid_t usboid, usb_devinfo_desc_t *desc);
```
- `usb_hostLookup(oid_t*)` — blocks until `/dev/usb` is available
- Retry loop for USB host availability
- Returns full device descriptor data

## 3. URB Control Commands (2024)

New message type `usb_msg_urbcmd` with three operations:
- `urbcmd_submit` — submit URB for processing
- `urbcmd_cancel` — cancel pending URB
- `urbcmd_free` — free URB resources

## 4. Hub Interrupt Handling

- `hub_interrupt()` function for status change detection
- Status change endpoint polling mechanism
- Debounce state machine (1.5s timeout, 100ms stability, 25ms sampling, 3 retries)

## 5. Driver Binding Algorithm

"Most specific match wins" with precedence order:
1. PID/VID match (most specific)
2. Device class match
3. Subclass match
4. Protocol match (least specific)

Algorithm details and tie-breaking rules are not documented.

## 6. Device Address Allocation

Bitmap-based address pool using `uint32_t addrmask[4]` (128 addresses):
- O(1) allocation via `__builtin_ffsl()` (find first set bit)
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
