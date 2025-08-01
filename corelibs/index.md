# Libraries

Phoenix-RTOS provides libraries, which enable the development of applications.

The source code is available in the [phoenix-rtos-corelibs](https://github.com/phoenix-rtos/phoenix-rtos-corelibs)
GitHub repository.
The example of usage can be found in the `_user` directory, placed in
[phoenix-rtos-project](https://github.com/phoenix-rtos/phoenix-rtos-project).

Read more about the reference project in [Reference project](../project/index.md) chapter.

There are following Phoenix-RTOS libraries:

- Graphics library called `libgraph`, which provides drivers for graphic adapters,
- Common Gateway Interface library called `libcgi`,
- Video Graphics Array access library called `libvga`, used in graphic adapters' implementation,
  for example Cirrus,
- Virtual I/O Device library called `libvirtio`, used for device emulation,
- Universally Unique identifiers library called `libuuid`,
- Cache library called `libcache` which provides the user with n-way set-associative cache,
- Software watchdog library called `libswdg` which provides the user with multichannel software watchdog.

```{toctree}
:maxdepth: 1

libcgi.md
libvirtio.md
libvga.md
libgraph.md
libuuid.md
libcache.md
libswdg.md
```
