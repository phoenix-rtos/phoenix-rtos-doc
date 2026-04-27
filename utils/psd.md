# Phoenix Serial Downloader (psd)

The Phoenix Serial Downloader implements the SDP (Serial Download Protocol) used by NXP microcontrollers for booting
and flash memory management. It allows for direct communication with the device's flash memory, facilitating firmware
updates, partition management, and device configuration. PSD supports operations on various NXP platforms, including
i.MX 6ULL and i.MX RT.

## Supported Platforms

- i.MX 6ULL
- i.MX RT106x
- i.MX RT117x

## Functionality

PSD acts as a USB device that responds to SDP commands from the host computer's `psu` tool. It provides:

- Flash memory read and write operations
- Partition table management
- Firmware image flashing
- Device register access

## Usage

PSD is typically started from a PLO boot script or from the Phoenix-RTOS shell. It registers as a USB device and
waits for commands from the host-side `psu` tool.

For host-side usage, see the [psu documentation](../hostutils/psu.md).
