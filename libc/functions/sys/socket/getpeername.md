# getpeername

## Synopsis

```c
#include <sys/socket.h>

int getpeername(int socket, struct sockaddr *restrict address,
                socklen_t *restrict address_len);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getpeername()` function shall retrieve the peer address of the specified socket, store this address in the
`sockaddr` structure pointed to by the _address_ argument, and store the length of this address in the object pointed
to by the _address_len_ argument.

The _address_len_ argument points to a `socklen_t` object which on input specifies the length of the supplied
`sockaddr` structure, and on output specifies the length of the stored address. If the actual length of the address is
greater than the length of the supplied `sockaddr` structure, the stored address shall be truncated.

If the protocol permits connections by unbound clients, and the peer is not bound, then the value stored in the object
pointed to by _address_ is unspecified.

The address of an `AF_UNIX` socket is the path name it was bound to, reported with its terminating null character. A
peer that was never bound is reported with the address family alone.

## Return value

Upon successful completion, `0` shall be returned. Otherwise, `-1` shall be returned and `errno` set to indicate the
error.

## Errors

The `getpeername()` function shall fail if:

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `EINVAL` - The socket has been shut down.

* `ENOTCONN` - The socket is not connected or otherwise has not had the peer pre-specified.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The operation is not supported for the socket protocol.

The `getpeername()` function may fail if:

* `ENOBUFS` - Insufficient resources were available in the system to complete the call.

## POSIX deviations

If the address of the peer of an `AF_UNIX` socket is longer than the supplied `sockaddr` structure, the stored address
is truncated, and the object pointed to by _address_len_ is set to the length of the full address, as in IEEE Std
1003.1g, not to the length of the stored address as IEEE Std 1003.1-2017 specifies. The behavior is intentional: the
application detects the truncation by comparing the returned length with the size of its buffer and can repeat the call
with a larger one, which is more useful on a memory-constrained embedded system than silently working with a cut path
name.
