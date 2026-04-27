# Utilities

This chapter describes the Phoenix-RTOS system utilities. After reading this chapter, you will know:

- How to use the Phoenix Shell (psh) and its applets.
- The available standalone utilities.
- How to add custom psh applets to the build.

The source code is in the
[phoenix-rtos-utils](https://github.com/phoenix-rtos/phoenix-rtos-utils) GitHub repository.

## psh (Phoenix-RTOS Shell)

Phoenix-RTOS shell provides a UNIX-like command-line shell with built-in applets. See the
[psh documentation](psh/index.md) for details.

## Standalone Utilities

| Utility | Purpose |
|---|---|
| `psd` | Phoenix Serial Downloader  -  SDP protocol for NXP microcontrollers |
| `nandtool` | NAND flash programming and erasing tool |
| `cm4-tool` | Communication tool for i.MX RT117x Cortex-M4 server |
| `gsm` | Gateway/Serial Module tool |
| `spitool` | SPI interface tool |
| `metacheck` | Metadata validation tool |
| `meterfs-migrate` | MeterFS data migration utility |
| `nandpart` | NAND flash partition tool |
| `benchmarks` | Performance benchmark suite |

```{toctree}
:maxdepth: 1

psh/index.md
psd.md
```
