# VGA library (libvga)

`libvga` provides VGA-compatible register access and mode-state helpers used by graphics adapter implementations.

The public interface is declared in `<vga.h>`. The low-level `vgahw_*()` functions are hardware abstraction hooks.
The high-level `vga_*()` functions build on those hooks to save, restore, and initialize VGA state.

## Sizes and mode flags

| Constant | Value | Meaning |
| --- | --- | --- |
| `VGA_CTXSZ` | `0x80` | Hardware context size used by VGA backends. |
| `VGA_MEMSZ` | `0x10000` | VGA memory aperture size. |
| `VGA_CMAPSZ` | `768` | Color map size, `256` entries with 3 channels. |
| `VGA_TEXTSZ` | `VGA_MEMSZ >> 1` | Text plane storage size. |
| `VGA_FONTSZ` | `VGA_MEMSZ` | Font plane storage size. |
| `VGA_HSYNCP` | `1 << 0` | Horizontal sync positive polarity. |
| `VGA_VSYNCP` | `1 << 1` | Vertical sync positive polarity. |
| `VGA_CLKDIV` | `1 << 2` | Pixel clock divided by 2. |
| `VGA_DBLSCAN` | `1 << 3` | Double-scan vertical timings. |
| `VGA_INTERLACE` | `1 << 4` | Interlaced vertical timings. |

## State structures

`vga_cfg_t`
: Mode timing configuration used by `vga_initstate()`.

  The structure stores clock source, clock frequency in kHz, horizontal and vertical timing values, and mode flags.

`vga_state_t`
: Saved or generated VGA register and memory state.

  The structure stores the miscellaneous register, CRT controller registers, sequencer registers, graphics controller
  registers, attribute controller registers, and optional pointers for the color map, text planes, and font planes.

## Hardware abstraction functions

````{function} vgahw_mem(hwctx)
Returns the mapped VGA memory aperture for the hardware context.

:param hwctx: Hardware-specific VGA context.
:returns: Pointer to VGA memory. The empty backend returns `NULL`.
````

````{function} vgahw_status(hwctx)
Reads the VGA input status register.

:param hwctx: Hardware-specific VGA context.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_readfcr(hwctx)
Reads the feature control register.

:param hwctx: Hardware-specific VGA context.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_writefcr(hwctx, val)
Writes the feature control register.

:param hwctx: Hardware-specific VGA context.
:param val: Register value to write.
:returns: Nothing.
````

````{function} vgahw_readmisc(hwctx)
Reads the miscellaneous output register.

:param hwctx: Hardware-specific VGA context.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_writemisc(hwctx, val)
Writes the miscellaneous output register.

:param hwctx: Hardware-specific VGA context.
:param val: Register value to write.
:returns: Nothing.
````

````{function} vgahw_readcrtc(hwctx, reg)
Reads a CRT controller register.

:param hwctx: Hardware-specific VGA context.
:param reg: CRT controller register index.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_writecrtc(hwctx, reg, val)
Writes a CRT controller register.

:param hwctx: Hardware-specific VGA context.
:param reg: CRT controller register index.
:param val: Register value to write.
:returns: Nothing.
````

````{function} vgahw_readseq(hwctx, reg)
Reads a sequencer register.

:param hwctx: Hardware-specific VGA context.
:param reg: Sequencer register index.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_writeseq(hwctx, reg, val)
Writes a sequencer register.

:param hwctx: Hardware-specific VGA context.
:param reg: Sequencer register index.
:param val: Register value to write.
:returns: Nothing.
````

````{function} vgahw_readgfx(hwctx, reg)
Reads a graphics controller register.

:param hwctx: Hardware-specific VGA context.
:param reg: Graphics controller register index.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_writegfx(hwctx, reg, val)
Writes a graphics controller register.

:param hwctx: Hardware-specific VGA context.
:param reg: Graphics controller register index.
:param val: Register value to write.
:returns: Nothing.
````

````{function} vgahw_readattr(hwctx, reg)
Reads an attribute controller register.

:param hwctx: Hardware-specific VGA context.
:param reg: Attribute controller register index.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_writeattr(hwctx, reg, val)
Writes an attribute controller register.

:param hwctx: Hardware-specific VGA context.
:param reg: Attribute controller register index.
:param val: Register value to write.
:returns: Nothing.
````

````{function} vgahw_readdac(hwctx, reg)
Reads a Digital-to-Analog Converter (DAC) register.

:param hwctx: Hardware-specific VGA context.
:param reg: DAC register index.
:returns: Register value. The empty backend returns `0`.
````

