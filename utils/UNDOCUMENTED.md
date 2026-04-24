# Utilities Documentation — Undocumented Areas

## 1. Completely Undocumented Utilities

The following exist in `phoenix-rtos-utils/` with no documentation:

### benchmarks — Performance Benchmarks
Source: `phoenix-rtos-utils/benchmarks/`. No documentation.

### gsm — Gateway/Serial Module Tool
Source: `phoenix-rtos-utils/gsm/`. No documentation.

### spitool — SPI Interface Tool
Source: `phoenix-rtos-utils/spitool/`. No documentation.

### metacheck — Metadata Validation Tool
Source: `phoenix-rtos-utils/metacheck/`. No documentation.

### meterfs-migrate — MeterFS Migration Utility
Source: `phoenix-rtos-utils/meterfs-migrate/`. No documentation.

### nandpart — NAND Partition Tool
Source: `phoenix-rtos-utils/nandpart/`. No documentation.

## 2. Undocumented PSH Applets

### chmod
File permission modification. Directory exists with implementation but no markdown documentation page.

### hd
Hex dump utility. Directory exists with implementation but no documentation.

### route
Routing table management. Directory exists with implementation but no documentation.

## 3. Undocumented PSH Architecture

### Auto-Registration Mechanism
Applets use `__attribute__((constructor))` to register themselves at load time. Verified in source:
- `psh/cat/cat.c` line 123: `void __attribute__((constructor)) cat_registerapp(void)`
- `psh/mem/mem.c` line 355: `void __attribute__((constructor)) mem_registerapp(void)`
- `psh/sync/sync.c` line 49: `void __attribute__((constructor)) sync_registerapp(void)`

### Symlink Invocation Pattern
PSH can be invoked via symlinks — the binary checks `argv[0]` to determine which applet to run. This allows individual commands to appear as standalone executables.

### History Buffer Implementation
- 512-entry circular buffer
- ~128 bytes per entry
- Not configurable at runtime

### Custom Applet Plugin System
`PSH_PROJECT_DEPS` make variable allows project-specific applets to be added to the PSH build. Build selection via:
```makefile
PSH_COMMANDS ?= $(PSH_ALLCOMMANDS)  # Default: all applets
PSH_INTERNAL_APPLETS := pshapp help $(filter $(PSH_ALLCOMMANDS), $(PSH_COMMANDS))
PSH_LINK_APPLETS := $(PSH_COMMANDS) pshlogin
```
This enables per-target customization.

### Authentication System
`auth.c` in `pshapp/` handles authentication. `pshlogin` applet provides login functionality. Not documented beyond existence in applet list.

### Environment Variable Handling
`env.c` in `pshapp/` manages `export` and `unset` operations. Environment propagation and scope rules are not documented.

### Interactive vs Script Modes
PSH supports both interactive and script modes, but the distinction and behavior differences are not documented.

## 4. Missing Developer Guide

No documentation on:
- How to create a new PSH applet
- The required function naming convention (`psh_<cmd>info()`, `psh_<cmd>()`)
- How to add applets to the build system
- How the registration system works internally
