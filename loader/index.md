# Loader (plo)

The Phoenix-RTOS loader (PLO) prepares hardware, builds the syspage, and loads the kernel and initial programs before
control is transferred to Phoenix-RTOS.

The bootloader prepares the system setup structure and loads the kernel and applications into memory areas
(maps). Its configuration allows customizing functionality to match available hardware resources.

The Phoenix-RTOS loader supports all the target platforms listed in the [Building](../building/index.md) chapter.

```{toctree}
:maxdepth: 1

functionality.md
architecture.md
cli.md
```
