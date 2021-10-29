# libusb
The main purpose of the `libusb` is to generalize access to USB resources and to simplify communication with the USB Host Stack. It also provides definitions of generic types used by both USB device driver, USB Host Stack and USB client applications.

## usb.h
This header contains definitions of types and constant values defined by the USB standard, such as descriptors and its fields' values.

## cdc.h
This header contains definitions of descriptors and constants assigned to USB communications device class based on the USB standard. It can be used by both sides of USB communication.

## hid.h
This header contains definitions of descriptors and constants assigned to USB human interface device based on the USB standard. It can be used by both sides of USB communication.

## usbdriver.h
This header contains declarations of functions and definitions of types used by USB Device Drivers to communicate with the USB Host Stack, e.g. to register a driver, open a pipe or schedule a USB transfer.

## usbclient.h
This header contains declarations of functions used by applications, which use the USB device (client) side of communication.

## cdc_client.h
This header contains declarations of functions used by application, that needs to make a Phoenix-RTOS device act as a USB CDC device.

## hid_client.h
This header contains declarations of functions used by application, that needs to make a Phoenix-RTOS device act as a USB HID device.
