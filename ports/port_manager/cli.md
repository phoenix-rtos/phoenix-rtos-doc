# CLI and commands

The port manager is invoked as a Python module from the build system. It exposes two
subcommands: `build` and `validate`.

## Invocation

```text
port_manager.py [--dry] [-v] [--quiet] {build,validate} ...
```

### Global options

| Option | Effect |
|--------|--------|
| `--dry` | Skip actual build steps; mark ports as installed without running shell scripts. |
| `-v` | Enable verbose (debug-level) output. |
| `--quiet` | Suppress all output. |

### Environment variables

| Variable | Effect |
|----------|--------|
| `RAW_LOG` | When true, disables the rolling log panel and prints raw build output. |
| `BUILD_ALL_PORTS` | When true, builds every discovered port. |
| `PHOENIX_VER` | Phoenix-RTOS version string (e.g. `v3.3.1`). Used to create the `phoenix` OS candidate for `supports` requirements. |
| `PREFIX_BUILD` | Base installation directory for non-conflicting ports. |
| `PREFIX_BUILD_VERSIONED` | Base installation directory for conflicting ports. Each such port is installed into a subdirectory named `NAME-VERSION`. |

## `build` subcommand

```text
port_manager.py build <ports_yamls> <ports_dir>
```

`ports_yamls`
: Colon-separated list of paths to `ports.yaml` files. Files are loaded in order and
  merged. Later files can override or extend the port list from earlier files.

`ports_dir`
: Path to the directory tree containing `port.def.sh` files.

The `build` command performs the full pipeline:

1. Discovers all port definitions under `ports_dir`.
2. Reads and merges the `ports.yaml` files to determine the requested ports.
3. Resolves dependencies for each requested port independently.
4. Propagates USE flags, re-resolves mappings with newly activated conditional dependencies,
   and repeats until all mappings are complete (`resolve_propagated_deps`).
5. Detects stale port build state and cleans stale ports before rebuild.
6. Installs each port and its dependencies in dependency order.
7. Prints an install summary listing each installed port and its trigger
   (`U` for user requirement, `D:name` for dependency of another port).

### Install summary example

```text
INFO: Install summary:
 * bar-2.0.0 (D:foo-1.2.3)
 * foo-1.2.3 (U)
Trigger legend: 'U' - user requirement, 'D' - dependency
```

## `validate` subcommand

```text
port_manager.py validate <ports_dir>
```

`ports_dir`
: Path to the directory tree containing `port.def.sh` files.

The `validate` command discovers all port definitions and prints their parsed metadata as
JSON to standard output. It does not resolve dependencies or build anything.

Use this command to verify that all `port.def.sh` files in a ports tree parse correctly and
to inspect the discovered candidate set:

```bash
python3 -m port_manager validate phoenix-rtos-ports/
```

The output JSON is keyed by port name, with each value being a dictionary of version
strings to candidate metadata (version, requirements, conflicts, definition path,
`iuse`, `required_use`, and description).
