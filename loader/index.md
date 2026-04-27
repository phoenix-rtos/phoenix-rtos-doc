# Loader (plo)

This chapter covers the Phoenix-RTOS bootloader (plo): hardware preparation, kernel loading, CLI commands, supported device types, the PHFS filesystem abstraction, and internal limits.

The bootloader prepares the system setup structure and loads the kernel and applications into memory areas
(maps). Its configuration allows customizing functionality to match available hardware resources.

The Phoenix-RTOS loader supports all the target platforms listed in the [Building](../building/index.md) chapter.

```{toctree}
:maxdepth: 1

functionality.md
architecture.md
cli.md
```
