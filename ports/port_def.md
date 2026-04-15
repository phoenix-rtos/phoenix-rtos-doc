# Port definition (port.def.sh) specification

This document serves as a formal representation of the **Ports API 1** interface.

The `port.def.sh` file is a declarative manifest and build script used by the
Phoenix-RTOS port management tooling. It defines how a third-party application
should be fetched, configured, built, and integrated into the Phoenix-RTOS.

This format is designed to be sourced directly by Bash scripts invoked
internally by the build system during port discovery and dependency resolution.

The `port.def.sh` file contains two parts: a static section that supplies the
build system with essential metadata about the port, and an executable section
that implements the functions responsible for preparing, patching, building, and
installing the port.

## Static section

All static fields must be defined, unless stated otherwise.

### Identification

`ports_api`
: Version of the port manager API this script supports.

  Currently supported API versions: `1`.

`name`
: Case-sensitive unique identifier for the port, usually a package name (e.g. `busybox`).

`version`
: Version of the port, usually derived from the upstream version.

  Must follow [Python Version
  specifiers](https://packaging.python.org/en/latest/specifications/version-specifiers/)
  scheme.

`desc` (optional)
: A short, human-readable description of the ported package.

### Source acquisition & verification  

A port definition can either pull the source from an archive file or from a Git
repository (options are mutually exclusive):

* If pulling from an archive file, it must supply:

  `source`
  : Base URL where the source is hosted.

  `archive_filename`
  : The name of the downloaded archive file. The download will be attempted from
  the `${source}/${archive_filename}` URL and if that fails, then the mirror
  will be tried (e.g. `https://files.phoesys.com/ports/${archive_filename}`).
  This field can be either a single string or a two-element Bash array where the
  first element is the archive file name for the mirror repository and the
  second is for the `source` URL. The second option is provided in case the
  archive names differ - for example, the expected name under the `source` URL
  for the `foo` port could be `v3.2.1.tar.gz`, but on the mirror it is
  `foo-3.2.1.tar.gz`.

* If pulling from a Git repository, it must supply:

  `git_source`
  : URL of Git repository from which to pull the source.

  `git_rev`
  : Git revision to pull.

Currently, only a single archive file/repository to pull can be defined per port
definition.

The rest of the fields are common to both cases:

`src_path`
: Path to a source tree in the archive/repository, relative to
archive/repository root. For example, when extraction of `./somepkg-1.27.tar.gz`
creates a directory `./somepkg-1.27-src` that contains the source of `somepkg`,
then `src_path="somepkg-1.27-src"`.

`sha256`
: An expected SHA256 checksum of the downloaded archive, obtained through

  ```bash
  sha256sum | cut -d' ' -f1
  ```

  or of the cloned repository, obtained through

  ```bash
  git archive --format=tar HEAD | sha256sum | cut -d' ' -f1
  ```

`size`
: Size (in bytes) of the downloaded archive or the git repository excluding `.git`.

### Licensing

`license`
: The [SPDX identifier](https://spdx.org/licenses/) for the software license (e.g., `GPL-2.0-only`).

`license_file`
: Path to the license file within the source tree.

### Requirements

`supports`
: Defines OS compatibility requirements (e.g., `phoenix>=3.3` defines
  compatibility with Phoenix-RTOS release 3.3 and higher).

`depends`
: Defines mandatory dependencies on other ports (e.g. `openssl>=1.1.1`, enforces
  that OpenSSL >=1.1.1 will be installed prior to the port).

`optional`
: Like `depends`, but will build the dependency only if it is explicitly enabled
  in the [ports.yaml configuration file](./ports_yaml.md).

`conflicts`
: Expresses conflicts with other ports that provide the same functionality (e.g.
  OpenSSL 3.0 can conflict with OpenSSL 1.1.1, but both are commonly used
  today).

(port_def_variant_flags)=

### Variant flags

A similar behaviour to FreeBSD
[flavors](https://docs.freebsd.org/en/books/porters-handbook/flavors/) and
Gentoo's [USE flags](https://wiki.gentoo.org/wiki/USE_flag) can be achieved
using `iuse` coupled with helpers like {func}`b_use()`.

`iuse`
: List of flags exported by the port. For example, `iuse="longtest safe"` declares that
  a given port supports two flags, `longtest` and `safe`, that alter the build
  process.

## Executable section

Aside from static section, the `port.def.sh` must supply the implementation
of functions necessary for the actual port installation.

After sourcing the static section, the build system executes the following
functions sequentially:

````{function} p_common() (optional)
Initial phase - should be used, e.g. for exporting common
variables/functions to be used across the remaining functions.
````

````{function} p_prepare()
Port preparation phase - place for patching, initializing the port
build (autoconf, CMake, bootstrap, etc.).
````

````{function} p_build()
Port building and installation phase invoked after {func}`p_prepare()`. Any
`make`, {func}`b_install` commands must go here.
````

````{function} p_build_test() (optional)
Port tests building phase, invoked after {func}`p_build()` when the port is
built with tests enabled. Any `make`, {func}`b_install` commands for building
port tests must go here.
````

## Provided environment in the executable section

The build system provides the following environment for the use in the
executable section implementation.

### Variables

`STRIP`
: Target-specific binary stripper

`CROSS`
: The cross-compiler prefix (e.g., `arm-phoenix-`).

`PREFIX_PORT`
: The directory containing the `port.def.sh` file.

`PREFIX_PORT_WORKDIR`
: Absolute path (based on declared `src_path`) to the directory where port source
tree is extracted.

`PREFIX_PORT_INSTALL`
: Points to the target installation directory (potentially different for various
  ports, depending on whether they conflict with each other). Can be an arbitrary
  path.

`PREFIX_H`
: Points to the target include directory where the headers should be installed.

`PREFIX_A`
: Points to the target library directory where the libraries should be installed.

`PREFIX_FS`
: The root of the Phoenix-RTOS `rootfs` partition.

`PREFIX_PROG`
: The destination directory for built binaries.

`PREFIX_STRIPPED`
: The destination directory for stripped built binaries.

`PREFIX_PROG_TO_INSTALL`
: Variable equal to either `PREFIX_PROG` or `PREFIX_PROG_STRIPPED`, depending on
  whether to install stripped binaries. Usually used as an argument to
  {func}`b_install()`.

### Helper functions

````{function} b_port_apply_patches(srcdir, [patch_subdir])

Applies patches to the source tree located in ``srcdir``. This function is
non-recursive; if patches are organized into subdirectories, call this function
multiple times with the appropriate ``patch_subdir``.

Looks for files ending in ``*.patch`` within
``${PREFIX_PORT}/patches/${patch_subdir}``.

To prevent double-patching, the function creates a marker file for every
successfully applied patch. 

:param srcdir: The absolute path to the extracted source code (usually
``$PREFIX_PORT_WORKDIR``).
:param patch_subdir: (Optional) A subdirectory within the port's ``patches/``
folder. Defaults to ``.`` (the root of the patches folder).

Example:
  ```bash
  p_prepare() {
     # Apply patches from the root ./patches directory
     b_port_apply_patches "${PREFIX_PORT_WORKDIR}"

     # Apply architecture-specific patches from ./patches/arm
     b_port_apply_patches "${PREFIX_PORT_WORKDIR}" "arm"
  }
  ```
````

````{function} b_dependency_dir(dep_name)

Returns the installation directory of a required dependency named `dep_name`. 

If the dependency is not installed, the function aborts the installation
process.

:param dep_name: The name of the optional dependency to query (e.g. `openssl`).
````

````{function} b_optional_dir(dep_name)

Returns the installation directory of an optional dependency named `dep_name`. 

If the optional dependency is not installed, the function returns an empty
string.

:param dep_name: The name of the optional dependency to query (e.g. `openssl`).
````

The installation directory returned by `b_dependency_dir()` and
`b_optional_dir()` serves as the root for `lib` and `include` directories
containing the dependency's libraries and headers.

````{function} b_use(flag_name)
Returns 0 (success) if the specified flag is enabled, and a non-zero value
otherwise.

This is typically used in conditional logic within port functions to check if
optional features or configurations have been toggled on by the user or the
system.

:param flag_name: The name of the flag to check.

Example:
```bash
local conf_args=()
if b_use "x11"; then
   conf_args+=("--with-x")
fi
```
````

````{function} b_use_ensure(flag_name, reason)
Ensures that a specific flag is enabled. If the flag is not enabled, the
function terminates the build process with an error message indicating the
required flag and the reason it is needed.

:param flag_name: The name of the flag to verify.
:param reason: A descriptive string explaining why this flag is mandatory for
the current operation.
````

````{function} b_install(*filelist, dstdir)
Installs one or more files into the target filesystem directory. The destination
path is relative to the package root (`${PREFIX_FS}/root/`).

The function creates the destination directory if it does not exist and verifies
that each source file is present before attempting installation. Files are
installed with executable permissions (`755`).

:param *filelist: One or more absolute paths to the source files to be
installed.
:param dstdir: The destination directory path (relative to the target root)
where the files should be placed.

Example:
  ```bash
  # Install lua, luac to /usr/bin
  b_install "${PREFIX_PROG_TO_INSTALL}/lua" /usr/bin

  # Install multiple lua tests to /usr/share/lua/tests
  b_install "${lua_test_dir}"/*.lua /usr/share/lua/tests
  ```
````

````{function} b_install_host(*filelist)
Installs one or more executable files into the host-specific build directory
(e.g. `${PREFIX_BUILD}/host-prog/`). This is typically used for build-time tools
(like code generators or custom compilers) that need to be executed on the host
system during the cross-compilation process.

The function ensures the destination directory exists and verifies the existence
of each source file before installation.

:param *filelist: A list of absolute or relative paths to the files intended for
installation.
````

## Example port definition

Below is an example port of `openvpn` that applies patches using
{func}`b_port_apply_patches()`, invokes `./configure`, builds the port using
`make` and installs the `openvpn` binary to `/sbin`.

```bash
#!/usr/bin/env bash
#shellcheck disable=2034
{
  ports_api=1

  name="openvpn"
  version="2.4.7"
  desc="Secure IP/Ethernet tunnel daemon"

  source="https://swupdate.openvpn.org/community/releases/"
  archive_filename="${name}-${version}.tar.gz"
  src_path="${name}-${version}/"

  size="1457784"
  sha256="73dce542ed3d6f0553674f49025dfbdff18348eb8a25e6215135d686b165423c"

  license="GPL-2.0-only"
  license_file="COPYING"

  conflicts=""
  depends="openssl>=1.1.1a lzo>=2.10"
  optional=""

  supports="phoenix>=3.3"
}

p_prepare() {
  b_port_apply_patches "${PREFIX_PORT_WORKDIR}"

  if [ ! -f "$PREFIX_PORT_WORKDIR/config.h" ]; then
    OPENVPN_CFLAGS="-std=gnu99 -I${PREFIX_H}"
    (cd "$PREFIX_PORT_WORKDIR" && autoreconf -i -v -f)
    (cd "$PREFIX_PORT_WORKDIR" && \
      "./configure" CFLAGS="$CFLAGS $OPENVPN_CFLAGS" LDFLAGS="$LDFLAGS" \
      --host="${HOST}" --sbindir="$PREFIX_PROG")
  fi
}

p_build() {
  make -C "$PREFIX_PORT_WORKDIR"
  make -C "$PREFIX_PORT_WORKDIR" install-exec

  $STRIP -o "$PREFIX_PROG_STRIPPED/openvpn" "$PREFIX_PROG/openvpn"
  b_install "$PREFIX_PROG_TO_INSTALL/openvpn" /sbin/
}
```
