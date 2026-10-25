# getsockname

## Synopsis

```c
#include <sys/socket.h>

int getsockname(int socket, struct sockaddr *restrict address,
                socklen_t *restrict address_len);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getsockname()` function shall retrieve the locally-bound name of the specified socket, store this address in the
`sockaddr` structure pointed to by the _address_ argument, and store the length of this address in the object pointed
to by the _address_len_ argument.

The _address_len_ argument points to a `socklen_t` object which on input specifies the length of the supplied
`sockaddr` structure, and on output specifies the length of the stored address. If the actual length of the address is
greater than the length of the supplied `sockaddr` structure, the stored address shall be truncated.

If the socket has not been bound to a local name, the value stored in the object pointed to by _address_ is
unspecified. An `AF_UNIX` socket that was never bound is reported with the address family alone, a bound one with the
path name it was bound to, including its terminating null character.

## Return value

Upon successful completion, `0` shall be returned, the _address_ argument shall point to the address of the socket, and
the _address_len_ argument shall point to the length of the address. Otherwise, `-1` shall be returned and `errno` set
to indicate the error.

## Errors

The `getsockname()` function shall fail if:

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

* `EOPNOTSUPP` - The operation is not supported for this socket's protocol.

The `getsockname()` function may fail if:

* `EINVAL` - The socket has been shut down.

* `ENOBUFS` - Insufficient resources were available in the system to complete the function.

## POSIX deviations

If the address of an `AF_UNIX` socket is longer than the supplied `sockaddr` structure, the stored address is truncated,
and the object pointed to by _address_len_ is set to the length of the full address, as in IEEE Std 1003.1g, not to the
length of the stored address as IEEE Std 1003.1-2017 specifies. The behavior is intentional: the application detects the
truncation by comparing the returned length with the size of its buffer and can repeat the call with a larger one, which
is more useful on a memory-constrained embedded system than silently working with a cut path name.
