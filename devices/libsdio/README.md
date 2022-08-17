# libsdio

## Description

libsdio is a static, precompiled library containing a generic SDIO driver which directly controls platform hardware. This driver defines an API providing basic interface control functionality.

## Platform support

| Target            | Supported?       |
|-------------------|------------------|
| armv7a7-imx6ull   |:heavy_check_mark:|
| armv7m7-imxrt106x |:x:               |
| ia32-generic-pc   |:x:               |

## Limitations

- only one library instance per system
- no fallback SD protocol support
- no support for multiple SDIO devices
- no support for SDIO in SPI mode
- only 4-bit data transfer mode supported
- only 50/25 MHz clock speeds available

## API summary

The library header `<sdio.h>` provides the following API functions:

```c
int sdio_init(void);


void sdio_free(void);


int sdio_config(uint32_t freq, uint16_t blocksz);


int sdio_transferDirect(sdio_dir_t dir, uint32_t address, uint8_t area, uint8_t *data);


int sdio_transferBulk(sdio_dir_t dir, int blockMode, uint32_t address, uint8_t area,
	uint8_t *data, size_t len);


void sdio_eventRegister(uint8_t event, sdio_event_handler_t handler, void *arg);


void sdio_eventEnable(uint8_t event, int enabled);
```

Types:

```c
typedef enum {
	sdio_read,
	sdio_write
} sdio_dir_t;


typedef void (*sdio_event_handler_t)(void *arg);
```

The API also defines the following interrupt events:

| define                   | description                                   |
|--------------------------|-----------------------------------------------|
|SDIO_EVENT_CARD_IN        | SDIO device is inserted                       |
|SDIO_EVENT_CARD_OUT       | SDIO device is removed                        |
|SDIO_EVENT_CARD_IRQ       | SDIO device requested an interrupt            |
|SDIO_EVENT_RW_DONE        | transfer has been completed                   |
|SDIO_EVENT_RW_WRITE_READY | host write buffer is ready                    |
|SDIO_EVENT_RW_READ_READY  | host read buffer is ready                     |
|SDIO_EVENT_CMD_DONE       | issued command has been completed             |
|SDIO_EVENT_CMD_TIMEOUT    | issued command timed out                      |
|SDIO_EVENT_CMD_CRC        | command redundancy check error ocurred        |
|SDIO_EVENT_CMD_ENDBIT     | command end bit error occurred                |
|SDIO_EVENT_CMD_INDEX      | issued command is not valid                   |
|SDIO_EVENT_DATA_TIMEOUT   | data transfer timed out                       |
|SDIO_EVENT_DATA_CRC       | data redundancy check error ocurred           |
|SDIO_EVENT_DATA_ENDBIT    | data end bit error occurred                   |
|SDIO_EVENT_DMA_BUFFER     | DMA buffer boundary encountered               |
|SDIO_EVENT_DMA_ERROR      | a DMA error ocurred                           |
|SDIO_EVENT_TUNING_RETUNE  | host controller signals the need for retuning |
|SDIO_EVENT_TUNING_ERROR   | host controller tuning error                  |
|SDIO_EVENT_BLOCK_GAP      | a transfer was interrupted                    |

These defines are meant for usage with `sdio_eventEnable` and `sdio_eventRegister` functions exclusively.

## API description

Following sections describe the API in detail, including the behaviour of certain functions.

---

```c
typedef enum {
	sdio_read,
	sdio_write
} sdio_dir_t;
```

This enumeration type is meant as parameter for `sdio_transferDirect` and `sdio_transferBulk` functions to indicate the direction of a given data transfer.

---

```c
typedef void (*sdio_event_handler_t)(void *arg);
```

This type describes a function pointer for an interrupt handler. Handlers of interrupts events are assigned to a specific event, and every event can only have a single handler. Handler argument is provided during handler registration using `sdio_eventRegister`, and will remain unchanged until the handler registration is modified via the same function.

---

```c
int sdio_init(void);
```

This function initializes the SDIO inteface hardware and tries to detect and enable connected device. Should no device be present or it could not respond to SDIO initialization sequence, this function will return an error code and free unusued resources it acquired.

> **NOTE:** This function should not be called multiple times. In order to reinitialize the interface, `sdio_free` should be called between concurrent `sdio_init` calls instead.

Parameters:

- none

Returns:

| code | description |
|------|-------------|
|  0   | success     |
| -1   | failure     |

> **NOTE:** Every failure is accompanied by explicit fault description printed into standard output.

