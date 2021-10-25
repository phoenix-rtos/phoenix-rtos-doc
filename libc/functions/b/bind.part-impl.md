###Synopsis
`#include <sys/socket.h>`

`int bind(int socket, const struct sockaddr *address,
       socklen_t address_len);`

###Description

The `bind()` function binds a name to socket <u>socket</u>.

Arguments:
<u>socket</u> - the file descriptor of the socket.
<u>address</u> - the pointer to a sockaddr structure containing the address to be bound to the socket. The length and format of the address depend on the address family of the socket.
<u>address_len</u> - the length of the `sockaddr` structure pointed to by the <u>address</u> argument.

The `bind()` function assigns a local socket address <u>address</u> to a socket identified by descriptor <u>socket</u> that has no local socket address assigned. Sockets created with the `socket()` function are initially unnamed; they are identified only by their address family.

###Return value
`0` on successful completion, 
`-1` otherwise (`errno` is set then adequately)

###Errors

[`EADDRINUSE`] - the specified address is already in use.
[`EADDRNOTAVAIL`] - the specified address is not available from the local machine.
[`EAFNOSUPPORT`] - the specified address is not a valid address for the address family of the specified socket.
[`EALREADY`] - an assignment request is already in progress for the specified socket.
[`EBADF`] - the socket argument is not a valid file descriptor.
[`EINPROGRESS`] - `O_NONBLOCK` is set for the file descriptor for the socket and the assignment cannot be immediately performed; the assignment is performed asynchronously.
[`EINVAL`] - the socket is already bound to an address, and the protocol does not support binding to a new address; or the socket has been shut down.
[`ENOBUFS`] - insufficient resources were available to complete the call.
[`ENOTSOCK`] - the socket argument does not refer to a socket.
[`EOPNOTSUPP`] - the socket type of the specified socket does not support binding to an address.

[`EACCES`] - the specified address is protected and the current user does not have permission to bind to it.
[`EINVAL`] - the <u>address_len</u> argument is not a valid length for the address family.
[`EISCONN`] - the socket is already connected.
[`ELOOP`] - more than {`SYMLOOP_MAX`} symbolic links were encountered during resolution of the pathname in <u>address</u>.
[`ENAMETOOLONG`] - the length of a pathname exceeds {`PATH_MAX`}, or pathname resolution of a symbolic link produced an intermediate result with a length that exceeds {`PATH_MAX`}. 


If the address family of the socket is `AF_UNIX`, then `bind()` fails if:

[`EACCES`] - a component of the path prefix denies search permission, or the requested name requires writing in a directory with a mode that denies write permission.
[`EDESTADDRREQ`] or [`EISDIR`] - the <u>address</u> argument is a null pointer.
[`EIO`] - an I/O error occurred.
[`ELOOP`] - a loop exists in symbolic links encountered during resolution of the pathname in <u>address</u>.
[`ENAMETOOLONG`] - the length of a component of a pathname is longer than {`NAME_MAX`}.
[`ENOENT`] - a component of the path prefix of the pathname in <u>address</u> does not name an existing file or the pathname is an empty string.
[`ENOENT`] or [`ENOTDIR`] - the pathname in <u>address</u> contains at least one non- <slash> character and ends with one or more trailing <slash> characters. If the pathname without the trailing <slash> characters would name an existing file, an [`ENOENT`] error shall not occur.
[`ENOTDIR`] - a component of the path prefix of the pathname in <u>address</u> names an existing file that is neither a directory nor a symbolic link to a directory, or the pathname in <u>address</u> contains at least one non- <slash> character and ends with one or more trailing <slash> characters and the last pathname component names an existing file that is neither a directory nor a symbolic link to a directory.
[`EROFS`] - the name would reside on a read-only file system.

###Implementation tasks

* Error codes as above

###Tests

======

###EXAMPLES
None.

