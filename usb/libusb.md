# Libusb

The main purpose of `libusb` is to generalize access to USB resources and to simplify communication with the USB
Host Stack. It also provides definitions of generic types used by both USB device drivers, USB Host Stack and USB client
applications.

## Examples

Host side device drivers:

* USB Mass Storage class driver:
	[umass.c](https://github.com/phoenix-rtos/phoenix-rtos-devices/blob/master/storage/umass/umass.c)
* [USB CDC ACM class driver](https://github.com/phoenix-rtos/phoenix-rtos-devices/blob/master/tty/usbacm/usbacm.c)

Client side applications:

* [USB CDC test application](https://github.com/phoenix-rtos/phoenix-rtos-devices/blob/master/usb/cdc-demo/cdc-demo.c)
* [PSD](https://github.com/phoenix-rtos/phoenix-rtos-utils/tree/master/core/psd)

## Headers

* [**usb.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usb.h) - types and constant
values defined by the USB standard, such as descriptors and their field values.
* [**usbdriver.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbdriver.h) - functions
and types used by USB device drivers to communicate with the USB Host Stack, e.g. to register a driver, open a pipe or
schedule a USB transfer. Defines 8 message types: `usb_msg_connect`, `usb_msg_insertion`, `usb_msg_deletion`,
`usb_msg_urb`, `usb_msg_open`, `usb_msg_urbcmd`, `usb_msg_completion`, `usb_msg_devdesc`.
* [**usbprocdriver.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbprocdriver.h) -
thread-pool based process driver API. Provides `usb_driverProcRun()` for automatic concurrent event handling, replacing
manual `msgRecv()` loops.
* [**usbdevinfo.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbdevinfo.h) - device
descriptor query API. Provides `usb_devinfoGet()` for querying device information via `/dev/usb` and `usb_hostLookup()`
for blocking host discovery.
* [**usbclient.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbclient.h) - functions
used by applications which use the USB device (client) side of communication.
* [**cdc.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/cdc.h) - descriptors and
constants assigned to USB communications device class based on the USB standard. It can be used by both sides of USB
communication.
* [**cdc_client.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/cdc_client.h) -
functions used by applications that need to make a Phoenix-RTOS device act as a USB CDC device.
* [**hid.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/hid.h) - descriptors and
constants assigned to USB human interface device based on the USB standard. It can be used by both sides of USB
communication.
* [**hid_client.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/hid_client.h) -
functions used by applications that need to make a Phoenix-RTOS device act as a USB HID device.

## Process driver API

`usbprocdriver.h` provides `usb_driverProcRun()` for process drivers.
The function initializes the driver, discovers the USB host server, registers the driver, creates a driver port, and
spawns a worker pool for insertion, deletion, and completion messages.
It does not return.

Drivers provide handlers through `usb_driver_t.handlers`:

| Handler | Input | Effect |
| --- | --- | --- |
| `insertion` | `usb_devinfo_t` | Creates device resources and can return `usb_event_insertion_t`. |
| `deletion` | `usb_deletion_t` | Removes resources for a detached device or interface. |
| `completion` | `usb_completion_t` and optional data buffer | Handles asynchronous URB completion. |

## Device info API

`usb_devinfoGet(oid_t oid, usb_devinfo_desc_t *desc)` queries the USB host server for descriptor information.
The helper blocks in `usb_hostLookup()` until `/dev/usb` or `devfs/usb` is available.
It returns a negative error from `msgSend()` or from the host response, and returns `0` on success.

`usb_devinfo_desc_t` contains the device descriptor and bounded manufacturer, product, and serial-number strings.

## Modeswitch helpers

`usb_modeswitchFind()` searches an array of `usb_modeswitch_t` entries by vendor ID and product ID.
`usb_modeswitchHandle()` opens control, bulk IN, and bulk OUT pipes, sets configuration `1`, and sends the mode switch
message over the bulk OUT pipe.
It returns `0` on success and `-EINVAL` on open, configuration, or transfer failure.
