# Port manager

The port manager (`phoenix-rtos-build/port_manager`) discovers port definitions, resolves
dependencies between ports, and orchestrates the prepare-and-build pipeline for each port
in the correct order. It is the entry point for all port-related operations in the
Phoenix-RTOS build system.

## Architecture

The port manager operates in five phases:

1. **Discovery** scans a ports directory for `port.def.sh` files, parses them into JSON
   with `port_def_to_json.sh`, and registers every port version as a resolver candidate.
2. **Resolution** reads the target `ports.yaml` to determine which ports the user
   requested, then runs a backtracking dependency resolver (based on
   [resolvelib](https://github.com/sarugaku/resolvelib)) to compute a complete,
   conflict-free installation set for each requested port.
3. **USE propagation and conditional re-resolution** propagates dependency USE flags to
   resolved candidates, then re-resolves any mapping whose newly activated conditional
   dependency target is absent, and repeats until all mappings are complete and stable.
4. **Stale rebuild detection** compares the current per-port state (USE flags and test mode)
   to the previous saved state and cleans stale ports, including reverse dependencies.
5. **Installation** walks the resolved dependency graph in topological order, invoking the
   shell scripts `port_prepare.sh` and `port_build.sh` for each port that is not yet
   installed.

## Modules

The port manager package consists of the following Python modules and shell scripts:

| Module | Purpose |
|--------|---------|
| `port_manager.py` | CLI entry point, orchestrates discovery, resolution, and installation. |
| `build_layer.py` | Build system interaction: port discovery I/O, YAML loading, subprocess execution. |
| `resolver.py` | `resolvelib` provider, reporter, and resolver wrapper (`PhxResolver`). |
| `candidates.py` | Candidate types: `Candidate`, `OsCandidate`, `InstallableCandidate`. |
| `requirements.py` | Requirement types: `BaseRequirement`, `ConditionalRequirement`, `ConflictRequirement`. |
| `required_use.py` | `REQUIRED_USE` grammar and validator for USE flag constraints. |
| `version.py` | `PhxVersion` class and `PhxVersionGrammar` parser. |
| `logger.py` | Leveled logger with rolling log display for build output. |
| `port_def_to_json.sh` | Sources a `port.def.sh` and emits its metadata as JSON. |
| `port_prepare.sh` | Downloads, extracts, patches, and prepares the port source tree. |
| `port_build.sh` | Executes the port build functions (`p_build`, `p_build_test`). |
| `port_clean.sh` | Removes a port build tree when stale state is detected. |
| `port.subr` | Shell helpers available inside `port.def.sh` (`b_port_download`, `b_port_apply_patches`, etc.). |
| `port_internal.subr` | Internal helpers for environment reset and `port.def.sh` loading. |

## Table of contents

```{toctree}
:maxdepth: 1

cli.md
resolution.md
build_pipeline.md
```
