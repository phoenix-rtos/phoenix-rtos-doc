# sendto

## Synopsis

```c
#include <sys/socket.h>

ssize_t sendto(int socket, const void *message, size_t length,
               int flags, const struct sockaddr *dest_addr,
               socklen_t dest_len);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `sendto()` function shall send a message through a connection-mode or connectionless-mode socket.

If the socket is a connectionless-mode socket, the message shall be sent to the address specified by _dest_addr_ if no
pre-specified peer address has been set. If a peer address has been pre-specified, either the message shall be sent to
the address specified by _dest_addr_ (overriding the pre-specified peer address), or the function shall return `-1` and
set `errno` to `EISCONN`.

If the socket is an `AF_UNIX` connection-mode socket, _dest_addr_ shall be a null pointer. If a destination address is
specified, `sendto()` shall return `-1` and set `errno` to `EISCONN`, whether the socket is connected or not. For other
connection-mode sockets _dest_addr_ shall be ignored.

The `sendto()` function takes the following arguments:

* _socket_ - Specifies the socket file descriptor.

* _message_ - Points to a buffer containing the message to be sent.

* _length_ - Specifies the size of the message in bytes.

* _flags_ - Specifies the type of message transmission. Values of this argument are formed by logically OR'ing zero or
more of the following flags:

  * `MSG_EOR` - Terminates a record (if supported by the protocol).

  * `MSG_OOB` - Sends out-of-band data on sockets that support out-of-band data. The significance and semantics of
  out-of-band data are protocol-specific.

  * `MSG_NOSIGNAL` - Requests not to send the `SIGPIPE` signal if an attempt to send is made on a stream-oriented socket
  that is no longer connected. The `EPIPE` error shall still be returned.

* _dest_addr_ - Points to a `sockaddr` structure containing the destination address. The length and format of the
address depend on the address family of the socket.

* _dest_len_ - Specifies the length of the `sockaddr` structure pointed to by the _dest_addr_ argument.

If the socket protocol supports broadcast and the specified address is a broadcast address for the socket protocol,
`sendto()` shall fail if the `SO_BROADCAST` option is not set for the socket.

The _dest_addr_ argument specifies the address of the target.

The _length_ argument specifies the length of the message.

Successful completion of a call to `sendto()` does not guarantee delivery of the message. A return value of `-1`
indicates only locally-detected errors.

If space is not available at the sending socket to hold the message to be transmitted and the socket file descriptor
does not have `O_NONBLOCK` set, `sendto()` shall block until space is available. If space is not available at the
sending socket to hold the message to be transmitted and the socket file descriptor does have `O_NONBLOCK` set,
`sendto()` shall fail.

The socket in use may require the process to have appropriate privileges to use the `sendto()` function.

## Return value

Upon successful completion, `sendto()` shall return the number of bytes sent. Otherwise, `-1` shall be returned and
`errno` set to indicate the error.

## Errors

The `sendto()` function shall fail if:

* `EAFNOSUPPORT` - Addresses in the specified address family cannot be used with this socket.

* `EAGAIN` or `EWOULDBLOCK` - The socket's file descriptor is marked `O_NONBLOCK` and the requested operation would
block.

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `ECONNRESET` - A connection was forcibly closed by a peer.

* `EINTR` - A signal interrupted `sendto()` before any data was transmitted.

* `EISCONN` - A destination address was specified, and the socket is already connected, or a destination address was
specified for an `AF_UNIX` connection-mode socket.

* `EMSGSIZE` - The message is too large to be sent all at once, as the socket requires.

* `ENOTCONN` - The socket is connection-mode but is not connected.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The _socket_ argument is associated with a socket that does not support one or more of the values set
in _flags_.

* `EPIPE` - The socket is shut down for writing, or the socket is connection-mode and is no longer connected. In the
latter case, and if the socket is of type `SOCK_STREAM` or `SOCK_SEQPACKET` and the `MSG_NOSIGNAL` flag is not set, the
`SIGPIPE` signal is generated to the calling thread.

If the address family of the socket is `AF_UNIX`, then `sendto()` shall fail if:

* `EIO` - An I/O error occurred while reading from or writing to the file system.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the path name in the socket address.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of the path name does not name an existing file or the path name is an empty string.

* `ENOTDIR` - A component of the path prefix of the path name in the socket address names an existing file that is
neither a directory nor a symbolic link to a directory, or the path name in the socket address contains at least one
non-`<slash>` character and ends with one or more trailing `<slash>` characters and the last path name component names
an existing file that is neither a directory nor a symbolic link to a directory.

The `sendto()` function may fail if:

* `EACCES` - Search permission is denied for a component of the path prefix; or write access to the named socket is
denied.

* `EDESTADDRREQ` - The socket is not connection-mode and does not have its peer address set, and no destination address
was specified.

* `EHOSTUNREACH` - The destination host cannot be reached (probably because the host is down, or a remote router cannot
reach it).

* `EINVAL` - The _dest_len_ argument is not a valid length for the address family.

* `EIO` - An I/O error occurred while reading from or writing to the file system.

* `ENETDOWN` - The local network interface used to reach the destination is down.

* `ENETUNREACH` - No route to the network is present.

* `ENOBUFS` - Insufficient resources were available in the system to perform the operation.

* `ENOMEM` - Insufficient memory was available to fulfill the request.

If the address family of the socket is `AF_UNIX`, then `sendto()` may fail if:

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the path name in the socket
address.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

## POSIX deviations

IEEE Std 1003.1-2017 requires _dest_addr_ to be ignored when the socket is connection-mode. In Phoenix-RTOS a
destination address passed to an `AF_UNIX` connection-mode socket (`SOCK_STREAM` or `SOCK_SEQPACKET`) is not ignored:
`sendto()` fails with `EISCONN`, also when the socket is not connected, where `ENOTCONN` would be reported otherwise. An
`AF_UNIX` connection-mode socket is expected to be used with a null _dest_addr_ (or with `send()`), which keeps the
semantics of the destination address unambiguous. `AF_INET` connection-mode sockets ignore _dest_addr_ as specified.
