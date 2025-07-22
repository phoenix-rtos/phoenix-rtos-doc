# connect

## Synopsis

```c
#include <sys/socket.h>

int connect(int socket, const struct sockaddr *address,
            socklen_t address_len)
```

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The purpose is to connect a socket. The `connect()` function shall attempt to make a connection on a connection-mode
socket or to set or reset the peer address of a connectionless-mode socket. The function takes the following arguments:

* _`socket`_ - Specifies the file descriptor associated with the _socket_.
* _`address`_ - Points to a sockaddr structure containing the peer address. The length and format of the address depend
on the address family of the socket.
* _`address_len`_ - Specifies the length of the sockaddr structure pointed to by the _address_ argument.

If the socket has not already been bound to a local address, `connect()` shall bind it to an address which, unless the
socket's address family is `AF_UNIX,` is an unused local address.

If the initiating socket is not connection-mode, then `connect()` shall set the socket's peer address, and no
connection is made. For `SOCK_DGRAM` sockets, the peer address identifies where all data grams are sent
on subsequent `send()` functions, and limits the remote sender for subsequent `recv()` functions. If the `sa_family`
member of address is `AF_UNSPEC,` the socket's peer address shall be reset. Note that despite no connection being made,
the term `connected` is used to describe a connectionless-mode socket for which a peer address has been set.

If the initiating socket is connection-mode, then `connect()` shall attempt to establish a connection to the address
specified by the _address_ argument. If the connection cannot be established immediately and `O_NONBLOCK` is not set for
the file descriptor for the socket, `connect()` shall block for up to an unspecified timeout interval until the
connection is established. If the timeout interval expires before the connection is established, `connect()` shall fail
and the connection attempt shall be aborted. If `connect()` is interrupted by a signal that is caught while blocked
waiting to establish a connection, `connect()` shall fail and set errno to `EINTR`, but the connection request
shall not be aborted, and the connection shall be established asynchronously.

If the connection cannot be established immediately and `O_NONBLOCK` is set for the file descriptor for the socket,
`connect()` shall fail and set `errno` to `EINPROGRESS`, but the connection request shall not be aborted, and the
connection shall be established asynchronously. Subsequent calls to `connect()` for the same socket, before the
connection is established, shall fail and set `errno` to `EALREADY`.

When the connection has been established asynchronously, `pselect()`, `select()`, and `poll()` shall indicate that the
file descriptor for the socket is ready for writing.

The socket in use may require the process to have appropriate privileges to use the `connect()` function.

## Return value

Upon successful completion, `connect()` shall return `0`, otherwise, `-1` shall be returned and `errno` set to indicate
the error.

## Errors

The `connect()` function shall fail if:

* `EADDRNOTAVAIL`- The specified address is not available from the local machine.

* `EAFNOSUPPORT` - The specified address is not a valid address for the address family of the specified socket.

* `EALREADY` - A connection request is already in progress for the specified socket.

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `ECONNREFUSED` - The target address was not listening for connections or refused the connection request.

* `EINPROGRESS` - `O_NONBLOCK` is set for the file descriptor for the socket and the connection cannot be immediately
established, the connection shall be established asynchronously.

* `EINTR` - The attempt to establish a connection was interrupted by delivery of a signal that was caught, the
connection shall be established asynchronously.

* `EISCONN` - The specified socket is connection-mode and is already connected.

* `ENETUNREACH` - No route to the network is present.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EPROTOTYPE` - The specified address has a different type than the socket bound to the specified peer address.

* `ETIMEDOUT` - The attempt to connect timed out before a connection was made.

If the address family of the socket is `AF_UNIX`, then `connect()` shall fail if:

* `EIO` - An `I/O` error occurred while reading from or writing to the file system.

* `ELOOP` - A loop exists in symbolic links encountered during resolution of the path name in _address_.

* `ENAMETOOLONG` - The length of a component of a path name is longer than `NAME_MAX`.

* `ENOENT` - A component of the path name does not name an existing file or the path name is an empty string.

* `ENOTDIR` - A component of the path prefix of the path name in _address_ names an existing file that is neither a
directory nor a symbolic link to a directory, or the path name in _address_ contains at least one non-`<slash>`
character and ends with one or more trailing `<slash>` characters and the last path name component names an existing
file that is neither a directory nor a symbolic link to a directory.

The `connect()` function may fail if:

* `EACCES` - Search permission is denied for a component of the path prefix, or write access to the named socket is
denied.

* `EADDRINUSE` - Attempt to establish a connection that uses addresses that are already in use.

* `ECONNRESET` - Remote host reset the connection request.

* `EHOSTUNREACH` - The destination host cannot be reached (probably because the host is down, or a remote router cannot
reach it).

* `EINVAL` - The _address_len_ argument is not a valid length for the address family; or invalid address family in
the sockaddr structure.

* `ELOOP` - More than `SYMLOOP_MAX` symbolic links were encountered during resolution of the path name in _address_.

* `ENAMETOOLONG` - The length of a path name exceeds `PATH_MAX`, or path name resolution of a symbolic link produced an
intermediate result with a length that exceeds `PATH_MAX`.

* `ENETDOWN` - The local network interface used to reach the destination is down.

* `ENOBUFS` - No buffer space is available.

* `EOPNOTSUPP` - The socket is listening and cannot be connected.

## Tests

Untested

## Known bugs

None
