# Synopsis

`#include <sys/socket.h>`</br>

`int accept(int socket, struct sockaddr *restrict address,`</br>
`socklen_t *restrict address_len);`</br>

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `accept()` function shall extract the first connection on the queue of pending connections, create a new socket with
the same socket type protocol and address family as the specified _socket_, and allocate a new file descriptor for that
socket. The file descriptor shall be allocated as described in File Descriptor
Allocation.

The `accept()` function takes the following arguments:

* _`socket`_ Specifies a socket that was created with `socket()`, has been bound to an _address_ with `bind()`, and has
issued a successful call to `listen()`.
* _`address`_ Either a `null` pointer, or a pointer to a sockaddr structure where the address of the connecting socket
shall be returned.
* _`address_len`_ Either a `null` pointer, if _address_ is a `null` pointer, or a pointer to a `socklen_t` object which
on input specifies the length of the supplied sockaddr structure,
and on output specifies the length of the stored address.

If _address_ is not a `null` pointer, the address of the peer for the accepted connection shall be stored in the
`sockaddr` structure pointed to by _address_, and the length of this address shall be stored in the object pointed to
by _`address_len`_.

If the actual length of the address is greater than the length of the supplied sockaddr structure, the stored address
shall be truncated.

If the protocol permits connections by unbound clients, and the peer is not bound, then the value stored in the object
pointed to by _address_ is unspecified.

If the listen queue is empty of connection requests and `O_NONBLOCK` is not set on the file descriptor for the socket,
`accept()` shall block until a connection is present.

If the `listen()` queue is
empty of connection requests and `O_NONBLOCK` is set on the file descriptor for the socket, `accept()` shall fail
and set `errno` to `EAGAIN` or `EWOULDBLOCK`.

The accepted socket cannot itself accept more connections. The original socket remains open
and can accept more connections.

## Return value

Upon successful completion, `accept()` shall return the non-negative file descriptor of the accepted socket. Otherwise,
`-1` shall be returned, `errno` shall be set to indicate the error, and any object pointed to by _address_len_
shall remain unchanged.

## Errors

The `accept()` function shall fail if:

`EAGAIN` or `EWOULDBLOCK`

O_NONBLOCK is set for the _socket_ file descriptor and no connections are present to be accepted.

* `EBADF` - The _socket_ argument is not a valid file descriptor.
`ECONNABORTED`

A connection has been aborted.

* `EINTR` - The `accept()` function was interrupted by a signal that was caught before a valid connection arrived.

* `EINVAL` - The _socket_ is not accepting connections.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENFILE` - The maximum number of file descriptors in the system are already open.

* `ENOBUFS` - No buffer space is available.

* `ENOMEM` - There was insufficient memory available to complete the operation.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The socket type of the specified _socket_ does not support accepting connections.

The `accept()` function may fail if:

* `EPROTO` - A protocol error has occurred; [OB XSR] for example, the STREAMS protocol stack has not been initialized.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
