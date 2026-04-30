# USB documentation undocumented areas

No open undocumented points remain after the current source audit.

## Resolved in this update

| Former item | Current documentation |
| --- | --- |
| Procdriver API | `libusb.md` documents startup, thread pool creation, worker messages, and stack size. |
| Device info query API | `libusb.md` documents `usb_devinfoGet()`, output data, lookup blocking, and error returns. |
| URB control commands | `usbhost.md` documents `submit`, `cancel`, and `free` handling in the transfer lifecycle. |
| Hub interrupt handling | `usbhost.md` documents status transfer allocation, submission, and notification. |
| Driver binding algorithm | `usbhost.md` documents match fields, class fallback, numerical score, and tie behavior. |
| Device address allocation | `usbhost.md` documents `addrmask[4]`, address 0 reservation, and first-free allocation. |
| Port status flags | `usbhost.md` documents status bits, change bits, speed bits, and feature codes. |
| Device speed detection | `usbhost.md` documents the `usb_speed` values and storage in `usb_dev_t.speed`. |
| String descriptor language support | `usbhost.md` documents language ID, cached strings, and fallback strings. |
| HCD callback interface | `usbhost.md` documents `hcd_ops_t` callbacks and their effects. |
| Configuration limitations | `usbhost.md` documents the first-configuration limitation and source TODO. |
| Hub tree structure | `usbhost.md` documents parent hub pointers, child arrays, port number, and port count. |
| Modeswitch helpers | `libusb.md` documents `usb_modeswitchFind()` and `usb_modeswitchHandle()`. |

## Verification

The current pass checked the USB host server, `libusb` headers, `libusb` process-driver implementation, and class-driver
support helpers in `phoenix-rtos-usb`.
