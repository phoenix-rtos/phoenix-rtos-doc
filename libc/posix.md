# POSIX emulation server

The `libphoenix` repository provides POSIX API enabling users to build and run portable POSIX applications. The
emulation layer is built upon Phoenix-RTOS native messaging API and a dedicated server (`posixsrv`).

The purpose of `posixsrv` is to store data that can be shared between processes, i.e.:

- keep track of file descriptors and their mapping to open files,
- manage standard IPC mechanisms: pipes, UNIX sockets,
- provide UNIX 98 pseudo-terminals,
- dispatch events for efficient `poll()`-like functions

It also registers and handles special files, such as `/dev/null` or `/dev/random`.

In the current implementation, some parts of `posixsrv` functionality is kept inside the kernel and accessed using a set
of system calls. Future implementations will instead delegate requests directly to `posixsrv`.

The source code of `posixsrv` is available on GitHub and can be obtained using the following command:

```shell
git clone https://github.com/phoenix-rtos/phoenix-rtos-posixsrv.git
```

## Blocking operations are not interruptible

A POSIX call that blocks in `posixsrv` - `sem_wait()` on a named semaphore, a read from an
empty pipe or pseudo-terminal, an event queue wait - is a message send. The calling thread
parks inside `msgSend()` in the kernel's `msg_received` state, and that wait is deliberately
uninterruptible: the kernel message descriptor is allocated on the sender's kernel stack, so
the thread cannot be unwound while a server holds the request.

This is a known deviation from IEEE Std 1003.1-2017. For the affected calls:

- they never fail with `EINTR`, whatever signal is delivered;
- they are not cancellation points, although the standard lists them as such
  (XSH 2.9.5), so `pthread_cancel()` has no effect until the call returns;
- a thread blocked on a condition that never occurs cannot be killed, and the process
  cannot be terminated until the server answers.

The deviation is a property of the messaging layer, not of any individual server, so it
applies uniformly to every blocking POSIX operation that `posixsrv` implements.
