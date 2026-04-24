# Ports Documentation — Undocumented Areas

## 1. Port Compatibility Matrix

No matrix showing which ports are available/tested for which target architectures. Users cannot determine if a specific port works on their target without trying to build it.

## 2. Port Interdependency Graph

Dependency chains (e.g., `azure_sdk → {openssl, curl, phoenix≥3.3}`) are declared in port definitions but no visual graph or comprehensive listing is provided.

## 3. Conflict Resolution Strategy

How conflicts between ports (e.g., `openssl` vs `openssl111`) are resolved during build is not documented. Precedence rules and error handling are unclear.

## 4. PREFIX_ROOTFS vs PREFIX_FS Distinction

Both variables appear in port build scripts. The distinction between them and when to use each is not explained.

## 5. Stripping Behavior

`PORTS_INSTALL_STRIPPED` affects binary installation. How stripping is applied and its effects on debug capabilities are not documented.

## 6. Platform-Specific Port Availability

Some ports may only work on certain architectures (e.g., ports requiring MMU, specific libc features, or hardware). This information is not charted.

## 7. ports.yaml Evolution

Migration guide for `ports.yaml` format changes is missing. When the format evolves, existing configurations may break without guidance.

## 8. Port Version Requirements

Ports can declare Phoenix-RTOS version requirements (e.g., `phoenix≥3.3`). How version checking works and what happens on mismatch is not documented.

## 9. iuse Variant Flags

While documented at a high level, specific `iuse` flags available for each port and their effects are not listed.

## 10. Port Test Phase

`p_build_test()` is optional. Which ports include tests, how to run them, and interpreting results is undocumented.