---

```c
void sdio_free(void);
```

This function will free the SDIO bus, deregister and disable all previously registered event handlers.

> **NOTE:** Due to its current implementation, calling this function does not allow for creation of new library instances in other running processes.

Parameters:

- none

Returns:

- nothing

---

```c
int sdio_config(uint32_t freq, uint16_t blocksz);
```

This function provides a configuration interface for the SDIO bus.

Parameters:

| parameter               | description                   |
|-------------------------|-------------------------------|
| [in] `uint32_t freq`    | SDIO clock frequency in Hz    |
| [in] `uint16_t blocksz` | block size for bulk transfers |

> **NOTE:** `uint32_t freq` can only be specified as either 25000000 or 50000000, since only 25 and 50 MHz clock speeds are supported.

Returns:

| code | description |
|------|-------------|
|  0   | success     |
| -1   | failure     |

> **NOTE:** Every failure is accompanied by explicit fault description printed into standard output.

---

```c
int sdio_transferDirect(sdio_dir_t dir, uint32_t address, uint8_t area, uint8_t *data);
```

This function initiates a direct, single 8-bit register read/write opetation. When `dir` is specified as `sdio_write` the byte inside the `data` buffer is written to the card, otherwise if `dir` equals `sdio_read` is specified, the buffer is set to value read from the card.

Parameters:

| parameter                | description                       |
|--------------------------|-----------------------------------|
| [in] `sdio_dir_t dir`    | transfer direction                |
| [in] `uint32_t address`  | card register address to access   |
| [in] `uint8_t area`      | card I/O area index to access     |
| [in/out] `uint8_t *data` | bi-directional single byte buffer |

Returns:

| code | description |
|------|-------------|
|  0   | success     |
| -1   | failure     |

> **NOTE:** Every failure is accompanied by explicit fault description printed into standard output.

---

```c
int sdio_transferBulk(sdio_dir_t dir, int blockMode, uint32_t address, uint8_t area, uint8_t *data, size_t len);
```

This function initiates an indirect, multi-byte transfer of up to 2048 bytes at once. As is the case with `sdio_transferDirect`, this call can service bi-directional transfers.

Parameters:

| parameter                | description                             |
|--------------------------|-----------------------------------------|
| [in] `sdio_dir_t dir`    | transfer direction                      |
| [in] `int blockMode`     | wheter to use blocks for transfer (1/0) |
| [in] `uint32_t address`  | card base address to access             |
| [in] `uint8_t area`      | card I/O area index to access           |
| [in/out] `uint8_t *data` | bi-directional multi byte buffer        |
| [in] `size_t len`        | total transfer size in bytes            |

> **NOTE:** `address` parameter specifies only the base address of the transfer. If `blockMode` is set to 1, then the address is automatically incremented by the card with every following block.

Returns:

| code        | description                                                 |
|-------------|-------------------------------------------------------------|
|  0          | success                                                     |
| -1          | failure                                                     |
| EINVAL (22) | `blocksz` is unset or `len` is not a multiple of block size |

> **NOTE:** Every failure is accompanied by explicit fault description printed into standard output.

---

```c
void sdio_eventRegister(uint8_t event, sdio_event_handler_t handler, void *arg);
```

This function registers an event handler to be called when a given interrupt event occurs. An interrupt event will not be signalled until its detection is enabled by `sdio_eventEnable`. Please note that only one handler can be registered per event - calling this function multiple times for the same event will result in the previous handler being overwritten.

Parameters:

| parameter                           | description                             |
|-------------------------------------|-----------------------------------------|
| [in] `uint8_t event`                | event to be handled                     |
| [in] `sdio_event_handler_t handler` | pointer to event handler function       |
| [in/out] `void *arg`                | argument for the handler function       |

> **NOTE:** `event` argument is passed using appropriate define beginning with `SDIO_EVENT`.

Returns:

- nothing

---

```c
void sdio_eventEnable(uint8_t event, int enabled);
```

This function can enable or disable interrupt event signalling of the SD host controller. If a handler is registered via `sdio_eventRegister` for a given enabled event, it will be called when an interrupt fires.

Parameters:

| parameter            | description                                    |
|----------------------|------------------------------------------------|
| [in] `uint8_t event` | event for which signalling enable is to be set |
| [in] `int enabled`   | state of signalling enable (1/0)               |

> **NOTE:** `event` argument is passed using appropriate define beggining with `SDIO_EVENT`.

Returns:

- nothing
