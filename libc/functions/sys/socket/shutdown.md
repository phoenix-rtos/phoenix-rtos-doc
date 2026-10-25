# shutdown

## Synopsis

```c
#include <sys/socket.h>

int shutdown(int socket, int how);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `shutdown()` function shall cause all or part of a full-duplex connection on the socket associated with the file
descriptor _socket_ to be shut down.

The `shutdown()` function takes the following arguments:

* _socket_ - Specifies the file descriptor of the socket.

* _how_ - Specifies the type of shutdown. The values are as follows:

  * `SHUT_RD` - Disables further receive operations.

  * `SHUT_WR` - Disables further send operations.

  * `SHUT_RDWR` - Disables further send and receive operations.

The `shutdown()` function disables subsequent send and/or receive operations on a socket, depending on the value of the
_how_ argument.

## Return value

Upon successful completion, `shutdown()` shall return `0`; otherwise, `-1` shall be returned and `errno` set to
indicate the error.

## Errors

The `shutdown()` function shall fail if:

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `EINVAL` - The _how_ argument is invalid.

* `ENOTCONN` - The socket is not connected.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

The `shutdown()` function may fail if:

* `ENOBUFS` - Insufficient resources were available in the system to perform the operation.

## POSIX deviations

No POSIX deviations discovered.
