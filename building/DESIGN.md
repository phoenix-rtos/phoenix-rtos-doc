# Building System — Design Observations

## Three-Level Target Hierarchy

```
FAMILY (arm, ia32, riscv64, sparc, etc.)
  └─ SUBFAMILY (a7, a9, generic, etc.)
      └─ PROJECT (qemu, zedboard, som, etc.)
```

This allows shared architecture code at the FAMILY level, variant-specific code at the SUBFAMILY level, and board/configuration-specific code at the PROJECT level.

## Inversion of Control via Shell Sourcing

```
build.project (top-level)
  → sources _targets/FAMILY/SUBFAMILY/build.project
  → sources _projects/TARGET/build.project
  → calls b_build(), b_image(), etc.
```

Functions defined in target/project files are called from the main `build.sh`. The orchestrator is platform-agnostic; all specialization lives in the sourced files.

## Dual-Phase Build for Host Tools

When `TARGET != host-generic-pc`, the build re-executes with `TARGET=host-generic-pc` first. This ensures host utilities are built with native tools, preventing cross-compilation issues.

## Docker Abstraction

Two distinct Docker workflows:
- **`docker-build.sh`**: Build artifacts in isolation — read-only mounts, dropped privileges
- **`docker-devel.sh`**: Interactive development — privileged mode, USB access at `/dev/bus/usb`

## Rootfs Composition Chain

```
_fs/root-skel/          → default skeleton
_fs/$TARGET/root/       → target-specific overlay
$PROJECT_PATH/rootfs-overlay  → project-specific overlay
${ROOTFS_OVERLAYS}       → user-provided overlays
```

Multiple overlay layers compose the final root filesystem. This pattern supports both platform and project customization.

## Versioned Ports Directory

```
PREFIX_BUILD_VERSIONED = ${PREFIX_BUILD}/versioned-ports/
PHOENIX_VER extracted from git tags
```

Ports are built into versioned directories, allowing multiple Phoenix-RTOS versions to coexist during development.

## Compilation Database Integration

The build uses `bear` to automatically capture compiler invocations and produce `compile_commands.json`. This enables IDE features (code navigation, error highlighting) without manual configuration.

## Makefile Common Framework

Centralized in `phoenix-rtos-build/makes/`, this provides consistent compilation environment across all targets: standard toolchain selection, sysroot initialization, and build utility functions.
