# Ports Documentation — Undocumented Areas

## 1. Port Compatibility Matrix

No matrix showing which ports are available/tested for which target architectures. Users cannot determine if a specific port works on their target without trying to build it.

## 2. Port Interdependency Graph

Dependency chains are declared in `port.def.sh` files via `depends`, `optional`, and `conflicts` fields. For example:
- `azure_sdk/port.def.sh` (line 23): `depends="openssl>=1.1.1a curl>=7.64.1"`
- `openssl111/port.def.sh` (line 21): `conflicts="openssl3>=0.0"`

No visual graph or comprehensive listing of the dependency network is provided.

## 3. Conflict Resolution Strategy

Conflicts are declared per-port (e.g., `openssl111/port.def.sh` line 21: `conflicts="openssl3>=0.0"`). How the build system enforces mutual exclusion and what errors appear on violation is not documented.

## 4. PREFIX_ROOTFS vs PREFIX_FS Distinction

Both variables appear in port build scripts. The distinction between them and when to use each is not explained.

## 5. Stripping Behavior

`PORTS_INSTALL_STRIPPED` is checked in port build scripts (e.g., `busybox/port.def.sh` line 45: `if [ -n "$PORTS_INSTALL_STRIPPED" ] && [ "$PORTS_INSTALL_STRIPPED" = "n" ]`). How stripping is applied by default and its effects on debug capabilities are not documented.

## 6. Platform-Specific Port Availability

Some ports may only work on certain architectures (e.g., ports requiring MMU, specific libc features, or hardware). This information is not charted.

## 7. ports.yaml Evolution

Migration guide for `ports.yaml` format changes is missing. When the format evolves, existing configurations may break without guidance.

## 8. Port Version Requirements

Ports declare version requirements via `supports` field (e.g., `lzo/port.def.sh` line 25: `supports="phoenix>=3.3"`). At least 5 ports use this. How version checking is enforced and what happens on mismatch is not documented.

## 9. iuse Variant Flags

Only 3 ports use `iuse`:
- `lua/port.def.sh` (line 25): `iuse="safe"`
- `micropython/port.def.sh` (line 27): `iuse="longtest"`
- `azure_sdk/port.def.sh` (line 28): `iuse="longtest"`

The effects of these flags and how to activate them are not documented.

## 10. Port Test Phase

`p_build_test()` is implemented in 5 ports: `azure_sdk`, `busybox`, `lua`, `mbedtls`, `micropython`. How to invoke the test phase, expected output format, and how results are interpreted is undocumented.
