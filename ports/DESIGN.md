# Ports — Design Observations

## Declarative + Imperative Separation

Port definitions (`port.def.sh`) combine:
- **Static metadata**: name, version, source URL, checksums, license, dependencies
- **Executable functions**: `p_prepare()`, `p_build()`, `p_build_test()`

This Bash sourcing pattern provides declarative configuration with imperative customization.

## Reproducibility Emphasis

- SHA256 checksums for source archives
- Version pinning in port definitions
- Precise source URL tracking
- SPDX license identifiers

## Sophisticated Dependency Management

Three dependency types in `port.def.sh`:
- `depends`: Required ports (e.g., `azure_sdk`: `depends="openssl>=1.1.1a curl>=7.64.1"`)
- `optional`: Optional enhancements (all currently empty strings)
- `conflicts`: Mutually exclusive ports (e.g., `openssl111`: `conflicts="openssl3>=0.0"`)

Supports version specifiers via `supports` field (e.g., `supports="phoenix>=3.3"` — used by at least 5 ports).

## Variant System (iuse)

Inspired by Gentoo USE flags / FreeBSD flavors. Currently used by 3 ports:
- `lua/port.def.sh`: `iuse="safe"`
- `micropython/port.def.sh`: `iuse="longtest"`
- `azure_sdk/port.def.sh`: `iuse="longtest"`

Enables custom build configurations per port.

## Environment Injection

Port builds receive the cross-compilation environment via `PREFIX_*` variables:
- `PREFIX_FS`: Filesystem installation path
- `PREFIX_PROG`: Host program installation
- `PREFIX_ROOTFS`: Root filesystem path
- `CROSS_COMPILE`: Tool prefix
- `CONFIG_PREFIX`: Configuration path

## Port Manager (Python)

The modern port building system uses a Python-based `port_manager` tool with Jinja2 templating for `ports.yaml` configuration. This replaces/augments the shell-based approach.

## Test Phase Separation

Optional `p_build_test()` function allows ports to include test suites. Currently implemented by 5 ports: `azure_sdk`, `busybox`, `lua`, `mbedtls`, `micropython`.
