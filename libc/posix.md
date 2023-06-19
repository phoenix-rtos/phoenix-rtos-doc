# POSIX emulation

The `libphoenix` repository provides POSIX API enabling users to build and run portable POSIX applications. The
emulation layer is built upon Phoenix-RTOS native messaging API and a dedicated server (`posixsrv`).

The purpose of `posixsrv` is to store data that can be shared between processes, i.e.:

- keep track of file descriptors and their mapping to open files,
- manage standard IPC mechanisms: pipes, UNIX sockets,
- provide UNIX 98 pseudo-terminals,
- dispatch events for efficient `poll()`-like functions

It also registers and handles special files, such as `/dev/null` or `/dev/random`.

In the current implementation some parts of `posixsrv` functionality is kept inside the kernel and accessed using a set
of system calls. Future implementations will instead delegate requests directly to `posixsrv`.

## Source code

The source code of `posixsrv` is available on GitHub and can be obtained using the following command:

```bash
git clone https://github.com/phoenix-rtos/phoenix-rtos-posixsrv
```

## See also

1. [Standard library functions](functions/README.md)
2. [Table of Contents](../README.md)
