# listen

## Synopsis

```c
#include <sys/socket.h>

int listen(int socket, int backlog);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `listen()` function shall mark a connection-mode socket, specified by the _socket_ argument, as accepting
connections.

The _backlog_ argument provides a hint to the implementation which the implementation shall use to limit the number of
outstanding connections in the socket's listen queue. Implementations may impose a limit on _backlog_ and silently
reduce the specified value. Normally, a larger _backlog_ argument value shall result in a larger or equal length of the
listen queue. Implementations shall support values of _backlog_ up to `SOMAXCONN`, defined in `<sys/socket.h>`.

The implementation may include incomplete connections in its listen queue. The limits on the number of incomplete
connections and completed connections queued may be different.

The implementation may have an upper limit on the length of the listen queue - either global or per accepting socket.
If _backlog_ exceeds this limit, the length of the listen queue is set to the limit.

If `listen()` is called with a _backlog_ argument value that is less than `0`, the function behaves as if it had been
called with a _backlog_ argument value of `0`.

A _backlog_ argument of `0` may allow the socket to accept connections, in which case the length of the listen queue
may be set to an implementation-defined minimum value. For `AF_UNIX` sockets a _backlog_ of `0` sets the length of the
listen queue to `1`. Calling `listen()` again on a listening socket changes the length of its listen queue.

The socket in use may require the process to have appropriate privileges to use the `listen()` function.

## Return value

Upon successful completion, `listen()` shall return `0`; otherwise, `-1` shall be returned and `errno` set to
indicate the error.

## Errors

The `listen()` function shall fail if:

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `EDESTADDRREQ` - The socket is not bound to a local address, and the protocol does not support listening on an
unbound socket.

* `EINVAL` - The socket is already connected.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The socket protocol does not support `listen()`.

The `listen()` function may fail if:

* `EACCES` - The calling process does not have appropriate privileges.

* `EINVAL` - The socket has been shut down.

* `ENOBUFS` - Insufficient resources are available in the system to complete the call.

## POSIX deviations

No POSIX deviations discovered.
