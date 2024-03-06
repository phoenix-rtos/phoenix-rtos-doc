# VirtIO library (libvirtio)

`libvirtio` provides an abstraction layer for working with `VirtIO` devices. `VirtIO` is a standard dedicated to provide
a common device API (e.g. network and mass storage adapters) for virtualized execution environment.

## Contents

- [General information](#general-information)
- [libvirtio interface](#libvirtio-interface)
  - [Device and Queue Management](#device-and-queue-management)
  - [Data Exchange](#data-exchange)
  - [Configuration and Status](#configuration-and-status)
  - [Utility](#utility)
  - [Memory Barriers](#memory-barriers)
  - [Data Structures](#data-structures)
- [Using libvirtio](#using-libvirtio)
- [Running tests](#running-tests)

## General information

The library offers a set of functionalities for `VirtIO` device initialization, configuration, data exchange, and
cleanup. It supports both legacy and modern `VirtIO` device models, offering compatibility with various device types
including network (virtio-net) and block devices (virtio-blk). The library uses condition variables and mutexes
(handle_t) to ensure thread-safe interactions with `VirtIO` devices and queues.

## libvirtio interface

### Device and Queue Management

- `virtio_initDev` - Initializes a `VirtIO` device.

```c
int virtio_initDev(virtio_dev_t *vdev)
```

- `virtio_destroyDev` - Cleans up resources associated with a `VirtIO` device.

```c
void virtio_destroyDev(virtio_dev_t *vdev)
```

- `virtqueue_init` - Initializes a `VirtIO` queue.

```c
int virtqueue_init(virtio_dev_t *vdev, virtqueue_t *vq, unsigned int idx, unsigned int size)
```

- `virtqueue_destroy` - Cleans up resources associated with a `VirtIO` queue.

```c
void virtqueue_destroy(virtio_dev_t *vdev, virtqueue_t *vq)
```

### Data Exchange

- `virtqueue_enqueue` - Enqueues a request in a `VirtIO` queue for processing by the device.

```c
int virtqueue_enqueue(virtio_dev_t *vdev, virtqueue_t *vq, virtio_req_t *req)
```

- `virtqueue_dequeue` - Dequeues a processed request from a `VirtIO` queue.

```c
void *virtqueue_dequeue(virtio_dev_t *vdev, virtqueue_t *vq, unsigned int *len)
```

- `virtqueue_notify` - Notifies the device that there are available requests in the queue.

```c
void virtqueue_notify(virtio_dev_t *vdev, virtqueue_t *vq)
```

- `virtqueue_enableIRQ` - Enable interrupts for a `VirtIO` queue.

```c
void virtqueue_enableIRQ(virtio_dev_t *vdev, virtqueue_t *vq)
```

- `virtqueue_disableIRQ` - Disable interrupts for a `VirtIO` queue.

```c
void virtqueue_disableIRQ(virtio_dev_t *vdev, virtqueue_t *vq)
```

### Configuration and Status

- `virtio_readConfig` - Read from the `VirtIO` device's configuration space.

```c
uint8_t virtio_readConfig8(virtio_dev_t *vdev, unsigned int reg);

uint16_t virtio_readConfig16(virtio_dev_t *vdev, unsigned int reg);

uint32_t virtio_readConfig32(virtio_dev_t *vdev, unsigned int reg);

uint64_t virtio_readConfig64(virtio_dev_t *vdev, unsigned int reg);
```

- `virtio_writeConfig` -Write to the `VirtIO` device's configuration space.

```c
void virtio_writeConfig8(virtio_dev_t *vdev, unsigned int reg, uint8_t val);

void virtio_writeConfig16(virtio_dev_t *vdev, unsigned int reg, uint16_t val);

void virtio_writeConfig32(virtio_dev_t *vdev, unsigned int reg, uint32_t val);

void virtio_writeConfig64(virtio_dev_t *vdev, unsigned int reg, uint64_t val);
```

- `virtio_readFeatures` - Read `VirtIO` device features.

```c
uint64_t virtio_readFeatures(virtio_dev_t *vdev)
```

- `virtio_writeFeatures` - Write `VirtIO` device features.

```c
int virtio_writeFeatures(virtio_dev_t *vdev, uint64_t features)
```

- `virtio_readStatus` - Read the `VirtIO` device status register.

```c
uint8_t virtio_readStatus(virtio_dev_t *vdev)
```

- `virtio_writeStatus` - Write the `VirtIO` device status register.

```c
void virtio_writeStatus(virtio_dev_t *vdev, uint8_t status)
```

- `virtio_isr` - Reads the interrupt status.

```c
unsigned int virtio_isr(virtio_dev_t *vdev)
```

### Utility

- `virtio_reset` - Resets a `VirtIO` device to its initial state.

```c
void virtio_reset(virtio_dev_t *vdev)
```

- `virtio_find` - Detects the next `VirtIO` device matching a given device descriptor.

```c
int virtio_find(const virtio_devinfo_t *info, virtio_dev_t *vdev, virtio_ctx_t *vctx)
```

- `virtio_init` - Initialize the `VirtIO` library.

```c
int virtio_init(void)
```

- `virtio_done` - Clean up the `VirtIO` library.

```c
int virtio_done(void)
```

### Memory Barriers

- `virtio_mb` - Provides a memory barrier to ensure memory operations' ordering.

```c
void virtio_mb(void)
```

### Data Structures

- `virtio_devtype_t` - Enumerates the types of `VirtIO` devices, such as PCI and MMIO devices.

```C
typedef enum {
	vdevNONE = 0x00, /* No VirtIO device */
	vdevPCI  = 0x01, /* VirtIO PCI device */
	vdevMMIO = 0x02  /* VirtIO MMIO device */
} virtio_devtype_t;
```

- `virtio_seg_t` - Represents a segment of a data buffer for I/O operations, forming a doubly linked list.

```C
struct _virtio_seg_t {
	void *buff;                /* Buffer exposed to device */
	unsigned int len;          /* Buffer length */
	virtio_seg_t *prev, *next; /* Doubly linked list */
};
```

- `virtio_req_t` - Encapsulates a request to be processed by a `VirtIO` device, comprising a list of segments.

```C
typedef struct {
	virtio_seg_t *segs; /* Request segments list */
	unsigned int rsegs; /* Number of device readable segments */
	unsigned int wsegs; /* Number of device writable segments */
} virtio_req_t;
```

- `virtio_desc_t` - Represents a descriptor in the `VirtIO` queue.

```C
typedef struct {
	uint64_t addr;  /* Buffer physical address */
	uint32_t len;   /* Buffer length */
	uint16_t flags; /* Descriptor flags */
	uint16_t next;  /* Next chained descriptor index (if flags & 0x1) */
} __attribute__((packed)) virtio_desc_t;
```

- `virtio_avail_t` / `virtio_used_t` - Structures used to manage available and used rings in a `VirtIO` queue.

```C
typedef struct {
	uint16_t flags;  /* Used buffer notification suppression */
	uint16_t idx;    /* Next available request index */
	uint16_t ring[]; /* Available requests (descriptor chain IDs) */
} __attribute__((packed)) virtio_avail_t;
```

```C
typedef struct {
	uint16_t flags;            /* Available buffer notification suppression */
	uint16_t idx;              /* Next processed request ring index */
	virtio_used_elem_t ring[]; /* Processed requests */
} __attribute__((packed)) virtio_used_t;
```

- `virtqueue_t` - Represents a `VirtIO` queue, holding the queue's descriptors, available and used rings,
and synchronization primitives.

```C
typedef struct {
	/* Standard split virtqueue layout */
	volatile virtio_desc_t *desc;   /* Descriptors */
	volatile virtio_avail_t *avail; /* Avail ring */
	volatile uint16_t *uevent;      /* Used event notification suppression */
	volatile virtio_used_t *used;   /* Used ring */
	volatile uint16_t *aevent;      /* Avail event notification suppression */

	/* Custom helper fields */
	void **buffs;       /* Descriptors buffers */
	void *mem;          /* Allocated virtqueue memory */
	unsigned int memsz; /* Allocated virtqueue memory size */
	unsigned int idx;   /* Virtqueue index */
	unsigned int size;  /* Virtqueue size */
	unsigned int noffs; /* Virtqueue notification area offset (modern VirtIO PCI device only) */
	unsigned int nfree; /* Number of free descriptors */
	uint16_t free;      /* Next free descriptor index */
	uint16_t last;      /* Last processed request index */

	/* Synchronization */
	handle_t cond; /* Free descriptors condition variable */
	handle_t lock; /* Virtqueue mutex */
} virtqueue_t;
```

- `virtio_devinfo_t` - Contains basic information about a VirtIO device, including its type, ID, and register addresses.

```C
typedef struct {
	virtio_devtype_t type; /* VirtIO device type */
	unsigned int id;       /* VirtIO device ID */
	unsigned int irq;      /* Interrupt number */
	unsigned int xntf;     /* Notification registers offset multiplier */
	virtio_reg_t base;     /* Base registers */
	virtio_reg_t ntf;      /* Notification register */
	virtio_reg_t isr;      /* Interrupt status register */
	virtio_reg_t cfg;      /* Configuration registers */
} virtio_devinfo_t;
```

- `virtio_dev_t` - Encapsulates a VirtIO device, including its features and device-specific information.

```C
typedef struct {
	virtio_devinfo_t info; /* VirtIO device core data */
	uint64_t features;     /* VirtIO device features */
} virtio_dev_t;
```

- `virtio_ctx_t` - Used for device detection and context management.

```C
typedef struct {
	unsigned char reset;   /* Indicates that context to be reset */
	unsigned char ctx[32]; /* VirtIO device detection context */
} virtio_ctx_t;
```

## Using libvirtio

To use functions provided by `libvirtio` please add the library to the `LIBS` variable in `Makefile` and include the
required header file.

## Running tests

`VirtIO` library provides the basic set of tests, which is available in
[phoenix-rtos-tests](https://github.com/phoenix-rtos/phoenix-rtos-tests/tree/master).

## See also

1. [Phoenix-RTOS core libraries](README.md)
2. [Phoenix-RTOS Graphics Library](libgraph.md)
3. [Table of Contents](../README.md)
