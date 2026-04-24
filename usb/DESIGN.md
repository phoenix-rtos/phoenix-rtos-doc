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

Bitmap-based address pool: `uint32_t addrmask[4]` (128 addresses). O(1) allocation using `__builtin_ffsl()` (find first set bit). Efficient for USB 2.0's 127-device limit.

## Hub Enumeration Robustness

Hardware-aware debounce logic:
- 1.5s maximum debounce timeout
- 100ms required stability window
- 25ms sampling period
- 3 enumeration retry attempts on failure

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
