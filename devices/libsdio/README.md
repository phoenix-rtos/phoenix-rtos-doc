# libsdio

## General description

libsdio is a static, precompiled library containing a generic SDIO driver which directly controls the platform hardware.
This driver defines an API providing basic interface control functionality.

## Platform support

| Target            | Supported?         |
|-------------------|--------------------|
| armv7a7-imx6ull   | :heavy_check_mark: |
| armv7m7-imxrt106x | :x:                |
| ia32-generic-pc   | :x:                |

## Limitations

- only one library instance per system
- no fallback SD protocol support (SDIO only)
- no support for multiple SDIO devices
- no support for SDIO in SPI mode
- only 4-bit data transfer mode supported
- only 50/25 MHz clock speeds available on imx6ull

## API summary

Contents of `<sdio.h>` header are listed below.

**Functions:**

```c
int sdio_init(void);


void sdio_free(void);


int sdio_config(uint32_t freq, uint16_t blocksz);


int sdio_transferDirect(sdio_dir_t dir, uint32_t address, uint8_t area, uint8_t *data);


int sdio_transferBulk(sdio_dir_t dir, int blockMode, uint32_t address, uint8_t area,
	uint8_t *data, size_t len);


int sdio_eventRegister(uint8_t event, sdio_event_handler_t handler, void *arg);


int sdio_eventEnable(uint8_t event, int enabled);
```

**Types:**

```c
typedef enum {
	sdio_read,
	sdio_write
} sdio_dir_t;


typedef void (*sdio_event_handler_t)(void *arg);
```

**Definitions:**

| define              | description                        |
|---------------------|------------------------------------|
| SDIO_EVENT_CARD_IN  | SDIO device is inserted            |
| SDIO_EVENT_CARD_OUT | SDIO device is removed             |
| SDIO_EVENT_CARD_IRQ | SDIO device requested an interrupt |

> **NOTE:** These definitions are meant for use with `sdio_eventEnable` and `sdio_eventRegister` functions exclusively.

## API description

Following sections describe the API in detail, including the behaviour of certain functions.

> **NOTE:** Codes returned by API calls are defined in `<errno.h>` header, which provides more detailed information
about specific values.

---

```c
typedef enum {
	sdio_read,
	sdio_write
} sdio_dir_t;
```

**Description:**

This enumeration type is meant as parameter for `sdio_transferDirect` and `sdio_transferBulk` functions to indicate the
direction of a given data transfer.

---

```c
typedef void (*sdio_event_handler_t)(void *arg);
```

**Description:**

This type describes a callback for an interrupt handler. Handlers of interrupts events are assigned to a specific event,
and every event can only have a single handler. Handler argument is provided during handler registration using
`sdio_eventRegister`, and will remain unchanged until the handler registration is modified via the same function.

---

```c
int sdio_init(void);
```

**Description:**

This function initializes the SDIO inteface hardware and tries to detect and select the connected device. It has to be
called before any other API function. Should no device be present or it does not respond to SDIO initialization
sequence, this function shall return an error code and free resources it acquired.

> **NOTE:** Calling this function more than once after successful completion will have no effect. In order to
reinitialize the interface, `sdio_free` should be called between concurrent `sdio_init` calls instead.

**Parameters:**

- none

**Returns:**

| code    | description                 |
|---------|-----------------------------|
|  EOK    | success                     |
| -EIO    | I/O hardware fault occured  |
| -ENOMEM | not enough memory available |

---

```c
void sdio_free(void);
```

**Description:**

This function frees the SDIO bus, reset the host controller, deregister and disable all previously registered event
handlers. Calling this function before `sdio_init` has no effect.

> **NOTE:** Due to its current implementation, calling this function does not allow for creation of new library
instances in other running processes.

**Parameters:**

- none

**Returns:**

- nothing

---

```c
int sdio_config(uint32_t freq, uint16_t blocksz);
```

**Description:**

This function provides a configuration interface for the SDIO bus controller. This function can be called at any time
after `sdio_init`.

**Parameters:**

| parameter               | description                   | possible values     |
|-------------------------|-------------------------------|---------------------|
| [in] `uint32_t freq`    | SDIO clock frequency in Hz    | *any*               |
| [in] `uint16_t blocksz` | block size for bulk transfers | 25000000 / 50000000 |

**Returns:**

| code       | description                        |
|------------|------------------------------------|
|  EOK       | success                            |
| -EINVAL    | provided `blocksz` is invalid      |
| -ETIMEDOUT | device configuration took too long |
| -EIO       | I/O hardware fault occured         |

---

```c
int sdio_transferDirect(sdio_dir_t dir, uint32_t address, uint8_t area, uint8_t *data);
```

