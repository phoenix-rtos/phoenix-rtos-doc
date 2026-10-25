# socketpair

## Synopsis

```c
#include <sys/socket.h>

int socketpair(int domain, int type, int protocol,
               int socket_vector[2]);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `socketpair()` function shall create an unbound pair of connected sockets in a specified domain, of a specified
type, under the protocol optionally specified by the _protocol_ argument. The two sockets shall be identical. The file
descriptors used in referencing the created sockets shall be returned in _socket_vector[0]_ and _socket_vector[1]_.
The file descriptors shall be allocated as described in File Descriptor Allocation.

The `socketpair()` function takes the following arguments:

* _domain_ - Specifies the communications domain in which the sockets are to be created. Only the `AF_UNIX` domain is
supported.

* _type_ - Specifies the type of sockets to be created.

* _protocol_ - Specifies a particular protocol to be used with the sockets. Specifying a _protocol_ of `0` causes
`socketpair()` to use an unspecified default protocol appropriate for the requested socket type.

* _socket_vector_ - Specifies a 2-integer array to hold the file descriptors of the created socket pair.

The _type_ argument specifies the socket type, which determines the semantics of communications over the socket. The
following socket types are defined; implementations may specify additional socket types:

* `SOCK_STREAM` - Provides sequenced, reliable, bidirectional, connection-mode byte streams, and may provide a
transmission mechanism for out-of-band data.

* `SOCK_DGRAM` - Provides datagrams, which are connectionless-mode, unreliable messages of fixed maximum length.

* `SOCK_SEQPACKET` - Provides sequenced, reliable, bidirectional, connection-mode transmission paths for records. A
record can be sent using one or more output operations and received using one or more input operations, but a single
operation never transfers part of more than one record. Record boundaries are visible to the receiver via the `MSG_EOR`
flag.

If the _protocol_ argument is non-zero, it shall specify a protocol that is supported by the address family. If the
_protocol_ argument is zero, the default protocol for this address family and type shall be used. The protocols
supported by the system are implementation-defined.

The process may need to have appropriate privileges to use the `socketpair()` function or to create some sockets.

## Return value

Upon successful completion, this function shall return `0`; otherwise, `-1` shall be returned and `errno` set to
indicate the error, no file descriptors shall be allocated, and the contents of _socket_vector_ shall be left
unmodified.

## Errors

The `socketpair()` function shall fail if:

* `EAFNOSUPPORT` - The implementation does not support the specified address family.

* `EMFILE` - All, or all but one, of the file descriptors available to the process are currently open.

* `ENFILE` - No more file descriptors are available for the system.

* `EOPNOTSUPP` - The specified protocol does not permit creation of socket pairs.

* `EPROTONOSUPPORT` - The protocol is not supported by the address family, or the protocol is not supported by the
implementation.

* `EPROTOTYPE` - The socket type is not supported by the protocol.

The `socketpair()` function may fail if:

* `EACCES` - The process does not have appropriate privileges.

* `ENOBUFS` - Insufficient resources were available in the system to perform the operation.

* `ENOMEM` - Insufficient memory was available to fulfill the request.

## POSIX deviations

No POSIX deviations discovered.
