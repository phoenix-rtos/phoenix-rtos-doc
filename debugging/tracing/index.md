# Tracing

The Phoenix-RTOS kernel supports kernel event tracing by emitting
CTF-1.8 events convertible to Perfetto trace viewer format.

The trace can be captured from userspace by psh `perf` applet or through libtrace
bindings. Once captured, the trace can be converted on Linux from CTF to
the format of the trace viewer using babeltrace2-based Python script.

(tracing_common_prerequisites)=

## Common prerequisites

### hostutils dependencies

* Protobuf compiler and Python bindings are required for the tracing hostutils.
  For Ubuntu:

  ```bash
  $ sudo apt install protobuf-compiler python3-protobuf
  ```

### babeltrace

If your distribution ships babeltrace2 **2.0.5**, then install it along
python bindings, e.g.:

```bash
$ sudo apt install babeltrace2 python3-bt2
```

If it ships a newer version, install babeltrace2 from source[^1]. For example:

```bash
$ git clone https://github.com/efficios/babeltrace
$ cd babeltrace
$ git checkout 502ef2f72
$ ./bootstrap
$ ./configure \
  --enable-python-bindings --enable-python-plugins \
  --enable-vendor-fmt --disable-tests --disable-man-pages --prefix=/usr
$ make && make install
```

[^1]: babeltrace2 2.0.6+ suffers from [bug #1389](https://bugs.lttng.org/issues/1389)
    that causes the kernel-emitted trace to crash babeltrace2 internally. We
    have already fixed this issue upstream, but it may take a while until it is
    included in a release.

```{toctree}
:maxdepth: 1

large-targets.md
small-targets.md
obtaining-trace-from-qemu.md
using-perfetto.md
custom-events.md
```