**Description:**

This function initiates a direct, single 8-bit register read/write opetation. When `dir` is specified as `sdio_write`
the byte inside the `data` buffer is written to the device, otherwise if `dir` equals `sdio_read` , the buffer is set
to the value read from the device.

> **NOTE:** This function is a blocking call which only returns upon successful transfer completion or failure.

**Parameters:**

| parameter                | description                       | possible values        |
|--------------------------|-----------------------------------|------------------------|
| [in] `sdio_dir_t dir`    | transfer direction                | sdio_read / sdio_write |
| [in] `uint32_t address`  | card register address to access   | *any 17-bit value*     |
| [in] `uint8_t area`      | card I/O area index to access     | *any 3-bit value*      |
| [in/out] `uint8_t *data` | bi-directional single byte buffer | *any valid pointer*    |

**Returns:**

| code       | description                    |
|------------|--------------------------------|
|  EOK       | success                        |
| -EBUSY     | device is currently busy       |
| -ETIMEDOUT | device did not respond in time |

---

```c
int sdio_transferBulk(sdio_dir_t dir, int blockMode, uint32_t address, uint8_t area,
	uint8_t *data, size_t len);
```

**Description:**

This function initiates an indirect, multi-byte transfer of up to 2048 bytes at once. As is the case with
`sdio_transferDirect`, this call can service bi-directional transfers.

> **NOTE:** This function is a blocking call which only returns upon successful transfer completion or failure.

**Parameters:**

| parameter                | description                      | possible values        |
|--------------------------|----------------------------------|------------------------|
| [in] `sdio_dir_t dir`    | transfer direction               | sdio_read / sdio_write |
| [in] `int blockMode`     | divide transfer into blocks      | *boolean*              |
| [in] `uint32_t address`  | card base address to access      | *any 17-bit value*     |
| [in] `uint8_t area`      | card I/O area index to access    | *any 3-bit value*      |
| [in/out] `uint8_t *data` | bi-directional multi byte buffer | *any valid pointer*    |
| [in] `size_t len`        | total transfer size in bytes     | <=2048                 |

> **NOTE:** `len` parameter has to be a multiple of `blocksz` when performing a block transfer with `blockMode` set to
*true*.
> **NOTE:** `address` parameter specifies only the base address of the transfer. If `blockMode` is set to *true*, then
the address is automatically incremented by the device with every completed block.

**Returns:**

| code       | description                               |
|------------|-------------------------------------------|
|  EOK       | success                                   |
| -EIO       | I/O hardware fault occured                |
| -EBUSY     | interface is currently busy               |
| -ETIMEDOUT | transfer request was not serviced in time |
| -EINVAL    | *see parameters section*                  |

---

```c
int sdio_eventRegister(uint8_t event, sdio_event_handler_t handler, void *arg);
```

This function registers an event handler to be called when a given interrupt event occurs. An interrupt event will not
be signalled until its detection is enabled by `sdio_eventEnable`. Please note that only one handler can be registered
per event - calling this function multiple times for the same event will result in the previous handler being
overwritten. In order to deregister the handler one can pass `NULL` as the `handler` parameter.

**Parameters:**

| parameter                           | description                       | possible values  |
|-------------------------------------|-----------------------------------|------------------|
| [in] `uint8_t event`                | event to be handled               | *see note below* |
| [in] `sdio_event_handler_t handler` | pointer to event handler function | *any pointer*    |
| [in/out] `void *arg`                | argument for the handler function | *any pointer*    |

> **NOTE:** `event` argument is passed using appropriate defines beginning with `SDIO_EVENT`.

**Returns:**

| code    | description                   |
|---------|-------------------------------|
|  EOK    | success                       |
| -EINVAL | provided `event` is not valid |

> **NOTE:** Codes returned are defined in `<errno.h>` header.

---

```c
int sdio_eventEnable(uint8_t event, int enabled);
```

This function can enable or disable interrupt event signalling of the SD host controller. If a handler is registered via
`sdio_eventRegister` for a given enabled event, it will be called when an interrupt fires.

**Parameters:**

| parameter            | description                                    | possible values  |
|----------------------|------------------------------------------------|------------------|
| [in] `uint8_t event` | event for which signalling enable is to be set | *see note below* |
| [in] `int enabled`   | state of signalling enable (1/0)               | *boolean*        |

> **NOTE:** `event` argument is passed using appropriate defines beggining with `SDIO_EVENT`.

**Returns:**

| code    | description                   |
|---------|-------------------------------|
|  EOK    | success                       |
| -EINVAL | provided `event` is not valid |
