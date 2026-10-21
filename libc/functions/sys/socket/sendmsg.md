# sendmsg

## Synopsis

```c
#include <sys/socket.h>

ssize_t sendmsg(int socket, const struct msghdr *message, int flags);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sendmsg()` function shall send a message through a connection-mode or connectionless-mode socket. If the socket is
a connectionless-mode socket, the message shall be sent to the address specified by `msghdr` if no pre-specified peer
address has been set. If a peer address has been pre-specified, either the message shall be sent to the address
specified in `msghdr` (overriding the pre-specified peer address), or the function shall return `-1` and set `errno` to
`EISCONN`. If the socket is an `AF_UNIX` connection-mode socket, the destination address in `msghdr` shall not be
specified; if it is, `sendmsg()` shall return `-1` and set `errno` to `EISCONN`, whether the socket is connected or not.
For other connection-mode sockets the destination address in `msghdr` shall be ignored.

The `sendmsg()` function takes the following arguments:

* _socket_ - Specifies the socket file descriptor.

* _message_ - Points to a `msghdr` structure, containing both the destination address and the buffers for the outgoing
message. The length and format of the address depend on the address family of the socket. The `msg_flags` member is
ignored.

* _flags_ - Specifies the type of message transmission. The application may specify `0` or the following flag:

  * `MSG_EOR` - Terminates a record (if supported by the protocol).

  * `MSG_OOB` - Sends out-of-band data on sockets that support out-of-bound data. The significance and semantics of
  out-of-band data are protocol-specific.

  * `MSG_NOSIGNAL` - Requests not to send the `SIGPIPE` signal if an attempt to send is made on a stream-oriented socket
  that is no longer connected. The `EPIPE` error shall still be returned.

The `msg_iov` and `msg_iovlen` fields of _message_ specify zero or more buffers containing the data to be sent.
`msg_iov` points to an array of `iovec` structures; `msg_iovlen` shall be set to the dimension of this array. In each
`iovec` structure, the `iov_base` field specifies a storage area and the `iov_len` field gives its size in bytes. Some
of these sizes can be zero. The data from each storage area indicated by `msg_iov` is sent in turn.

Successful completion of a call to `sendmsg()` does not guarantee delivery of the message. A return value of `-1`
indicates only locally-detected errors.

If space is not available at the sending socket to hold the message to be transmitted and the socket file descriptor
does not have `O_NONBLOCK` set, the `sendmsg()` function shall block until space is available. If space is not
available at the sending socket to hold the message to be transmitted and the socket file descriptor does have
`O_NONBLOCK` set, the `sendmsg()` function shall fail.

If the socket protocol supports broadcast and the specified address is a broadcast address for the socket protocol,
`sendmsg()` shall fail if the `SO_BROADCAST` option is not set for the socket.

The socket in use may require the process to have appropriate privileges to use the `sendmsg()` function.

## Return value

Upon successful completion, `sendmsg()` shall return the number of bytes sent. Otherwise, `-1` shall be returned and
`errno` set to indicate the error.

## Errors

The `sendmsg()` function shall fail if:

* `EAGAIN` or `EWOULDBLOCK` - The socket's file descriptor is marked `O_NONBLOCK` and the requested operation would
block.

* `EAFNOSUPPORT` - Addresses in the specified address family cannot be used with this socket.

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `ECONNRESET` - A connection was forcibly closed by a peer.

* `EINTR` - A signal interrupted `sendmsg()` before any data was transmitted.

* `EINVAL` - The sum of the `iov_len` values overflows an `ssize_t`.

* `EISCONN` - A destination address was specified, and the socket is already connected, or a destination address was
specified for an `AF_UNIX` connection-mode socket.

* `EMSGSIZE` - The message is too large to be sent all at once (as the socket requires), or the `msg_iovlen` member of
the `msghdr` structure pointed to by _message_ is less than or equal to `0` or is greater than `IOV_MAX`.

* `ENOTCONN` - The socket is connection-mode but is not connected.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The _socket_ argument is associated with a socket that does not support one or more of the values set
in _flags_.

* `EPIPE` - The socket is shut down for writing, or the socket is connection-mode and is no longer connected. In the
latter case, and if the socket is of type `SOCK_STREAM` or `SOCK_SEQPACKET` and the `MSG_NOSIGNAL` flag is not set, the
`SIGPIPE` signal is generated to the calling thread.

If the address family of the socket is `AF_UNIX`, then `sendmsg()` shall fail if:

* `EIO` - An I/O error occurred while reading from or writing to the file system.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the path name in the socket address.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of the path name does not name an existing file or the path name is an empty string.

* `ENOTDIR` - A component of the path prefix of the path name in the socket address names an existing file that is
neither a directory nor a symbolic link to a directory, or the path name in the socket address contains at least one
non-`<slash>` character and ends with one or more trailing `<slash>` characters and the last path name component names
an existing file that is neither a directory nor a symbolic link to a directory.

The `sendmsg()` function may fail if:

* `EACCES` - Search permission is denied for a component of the path prefix; or write access to the named socket is
denied.

* `EDESTADDRREQ` - The socket is not connection-mode and does not have its peer address set, and no destination address
was specified.

* `EHOSTUNREACH` - The destination host cannot be reached (probably because the host is down, or a remote router cannot
reach it).

* `EIO` - An I/O error occurred while reading from or writing to the file system.

* `ENETDOWN` - The local network interface used to reach the destination is down.

* `ENETUNREACH` - No route to the network is present.

* `ENOBUFS` - Insufficient resources were available in the system to perform the operation.

* `ENOMEM` - Insufficient memory was available to fulfill the request.

If the address family of the socket is `AF_UNIX`, then `sendmsg()` may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the path name in the socket
address.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

## POSIX deviations

IEEE Std 1003.1-2017 requires the destination address in `msghdr` to be ignored when the socket is connection-mode. In
Phoenix-RTOS a destination address (`msg_name`) passed to an `AF_UNIX` connection-mode socket (`SOCK_STREAM` or
`SOCK_SEQPACKET`) is not ignored: `sendmsg()` fails with `EISCONN`, also when the socket is not connected, where
`ENOTCONN` would be reported otherwise. An `AF_UNIX` connection-mode socket is expected to be used with `msg_name` set
to a null pointer, which keeps the semantics of the destination address unambiguous. `AF_INET` connection-mode sockets
ignore the destination address as specified.
