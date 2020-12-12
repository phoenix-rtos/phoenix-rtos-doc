###Synopsis

`#include <sys/socket.h>`

`int connect(int socket, const struct sockaddr *address,
       socklen_t address_len);`

###Description

The `connect()` function attempts to make a connection on a connection-mode socket or to set or reset the peer address of a connectionless-mode socket. 


Arguments:
<u>socket</u> - the file descriptor of the specified socket.
<u>address</u> - a pointer to a `sockaddr` structure containing the peer address. The length and format of the address depend on the address family of the socket.,
<u>address_len</u> - the length of the `sockaddr` structure pointed to by the <u>address</u> argument.

If the socket has not already been bound to a local address, `connect()` binds it to an address which, unless the socket's address family is `AF_UNIX`, is an unused local address.

If the initiating socket is not connection-mode, then `connect()` sets the socket's peer address, and no connection is made. For `SOCK_DGRAM` sockets, the peer address identifies the destination of all datagrams to be sent on subsequent `send()` functions, and limits the remote sender for subsequent `recv()` functions. If the `sa_family` member of address is `AF_UNSPEC`, the socket's peer address is reset. Note that despite no connection being made, the term `connected` is used to describe a connectionless-mode socket for which a peer address has been set.

If the initiating socket is connection-mode, then `connect()` attempts to establish a connection to the address specified by the <u>address</u> argument. If the connection cannot be established immediately and `O_NONBLOCK` is not set for the socket, `connect()` blocks until the connection is established. If the timeout interval expires before the connection is established, `connect()` fails and the connection attempt is aborted. 

If `connect()` is interrupted by a signal that is caught while blocked waiting to establish a connection, `connect()` fails and set `errno` to [`EINTR`], but the connection request is not aborted, and the connection is established asynchronously.

If the connection cannot be established immediately and `O_NONBLOCK` is set for the file descriptor for the socket, `connect()` fails and sets `errno` to [`EINPROGRESS`], but the connection request is not aborted, and the connection is established asynchronously. Subsequent calls to `connect()` for the same socket, before the connection is established, fail and `errno` is set to [`EALREADY`].

When the connection has been established asynchronously, `pselect()`, `select()`, and `poll()` indicate that the file descriptor for the socket is ready for writing.

The socket in use requires the process to have appropriate privileges to use the `connect()` function.

###Return value

`0` on success, `-1` otherwise (`errno` is then set to indicate the corresponding error).

###Errors

[`EADDRNOTAVAIL`] - The specified address is not available from the local machine.
[`EAFNOSUPPORT`] - The specified address is not a valid address for the address family of the specified socket.
[`EALREADY`] - A connection request is already in progress for the specified socket.
[`EBADF`] - The socket argument is not a valid file descriptor.
[`ECONNREFUSED`] - The target address was not listening for connections or refused the connection request.
[`EINPROGRESS`] - `O_NONBLOCK` is set for the file descriptor for the socket and the connection cannot be immediately established; the connection will be established asynchronously.
[`EINTR`] - The attempt to establish a connection was interrupted by delivery of a signal that was caught; the connection will be established asynchronously.
[`EISCONN`] - The specified socket is connection-mode and is already connected.
[`ENETUNREACH`] - No route to the network is present.
[`ENOTSOCK`] - The socket argument does not refer to a socket.
[`EPROTOTYPE`] - The specified address has a different type than the socket bound to the specified peer address.
[`ETIMEDOUT`] - The attempt to connect timed out before a connection was made.

For `AF_UNIX` address family of the socket:

[`EIO`] - An I/O error occurred while reading from or writing to the file system.
[`ELOOP`] - A loop exists in symbolic links encountered during resolution of the pathname in address.
[`ENAMETOOLONG`] - The length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENOENT`] - A component of the pathname does not name an existing file or the pathname is an empty string.
[`ENOTDIR`] - A component of the path prefix of the pathname in <u>address</u> names an existing file that is neither a directory nor a symbolic link to a directory, or the pathname in <u>address</u> contains at least one non- <`slash`> character and ends with one or more trailing <`slash`> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.

The `connect()` function may fail if:

[`EACCES`] - Search permission is denied for a component of the path prefix; or write access to the named socket is denied.
[`EADDRINUSE`] - Attempt to establish a connection that uses addresses that are already in use.
[`ECONNRESET`] - Remote host reset the connection request.
[`EHOSTUNREACH`] - The destination host cannot be reached (probably because the host is down or a remote router cannot reach it).
[`EINVAL`] - The <u>address_len</u> argument is not a valid length for the address family; or invalid address family in the sockaddr structure.
[`ELOOP`] - More than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the pathname in <u>address</u>.
[`ENAMETOOLONG`] - The length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}.
[`ENETDOWN`] - The local network interface used to reach the destination is down.
[`ENOBUFS`] - No buffer space is available.
[`EOPNOTSUPP`] - The socket is listening and cannot be connected. 
    
###Implementation tasks

*Implement error detection as described above.