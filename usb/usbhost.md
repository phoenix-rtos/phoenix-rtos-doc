# USB Host stack

This chapter covers the USB Host stack server's internal architecture: Host Controller Device management, USB device enumeration, driver communication, and data transfers.

The USB Host stack server - `usb` - provides the generic core functionality, including abstraction of Host Controller
Devices, managing device enumeration, hub management, and communication with device drivers. The USB Host stack is
accessible to other processes through a port registered at `/dev/usb`.

## Host Controller Devices

The USB Host stack allows using different types and multiple instances of HCDs. It provides generic types `hcd_t` and
`hcd_ops_t`. Specific drivers for different types of HCDs such as `ehci`, `ohci` etc. are a part of the
`phoenix-rtos-devices` repository in the form of a static library named, e.g. `libusbehci`. When building the USB Host
stack, one should set the environmental variable `USB_HCD_LIBS` to an appropriate value denoting host controllers
available on the platform. Each Host Controller driver library should register its `hcd_ops_t` instance using a GCC
constructor. It allows the USB Host stack to communicate with an HCD driver using callbacks within a `hcd_ops_t`
structure.

The HCD callback interface consists of:

- `init` - initialize the host controller
- `transferEnqueue` - submit a transfer for processing
- `transferDequeue` - cancel a queued transfer
- `pipeDestroy` - destroy a pipe and free resources
- `getRoothubStatus` - read the root hub port status

The USB Host stack during initialization first fetches the platform-dependent information on the available HCD instances
using `hcd_info_t` structure via the `hcd_getInfo()` function. It then matches instances with previously registered HCD
ops and creates `hcd_t` instances, with which it communicates in terms of scheduling transfers and detecting device
connection/disconnection.

```{note}
Device tree-based HCD enumeration is not currently implemented. The `hcd_getInfo()` function with static
per-platform registration via GCC constructors is the only supported method.
```

## Hubs

Hubs are the basis of the USB device tree. Each HCD has its own Root Hub with at least one port. Both Root Hubs and
additional physical hub devices are managed using the hub driver, which is the only USB class driver implemented as a
part of the USB stack (as a linked library driver), while other USB classes are implemented as separate processes.

The hub driver is responsible for managing port status changes, e.g. device connection or disconnection. When a new
device is connected the hub module performs the enumeration process and binds a device with appropriate drivers. On
device disconnection, it unbinds a device from drivers and destroys the device and all its resources.

### Enumeration Timing

Hub enumeration uses the following timing parameters (defined in `usb/hub.c`):

| Parameter | Value | Purpose |
|---|---|---|
| `HUB_DEBOUNCE_TIMEOUT` | 1500 ms | Maximum time to wait for connection to stabilize |
| `HUB_DEBOUNCE_STABLE` | 100 ms | Required stable time before accepting a connection |
| `HUB_DEBOUNCE_PERIOD` | 25 ms | Sampling interval during debounce |
| `HUB_ENUM_RETRIES` | 3 | Number of enumeration retry attempts on failure |

After connection is detected, the hub resets the port and polls for reset completion with up to 5 retries at 100 ms
intervals.

### Device Address Allocation

Each device on the USB bus requires a unique address (1-127, per USB 2.0 specification). The USB Host stack allocates
addresses using a bitmap-based pool: `uint32_t addrmask[4]` in the `hcd_t` structure (128 bits total). Address 0 is
reserved for device enumeration. Allocation uses `__builtin_ffsl()` for O(1) lookup of the first available address.

## Message Protocol

Drivers communicate with the USB Host stack using a message-based protocol. The following message types are defined in
`libusb/include/usbdriver.h`:

| Message Type | Purpose |
|---|---|
| `usb_msg_connect` | Register a driver with the Host stack |
| `usb_msg_insertion` | Notify a driver that a matching device was connected |
| `usb_msg_deletion` | Notify a driver that a device was disconnected |
| `usb_msg_urb` | Submit a USB Request Block (data transfer) |
| `usb_msg_open` | Open a pipe to a specific endpoint |
| `usb_msg_urbcmd` | URB control operations: submit, cancel, or free |
| `usb_msg_completion` | Transfer completion notification |
| `usb_msg_devdesc` | Query device descriptor information |

## Drivers

Drivers are separate processes, which communicate with the Host stack using messages and are represented in the USB Host
stack as `usb_drv_t` instances.

### Driver Registration

A driver first registers itself using a `usb_msg_connect` message (implemented in `libusb`
as `usb_connect()` function). It then waits for events such as `usb_msg_insertion` or `usb_msg_deletion` sent by the
USB Host stack.

