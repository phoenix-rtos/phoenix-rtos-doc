# Quickstart — Design Observations

## Build-Artifact Assumption

The quickstart workflow assumes pre-built artifacts in `_boot/`. It is a post-build step that focuses on launching and interacting with the system, not building it.

## Target Uniformity

All targets follow the same script-based launch pattern (`./scripts/TARGET.sh`), enabling consistent workflow across 20+ architectures. This uniformity lowers the learning curve when switching between targets.

## Emulation-First Development

QEMU integration for multiple architectures enables rapid iteration without physical hardware. Targets like `ia32-generic-qemu`, `riscv64-generic-qemu`, `armv7a9-zynq7000-qemu` provide zero-hardware-cost development.

## Output Directory Organization

```
_boot/$TARGET/   → Final bootable images (kernel + apps + rootfs)
_build/$TARGET/  → Intermediate build artifacts (object files, libraries)
_fs/$TARGET/     → Filesystem templates and overlays
```

This separation allows clean rebuilds and target isolation.

## Progressive Complexity

Example applications in `_user/` range from simple (hello) to advanced (voxeldemo, serverdemo), providing a learning path for new developers.
