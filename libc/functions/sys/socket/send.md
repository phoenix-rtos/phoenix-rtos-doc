# send

## Synopsis

```c
#include <sys/socket.h>

ssize_t send(int socket, const void *buffer, size_t length, int flags);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `send()` function shall initiate transmission of a message from the specified socket to its peer. The `send()`
function shall send a message only when the socket is connected. If the socket is a connectionless-mode socket, the
message shall be sent to the pre-specified peer address.

The `send()` function takes the following arguments:

* _socket_ - Specifies the socket file descriptor.

* _buffer_ - Points to the buffer containing the message to send.

* _length_ - Specifies the length of the message in bytes.

* _flags_ - Specifies the type of message transmission. Values of this argument are formed by logically OR'ing zero or
more of the following flags:

  * `MSG_EOR` - Terminates a record (if supported by the protocol).

  * `MSG_OOB` - Sends out-of-band data on sockets that support out-of-band communications. The significance and
  semantics of out-of-band data are protocol-specific.

  * `MSG_NOSIGNAL` - Requests not to send the `SIGPIPE` signal if an attempt to send is made on a stream-oriented socket
  that is no longer connected. The `EPIPE` error shall still be returned.

The length of the message to be sent is specified by the _length_ argument. If the message is too long to pass through
the underlying protocol, `send()` shall fail and no data shall be transmitted.

Successful completion of a call to `send()` does not guarantee delivery of the message. A return value of `-1`
indicates only locally-detected errors.

If space is not available at the sending socket to hold the message to be transmitted, and the socket file descriptor
does not have `O_NONBLOCK` set, `send()` shall block until space is available. If space is not available at the
sending socket to hold the message to be transmitted, and the socket file descriptor does have `O_NONBLOCK` set,
`send()` shall fail. The `select()` and `poll()` functions can be used to determine when it is possible to send more
data.

The socket in use may require the process to have appropriate privileges to use the `send()` function.

## Return value

Upon successful completion, `send()` shall return the number of bytes sent. Otherwise, `-1` shall be returned and
`errno` set to indicate the error.

## Errors

The `send()` function shall fail if:

* `EAGAIN` or `EWOULDBLOCK` - The socket's file descriptor is marked `O_NONBLOCK` and the requested operation would
block.

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `ECONNRESET` - A connection was forcibly closed by a peer.

* `EDESTADDRREQ` - The socket is not connection-mode and no peer address is set.

* `EINTR` - A signal interrupted `send()` before any data was transmitted.

* `EMSGSIZE` - The message is too large to be sent all at once, as the socket requires.

* `ENOTCONN` - The socket is not connected.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The _socket_ argument is associated with a socket that does not support one or more of the values set
in _flags_.

* `EPIPE` - The socket is shut down for writing, or the socket is connection-mode and is no longer connected. In the
latter case, and if the socket is of type `SOCK_STREAM` or `SOCK_SEQPACKET` and the `MSG_NOSIGNAL` flag is not set, the
`SIGPIPE` signal is generated to the calling thread.

The `send()` function may fail if:

* `EACCES` - The calling process does not have appropriate privileges.

* `EIO` - An I/O error occurred while reading from or writing to the file system.

* `ENETDOWN` - The local network interface used to reach the destination is down.

* `ENETUNREACH` - No route to the network is present.

* `ENOBUFS` - Insufficient resources were available in the system to perform the operation.

## POSIX deviations

No POSIX deviations discovered.
