# socket

## Synopsis

```c
#include <sys/socket.h>

int socket(int domain, int type, int protocol);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `socket()` function shall create an unbound socket in a communications domain, and return a file descriptor that
can be used in later function calls that operate on sockets. The file descriptor shall be allocated as described in
File Descriptor Allocation.

The `socket()` function takes the following arguments:

* _domain_ - Specifies the communications domain in which a socket is to be created.

* _type_ - Specifies the type of socket to be created.

* _protocol_ - Specifies a particular protocol to be used with the socket. Specifying a _protocol_ of `0` causes
`socket()` to use an unspecified default protocol appropriate for the requested socket type.

The _domain_ argument specifies the address family used in the communications domain. The address families supported by
the system are implementation-defined. `AF_UNIX` sockets are handled by the kernel, while `AF_INET` sockets are
handled by the network stack based on lwIP.

Symbolic constants that can be used for the _domain_ argument are defined in the `<sys/socket.h>` header.

The _type_ argument specifies the socket type, which determines the semantics of communication over the socket. The
following socket types are defined; implementations may specify additional socket types:

* `SOCK_STREAM` - Provides sequenced, reliable, bidirectional, connection-mode byte streams, and may provide a
transmission mechanism for out-of-band data.

* `SOCK_DGRAM` - Provides datagrams, which are connectionless-mode, unreliable messages of fixed maximum length.

* `SOCK_SEQPACKET` - Provides sequenced, reliable, bidirectional, connection-mode transmission paths for records. A
record can be sent using one or more output operations and received using one or more input operations, but a single
operation never transfers part of more than one record. Record boundaries are visible to the receiver via the `MSG_EOR`
flag.

The `SOCK_NONBLOCK` and `SOCK_CLOEXEC` flags may be OR'ed into _type_ to set `O_NONBLOCK` on the new socket and
`FD_CLOEXEC` on the new file descriptor.

If the _protocol_ argument is non-zero, it shall specify a protocol that is supported by the address family. If the
_protocol_ argument is zero, the default protocol for this address family and type shall be used. The protocols
supported by the system are implementation-defined. `AF_UNIX` sockets support only the default protocol.

The process may need to have appropriate privileges to use the `socket()` function or to create some sockets.

## Return value

Upon successful completion, `socket()` shall return a non-negative integer, the socket file descriptor. Otherwise, a
value of `-1` shall be returned and `errno` set to indicate the error.

## Errors

The `socket()` function shall fail if:

* `EAFNOSUPPORT` - The implementation does not support the specified address family.

* `EMFILE` - All file descriptors available to the process are currently open.

* `ENFILE` - No more file descriptors are available for the system.

* `EPROTONOSUPPORT` - The protocol is not supported by the address family, or the protocol is not supported by the
implementation.

* `EPROTOTYPE` - The socket type is not supported by the protocol.

The `socket()` function may fail if:

* `EACCES` - The process does not have appropriate privileges.

* `ENOBUFS` - Insufficient resources were available in the system to perform the operation.

* `ENOMEM` - Insufficient memory was available to fulfill the request.

## POSIX deviations

No POSIX deviations discovered.
