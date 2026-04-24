# Project Documentation — Outdated Points

## 1. Repository Links vs Local Submodules

**Documentation (`project/index.md`):** Lists repositories as remote GitHub links.

**Current workspace:** All repositories are local submodules in the workspace directory. The documentation should clarify both the remote origin and the local submodule layout.

**Recommendation:** Document the submodule-based project organization alongside GitHub links.

---

## 2. Missing `compile_commands.json` Reference

**Documentation:** Does not mention `compile_commands.json`.

**Current code:** `phoenix-rtos-build/build.sh` (lines 135–150) generates `compile_commands.json` via `bear` for IDE/LSP support. The file exists at the project root.

**Recommendation:** Document IDE integration via compilation database.

---

## 3. Build Entry Points Not Documented

**Documentation:** Does not explain the build entry point.

**Current code:** The project root contains only `build.project` (no Makefiles). Building is done via `./phoenix-rtos-build/build.sh` which sources `build.project`. Individual submodules have their own Makefiles (e.g., `phoenix-rtos-tests/Makefile`, `phoenix-rtos-tests/Makefile.host`, `phoenix-rtos-tests/Makefile.riscv64`), but at the project level, the shell-based build system is the sole entry point.

**Recommendation:** Document `build.project` as the project-level build configuration and clarify there are no project-root Makefiles.

---

## 4. Docker Workflow Not Detailed

**Documentation:** Mentions Docker but does not detail the build/development workflow.

**Current code:** Two Docker scripts:
- `docker-build.sh` — isolated artifact generation with macOS tmpfs optimization (lines 11–14), `.docker_env` passthrough (line 25)
- `docker-devel.sh` — interactive development with USB access at `/dev/bus/usb` (line 13), privileged mode

**Recommendation:** Document both Docker workflows with their differences.
