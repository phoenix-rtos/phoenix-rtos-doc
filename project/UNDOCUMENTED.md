# Project Documentation — Undocumented Areas

## 1. How to Add a New Target Architecture

No guide for adding a new target to the project. This would require:
- Creating `_projects/<target>/` configuration (build.project, optionally ports.yaml)
- Creating `_targets/<family>/<subfamily>/` build rules
- Creating launch scripts in `scripts/`
- Configuring rootfs overlays in `_fs/<target>/`

## 2. `_projects/` Structure

The relationship between `_projects/` (project-level configuration) and `_targets/` (architecture-level rules) is not documented. Each `_projects/<target>/` contains a `build.project` that defines board-specific functions, and optionally `ports.yaml` for port selection.

## 3. busybox-config Integration

The `busybox_config` file in the project root is not explained. How BusyBox is integrated as a baseline toolkit is undocumented.

## 4. Docker Workflows in Detail

Two distinct Docker workflows exist but neither is documented in detail:
- `docker-build.sh`: Container-based isolated builds, macOS tmpfs optimization (lines 11–14), `.docker_env` passthrough (line 25)
- `docker-devel.sh`: Interactive development with hardware access via privileged mode + USB mount (line 13)

## 5. `compile_commands.json` Generation

IDE integration via compilation database: `phoenix-rtos-build/build.sh` (lines 135–150) detects `bear` and auto-generates `compile_commands.json`. Not documented for users.

## 6. Submodule Versioning and Pinning

How submodule versions are managed, updated, and pinned is not documented. No guidance on updating individual submodules.

## 7. Build Artifact Organization

The relationship and lifecycle of output directories is undocumented:
- `_boot/` — Final bootable images (kernel + apps + rootfs)
- `_build/` — Intermediate build artifacts (object files, libraries, sysroot)
- `_fs/` — Filesystem templates and overlays

## 8. mtd-utils Integration

`mtd-utils/` exists in the project root but its integration with the build system is not documented.

## 9. scripts/ Directory

Launch scripts for various targets follow `./scripts/<target>.sh` naming convention. These automate QEMU/simulator startup but the pattern is not explicitly documented.

## 10. _user/ Example Applications

`_user/` contains example applications: hello, hellocpp, msgmark_client, msgmark_server, rotrectangle, serverdemo, voxeldemo. Has its own `Makefile`. Not referenced in project documentation.
