# Loader (plo)

This chapter describes the Phoenix-RTOS bootloader (plo). After reading this chapter, you will know:

- How the loader prepares hardware and loads the kernel.
- The available CLI commands and their usage.
- The device types supported by the loader.
- The PHFS filesystem abstraction and its protocols.
- Internal limits for commands, devices, and aliases.

The bootlader is an inherent part of Phoenix-RTOS used to prepare the system setup structure and load the kernel and
applications to selected memory areas defined as maps. The loader configuration is flexible and allows the user to
customize appropriate sets of functionality depending on hardware resources.

The Phoenix-RTOS loader supports all the target platforms listed in the [Building](../building/index.md) chapter.

```{toctree}
:maxdepth: 1

functionality.md
architecture.md
cli.md
```
