# getsockopt

## Synopsis

```c
#include <sys/socket.h>

int getsockopt(int socket, int level, int option_name,
               void *restrict option_value, socklen_t *restrict option_len);
```

## Status

Implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `getsockopt()` function manipulates options associated with a socket.

The `getsockopt()` function shall retrieve the value for the option specified by the _option_name_ argument for the
socket specified by the _socket_ argument. If the size of the option value is greater than _option_len_, the value
stored in the object pointed to by the _option_value_ argument shall be silently truncated. Otherwise, the object
pointed to by the _option_len_ argument shall be modified to indicate the actual length of the value.

The _level_ argument specifies the protocol level at which the option resides. To retrieve options at the socket level,
specify the _level_ argument as `SOL_SOCKET`. To retrieve options at other levels, supply the appropriate level
identifier for the protocol controlling the option. For example, to indicate that an option is interpreted by the TCP
(Transmission Control Protocol), set _level_ to `IPPROTO_TCP` as defined in the `<netinet/in.h>` header.

The socket in use may require the process to have appropriate privileges to use the `getsockopt()` function.

The _option_name_ argument specifies a single option to be retrieved. It can be one of the socket-level options defined
in `<sys/socket.h>`.

The default value of the `SO_SNDBUF` option is implementation-defined. `AF_UNIX` sockets have no send buffer, as the
sent data is stored directly in the receive buffer of the peer socket, so `SO_SNDBUF` is reported as `0`.

## Return value

Upon successful completion, `getsockopt()` shall return `0`; otherwise, `-1` shall be returned and `errno` set to
indicate the error.

## Errors

The `getsockopt()` function shall fail if:

* `EBADF` - The _socket_ argument is not a valid file descriptor.

* `EINVAL` - The specified option is invalid at the specified socket level.

* `ENOPROTOOPT` - The option is not supported by the protocol.

* `ENOTSOCK` - The _socket_ argument does not refer to a socket.

The `getsockopt()` function may fail if:

* `EACCES` - The calling process does not have appropriate privileges.

* `EINVAL` - The socket has been shut down.

* `ENOBUFS` - Insufficient resources are available in the system to complete the function.

## POSIX deviations

IEEE Std 1003.1-2017 requires the option value to be silently truncated when its size is greater than _option_len_. In
Phoenix-RTOS, `getsockopt()` fails with `EINVAL` in that case, both for `AF_UNIX` and `AF_INET` sockets. A truncated
value of a multibyte option (for example an `int` or a `struct timeval`) can't be interpreted correctly by the
application, so reporting an error is the safer behavior.
