# Project Documentation — Undocumented Areas

## 1. How to Add a New Target Architecture

No guide for adding a new target to the project. This would require:
- Creating `_projects/` configuration
- Creating `_targets/` build rules
- Creating launch scripts
- Configuring rootfs overlays

## 2. `_projects/` Structure

The relationship between `_projects/` (project-level configuration) and `_targets/` (architecture-level rules) is not documented.

## 3. busybox-config Integration

The `busybox_config` file in the project root is not explained. How BusyBox is integrated as a baseline toolkit is undocumented.

## 4. Docker Workflows in Detail

- `docker-build.sh`: Container-based isolated builds
- `docker-devel.sh`: Interactive development with hardware access
- `.docker_env`: Environment variable passthrough
- macOS tmpfs optimization

None of these are documented in detail.

## 5. Per-Architecture Makefile Variants

`Makefile.riscv64`, `Makefile.sparcv8leon` exist alongside the main `Makefile`. Their purpose (likely toolchain-specific build entry points) and when to use them is undocumented.

## 6. `compile_commands.json` Generation

IDE integration via compilation database is automatically generated during builds but not documented for users.

## 7. Submodule Versioning and Pinning

How submodule versions are managed, updated, and pinned is not documented. No guidance on updating individual submodules.

## 8. Build Artifact Organization

The relationship and lifecycle of output directories is undocumented:
- `_boot/`: Final images
- `_build/`: Intermediate artifacts
- `_fs/`: Filesystem templates

## 9. mtd-utils Integration

`mtd-utils/` exists in the project root but its integration with the build system is not documented.

## 10. scripts/ Directory

Launch scripts for various targets (QEMU, simulators) follow a naming convention that is not explicitly documented.
