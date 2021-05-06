# Synopsis

`#include <sys/socket.h>`

`int accept(int socket, struct sockaddr *address,
       socklen_t *address_len);`

## Status

Parially implemented

## Description

The `accept()` function extracts the first connection on the queue of pending connections, create a new socket with the same socket type protocol and address family as the specified socket, and allocate a new file descriptor for that socket. The file descriptor is  allocated as described in File Descriptor Allocation.

### Arguments:

<u>socket</u> - a socket that was created with `socket()`, has been bound to an address with `bind()`, and has issued a successful call to `listen()`.
<u>address</u> - either a null pointer, or a pointer to a `sockaddr` structure where the address of the connecting socket is returned.
<u>address_len</u> - either a null pointer, if address is a null pointer, or a pointer to a `socklen_t` object which on input specifies the length of the supplied `sockaddr` structure, and on output specifies the length of the stored address.

If address is not a null pointer, the address of the peer for the accepted connection is stored in the `sockaddr` structure pointed to by address, and the length of this address is stored in the object pointed to by <u>address_len</u>.

If the actual length of the address is greater than the length of the supplied `sockaddr` structure, the stored address is truncated.

If the protocol permits connections by unbound clients, and the peer is not bound, then the value stored in the object pointed to by address is unspecified.

If the listen queue is empty of connection requests and `O_NONBLOCK` is not set on the file descriptor for the socket, `accept()` blocks until a connection is present. If the `listen()` queue is empty of connection requests and `O_NONBLOCK` is set on the file descriptor for the socket, `accept()` fails and sets `errno` to [`EAGAIN`] or [`EWOULDBLOCK`].

The accepted socket cannot itself accept more connections. The original socket remains open and can accept more connections.

## Return value

Upon successful completion, `accept()` returns the non-negative file descriptor of the accepted socket. Otherwise, `-1` is returned, `errno` is set to indicate the error, and any object pointed to by <u>address_len</u> remains unchanged.

## Errors

[`EAGAIN`] or [`EWOULDBLOCK`] - `O_NONBLOCK` is set for the socket file descriptor and no connections are present to be accepted.

[`EBADF`] - The socket argument is not a valid file descriptor.

[`ECONNABORTED`] - A connection has been aborted.

[`EINTR`] - The `accept`() function was interrupted by a signal that was caught before a valid connection arrived.

[`EINVAL`] - The socket is not accepting connections.

[`EMFILE`] - All file descriptors available to the process are currently open.

[`ENFILE`] - The maximum number of file descriptors in the system is already open.

[`ENOBUFS`] - No buffer space is available.

[`ENOMEM`] - There was insufficient memory available to complete the operation.

[`ENOTSOCK`] - The socket argument does not refer to a socket.

[`EOPNOTSUPP`] - The socket type of the specified socket does not support accepting connections.

The `accept()` function may fail if:

[`EPROTO`] - A protocol error has occurred; for example, the `STREAMS` protocol stack has not been initialized. 


## Implementation tasks

* Implement error detection with errors mentioned above.

## Tests

======

## EXAMPLES

None.
