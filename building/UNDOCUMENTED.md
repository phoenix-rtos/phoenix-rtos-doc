# Building Documentation — Undocumented Areas

## 1. Compilation Database Generation via `bear`

`build.sh` automatically detects the `bear` tool and re-executes itself under `bear --append` to generate `compile_commands.json`. This provides IDE/LSP support for code navigation and is critical for developer experience.

## 2. Git Version Tracking

The build system writes a `git-version` file containing the commit hash and module status. This file is installed into the rootfs at `/etc/git-version`.

## 3. Sysroot Management (`LIBPHOENIX_DEVEL_MODE`)

When `LIBPHOENIX_DEVEL_MODE=y` (the default):
- Creates `$PREFIX_BUILD/sysroot` with symlinks and structure
- Enables project-specific kernel headers + libphoenix isolation
- Sets `PREFIX_SYSROOT=$PREFIX_BUILD/sysroot`

When disabled, the toolchain's built-in sysroot is used instead. This mechanism is not documented.

## 4. Rootfs Overlay System

The `ROOTFS_OVERLAYS` environment variable supports colon-separated overlay paths. The default chain is:
```
$PROJECT_PATH/rootfs-overlay : ${ROOTFS_OVERLAYS}
```
Overlays are applied on top of the base rootfs from `_fs/$TARGET/root/` and `_fs/root-skel/`.

## 5. Three-Level Target Hierarchy

The build system uses a FAMILY → SUBFAMILY → PROJECT hierarchy:
- `_targets/FAMILY/SUBFAMILY/build.project` — architecture-level config
- `_projects/FAMILY-SUBFAMILY-PROJECT/build.project` — board-level config

Functions defined in target/project files are called from main `build.sh` via shell sourcing (inversion of control).

## 6. Makefile.common Framework

`phoenix-rtos-build/makes/` provides a standardized make framework:
- `include-target.mk` — target-specific variable setup
- `setup-tools.mk` — toolchain path resolution
- `setup-sysroot.mk` — sysroot initialization
- `funcs.mk` — build utility functions
- `ports.mk` — port management integration

## 7. Optional Build Variables

Undocumented environment variables that affect the build:
- `NOSAN=1` — disables sanitizers for host builds
- `RAW_LOG=1` — enables raw logging for ports
- `DEBUG=1` — affects CPPFLAGS for debug builds
- `WATCHDOG` — enables watchdog support
- `OLVL` — optimization level override
- `HAVE_MMU` — controls MMU support in the build

## 8. Cross-Compiler Flag Export

Build exports flags for port cross-compilation:
- `EXPORT_CFLAGS`, `EXPORT_CXXFLAGS`, `EXPORT_LDFLAGS`, `EXPORT_STRIP`
- Default parallelism: `MAKEFLAGS=-j 9`

## 9. PLO Script System

`b_mkscript_user()` in `_targets/build.common` manages bootloader configuration:
- `PLO_SCRIPT_DIR = $PREFIX_BUILD/plo-scripts/`
- Sources both `preinit.plo.yaml` and `user.plo.yaml`
- Target baseline + project-specific overrides

## 10. macOS Docker Optimization

`docker-build.sh` adds `--tmpfs /src/_build:exec,size=2g` on macOS to compensate for filesystem performance overhead. Not mentioned in any documentation.

## 11. `.docker_env` Environment Passthrough

Docker build uses a `.docker_env` file to pass environment variables into the container. This mechanism is not documented.

## 12. Port Version Detection

`build-ports.sh` detects the Phoenix-RTOS version from git tags:
```
git describe --tags --match "v[digit]..."
```
Sets `PHOENIX_VER` and creates versioned port directories at `PREFIX_BUILD_VERSIONED`.
