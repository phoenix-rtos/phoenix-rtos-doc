# USB design observations

## Architecture evolution

- Linked library drivers run inside the USB host process and call host stack functions directly.
- Process drivers communicate with the host through IPC and use `usb_driverProcRun()` for event dispatch.

The process driver helper initializes the driver, waits for `/dev/usb` or `devfs/usb`, creates a driver port, registers
the driver, and starts the worker pool. It then enters the same worker loop in the caller thread and does not return.

## Two driver initialization paths

### Linked library path

```
usb_internalDriverInit() -> usb_libDrvInit() -> direct function calls
```

The hub driver uses this path.
Completion paths can wait on condition variables inside the host process.

### Process driver path

```
usb_connect() -> message registration -> usb_driverProcRun() -> worker pool
```

External class drivers use this path.
The worker loop handles insertion, deletion, and completion messages.

## Transfer submission paths

### Internal library drivers

```
usb_transferSubmit(t, pipe, cond) -> hcd->ops->transferEnqueue() -> condWait()
```

Internal transfers use a caller-provided condition variable for synchronous completion.

### Process drivers

```
URB message -> usb_handleUrb() -> hcd->ops->transferEnqueue() -> completion message
```

Process-driver transfers use URB IDs, `urbcmd_submit`, `urbcmd_cancel`, and `urbcmd_free` messages.
Completion is reported through `usb_msg_completion`.

## Address allocation strategy

Each HCD stores address ownership in `uint32_t addrmask[4]`.
The allocation path uses `__builtin_ffsl()` to select the first free bit.
The initial mask reserves address 0, leaving the USB address range 1 through 127 for devices.

## Hub enumeration timing

The hub code uses fixed timing constants during connection handling:

- 1.5s maximum debounce timeout (`HUB_DEBOUNCE_TIMEOUT`)
- 100ms required stability window (`HUB_DEBOUNCE_STABLE`)
- 25ms sampling period (`HUB_DEBOUNCE_PERIOD`)
- 3 enumeration retry attempts on failure (`HUB_ENUM_RETRIES`)
- Additional reset polling with 5 retries at 100 ms intervals

## USB device tree

USB devices form a tree through parent and child pointers:

```
Root Hub
  ├── Device (port 1)
  ├── Hub (port 2)
  │   ├── Device (port 1)
  │   └── Device (port 2)
  └── Device (port 3)
```

The relevant fields in `usb_dev_t` are `hub`, `devs`, `port`, and `nports`.

## Single configuration assumption

The current enumeration path allocates and processes one `usb_configuration_desc_t` per device.
The source contains a `TODO` for devices with multiple configurations.
