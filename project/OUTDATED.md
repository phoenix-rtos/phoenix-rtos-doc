# Project Documentation — Outdated Points

## 1. Repository Links vs Local Submodules

**Documentation:** Lists repositories as remote GitHub links.

**Current workspace:** All repositories are local submodules in the workspace directory. The documentation should clarify both the remote origin and the local submodule layout.

**Recommendation:** Document the submodule-based project organization alongside GitHub links.

---

## 2. Missing `compile_commands.json` Reference

**Documentation:** Does not mention `compile_commands.json`.

**Current code:** The build system generates `compile_commands.json` via `bear` for IDE/LSP support. This is critical for developer experience.

**Recommendation:** Document IDE integration via compilation database.

---

## 3. Missing Makefile Variants

**Documentation:** Does not mention alternative Makefiles.

**Current code:** Multiple Makefile variants exist: `build.project`, `Makefile`, `Makefile.riscv64`, `Makefile.sparcv8leon`.

**Recommendation:** Explain the purpose of each Makefile variant.

---

## 4. Docker Workflow Not Detailed

**Documentation:** Mentions Docker but does not detail the build/development workflow.

**Current code:** Two Docker scripts (`docker-build.sh`, `docker-devel.sh`) with distinct purposes:
- Build: Isolated artifact generation
- Devel: Interactive development with USB access

**Recommendation:** Document both Docker workflows.
