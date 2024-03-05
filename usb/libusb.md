# libusb

The main purpose of the `libusb` is to generalize access to USB resources and to simplify communication with the USB
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

* [**usb.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/usb.h) - types and constant values
defined by the USB standard, such as descriptors and its fields' values.
* [**usbdriver.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/usbdriver.h) - functions and
types used by USB Device Drivers to communicate with the USB Host Stack, e.g. to register a driver, open a pipe or
schedule a USB transfer.
* [**usbclient.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/usbclient.h) - functions used by
applications, which use the USB device (client) side of communication.
* [**cdc.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/cdc.h) - descriptors and constants
assigned to USB communications device class based on the USB standard. It can be used by both sides of USB
communication.
* [**cdc_client.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/cdc_client.h) - functions used
by applications, that needs to make a Phoenix-RTOS device act as a USB CDC device.
* [**hid.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/hid.h) - descriptors and constants
assigned to USB human interface device based on the USB standard. It can be used by both sides of USB communication.
* [**hid_client.h**](https://github.com/phoenix-rtos/phoenix-rtos-usb/blob/master/libusb/hid_client.h) - functions
used by applications, that needs to make a Phoenix-RTOS device act as a USB HID device.
