# Project — Design Observations

## Monorepo with Submodules

Balances modularity with integrated development. Each component (kernel, drivers, filesystems, etc.) is an independent git repository, aggregated via submodules in `phoenix-rtos-project`. This allows:
- Independent version control per component
- Integrated build across all components
- Single checkout for complete development environment

## Multi-Target Architecture

The project infrastructure supports 29 target architectures (in `_projects/`) across 13 architecture families (in `_targets/`) through:
- `_targets/`: Per-architecture build rules (DRY via `build.common`)
- `_projects/`: Per-target project configuration (each contains `build.project`)
- `scripts/`: Per-target launch scripts (15 scripts for QEMU/simulator targets)
- `_fs/`: Per-target filesystem templates and overlays

## Hierarchical Build Rules

```
_targets/build.common          → Shared build functions
_targets/FAMILY/SUBFAMILY/     → Architecture-specific rules
_projects/TARGET/              → Board/project-specific configuration
```

Follows DRY principle: common logic shared, specialized logic isolated.

## Separation of Concerns

```
_user/       → User applications (examples, demos)
libphoenix/  → Standard C library
phoenix-rtos-kernel/  → Microkernel
phoenix-rtos-devices/ → Device drivers
phoenix-rtos-filesystems/ → Filesystem servers
phoenix-rtos-posixsrv/ → POSIX emulation
phoenix-rtos-lwip/   → Network stack
phoenix-rtos-usb/    → USB stack
phoenix-rtos-utils/  → System utilities
phoenix-rtos-tests/  → Test suite
phoenix-rtos-ports/  → Third-party software
phoenix-rtos-build/  → Build infrastructure
phoenix-rtos-corelibs/ → Reusable libraries
phoenix-rtos-hostutils/ → Host development tools
plo/                 → Bootloader
```

## Documentation as Submodule

`phoenix-rtos-doc` is tracked as a submodule, enabling versioned documentation that can be tied to specific code releases.

## Build Flexibility

Multiple entry points for building:
- Shell scripts (`phoenix-rtos-build/build.sh`, `docker-build.sh`, `docker-devel.sh`)
- Project configuration files (`build.project` at root and per-target in `_projects/`)
- Docker containers (build and development modes)
- IDE integration via auto-generated `compile_commands.json` (bear detection in `build.sh` lines 135–150)
