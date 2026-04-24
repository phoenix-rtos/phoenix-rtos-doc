# Building Documentation — Outdated Points

## 1. Primary Build Method Emphasis

**Documentation (`linux.md`):** Docker is already presented first as "the fastest way to start development." Manual toolchain building is a secondary section. This point is **no longer outdated** — the documentation correctly prioritizes Docker.

**Source evidence:** `docker-build.sh` (line 25) and `docker-devel.sh` (line 13) exist with pre-built images (`phoenixrtos/build`, `phoenixrtos/devel`).

**Recommendation:** No change needed; Docker emphasis is already correct.

---

## 2. Supported Target Count

**Documentation lists:** 27 targets in `building/index.md`.

**Current code shows:** 29 targets in `_projects/` directory. Missing from docs:
- `armv7r5f-zynqmp-som`
- `armv8m33-mcxn94x-frdm_cpu1`

**Source evidence:** `ls -d _projects/*/` shows 29 directories.

**Recommendation:** Add the 2 missing targets to the list in `building/index.md`.

---

## 3. Port Building Process

**Documentation says:** Nothing about how ports are built.

**Current code:** Uses a Python-based `port_manager` tool invoked via `python3 -m "port_manager.main"` in `phoenix-rtos-build/build-ports.sh` (line 16). Per-target `ports.yaml` configuration files exist in `_projects/` directories (e.g., `_projects/ia32-generic-qemu/ports.yaml`, `_projects/armv7a7-imx6ull-evk/ports.yaml`). Version detection uses `git describe --tags` (build-ports.sh line 28).

**Recommendation:** Add a section documenting the port building mechanism and `ports.yaml` configuration.

---

## 4. Ubuntu Version Reference

**Documentation says:** "most supported development platform is Linux, particularly Ubuntu 24.04" (`building/index.md`, line 9).

**Current state:** This reference is **accurate** as advisory guidance. Docker abstracts host-specific dependencies, but the native toolchain build instructions target Ubuntu packages.

**Recommendation:** No change strictly needed, but could note Docker eliminates host-specific dependencies.

---

## 5. Component `all` Description

**Documentation claims:** "for ia32-generic-qemu target `all` means `core fs image project ports host`" (`building/index.md`).

**Current code:** `phoenix-rtos-build/build.sh` line 128 defines `all` identically for ALL targets: `B_FS="y"; B_CORE="y"; B_HOST="y"; B_PORTS="y"; B_PROJECT="y"; B_IMAGE="y"`. The description is misleading by specifying a single target when it applies generically.

**Recommendation:** Remove the target-specific framing. State that `all` means `core fs image project ports host` for every target.

---

## 6. HOST_TOOLS Implicit Behavior

**Documentation:** Does not mention that host tools are built automatically for every cross-compilation build.

**Current code:** `phoenix-rtos-build/build.sh` lines 222–224: when `TARGET != host-generic-pc`, the build re-executes with `TARGET=$_TARGET_FOR_HOST_BUILD` (set to `host-generic-pc` at line 24) and `NOSAN=1` to build host utilities.

**Recommendation:** Document the implicit host tools build step.
