# VirtIO library (libvirtio)

`libvirtio` provides common VirtIO device discovery, feature negotiation, configuration access, and split virtqueue
helpers for Phoenix-RTOS drivers.

The public interface is declared in `<virtio.h>`. The implementation supports PCI devices through the platform PCI
backend and direct memory-mapped I/O (MMIO) devices described by the caller.

## Device and queue types

`virtio_devtype_t`
: Device transport type.

  | Value | Meaning |
  | --- | --- |
  | `vdevNONE` | No VirtIO device. |
  | `vdevPCI` | VirtIO PCI device. |
  | `vdevMMIO` | VirtIO MMIO device. |

`virtio_devinfo_t`
: Device location and transport registers. It stores transport type, device ID, interrupt number, notification
  multiplier, and register ranges for base, notification, interrupt status, and configuration areas.

`virtio_dev_t`
: Initialized device context. It stores `virtio_devinfo_t` and the negotiated feature bits.

`virtio_ctx_t`
: Discovery context passed between `virtio_find()` calls. Set `reset` before the first scan to clear iteration state.

`virtio_req_t`
: Request descriptor list passed to `virtqueue_enqueue()`.

  `rsegs` counts device-readable segments. `wsegs` counts device-writable segments. The first segment in `segs` is the
  head of a doubly linked list of `virtio_seg_t` objects.

`virtqueue_t`
: Split virtqueue state. The library allocates descriptor, available-ring, used-ring, and event areas in uncached
  contiguous memory and protects queue state with a mutex and condition variable.

## Device model helpers

````{function} virtio_legacy(vdev)
Tests whether a device uses the legacy VirtIO interface.

:param vdev: Initialized VirtIO device.
:returns: Non-zero when bit `32` is clear in `vdev->features`.
````

````{function} virtio_modern(vdev)
Tests whether a device uses the modern VirtIO interface.

:param vdev: Initialized VirtIO device.
:returns: Non-zero when `virtio_legacy(vdev)` is false.
````

````{function} virtio_mb()
Issues a compiler memory barrier used around VirtIO register and ring updates.

:returns: Nothing.
````

````{function} virtio_vtog16(vdev, val)
Converts a 16-bit VirtIO value to guest byte order.

:param vdev: VirtIO device used to select legacy or modern byte-order rules.
:param val: Value read from the device.
:returns: Converted value.
````

````{function} virtio_vtog32(vdev, val)
Converts a 32-bit VirtIO value to guest byte order.

:param vdev: VirtIO device used to select legacy or modern byte-order rules.
:param val: Value read from the device.
:returns: Converted value.
````

````{function} virtio_vtog64(vdev, val)
Converts a 64-bit VirtIO value to guest byte order.

:param vdev: VirtIO device used to select legacy or modern byte-order rules.
:param val: Value read from the device.
:returns: Converted value.
````

````{function} virtio_gtov16(vdev, val)
Converts a 16-bit guest value to VirtIO byte order.

:param vdev: VirtIO device used to select legacy or modern byte-order rules.
:param val: Guest value.
:returns: Converted value.
````

````{function} virtio_gtov32(vdev, val)
Converts a 32-bit guest value to VirtIO byte order.

:param vdev: VirtIO device used to select legacy or modern byte-order rules.
:param val: Guest value.
:returns: Converted value.
````

````{function} virtio_gtov64(vdev, val)
Converts a 64-bit guest value to VirtIO byte order.

:param vdev: VirtIO device used to select legacy or modern byte-order rules.
:param val: Guest value.
:returns: Converted value.
````

## Library and device lifecycle

````{function} virtio_init()
Initializes the library.

The current implementation has no global setup work.

:returns: `EOK`.
````

````{function} virtio_done()
Destroys global library state.

The current implementation has no global teardown work.

:returns: Nothing.
````

````{function} virtio_find(info, vdev, vctx)
Finds the next VirtIO device that matches the descriptor in `info`.

For PCI devices, the call is delegated to the PCI backend. For MMIO, a non-zero `info->base.len` describes one direct
device. MMIO bus enumeration is not implemented.

:param info: Device descriptor with transport type and optional expected device ID.
:param vdev: Output device context. On success, `vdev->info` is populated from `info` or the discovered PCI device.
:param vctx: Discovery context. Set `vctx->reset` before the first scan.
:returns: `EOK` when a matching device is found or a negative error such as `-ENODEV`.
````

````{function} virtio_initDev(vdev)
Maps transport registers, resets the device, sets ACKNOWLEDGE and DRIVER status bits, and reads device features.

For MMIO devices, the function maps the register range with `MAP_DEVICE`, `MAP_UNCACHED`, `MAP_PHYSMEM`, and
`MAP_ANONYMOUS`.

:param vdev: Device context returned by `virtio_find()`.
:returns: `EOK` on success, `-ENOMEM` when register mapping fails, `-ENODEV` when the device signature or ID does not
  match, `-ENOTSUP` for an unsupported MMIO version, `-EFAULT` for an invalid legacy/modern state, or a negative PCI
  backend error.
````

````{function} virtio_destroyDev(vdev)
Releases transport resources for a device initialized with `virtio_initDev()`.

:param vdev: Initialized device context.
:returns: Nothing.
````

