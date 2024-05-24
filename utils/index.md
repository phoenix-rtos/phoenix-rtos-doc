# Utilities

Phoenix-RTOS utilities are functional tools used by the system, similar to the
[host utilities](../hostutils/index.md), which are used by the host computer.

The source code of host utilities is placed in the
[phoenix-rtos-utils](https://github.com/phoenix-rtos/phoenix-rtos-utils)
GitHub repository. If you don't know what are `phoenix-rtos` repositories you can check the
[reference project repository](../building/project.md) chapter.

## Components

There are following utilities:

- [Phoenix-RTOS shell](psh/index.md), called `psh`,
- [Phoenix-RTOS serial downloader](psd.md), called `psd`,
- The programming/erasing tool for `NAND` flash memory, called `nandtool`,
- The tool for communication with `imxrt117x-cm4` server, called `cm4-tool`

## See also

1. [Table of Contents](../index.md)

```{toctree}
:hidden:
:maxdepth: 1

psh/index.md
psd.md
```
