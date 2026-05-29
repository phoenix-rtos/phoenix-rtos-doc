# Build pipeline

After dependency resolution completes, the port manager propagates USE flags,
detects stale build state, and then installs each port by invoking
`port_prepare.sh` and `port_build.sh`. Dependencies are installed before the
ports that require them.

## Pre-install phases

Before installation starts, `cmd_build()` runs two phases:

1. `resolve_propagated_deps()` propagates USE flags across resolved mappings,
   then checks whether any newly activated conditional dependency target is
   absent from a mapping. If absent, it re-resolves that mapping and propagates
   again. The loop repeats until all mappings are complete and no new flags
   appear. This ensures that a chain such as `baz` propagating `ssl` to `foo`,
   which then activates `ssl ? ( bar>=1.0 )`, results in `bar` being added to
   `baz`'s mapping.
2. `clean_stale_ports()` compares the current per-port state against saved
   state files (`.port_state/NAME-VERSION.json`). If a state changed, the port
   and all reverse dependencies are marked stale and cleaned with `port_clean.sh`.

State currently contains:

- `use_flags` (sorted list of active USE flags)
- `tests` (boolean test build mode)

After successful installation, `save_build_state()` writes the current state
for installed ports.

## Installation order

`InstallableCandidate.install()` is called for each user-requested port. Before building
the port itself, the method iterates over the resolved dependency mapping and recursively
installs any uninstalled `InstallableCandidate` dependencies.

Each candidate tracks an `installed` flag. If a dependency appears in multiple resolution
mappings (because several user ports share it), it is built only once.

## Environment setup

Before invoking the shell scripts, the port manager constructs a per-port environment by
copying `os.environ` and adding:

| Variable | Value |
|----------|-------|
| `PREFIX_PORT_INSTALL` | The installation prefix for this port. Equals `PREFIX_BUILD` for non-conflicting ports, or `PREFIX_BUILD_VERSIONED/NAME-VERSION` for conflicting ports. |
| `PORT_DEP_<name>` | For each resolved dependency, set to the dependency's `install_path`. Empty if the dependency was not installed. |
| `PKG_CONFIG_PATH` | Colon-separated list of `lib/pkgconfig` directories from all installed dependencies. |
| `PORT_DEP_LDFLAGS` | Space-separated `-L` flags pointing to `lib/` directories of all installed dependencies. |
| `PORT_USE_<flag>` | Set to `y` for each active USE flag (from `ports.yaml` and propagated dependency flags). |
| `PORT_BUILD_TESTS` | Set to `y` when the port is configured to build tests. |

## Preparation phase (`port_prepare.sh`)

`port_prepare.sh` is the first script invoked for each port. It performs:

1. **Environment reset** (`port_internal.subr:reset_env`): unsets the `DEBUG` variable,
   sets `HOST_TARGET` and `HOST` based on `TARGET_FAMILY`, and configures `CFLAGS`,
   `LDFLAGS`, `STRIP`, and `PORTS_MIRROR_BASEURL`.
2. **Definition loading** (`port_internal.subr:load_port_def`): sources the `port.def.sh`
   file, which populates metadata variables and defines the `p_prepare`, `p_build`, and
   optional `p_common`/`p_build_test` functions.
3. **Source acquisition**: if the port source directory does not exist, downloads and
   extracts the archive (or clones the Git repository), then verifies `sha256` and `size`.
4. **License verification**: checks that the declared `license_file` exists in the
   extracted source tree.
5. **User functions**: calls `p_common()` (if defined) and then `p_prepare()`.
6. **Environment export**: writes the resulting shell environment (null-delimited) to a
   file descriptor, which the Python layer reads back as the build environment for the
   next phase.

### Source verification

`port_prepare.sh` verifies the integrity of downloaded sources by comparing `sha256` and
`size` against the values declared in `port.def.sh`. For archive downloads, the check runs
on the downloaded file. For Git clones, the check runs on a `git archive` tarball of
`HEAD` and a `find`-based file size sum (excluding `.git`).

If either check fails, the work directory is removed and the build is aborted.

## Build phase (`port_build.sh`)

`port_build.sh` runs after preparation completes. It:

1. Sources `port_internal.subr` and loads the port definition.
2. Exports `PREFIX_H` and `PREFIX_A` as the header and library installation directories.
3. Calls `p_common()` if defined.
4. Calls `p_build()`.
5. If `PORT_BUILD_TESTS` is `y`, calls `p_build_test()` (which must be defined if tests
   are enabled).

## Clean phase (`port_clean.sh`)

`port_clean.sh` is invoked only for stale ports, before rebuild. It loads the
same `port.def.sh` metadata and removes the corresponding source build directory:

- `PREFIX_BUILD/port-sources/NAME-VERSION`

This guarantees that stale ports rebuild from a clean source tree.

### Build logging

Both scripts redirect their output through `tee` into log files:

- `port_prepare.sh` appends to a target-global `prepare.log` under `PREFIX_BUILD`.
- `port_build.sh` writes to a per-port `build.log` under `PREFIX_PORT_BUILD`.

The `prepare.log` file is erased at the start of each `build` command invocation to
prevent unbounded growth.

When the terminal is interactive and `RAW_LOG` is not set, the port manager captures
build output into a rolling log panel (rendered with
[rich](https://github.com/Textualize/rich)) that shows the last few lines and highlights
GCC diagnostics.

## Shell helpers (`port.subr`)

The following helper functions are available inside `port.def.sh` executable functions:

`b_port_download(baseurl, filename, [orig_filename])`
: Downloads a file from `baseurl/filename` (or `baseurl/orig_filename` if the upstream
  filename differs from the mirror name). Falls back to `PORTS_MIRROR_BASEURL/filename`
  if the primary download fails. Retries and timeout are controlled by
  `PORTS_DOWNLOAD_RETRIES` (default 5) and `PORTS_DOWNLOAD_TIMEOUT` (default 5).

`b_port_apply_patches(srcdir, [patch_subdir])`
: Applies all `*.patch` files from `PREFIX_PORT_PATCHES/patch_subdir` to `srcdir` using
  `patch -p1`. Tracks applied patches with marker files to avoid reapplying on
  incremental rebuilds.

`b_install_host(file...)`
: Installs host-side executables into `PREFIX_BUILD/host-prog/`.

`b_dependency_dir(dep_name)`
: Returns the installation directory of a required dependency. Aborts if the dependency
  is not installed.

`b_use(flag_name)`
: Returns success when `PORT_USE_<flag_name>` equals `y`.

`b_use_ensure(flag_name, reason)`
: Aborts when a required USE flag is not enabled.