````{function} virtio_reset(vdev)
Writes `0` to the device status register.

For modern PCI devices, the function waits until the device reports status `0`.

:param vdev: Initialized device context.
:returns: Nothing.
````

## Configuration and status

````{function} virtio_readConfig8(vdev, reg)
Reads an 8-bit value from device configuration space.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:returns: Register value.
````

````{function} virtio_readConfig16(vdev, reg)
Reads a 16-bit value from device configuration space.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:returns: Register value.
````

````{function} virtio_readConfig32(vdev, reg)
Reads a 32-bit value from device configuration space.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:returns: Register value.
````

````{function} virtio_readConfig64(vdev, reg)
Reads a stable 64-bit value from device configuration space.

For modern devices, the function repeats the read until the configuration generation value is unchanged.
For legacy devices, it repeats the 64-bit read until two consecutive values match.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:returns: Register value.
````

````{function} virtio_writeConfig8(vdev, reg, val)
Writes an 8-bit value to device configuration space.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:param val: Value to write.
:returns: Nothing.
````

````{function} virtio_writeConfig16(vdev, reg, val)
Writes a 16-bit value to device configuration space.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:param val: Value to write.
:returns: Nothing.
````

````{function} virtio_writeConfig32(vdev, reg, val)
Writes a 32-bit value to device configuration space.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:param val: Value to write.
:returns: Nothing.
````

````{function} virtio_writeConfig64(vdev, reg, val)
Writes a 64-bit value to device configuration space.

:param vdev: Initialized device context.
:param reg: Device-specific configuration register offset.
:param val: Value to write.
:returns: Nothing.
````

````{function} virtio_readFeatures(vdev)
Returns the feature bits stored in the device context.

:param vdev: Initialized device context.
:returns: Negotiated feature mask stored in `vdev->features`.
````

````{function} virtio_writeFeatures(vdev, features)
Negotiates the driver-supported feature mask with the device.

The function intersects `features` with the device feature mask and preserves the modern-device bit. For modern
devices, it sets the FEATURES_OK status bit and verifies that the device accepted it.

:param vdev: Initialized device context.
:param features: Driver-supported feature mask.
:returns: `EOK` on success or `-ENOTSUP` when a modern device rejects the negotiated feature set.
````

````{function} virtio_readStatus(vdev)
Reads the device status register.

:param vdev: Initialized device context.
:returns: Current status value.
````

````{function} virtio_writeStatus(vdev, status)
Writes the device status register and issues a memory barrier.

:param vdev: Initialized device context.
:param status: Status bits to write.
:returns: Nothing.
````

````{function} virtio_isr(vdev)
Reads the interrupt status register.

For MMIO devices, the function also writes the read value to the interrupt acknowledge register.

:param vdev: Initialized device context.
:returns: Interrupt status bits.
````

## Virtqueue operations

````{function} virtqueue_init(vdev, vq, idx, size)
Initializes a split virtqueue and activates it in the device.

`size` must be a non-zero power of two that fits in 16 bits. The negotiated queue size can be lower than the requested
size if the device exposes a smaller queue.

:param vdev: Initialized device context.
:param vq: Virtqueue object supplied by the caller.
:param idx: Queue index.
:param size: Requested queue size.
:returns: `EOK` on success, `-EINVAL` for an invalid index or size, `-ENOENT` when the device does not expose the
  queue, `-EFAULT` when queue activation does not stick, `-ENOMEM` on allocation failure, or a negative synchronization
  primitive error.
````

````{function} virtqueue_destroy(vdev, vq)
Destroys synchronization objects, unmaps queue memory, and frees descriptor buffer tracking.

:param vdev: Initialized device context.
:param vq: Virtqueue initialized by `virtqueue_init()`.
:returns: Nothing.
````

````{function} virtqueue_enqueue(vdev, vq, req)
Adds a request descriptor chain to the available ring.

The function waits until enough free descriptors are available. Device-readable segments are placed first, followed by
device-writable segments.

:param vdev: Initialized device context.
:param vq: Initialized virtqueue.
:param req: Request with linked segments and segment counts.
:returns: `EOK` on success, `-EINVAL` when the request has no segments, or `-ENOSPC` when the request needs more
  descriptors than the queue size.
````

````{function} virtqueue_dequeue(vdev, vq, len)
Reads one processed request from the used ring.

The function returns the head buffer pointer stored when the request was enqueued and releases the descriptor chain
back to the free list.

:param vdev: Initialized device context.
:param vq: Initialized virtqueue.
:param len: Optional output for the number of bytes written by the device.
:returns: Head buffer pointer for a processed request, or `NULL` when no request is ready.
````

````{function} virtqueue_notify(vdev, vq)
Notifies the device that new descriptors are available unless notification suppression is set in the used ring.

:param vdev: Initialized device context.
:param vq: Initialized virtqueue.
:returns: Nothing.
````

````{function} virtqueue_enableIRQ(vdev, vq)
Clears the available-ring interrupt suppression flag.

:param vdev: Initialized device context.
:param vq: Initialized virtqueue.
:returns: Nothing.
````

````{function} virtqueue_disableIRQ(vdev, vq)
Sets the available-ring interrupt suppression flag.

:param vdev: Initialized device context.
:param vq: Initialized virtqueue.
:returns: Nothing.
````