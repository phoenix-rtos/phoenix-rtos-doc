# Quickstart Documentation — Undocumented Areas

## 1. How to Add a New Target

No guide for adding a new target to the quickstart system (creating `_projects/` config, `_targets/` rules, launch scripts).

## 2. Root Filesystem Contents

The contents and organization of the root filesystem (`_fs/`) are not explained. Users cannot determine what's available on a booted system without inspecting the filesystem.

## 3. `_boot/` vs `_build/` vs `_fs/` Relationships

Three output directories exist but their purposes and relationships are not documented:
- `_boot/`: Final boot images
- `_build/`: Intermediate build artifacts
- `_fs/`: Filesystem templates and overlays

## 4. Networking Setup for QEMU

How to set up networking (bridge, TAP, user-mode) for QEMU targets is not covered.

## 5. Persistent Storage for Emulation

Disk image management for QEMU (creating, resizing, formatting disk images for ext2 or other filesystems) is undocumented.

## 6. Early Boot Debugging

How to debug issues before the shell prompt appears (PLO serial console, kernel debug output, JTAG attachment) is not covered.

## 7. Custom Configuration Workflow

How to modify the system and rebuild during development iteration (incremental builds, changing rootfs contents, modifying boot scripts) is undocumented.

## 8. User Application Examples

The `_user/` directory contains example applications with its own `Makefile`:
- `hello` — C hello world
- `hellocpp` — C++ hello world
- `msgmark_client` / `msgmark_server` — message passing benchmark
- `rotrectangle` — graphics demo
- `serverdemo` — server pattern example
- `voxeldemo` — 3D voxel rendering demo

These are not referenced in the quickstart documentation.

## 9. Multi-core Launch

Multi-core support is mentioned but how to verify multi-core operation and configure core count is not explained.
