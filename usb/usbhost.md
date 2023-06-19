# USB Host stack

The USB Host stack server - `usb` provides the generic core functionality, including abstraction of Host Controller
Device, managing devices enumeration and communication with device drivers. The USB Host stack is accessible to other
processes through a port `/dev/usb`.

## Host Controller Devices

The USB Host stack allows using different types and multiple instances of HCDs. It provides generic types `hcd_t` and
`hcd_ops_t`. Specific drivers for different types of HCDs such as `ehci`, `ohci` etc. are a part of the
`phoenix-rtos-devices` repository in the form of a static library named, e.g. `libusbehci`. When building the USB Host
stack, one should set the environmental variable `USB_HCD_LIBS` to an appropriate value denoting host controllers
available on the platform. Each Host Controller driver library should register its `hcd_ops_t` instance using a GCC
constructor. It allows the USB Host stack to communicate with an HCD driver using callbacks within a `hcd_ops_t`
structure.

The USB Host stack during initialization first fetches the platform-dependent information on the available HCD instances
using `hcd_info_t` structure. (At this moment it is done using `hcd_getInfo()` function. In the future it should be done
using a device tree.) Then it matches instances with previously registered HCD ops and creates `hcd_t` instances, with
which it would then communicate in terms of scheduling transfers and detecting devices connection/disconnection.

## Hubs

Hubs are the basis of the USB devices tree. Each HCD has its own Root Hub with at least one port. Both Root Hubs and
additional physical hub devices are managed using the hub driver, which is the only USB class driver implemented as a
part of the USB stack, while other USB classes are implemented as separate processes. The hub driver is responsible for
managing port status changes, e.g. devices connection or disconnection. When a new device is connected the hub module
performs the enumeration process and binds a device with appropriate drivers. On the device disconnection, it shall
unbind a device from drivers, destroy a device and all its resources.

## Drivers

Drivers are separate processes, which communicate with the Host stack using messages and are represented in the USB Host
stack as `usb_drv_t` instances. A driver first registers itself using a `connect` USB message (implemented in `libusb`
as `usb_connect()` function). It then waits for events such as `insertion` or `deletion` sent by the USB Host stack.
`insertion` message is sent, once the USB Host stack binds the newly connected device to a particular driver. A device
can be a composite device containing multiple interfaces. Each interface can be bound to a different driver.
A `insertion` message is sent for every interface separately. It works the same with `deletion` messages.

Drivers are bound to interfaces after matching device or interface descriptors with driver filters described by one or
many `usb_device_id_t` structures. An array of those structures is provided to the USB Host stack, when registering a
driver using `usb_connect()` function. It consists of the following fields (from most specific to most general):

- `pid` (product ID)
- `vid` (vendor ID)
- `protocol`
- `subclass`
- `dclass` (device class)

Each of those fields can have a fixed value or a wildcard value `USBDRV_ANY`. An interface can match multiple drivers,
but the host stack shall choose the most *specific* one to bind the interface to. For example, it shall prefer a driver,
which matches `pid` and `vid` fields over a driver that matches `dclass` and `subclass` fields.

It's the driver's responsibility to create ports in order to give other processes access to resources of a particular
device, e.g. `/dev/umass0`, `/dev/umass1`, `/dev/usbacm0`, etc.

## Pipes

Pipes are a software abstraction of a USB endpoint. Drivers communicate with specific endpoints using pipes. A pipe is
characterized with a direction (in or out) and type (control, bulk, interrupt isochronous). A device driver first
**opens** a pipe by sending a USB `open` message (implemented in `libusb` as `usb_open()` function). A driver gives
details on a pipe it requests to open. If the USB Host stack finds an endpoint on a given device interface with given
direction and type, it creates a pipe, allocates a `id` unique in the context of the driver and returns the ID to the
driver. The driver can then send transfers using this pipe ID. A pipe ID can be thought as a UN*X-like file
descriptors - it is a key to communicate with a specific endpoint.

A driver writes or reads data using a pipe by sending `urb` messages. The USB Host stack schedules a transfer on a
corresponding Host Controller Device, once it processes a `urb`. It then informs a driver, that a transfer has been
finished either in a synchronous way (calling `msgRespond()` to the `urb` message - bulk and control transfers) or
asynchronous (a new event message - interrupt and isochronous message).
