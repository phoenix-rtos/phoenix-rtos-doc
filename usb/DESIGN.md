# USB — Design Observations

## Architecture Evolution

- **Original (2021 docs)**: Single-threaded, message-per-operation model
- **Current (2024 code)**: Hybrid system supporting both linked library drivers (synchronous) and process drivers (IPC with thread pools)

The procdriver introduction (2024) is a paradigm shift that replaces manual message handling with automatic thread pool spawning for concurrent event processing.

## Two Driver Initialization Paths

### Linked Library Path (Internal)
```
usb_internalDriverInit() → usb_libDrvInit() → direct function calls
```
Synchronous, no IPC overhead. Hub driver uses this path.

### Process Driver Path (IPC)
```
usb_connect() → message registration → usb_driverProcRun() → thread pool
```
Asynchronous, enables fault isolation. External class drivers use this path.

## Transfer Submission Duality

### Internal (library drivers):
```
usb_transferSubmit(t, pipe, cond) → hcd->ops->transferEnqueue() → condWait()
```
Blocking, synchronous completion.

### External (process drivers):
```
URB message → usb_handleUrb() → hcd->ops->transferEnqueue() → completion message
```
Non-blocking, asynchronous completion via thread pool.

## Address Allocation Strategy

Bitmap-based address pool: `uint32_t addrmask[4]` (`usb/hcd.h` line 58, 128 addresses). O(1) allocation using `__builtin_ffsl()` (`usb/hcd.c` line 49). Initial mask `0x1` reserves address 0 (line 125). Efficient for USB 2.0's 127-device limit.

## Hub Enumeration Robustness

Hardware-aware debounce logic (`usb/hub.c` lines 36–39):
- 1.5s maximum debounce timeout (`HUB_DEBOUNCE_TIMEOUT`)
- 100ms required stability window (`HUB_DEBOUNCE_STABLE`)
- 25ms sampling period (`HUB_DEBOUNCE_PERIOD`)
- 3 enumeration retry attempts on failure (`HUB_ENUM_RETRIES`)
- Additional reset polling: 5 retries × 100ms (lines 207–208)

## Implicit Device Tree

USB devices form a tree via parent-child hub relationships:
```
Root Hub
  ├── Device (port 1)
  ├── Hub (port 2)
  │   ├── Device (port 1)
  │   └── Device (port 2)
  └── Device (port 3)
```

No explicit tree data structure — relationships tracked via pointers in `usb_dev_t`.

## Single Configuration Assumption

Code allocates and processes only one `usb_configuration_desc_t` per device. Multi-configuration USB devices (rare in practice) may not be fully supported. This is likely an intentional embedded simplification.
