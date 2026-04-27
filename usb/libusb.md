# Libusb

The main purpose of `libusb` is to generalize access to USB resources and to simplify communication with the USB
Host Stack. It also provides definitions of generic types used by both USB device drivers, USB Host Stack and USB client
applications.

## Examples

Host side device drivers:

* [USB Mass Storage class driver](https://github.com/phoenix-rtos/phoenix-rtos-devices/blob/master/storage/umass/umass.c)
* [USB CDC ACM class driver](https://github.com/phoenix-rtos/phoenix-rtos-devices/blob/master/tty/usbacm/usbacm.c)

Client side applications:

* [USB CDC test application](https://github.com/phoenix-rtos/phoenix-rtos-devices/blob/master/usb/cdc-demo/cdc-demo.c)
* [PSD](https://github.com/phoenix-rtos/phoenix-rtos-utils/tree/master/core/psd)

## Headers

* [**usb.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usb.h)  -  types and constant
values defined by the USB standard, such as descriptors and their field values.
* [**usbdriver.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbdriver.h)  -  functions
and types used by USB device drivers to communicate with the USB Host Stack, e.g. to register a driver, open a pipe or
schedule a USB transfer. Defines 8 message types: `usb_msg_connect`, `usb_msg_insertion`, `usb_msg_deletion`,
`usb_msg_urb`, `usb_msg_open`, `usb_msg_urbcmd`, `usb_msg_completion`, `usb_msg_devdesc`.
* [**usbprocdriver.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbprocdriver.h)  - 
thread-pool based process driver API. Provides `usb_driverProcRun()` for automatic concurrent event handling, replacing
manual `msgRecv()` loops.
* [**usbdevinfo.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbdevinfo.h)  -  device
descriptor query API. Provides `usb_devinfoGet()` for querying device information via `/dev/usb` and `usb_hostLookup()`
for blocking host discovery.
* [**usbclient.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/usbclient.h)  -  functions
used by applications which use the USB device (client) side of communication.
* [**cdc.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/cdc.h)  -  descriptors and
constants assigned to USB communications device class based on the USB standard. It can be used by both sides of USB
communication.
* [**cdc_client.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/cdc_client.h)  - 
functions used by applications that need to make a Phoenix-RTOS device act as a USB CDC device.
* [**hid.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/hid.h)  -  descriptors and
constants assigned to USB human interface device based on the USB standard. It can be used by both sides of USB
communication.
* [**hid_client.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/include/hid_client.h)  - 
functions used by applications that need to make a Phoenix-RTOS device act as a USB HID device.
