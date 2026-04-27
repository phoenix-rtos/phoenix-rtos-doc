# USB stack

This chapter describes the Phoenix-RTOS USB subsystem. After reading this chapter, you will know:

- How the USB Host stack enumerates devices and manages hubs.
- The two driver models: linked library drivers and process drivers.
- The USB message protocol and its message types.
- How to use `libusb` to write USB device drivers.
- How Phoenix-RTOS can act as a USB device using `libusbclient`.

Devices running Phoenix-RTOS can act as both sides of USB communication  -  host and device (client). When acting as a
host, the USB stack is implemented as a server called `usb`, which communicates with specific device `drivers`
using messages. Those `drivers` are separate processes and implement class or device specific communication layers.

To simplify adding new device drivers, `libusb` is used  -  more precisely, functions found in the `usbdriver.h` and
`usbprocdriver.h` headers. The `usbprocdriver.h` header provides a thread-pool based event handling model that replaces
manual message loops. Drivers for specific device classes can be found in the `phoenix-rtos-devices` repository.

When a Phoenix-RTOS device acts as a device side of the communication, both `libusb` and `libusbclient` must be linked
to the program. No additional server applications are needed. `libusbclient` is responsible for implementing
platform-specific details of communicating with USB hardware and is built using the `phoenix-rtos-devices` repository.

USB drivers follow the general device driver model; see [Device Drivers](../devices/index.md).

The `phoenix-rtos-usb` repository contains two directories that match two build targets: `libusb` and `usb`.

```{toctree}
:maxdepth: 1

usbhost.md
libusb.md
```
