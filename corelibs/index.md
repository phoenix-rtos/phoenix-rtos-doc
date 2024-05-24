# Libraries

Phoenix-RTOS provides libraries, which enable the development of applications.

The source code is available in the [phoenix-rtos-corelibs](https://github.com/phoenix-rtos/phoenix-rtos-corelibs)
GitHub repository.
The example of usage can be found in the `_user` directory, placed in
[phoenix-rtos-project](https://github.com/phoenix-rtos/phoenix-rtos-project).

Read more about the reference project repository [here](../building/project.md).

There are following Phoenix-RTOS libraries:

- [Graphics library](libgraph.md) called `libgraph`, which provides drivers for graphic adapters,
- [Common Gateway Interface library](libcgi.md) called `libcgi`,
- [Video Graphics Array access library](libvga.md) called `libvga`, used in graphic adapters' implementation,
  for example Cirrus,
- [Virtual I/O Device library](libvirtio.md) called `libvirtio`, used for device emulation,
- [Universally Unique identifiers library](libuuid.md) called `libuuid`,
- [Cache library](libcache.md) called `libcache` which provides the user with n-way set-associative cache,
- [Software watchdog library](libswdg.md) called `libswdg` which provides the user with multichannel software watchdog.

<!-- #TODO: add chapters on how to use each of this library in separate chapters -->

## See also

1. [Table of Contents](../index.md)

```{toctree}
:hidden:
:maxdepth: 1

libcgi.md
libvirtio.md
libvga.md
libgraph.md
libuuid.md
libcache.md
```
