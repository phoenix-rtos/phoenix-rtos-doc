# USB documentation outdated points

No open outdated points remain after the current source audit.

## Resolved in this update

| Former item | Current documentation |
| --- | --- |
| Procdriver architecture | `libusb.md` documents startup, worker pools, handlers, and `noreturn` behavior. |
| Message protocol | `usbhost.md` documents all eight `usb_msg_t` message types and their payloads. |
| Device info query API | `libusb.md` documents `usb_devinfoGet()` and blocking host lookup. |
| Hybrid driver architecture | `usbhost.md` and `DESIGN.md` document linked library drivers and process drivers. |
| HCD device tree status | `usbhost.md` documents static HCD registration and no device tree discovery path. |
| Hub timing constants | `usbhost.md` documents debounce, enumeration retry, and reset polling timing. |
| Transfer completion | `usbhost.md` documents URB states, references, completions, and control commands. |

## Verification

The current pass checked these source areas:

- `phoenix-rtos-usb/libusb/include/usbdriver.h`
- `phoenix-rtos-usb/libusb/include/usbprocdriver.h`
- `phoenix-rtos-usb/libusb/include/usbdevinfo.h`
- `phoenix-rtos-usb/libusb/procdriver.c`
- `phoenix-rtos-usb/libusb/devinfo.c`
- `phoenix-rtos-usb/libusb/internal.c`
- `phoenix-rtos-usb/libusb/driver.c`
- `phoenix-rtos-usb/usb/hcd.h`
- `phoenix-rtos-usb/usb/hub.h`
- `phoenix-rtos-usb/usb/dev.h`
- `phoenix-rtos-usb/usb/usbhost.h`
- `phoenix-rtos-usb/usb/hcd.c`
- `phoenix-rtos-usb/usb/hub.c`
- `phoenix-rtos-usb/usb/dev.c`
- `phoenix-rtos-usb/usb/drv.c`
- `phoenix-rtos-usb/usb/usb.c`
