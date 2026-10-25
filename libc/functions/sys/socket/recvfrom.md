# recvfrom

## Synopsis

```c
#include <sys/socket.h>

ssize_t recvfrom(int socket, void *restrict buffer, size_t length,
                 int flags, struct sockaddr *restrict address,
                 socklen_t *restrict address_len);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `recvfrom()` function shall receive a message from a connection-mode or connectionless-mode socket. It is normally
used with connectionless-mode sockets because it permits the application to retrieve the source address of received
data.

The `recvfrom()` function takes the following arguments:

* _socket_ - Specifies the socket file descriptor.

* _buffer_ - Points to the buffer where the message should be stored.

* _length_ - Specifies the length in bytes of the buffer pointed to by the _buffer_ argument.

* _flags_ - Specifies the type of message reception. Values of this argument are formed by logically OR'ing zero or
more of the following values:

  * `MSG_PEEK` - Peeks at an incoming message. The data is treated as unread and the next `recvfrom()` or similar
  function shall still return this data.

  * `MSG_OOB` - Requests out-of-band data. The significance and semantics of out-of-band data are protocol-specific.

  * `MSG_WAITALL` - On `SOCK_STREAM` sockets this requests that the function block until the full amount of data can be
  returned. The function may return the smaller amount of data if the socket is a message-based socket, if a signal is
  caught, if the connection is terminated, if `MSG_PEEK` was specified, or if an error is pending for the socket.

* _address_ - A null pointer, or points to a `sockaddr` structure in which the sending address is to be stored. The
length and format of the address depend on the address family of the socket.

* _address_len_ - Either a null pointer, if _address_ is a null pointer, or a pointer to a `socklen_t` object which on
input specifies the length of the supplied `sockaddr` structure, and on output specifies the length of the stored
address.

The `recvfrom()` function shall return the length of the message written to the buffer pointed to by the _buffer_
argument. For message-based sockets, such as `SOCK_RAW`, `SOCK_DGRAM`, and `SOCK_SEQPACKET`, the entire message shall
be read in a single operation. If a message is too long to fit in the supplied buffer, and `MSG_PEEK` is not set in the
_flags_ argument, the excess bytes shall be discarded. For stream-based sockets, such as `SOCK_STREAM`, message
boundaries shall be ignored. In this case, data shall be returned to the user as soon as it becomes available, and no
data shall be discarded.

If the `MSG_WAITALL` flag is not set, data shall be returned only up to the end of the first message.

Not all protocols provide the source address for messages. If the _address_ argument is not a null pointer and the
protocol provides the source address of messages, the source address of the received message shall be stored in the
`sockaddr` structure pointed to by the _address_ argument, and the length of this address shall be stored in the object
pointed to by the _address_len_ argument.

If the actual length of the address is greater than the length of the supplied `sockaddr` structure, the stored address
shall be truncated.

If the _address_ argument is not a null pointer and the protocol does not provide the source address of messages, the
value stored in the object pointed to by _address_ is unspecified. For `AF_UNIX` sockets the source address is provided
for datagrams sent from a bound socket; for a datagram from an unbound socket, and for connection-mode sockets, the
length of the address is set to `0`.

If no messages are available at the socket and `O_NONBLOCK` is not set on the socket's file descriptor, `recvfrom()`
shall block until a message arrives. If no messages are available at the socket and `O_NONBLOCK` is set on the socket's
file descriptor, `recvfrom()` shall fail and set `errno` to `EAGAIN` or `EWOULDBLOCK`.

## Return value

Upon successful completion, `recvfrom()` shall return the length of the message in bytes. If no messages are available
to be received and the peer has performed an orderly shutdown, `recvfrom()` shall return `0`. Otherwise, the function
shall return `-1` and set `errno` to indicate the error.

## Errors

The `recvfrom()` function shall fail if:

* `EAGAIN` or `EWOULDBLOCK` - The socket's file descriptor is marked `O_NONBLOCK` and no data is waiting to be
received; or `MSG_OOB` is set and no out-of-band data is available and either the socket's file descriptor is marked
`O_NONBLOCK` or the socket does not support blocking to await out-of-band data.

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `ECONNRESET` - A connection was forcibly closed by a peer.

* `EINTR` - A signal interrupted `recvfrom()` before any data was available.

* `EINVAL` - The `MSG_OOB` flag is set and no out-of-band data is available.

* `ENOTCONN` - A receive is attempted on a connection-mode socket that is not connected.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The specified flags are not supported for this socket type.

* `ETIMEDOUT` - The connection timed out during connection establishment, or due to a transmission timeout on active
connection.

The `recvfrom()` function may fail if:

* `EIO` - An I/O error occurred while reading from or writing to the file system.

* `ENOBUFS` - Insufficient resources were available in the system to perform the operation.

* `ENOMEM` - Insufficient memory was available to fulfill the request.

## POSIX deviations

No POSIX deviations discovered.
