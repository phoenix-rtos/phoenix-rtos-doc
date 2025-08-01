# USB stack

Devices running Phoenix-RTOS can act as both sides of USB communication - host and device (client). When acting as a
host, the USB stack is implemented as a server called simply `usb`, which communicates with specific device `drivers`
using messages. Those `drivers` are separate processes and implement class or device specific communication layers.

In order to simplify adding new device drivers `libusb` is used, more precisely functions found in `driver.h` header.
Drivers for specific device classes can be found in the `phoenix-rtos-devices` repository.

When we want Phoenix-RTOS device to act as a device side of the communication, we need to link both `libusb` and
`libusbclient` to our program and no additional server applications are needed. `libusbclient` is responsible for
implementing platform specific details of communicating with USB hardware and is built using `phoenix-rtos-devices`
repository.

The `phoenix-rtos-usb` repository contains two directories, that match two build targets: `libusb` and `usb`.

The source code of the USB host stack and Libusb can be obtained with the following command:

```console
git clone https://github.com/phoenix-rtos/phoenix-rtos-usb.git
```

```{toctree}
:maxdepth: 1

usbhost.md
libusb.md
```
