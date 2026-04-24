# Building Documentation — Outdated Points

## 1. Primary Build Method Emphasis

**Documentation says:** Significant space devoted to building toolchains from source on Linux, implying it is the primary workflow.

**Current code reality:** Docker-based builds (`docker-build.sh`, `docker-devel.sh`) are the primary method. Pre-built Docker images (`phoenixrtos/build`, `phoenixrtos/devel`) include toolchains. Manual toolchain building is a secondary, advanced path.

**Recommendation:** Reposition Docker as the primary build method and demote manual toolchain building to an advanced/optional section.

---

## 2. Supported Target Count

**Documentation lists:** ~24 targets.

**Current code shows:** 29 targets in `_projects/` directory. Missing from docs:
- `armv7r5f-zynqmp-som`
- `armv8m33-mcxn94x-frdm_cpu1`
- `armv7a9-zynq7000-zedboard`
- `armv7a9-zynq7000-zturn`
- `riscv64-generic-spike`

**Recommendation:** Update the target list in `index.md` to reflect all 29 build targets.

---

## 3. Port Building Process

**Documentation says:** Nothing about how ports are built.

**Current code:** Uses a Python-based `port_manager` tool (`python3 -m "port_manager.main"`) with `ports.yaml` configuration per target. `build-ports.sh` has version detection and git integration.

**Recommendation:** Add a section documenting the port building mechanism and `ports.yaml` configuration.

---

## 4. Ubuntu Version Reference

**Documentation says:** "Most supported development platform is Linux, particularly Ubuntu 24.04."

**Current code:** Docker approach abstracts the host platform; no version-specific dependencies in the build scripts.

**Recommendation:** Clarify that Docker eliminates host-specific dependencies and Ubuntu version is advisory only.

---

## 5. Component Dependencies Description

**Documentation claims:** "for ia32-generic-qemu target all means `core fs image project ports host`."

**Current code:** All targets use the same `all` logic defined in `build.sh`. The description should apply generically, not to a single target.

**Recommendation:** Clarify that `all` components are consistent across targets.

---

## 6. HOST_TOOLS Implicit Behavior

**Documentation:** Does not mention that host tools are built automatically for every cross-compilation build.

**Current code:** `build.sh` always re-execs with `TARGET=host-generic-pc` to build host utilities (metaelf, phoenixd, psdisk, psu, syspagen, mcxisp, mkrofs).

**Recommendation:** Document the implicit host tools build step.
