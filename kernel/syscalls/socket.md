# Communication sockets

## `syscalls_sockAccept` `(syscalls_sys_accept`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, struct sockaddr *, address, 1);
GETFROMSTACK(ustack, socklen_t *,address_len, 2);
````

Accepts incomming connection on socket given by `socket`. Connection information is returned in variables `address` and
 `len`.

## `syscalls_sockAccept4` (`syscalls_sys_accept4`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, struct sockaddr *, address, 1);
GETFROMSTACK(ustack, socklen_t *,address_len, 2);
GETFROMSTACK(ustack, int, flags, 3);
````

## `syscalls_sockBind` (`syscalls_sys_bind`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, const struct sockaddr *, address, 1);
GETFROMSTACK(ustack, socklen_t, address_len, 2);
````

## `syscalls_sockConnect` (`syscalls_sys_connect`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, const struct sockaddr *, address, 1);
GETFROMSTACK(ustack, socklen_t, address_len, 2);
````

## `syscalls_sockGetPeerName` (`syscalls_sys_getpeername`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, struct sockaddr *, address, 1);
GETFROMSTACK(ustack, socklen_t *, address_len, 2);
````

## `syscalls_sockGetSockName` (`syscalls_sys_getsockname`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, struct sockaddr *, address, 1);
GETFROMSTACK(ustack, socklen_t *, address_len, 2);
````

## `syscalls_sockSetSockOpt` (`syscalls_sys_setsockopt`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, int, level, 1);
GETFROMSTACK(ustack, int, optname, 2);
GETFROMSTACK(ustack, const void *, optval, 3);
GETFROMSTACK(ustack, socklen_t, optlen, 4);
````

## `syscalls_sockGetSockOpt` (`syscalls_sys_getsockopt`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, int, level, 1);
GETFROMSTACK(ustack, int, optname, 2);
GETFROMSTACK(ustack, void *, optval, 3);
GETFROMSTACK(ustack, socklen_t *, optlen, 4);
````

## `syscalls_sockListen` (`syscalls_sys_listen`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, int, backlog, 1);
````

## `syscalls_sockRecvFrom` (`syscalls_sys_recvfrom`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, void *, message, 1);
GETFROMSTACK(ustack, size_t, length, 2);
GETFROMSTACK(ustack, int, flags, 3);
GETFROMSTACK(ustack, struct sockaddr *, src_addr, 4);
GETFROMSTACK(ustack, socklen_t *, src_len, 5);
````

## `syscalls_sockSentTo` (`syscalls_sys_sendto`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, const void *, message, 1);
GETFROMSTACK(ustack, size_t, length, 2);
GETFROMSTACK(ustack, int, flags, 3);
GETFROMSTACK(ustack, const struct sockaddr *, dest_addr, 4);
GETFROMSTACK(ustack, socklen_t, dest_len, 5);
````

## `syscalls_sockSocket` (`syscalls_sys_socket`)

````C
GETFROMSTACK(ustack, int, domain, 0);
GETFROMSTACK(ustack, int, type, 1);
GETFROMSTACK(ustack, int, protocol, 2);
````

## `syscalls_sockShutdown` (`syscalls_sys_shutdown`)

````C
GETFROMSTACK(ustack, int, socket, 0);
GETFROMSTACK(ustack, int, how, 1);
````

## See also

1. [System calls](README.md)
2. [Table of Contents](../../README.md)
