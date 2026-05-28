# Core libraries documentation outdated points

## Resolved points

`libswdg.md` typo
: `corelibs/libswdg.md` now uses `swdg_reload(0)` and documents the API with function directives.

`libcache.md` open questions
: `corelibs/libcache.md` now documents the library type, callback error handling, `cache_deinit()` return values, and
  the API with function directives.

`libvga.md` API coverage
: `corelibs/libvga.md` now documents public register access, state save and restore, and mode initialization functions
  from `<vga.h>`.

## Open points

## 1. Documentation coverage ratio

**Documentation covers:** 7 out of 15 libraries (47%): libcache, libcgi, libgraph, libswdg, libuuid, libvga, libvirtio.

**Current code has:** 15 libraries total in `phoenix-rtos-corelibs/`:
- **Documented:** libcache, libcgi, libgraph, libswdg, libuuid, libvga, libvirtio
- **Undocumented:** libalgo, libmbr, libmodbus, libmtd, libptable, libstorage, libtinyaes, libtrace

The 8 undocumented libraries include critical infrastructure (storage, encryption, partitioning).

**Recommendation:** Prioritize documenting `libptable`, `libstorage`, `libmtd`, and `libtinyaes` because they support
embedded storage and partition workflows.
