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

Three dependency types:
- `depends`: Required ports
- `optional`: Optional enhancements
- `conflicts`: Mutually exclusive ports

Supports version specifiers (e.g., `phoenix>=3.3`).

## Variant System (iuse)

Inspired by Gentoo USE flags / FreeBSD flavors:
```bash
iuse="flag1 flag2"
```
Enables custom build configurations per port, allowing the same port to be built with different feature sets.

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

Optional `p_build_test()` function allows ports to include test suites that can be built and run independently from the main port build.