An `usb_msg_insertion` message is sent once the USB Host stack binds the newly connected device to a particular driver.
A device can be a composite device containing multiple interfaces. Each interface can be bound to a different driver.
An `usb_msg_insertion` message is sent for every interface separately. It works the same with `usb_msg_deletion`
messages.

### Driver Binding

Drivers are bound to interfaces after matching device or interface descriptors with driver filters described by one or
many `usb_device_id_t` structures. An array of those structures is provided to the USB Host stack, when registering a
driver using `usb_connect()` function. It consists of the following fields (from most specific to most general):

- `pid` (product ID)
- `vid` (vendor ID)
- `protocol`
- `subclass`
- `dclass` (device class)

Each of those fields can have a fixed value or a wildcard value `USBDRV_ANY`. An interface can match multiple drivers,
but the host stack chooses the most *specific* one to bind the interface to. The precedence order is:

1. PID/VID match (most specific)
2. Device class match
3. Subclass match
4. Protocol match (least specific)

It is the driver's responsibility to create ports to give other processes access to resources of a particular
device, e.g. `/dev/umass0`, `/dev/umass1`, `/dev/usbacm0`, etc.

### Two Driver Models

The USB subsystem supports two distinct driver architectures:

**Linked library drivers** are compiled directly into the USB Host stack. They communicate using direct function calls
with no IPC overhead. The hub driver uses this path:

```
usb_internalDriverInit() -> usb_libDrvInit() -> direct function calls
```

**Process drivers** are separate processes that communicate with the USB Host stack via IPC messages. They provide fault
isolation and use thread pools for concurrent event processing:

```
usb_connect() -> message registration -> usb_driverProcRun() -> thread pool
```

#### Process Driver API

The process driver API is defined in `libusb/include/usbprocdriver.h`. The main entry point is:

```c
__attribute__((noreturn)) void usb_driverProcRun(usb_driver_t *driver,
    unsigned int prio, unsigned int nthreads, void *args);
```

This function spawns a thread pool of `nthreads` threads at priority `prio`. The threads handle `usb_msg_insertion`,
`usb_msg_deletion`, and `usb_msg_completion` events concurrently. This function does not return.

The process driver initialization sequence is:

1. Call `usb_hostLookup()` to discover `/dev/usb` (blocks until the Host stack is available).
2. Register the driver using `usb_connect()`.
3. Call `usb_driverProcRun()` to enter the event processing loop.

#### Device Info Query

Drivers and applications can query USB device descriptor information using the device info API defined in
`libusb/include/usbdevinfo.h`:

```c
int usb_devinfoGet(oid_t oid, usb_devinfo_desc_t *desc);
```

The function blocks until `/dev/usb` becomes available, making it safe to call early in
process startup before the USB Host stack has finished initialization.

## Pipes

Pipes are a software abstraction of a USB endpoint. Drivers communicate with specific endpoints using pipes. A pipe is
characterized by a direction (in or out) and a type (control, bulk, interrupt, or isochronous). A device driver first
**opens** a pipe by sending a `usb_msg_open` message (implemented in `libusb` as `usb_open()` function). A driver gives
details on a pipe it requests to open. If the USB Host stack finds an endpoint on a given device interface with given
direction and type, it creates a pipe, allocates an `id` unique in the context of the driver and returns the ID to the
driver. The driver can then send transfers using this pipe ID. A pipe ID can be thought of as a UNIX-like file
descriptor - it is a key to communicate with a specific endpoint.

## Transfers

A driver writes or reads data using a pipe by sending `usb_msg_urb` messages. The USB Host stack schedules a transfer
on a corresponding Host Controller Device once it processes a URB.

The transfer model differs between the two driver architectures:

**Linked library drivers** use synchronous transfers:

```
usb_transferSubmit(t, pipe, cond) -> hcd->ops->transferEnqueue() -> condWait()
```

The calling thread blocks until the transfer completes.

**Process drivers** use asynchronous transfers:

```
usb_msg_urb message -> usb_handleUrb() -> hcd->ops->transferEnqueue() -> usb_msg_completion message
```

The driver's thread pool receives a `usb_msg_completion` message when the transfer finishes.

In addition to `usb_msg_urb`, process drivers can use `usb_msg_urbcmd` messages for fine-grained control:

- `urbcmd_submit` - submit a URB for processing
- `urbcmd_cancel` - cancel a pending URB
- `urbcmd_free` - free URB resources

Transfers are managed with a state machine using reference counting, mutex-protected states
(idle/ongoing/completed), and condition variables.