````{function} vgahw_writedac(hwctx, reg, val)
Writes a DAC register.

:param hwctx: Hardware-specific VGA context.
:param reg: DAC register index.
:param val: Register value to write.
:returns: Nothing.
````

````{function} vgahw_enablecmap(hwctx)
Enables color-map register access.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vgahw_disablecmap(hwctx)
Disables color-map register access.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vgahw_init(hwctx)
Initializes the hardware context.

The PC backend maps VGA memory and returns `EOK` on success. The empty backend returns `-ENODEV`.

:param hwctx: Hardware-specific VGA context storage.
:returns: `EOK`, `-ENOMEM`, or `-ENODEV`, depending on the backend.
````

````{function} vgahw_done(hwctx)
Destroys the hardware context.

:param hwctx: Hardware-specific VGA context initialized by `vgahw_init()`.
:returns: Nothing.
````

## High-level state functions

````{function} vga_lock(hwctx)
Locks CRT controller registers `0` through `7` by setting bit `7` of register `0x11`.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vga_unlock(hwctx)
Unlocks CRT controller registers `0` through `7` by clearing bit `7` of register `0x11`.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vga_mlock(hwctx)
Protects registers and memory during a mode switch.

The function disables display output, stops the sequencer, and enables color-map access.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vga_munlock(hwctx)
Releases mode-switch protection set by `vga_mlock()`.

The function restarts the sequencer, enables display output, and disables color-map access.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vga_blank(hwctx)
Blanks the display by setting the sequencer screen-off bit.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vga_unblank(hwctx)
Unblanks the display by clearing the sequencer screen-off bit.

:param hwctx: Hardware-specific VGA context.
:returns: Nothing.
````

````{function} vga_savemode(hwctx, state)
Reads VGA mode registers into `state`.

The function fills `mr`, `cr`, `sr`, `gr`, and `ar`. It does not allocate storage for optional pointers in `state`.

:param hwctx: Hardware-specific VGA context.
:param state: State object supplied by the caller.
:returns: Nothing.
````

````{function} vga_restoremode(hwctx, state)
Writes VGA mode registers from `state`.

The function unlocks restored CRT controller registers before writing the stored CRT controller array.

:param hwctx: Hardware-specific VGA context.
:param state: State object filled by `vga_savemode()` or `vga_initstate()`.
:returns: Nothing.
````

````{function} vga_savecmap(hwctx, state)
Copies the current DAC color map to `state->cmap`.

When `state->cmap == NULL`, the function returns without reading DAC data.

:param hwctx: Hardware-specific VGA context.
:param state: State object with optional `cmap` buffer of `VGA_CMAPSZ` bytes.
:returns: Nothing.
````

````{function} vga_restorecmap(hwctx, state)
Writes DAC color-map data from `state->cmap`.

When `state->cmap == NULL`, the function returns without writing DAC data.

:param hwctx: Hardware-specific VGA context.
:param state: State object with optional `cmap` buffer of `VGA_CMAPSZ` bytes.
:returns: Nothing.
````

````{function} vga_savetext(hwctx, state)
Copies VGA text and font planes into buffers referenced by `state`.

The function returns without copying when the current attribute mode indicates graphics mode. It copies only the
buffers whose pointers are non-`NULL`.

:param hwctx: Hardware-specific VGA context.
:param state: State object with optional `text`, `font1`, and `font2` buffers.
:returns: Nothing.
````

````{function} vga_restoretext(hwctx, state)
Restores VGA text and font planes from buffers referenced by `state`.

The function writes only the buffers whose pointers are non-`NULL`.

:param hwctx: Hardware-specific VGA context.
:param state: State object with optional `text`, `font1`, and `font2` buffers.
:returns: Nothing.
````

````{function} vga_save(hwctx, state)
Saves text planes, color map, and mode registers into `state`.

:param hwctx: Hardware-specific VGA context.
:param state: State object supplied by the caller.
:returns: Nothing.
````

````{function} vga_restore(hwctx, state)
Restores mode registers, color map, and text planes from `state`.

:param hwctx: Hardware-specific VGA context.
:param state: State object supplied by the caller.
:returns: Nothing.
````

````{function} vga_initstate(cfg, state)
Generates VGA register state for the timing configuration in `cfg`.

The function applies `VGA_DBLSCAN` and `VGA_INTERLACE` to vertical timings, fills the miscellaneous register, and
generates CRT controller, sequencer, graphics controller, and attribute controller register arrays.

:param cfg: Mode timing configuration.
:param state: State object whose register arrays are written by the function.
:returns: Nothing.
````