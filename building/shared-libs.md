# Shared libraries

Phoenix-RTOS supports building shared libs and dynamically-linked executables. Shared libs are support on all MMU platforms but aarch64 and on NOMMU arm. On NOMMU the FDPIC format is used.

## Usage

In target includes there are 3 variables connected to using shared libraries:

- **LIBPHOENIX_PIC** - if libphoenix should be built as PIC

- **LIBPHOENIX_SHARED** - if shared libphoenix should be built

- **HAVE_SHLIB** - defines if target supports shared libraries

**LIBPHOENIX_\*** flags may be overridden in project to control if it is meant to use shared libraries on not.

### Building shared library

To compile a library as a shared include of `include $(static-lib.mk)` to `include $(shared-lib.mk)`.

In cases of simple libraries this might be enough, however building a shared library is more similar to building a binary than a static library, thus more compilation options are available. Please refer for full list to `phoenix-rtos-build/makes/shared-lib.mk`. Most importantly libraries on which the shared library depends can be specified and few shared library specific options are available:

- **SONAME** - library soname, defaults to $(NAME).so, to disable set to 'nothing'

- **LOCAL_VERSION_SCRIPT** - version script relative to current makefile

### Building dynamically linked executable

In most cases compilation of a dynamically-linked executable is as easy as changing `include $(binary.mk)` to `include $(binary-dyn.mk)`.

`binary-dyn.mk` additionally allows specifying:

- **DEP_LIBS_SHARED** - shared libraries from current repo needed to be compiled/installed before this component (shortcut for putting something in LIBS and DEPS)

- **LIBS_SHARED** - names of the shared libs to link the binary against (without .so suffix)

### ldconfig

To create correct symlinks for shared libraries `ldconfig` needs to run at system boot. So, it has to be added to startup script on targets using shared libs.

Unfortunately, on SPARC targets read-only fs is used and user is on their own to correctly set paths in build time.
