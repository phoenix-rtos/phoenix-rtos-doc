# Advanced Build Options

This section describes build system features beyond the basic `build.sh` invocation.

## Build Output Directories

| Directory | Purpose |
|---|---|
| `_boot/<target>/` | Final bootable images (kernel + apps + rootfs) |
| `_build/<target>/` | Intermediate build artifacts (object files, libraries, sysroot) |
| `_fs/<target>/` | Filesystem templates and overlays |

## IDE Integration (compile_commands.json)

The build system automatically generates a `compile_commands.json` compilation database when the `bear` tool is
installed. This file enables code navigation and completion in editors that support the LSP protocol (VS Code,
CLion, Vim with clangd, etc.).

To use this feature, install `bear`:

```shell
sudo apt install bear
```

The build script detects `bear` automatically and re-executes the build under it. The resulting
`compile_commands.json` is placed at the project root.

## Git Version Tracking

Each build produces an `/etc/git-version` file in the root filesystem. This file contains the git commit hash of the
project at build time and can be used for firmware version identification.

## Build Variables

The following environment variables affect the build:

| Variable | Default | Description |
|---|---|---|
| `TARGET` | (required) | Target platform, e.g. `ia32-generic-qemu` |
| `CONSOLE` | (unset) | Set to `serial` to enable serial console output |
| `LIBPHOENIX_DEVEL_MODE` | `y` | Creates sysroot for development when enabled |
| `NOSAN` | (unset) | Disables sanitizers when set (used for host tools) |
| `OLVL` | `-O2` | Compiler optimization level |
| `HAVE_MMU` | (per-target) | Set automatically; indicates MMU-capable platforms |
| `RAW_LOG` | (unset) | Set to `1` to see raw port build output |
| `LONG_TEST` | (unset) | Set to `y` to enable long-running port tests |

## Host Tools Auto-Build

When building for a non-host target, the build system automatically re-executes itself with
`TARGET=host-generic-pc` to build the host utilities needed for image creation. The following tools are built:

- `metaelf` — ELF metadata embedder
- `phoenixd` — host communication daemon
- `psdisk` — disk image tool
- `psu` — serial uploader
- `syspagen` — system page generator
- `mcxisp` — MCX ISP tool
- `mkrofs` — ROFS image creator

## Port Manager

Third-party software ports are built using a Python-based port manager tool. The build script invokes it as:

```shell
python3 -m "port_manager.main"
```

Port selection is configured via `ports.yaml` files in each target's `_projects/<target>/` and `_targets/<target>/` directories.

For instructions on how to pick ports to install when building Phoenix-RTOS, see
{doc}`ports_yaml`.