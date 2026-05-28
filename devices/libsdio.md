# Libsdio

`libsdio` is a static SDIO host-controller library for targets that need direct SDIO device access from an
application or server.

## Platform support

| Target | Supported |
| --- | --- |
| `armv7a7-imx6ull` | Yes |
| `armv7m7-imxrt106x` | No |
| `ia32-generic-pc` | No |

## Limitations

- The implementation supports one library instance per system.
- The implementation supports SDIO only, not fallback SD mode.
- The implementation supports one SDIO device.
- The implementation does not support SDIO in SPI mode.
- The i.MX 6ULL implementation uses 4-bit transfers and accepts 25 MHz or 50 MHz bus clocks.

## Header interface

The public interface is declared in `<sdio.h>`.

### Types and constants

`sdio_dir_t`
: Transfer direction for direct and bulk transfers.

  ```c
  typedef enum {
      sdio_read,
      sdio_write
  } sdio_dir_t;
  ```

`sdio_event_handler_t`
: Callback type for SDIO interrupt events. The `arg` value is the pointer passed to `sdio_eventRegister()`.

  ```c
  typedef void (*sdio_event_handler_t)(void *arg);
  ```

| Constant | Meaning |
| --- | --- |
| `SDIO_EVENT_CARD_IN` | Card insertion event. |
| `SDIO_EVENT_CARD_OUT` | Card removal event. |
| `SDIO_EVENT_CARD_IRQ` | Card interrupt request event. |

### Functions

````{function} sdio_init()
Initializes the SDIO host controller and attempts to initialize the connected card.

Call this function before any other `libsdio` function. Calling it again after a successful initialization returns
success without reinitializing the controller.

:returns: `0` on success, `-EIO` for hardware, platform, reset, or card initialization failure, or `-ENOMEM` when DMA,
  mutex, or event-thread setup fails.
````


````{function} sdio_free()
Disables the SDIO module and releases resources owned by the current library instance.

The function resets the host controller and clears registered event handlers. Calling it before `sdio_init()` has no
effect.

:returns: Nothing.
````

````{function} sdio_config(freq, blocksz)
Configures the SDIO bus clock, 4-bit transfer mode, and block size used by bulk transfers.

:param freq: SDIO clock frequency in hertz. The i.MX 6ULL implementation accepts `25000000` and `50000000`.
:param blocksz: Block size used when `sdio_transferBulk()` is called with `blockMode != 0`.
:returns: `0` on success, `-EINVAL` for an unsupported `freq`, `-EIO` when the SD clock is not stable before
  reconfiguration, or `-ETIMEDOUT` when initialization clock cycles do not finish in time.
````

````{function} sdio_transferDirect(dir, address, area, data)
Transfers one byte with the SDIO direct read or write command.

For `sdio_write`, the function writes `*data` to the card. For `sdio_read`, it writes the received byte to `*data`.

:param dir: Transfer direction, `sdio_read` or `sdio_write`.
:param address: SDIO function register address. The implementation encodes the low 17 bits.
:param area: SDIO I/O area number. The implementation encodes the low 3 bits.
:param data: Pointer to the byte transferred to or from the card.
:returns: `0` on success or a negative error returned by the command path.
````

````{function} sdio_transferBulk(dir, blockMode, address, area, data, len)
Transfers up to 2048 bytes with the SDIO extended read or write command.

For `sdio_write`, the function copies `len` bytes from `data` to the DMA buffer before issuing the command. For
`sdio_read`, it copies received bytes from the DMA buffer to `data` after the command completes.

:param dir: Transfer direction, `sdio_read` or `sdio_write`.
:param blockMode: Non-zero value selects block mode. Zero selects byte mode.
:param address: SDIO function base address. The implementation encodes the low 17 bits.
:param area: SDIO I/O area number. The implementation encodes the low 3 bits.
:param data: Buffer used as the source for writes or destination for reads.
:param len: Number of bytes to transfer. The maximum is `2048`. In block mode, `len` must be a multiple of the block
  size configured with `sdio_config()`.
:returns: `0` on success, `-EINVAL` for an oversized transfer or invalid block-mode length, `-EBUSY` when the hardware
  reports an active command or data line, `-EIO` for a hardware error flag, or `-ETIMEDOUT` when the transfer does not
  complete in time.
````

````{function} sdio_eventRegister(event, handler, arg)
Registers the callback for one SDIO event.

Only one callback is stored for each event. A later registration for the same event replaces the previous callback.
Pass `NULL` as `handler` to clear the callback.

:param event: One of `SDIO_EVENT_CARD_IN`, `SDIO_EVENT_CARD_OUT`, or `SDIO_EVENT_CARD_IRQ`.
:param handler: Callback executed by the SDIO event thread, or `NULL` to clear the callback.
:param arg: Pointer passed to `handler` when the event fires.
:returns: `0` on success or `-EINVAL` when `event` is outside the supported range.
````

````{function} sdio_eventEnable(event, enabled)
Enables or disables interrupt signaling for one SDIO event.

:param event: One of `SDIO_EVENT_CARD_IN`, `SDIO_EVENT_CARD_OUT`, or `SDIO_EVENT_CARD_IRQ`.
:param enabled: Non-zero value enables the event. Zero disables it.
:returns: `0` on success or `-EINVAL` when `event` is outside the supported range.
````