# VGA library (libvga)

## Contents

- [General information](#general-information)
- [Mode Adjustment Flags](#mode-adjustment-flags)
- [Structures](#structures)
- [Low-Level Interface (Hardware Abstraction Layer)](#low-level-interface-hardware-abstraction-layer)
  - [Memory and Register Access](#memory-and-register-access)
  - [Color Map Management](#color-map-management)
  - [VGA Handle Management](#vga-handle-management)
- [High-Level Interface](#high-level-interface)
  - [VGA Register and Mode Management](#vga-register-and-mode-management)
  - [VGA State Management](#vga-state-management)
  - [VGA Configuration](#vga-configuration)
- [Using libvga](#using-libvga)

## General information

`libvga` is designed to interface with VGA-compatible display hardware. This library provides both low-level hardware
access and high-level functionality to manage VGA display settings, modes, and memory.

## Mode Adjustment Flags

Adjustment flags are used to modify the behavior of the VGA display modes.

`VGA_HSYNCP`: Set for HSync positive polarity.

`VGA_VSYNCP`: Set for VSync positive polarity.

`VGA_CLKDIV`: Indicates the pixel clock is divided by 2.

`VGA_DBLSCAN`: Enables double scanning.

`VGA_INTERLACE`: Activates interlace mode.

## Structures

- `vga_cfg_t` - Holds the configuration for a VGA mode, including pixel clock, horizontal and vertical timings,
and mode adjustment flags.

```C
typedef struct {
	/* Pixel clock */
	unsigned int clkidx; /* Pixel clock source index */
	unsigned int clk;    /* Pixel clock frequency (kHz) */
	/* Horizontal timings */
	unsigned int hres;   /* Horizontal resolution */
	unsigned int hsyncs; /* Horizontal sync start */
	unsigned int hsynce; /* Horizontal sync end */
	unsigned int htotal; /* Horizontal total pixels */
	/* Vertical timings */
	unsigned int vres;   /* Vertical resolution */
	unsigned int vsyncs; /* Vertical sync start */
	unsigned int vsynce; /* Vertical sync end */
	unsigned int vtotal; /* Vertical total lines */
	/* Mode adjustments */
	unsigned char flags; /* Mode adjustment flags */
} vga_cfg_t;
```

- `vga_state_t` - Represents the state of the VGA, including various registers, color map, text, and font data.

```C
typedef struct {
	unsigned char mr;     /* Miscellaneous register */
	unsigned char cr[25]; /* CRT controller registers */
	unsigned char sr[5];  /* Sequencer registers */
	unsigned char gr[9];  /* Graphics controller registers */
	unsigned char ar[21]; /* Attribute controller registers */
	unsigned char *cmap;  /* Color map */
	unsigned char *text;  /* Plane 0 and 1 text */
	unsigned char *font1; /* Plane 2 font */
	unsigned char *font2; /* Plane 3 font */
} vga_state_t;
```

## Low-Level Interface (Hardware Abstraction Layer)

### Memory and Register Access

- `vgahw_mem` - Returns the mapped VGA memory address.

```c
void *vgahw_mem(void *hwctx)
```

- `vgahw_status` - Reads from the input status register.

```c
unsigned char vgahw_status(void *hwctx)
```

- `vgahw_readfcr` - Read operations for the feature control register.

```c
unsigned char vgahw_readfcr(void *hwctx)
```

- `vgahw_writefcr` - Write operations for the feature control register.

```c
void vgahw_writefcr(void *hwctx, unsigned char val)
```

- `vgahw_readmisc` - Read operations for the miscellaneous register.

```c
unsigned char vgahw_readmisc(void *hwctx)
```

- `vgahw_readmisc` - Write operations for the miscellaneous register.

```c
void vgahw_writemisc(void *hwctx, unsigned char val)
```

- `vgahw_readcrtc` - Read operations for CRT controller registers.

```c
unsigned char vgahw_readcrtc(void *hwctx, unsigned char reg)
```

- `vgahw_writecrtc` - Write operations for CRT controller registers.

```c
void vgahw_writecrtc(void *hwctx, unsigned char reg, unsigned char val)
```

- `vgahw_readseq` - Read operations for sequencer registers.

```c
unsigned char vgahw_readseq(void *hwctx, unsigned char reg)
```

- `vgahw_writeseq` - Write operations for sequencer registers.

```c
void vgahw_writeseq(void *hwctx, unsigned char reg, unsigned char val)
```

- `vgahw_readgfx` - Read operations for graphics controller registers.

```c
unsigned char vgahw_readgfx(void *hwctx, unsigned char reg)
```

- `vgahw_writegfx` - Write operations for graphics controller registers.

```c
void vgahw_writegfx(void *hwctx, unsigned char reg, unsigned char val)
```

- `vgahw_readattr` - Read operations for attribute controller registers.

```c
unsigned char vgahw_readattr(void *hwctx, unsigned char reg)
```

- `vgahw_writeattr` - Write operations for attribute controller registers.

```c
void vgahw_writeattr(void *hwctx, unsigned char reg, unsigned char val)
```

- `vgahw_readdac` - Read operations for DAC controller registers.

```c
unsigned char vgahw_readdac(void *hwctx, unsigned char reg)
```

- `vgahw_writedac` - Write operations for DAC controller registers.

```c
void vgahw_writedac(void *hwctx, unsigned char reg, unsigned char val)
```

### Color Map Management

- `vgahw_enablecmap` - Enables the color map.

```c
void vgahw_enablecmap(void *hwctx)
```

- `vgahw_disablecmap` - Disables the color map.

```c
void vgahw_disablecmap(void *hwctx)
```

### VGA Handle Management

- `vgahw_init` - Initializes the VGA handle.

```c
int vgahw_init(void *hwctx)
```

- `vgahw_done` - Destroys the VGA handle.

```c
void vgahw_done(void *hwctx)
```

## High-Level Interface

### VGA Register and Mode Management

- `vga_lock` - Lock CRTC[0-7] registers.

```c
void vga_lock(void *hwctx)
```

- `vga_unlock` - Unlock CRTC[0-7] registers.

```c
void vga_unlock(void *hwctx)
```

- `vga_mlock` - Protect/release VGA registers and memory during mode switch.

```c
void vga_mlock(void *hwctx)
```

- `vga_munlock` - Protect/release VGA registers and memory during mode switch.

```c
void vga_munlock(void *hwctx)
```

- `vga_blank` - Blanks the screen.

```c
void vga_blank(void *hwctx)
```

- `vga_unblank` - Un blanks the screen.

```c
void vga_unblank(void *hwctx)
```

### VGA State Management

- `vga_savemode` - Save the VGA mode.

```c
void vga_savemode(void *hwctx, vga_state_t *state)
```

- `vga_restoremode` - Restore the VGA mode.

```c
void vga_restoremode(void *hwctx, vga_state_t *state)
```

- `vga_savecmap` - Save the VGA color map.

```c
void vga_savecmap(void *hwctx, vga_state_t *state)
```

- `vga_restorecmap` - Restore the VGA color map.

```c
void vga_restorecmap(void *hwctx, vga_state_t *state)
```

- `vga_savetext` - Save VGA fonts and text.

```c
void vga_savetext(void *hwctx, vga_state_t *state)
```

- `vga_restoretext` - Restore VGA fonts and text.

```c
void vga_restoretext(void *hwctx, vga_state_t *state)
```

- `vga_save` - Save all VGA settings.

```c
void vga_save(void *hwctx, vga_state_t *state)
```

- `vga_restore` - Restore all VGA settings.

```c
void vga_restore(void *hwctx, vga_state_t *state)
```

### VGA Configuration

- `vga_initstate` - Initializes the VGA state for a given mode configuration.

```c
void vga_initstate(vga_cfg_t *cfg, vga_state_t *state)
```

## Using libvga

To use functions provided by `libvga` please add the library to the `LIBS` variable in `Makefile` and include the
required header file.

## See also

1. [Feniks-RTOS core libraries](index.md)
2. [Feniks-RTOS Graphics Library](libgraph.md)
3. [Table of Contents](../index.md)
