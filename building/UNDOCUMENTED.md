# Building Documentation — Undocumented Areas

## 1. Compilation Database Generation via `bear`

`phoenix-rtos-build/build.sh` (lines 135–150) automatically detects the `bear` tool and re-executes itself under `bear --append` (or `bear --append --` for bear 3.x) to generate `compile_commands.json`. This provides IDE/LSP support for code navigation. If `bear` is not found, a warning is printed (line 137).

## 2. Git Version Tracking

`phoenix-rtos-build/build.sh` (lines 185–188, 214–215) writes a `git-version` file containing the commit hash, project name, and recursive submodule status via `git submodule status --recursive`. This file is installed into the rootfs at `/etc/git-version` (line 215).

## 3. Sysroot Management (`LIBPHOENIX_DEVEL_MODE`)

Defined in `phoenix-rtos-build/build.sh` (lines 56–62). When `LIBPHOENIX_DEVEL_MODE=y` (the default, line 60):
- Creates `$PREFIX_BUILD/sysroot` with symlinks and structure
- Sets `PREFIX_SYSROOT=$PREFIX_BUILD/sysroot`
- Enables project-specific kernel headers + libphoenix isolation

When disabled (e.g., `phoenix-rtos-build/target/host.mk` line 40 sets it to `n`), the toolchain's built-in sysroot is used. Platform-specific build scripts (e.g., `build-core-armv8m55-stm32n6.sh` line 17) check this variable for custom sysroot setup.

## 4. Rootfs Overlay System

The default chain is: `_fs/root-skel/` → `_fs/$TARGET/root/` → `$PROJECT_PATH/rootfs-overlay` → user-provided `ROOTFS_OVERLAYS` (colon-separated paths). Overlays are applied sequentially. This composable layering mechanism is not documented.

## 5. Three-Level Target Hierarchy

The build system uses a FAMILY → SUBFAMILY → PROJECT hierarchy:
- `_targets/FAMILY/SUBFAMILY/build.project` — architecture-level config
- `_projects/FAMILY-SUBFAMILY-PROJECT/build.project` — board-level config

Functions defined in target/project files are called from main `build.sh` via shell sourcing (inversion of control). Shared logic lives in `_targets/build.common`.

## 6. Makefile.common Framework

`phoenix-rtos-build/makes/` provides a standardized make framework:
- `include-target.mk` — target-specific variable setup
- `setup-tools.mk` — toolchain path resolution
- `setup-sysroot.mk` — sysroot initialization
- `funcs.mk` — build utility functions
- `ports.mk` — port management integration
- `check-env.mk` — validates required variables like `HAVE_MMU` (lines 10–22)
- `check-ports.mk` — port dependency checking
- `binary.mk`, `static-lib.mk` — compilation recipes

Target-specific makefiles in `phoenix-rtos-build/target/` (e.g., `armv7m.mk`, `ia32.mk`, `host.mk`, `sparcv8leon.mk`) set `OLVL`, cross-compiler paths, and architecture flags.

## 7. Optional Build Variables

Undocumented environment variables that affect the build:
- `NOSAN=1` — disables sanitizers for host builds (`phoenix-rtos-build/build.sh` line 224)
- `RAW_LOG=1` — enables raw logging for port builds (`phoenix-rtos-build/build-ports.sh` line 19)
- `WATCHDOG` — enables watchdog support, adds `-DWATCHDOG` to CPPFLAGS (`phoenix-rtos-build/Makefile.common` lines 39–172)
- `OLVL` — optimization level override, defaults to `-O2` per target (e.g., `phoenix-rtos-build/target/ia32.mk` line 14)
- `HAVE_MMU` — controls MMU support, validated as required in `phoenix-rtos-build/makes/check-env.mk` (line 10)

## 8. Cross-Compiler Flag Export

Build exports flags for port cross-compilation:
- `EXPORT_CFLAGS`, `EXPORT_CXXFLAGS`, `EXPORT_LDFLAGS`, `EXPORT_STRIP` — used by port build scripts
- Default parallelism controlled via MAKEFLAGS

## 9. PLO Script System

`b_mkscript_user()` in `_targets/build.common` manages bootloader configuration:
- `PLO_SCRIPT_DIR = $PREFIX_BUILD/plo-scripts/`
- Sources both `preinit.plo.yaml` (target baseline) and `user.plo.yaml` (project override)
- Scripts are generated during build and embedded in the bootloader binary

## 10. macOS Docker Optimization

`docker-build.sh` (lines 11–14) detects Darwin via `uname` and adds `--tmpfs /src/_build:exec,size=2g` to compensate for slow bind mount I/O on macOS. Also applies `chmod 777 "_build"` to fix permissions.

## 11. `.docker_env` Environment Passthrough

Both `docker-build.sh` (lines 19, 25) and `docker-devel.sh` (lines 13, 15) use `--env-file .docker_env` to pass environment variables into the container. This mechanism allows custom build configuration without modifying Docker arguments.

## 12. Port Version Detection

`phoenix-rtos-build/build-ports.sh` detects the Phoenix-RTOS version from git tags via `git describe --tags` (line 28). Sets `PHOENIX_VER` and creates versioned port directories at `PREFIX_BUILD_VERSIONED`.
