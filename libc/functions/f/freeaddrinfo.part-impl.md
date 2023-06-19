# Synopsis

`#include <sys/socket.h>`

`#include <netdb.h>`

`void freeaddrinfo(struct addrinfo *ai);`

`int getaddrinfo(const char *restrict nodename, const char *restrict servname, const struct addrinfo *restrict hints,
struct addrinfo **restrict res);`

## Status

Partially implemented

## Conformance

IEEE Std 1003.1-2017

## Description

The `freeaddrinfo()` function shall free one or more addrinfo structures returned by `getaddrinfo()`, along with any
additional storage associated with those structures. If the `ai_next` field of the structure is not `null`, the entire
list of structures shall be freed. The `freeaddrinfo()` function shall support the freeing of arbitrary sublists of an
addrinfo list originally returned by `getaddrinfo()`.

The `getaddrinfo()` function shall translate the name of a service location (for example, a host name) and/or a service
name and shall return a set of socket addresses and associated information to be used in creating a socket with which to
address
the specified service.

Note:
In many cases it is implemented by the Domain Name System, as documented in `RFC 1034`, `RFC 1035`, and `RFC 1886`.

The `freeaddrinfo()` and `getaddrinfo()` functions shall be thread-safe.

The _nodename_ and _servname_ arguments are either `null` pointers or pointers to `null`-terminated strings. One or both
of these two arguments shall be supplied by the application as a non-`null` pointer.

The format of a valid name depends on the address family or families. If a specific family is not given and the name
could be interpreted as valid within multiple supported families, the implementation shall attempt to resolve the name
in all supported families and, in absence of errors, one or more results shall be returned.

If the _nodename_ argument is not `null`, it can be a descriptive name or can be an address string. If the specified
address family is `AF_INET,` [IP6]   `AF_INET6,`  or `AF_UNSPEC,` valid descriptive names include host names. If the
specified address family is `AF_INET` or `AF_UNSPEC,` address strings using Internet standard dot notation as specified
in `inet_addr` are valid. If the specified address family is `AF_INET6` or `AF_UNSPEC,` standard IPv6 text forms
described in `inet_ntop` are valid. If _nodename_ is not `null`, the requested service location is named by _nodename_;
otherwise, the requested service location is local to the caller.

If _servname_ is `null`, the call shall return network-level addresses for the specified _nodename_. If _servname_ is
not `null`, it is a `null`-terminated character string identifying the requested service. This can be either a
descriptive name or a numeric representation suitable for use with the address family or families. If the specified
address family is `AF_INET,` `AF_INET6,`  or `AF_UNSPEC,` the service can be specified as a string specifying a decimal
port number.

If the _hints_ argument is not `null`, it refers to a structure containing input values that directs the operation by
providing options and by limiting the returned information to a specific socket type, address family, and/or protocol,
as described below. The application shall ensure that each of the `ai_addrlen,` `ai_addr,` `ai_canonname,` and `ai_next`
members, as well as each of the non-standard additional members, if any, of this _hints_ structure is initialized. If
any of these members has a value other than the value that would result from default initialization, the behavior is
implementation-defined. A value of `AF_UNSPEC` for `ai_family` means that the caller shall accept any address family.
 A value of zero for `ai_socktype` means that the caller shall accept any socket type. A value of zero for `ai_protocol`
 means that the caller shall accept any protocol. If _hints_ is a `null` pointer, the behavior shall be as if it
 referred to a structure containing the value zero for the `ai_flags,` `ai_socktype,` and `ai_protocol` fields, and
 `AF_UNSPEC` for the `ai_family` field.

The `ai_flags` field to which the _hints_ parameter points shall be set to zero or be the bitwise-inclusive OR of one
or more of the values `AI_PASSIVE,` `AI_CANONNAME,` `AI_NUMERICHOST,` `AI_NUMERICSERV,` `AI_V4MAPPED,` `AI_ALL,` and
`AI_ADDRCONFIG`.

If the `AI_PASSIVE` flag is specified, the returned address information shall be suitable for use in binding a socket
for accepting incoming connections for the specified service. In this case, if the _nodename_ argument is `null`, then
the IP address portion of the socket address structure shall be set to `INADDR_ANY` for an IPv4 address or
`IN6ADDR_ANY_INIT` for an IPv6 address. If the `AI_PASSIVE` flag is not specified, the returned address information
shall be suitable for a call to `connect()` (for a connection-mode protocol) or for a call to `connect()`, `sendto()`,
or `sendmsg()` (for a connectionless protocol). In this case, if the _nodename_ argument is `null`, then the IP address
portion of the socket address structure shall be set to the loopback address. The `AI_PASSIVE` flag shall be ignored if
the _nodename_ argument is not `null`.

If the `AI_CANONNAME` flag is specified and the _nodename_ argument is not `null`, the function shall attempt to
determine the canonical name corresponding to _nodename_ (for example, if _nodename_ is an alias or shorthand notation
for a complete name).

Note:
Since different implementations use different conceptual models, the terms canonical name '' and alias '' cannot be
precisely defined for the general case. However, Domain Name System implementations are expected to interpret them as
they are used in `RFC 1034`.

A numeric host address string is not a `name`, and thus does not have a `canonical name` form, no address to host name
translation is performed. See below for handling of the case where a canonical name cannot be obtained.

If the `AI_NUMERICHOST` flag is specified, then a non-`null` _nodename_ string supplied shall be a numeric host address
string.

Otherwise, an ``EAI_NONAME`` error is returned. This flag shall prevent any type of name resolution service
(for example, the DNS) from being invoked.

If the `AI_NUMERICSERV` flag is specified, then a non-`null` _servname_ string supplied shall be a numeric port string.

Otherwise, an ``EAI_NONAME`` error shall be returned. This flag shall prevent any type of name resolution service
(for example, NIS+) from being invoked.

By default, with an `ai_family` of `AF_INET6,` `getaddrinfo()` shall return only IPv6 addresses. If the `AI_V4MAPPED`
flag is specified along with an `ai_family` of `AF_INET6,` then `getaddrinfo()` shall return IPv4-mapped IPv6 addresses
on finding no matching IPv6 addresses. The `AI_V4MAPPED` flag shall be ignored unless `ai_family` equals `AF_INET6`. If
the `AI_ALL` flag is used with the `AI_V4MAPPED` flag, then `getaddrinfo()` shall return all matching IPv6 and IPv4
addresses. The `AI_ALL` flag without the `AI_V4MAPPED` flag shall be ignored.
If the `AI_ADDRCONFIG` flag is specified, IPv4 addresses shall be returned only if an IPv4 address is configured on the
local system, and IPv6 addresses shall be returned only if an IPv6 address is configured on the local system.
The `ai_socktype` field to which argument _hints_ points specifies the socket type for the service, as defined in
socket. If a specific socket type is not given (for example, a value of zero) and the service name could be interpreted
as valid with multiple supported socket types, the implementation shall attempt to resolve the service name for all
supported socket types and, in the absence of errors, all possible results shall be returned. A non-zero socket type
value shall limit the returned information to values with the specified socket type.

If the `ai_family` field to which _hints_ points has the value `AF_UNSPEC,` addresses shall be returned for use with any
address family that can be used with the specified _nodename_ and/or _servname_. Otherwise, addresses shall be returned
for use only with the specified address family. If `ai_family` is not `AF_UNSPEC` and `ai_protocol` is not zero, then
addresses shall be returned for use only with the specified address family and protocol; the value of `ai_protocol`
shall be interpreted as in a call to the `socket()` function with the corresponding values of `ai_family` and
`ai_protocol`.

## Return value

A zero return value for `getaddrinfo()` indicates successful completion, a non-zero return value indicates failure. The
possible values for the failures are listed in the `ERRORS` section.

Upon successful return of `getaddrinfo()`, the location to which _res_ points shall refer to a linked list of `addrinfo`
structures, each of which shall specify a socket address and information for use in creating a socket with which to use
that socket address. The list shall include at least one addrinfo structure. The `ai_next` field of each structure
contains a pointer to the next structure on the list, or a `null` pointer if it is the last structure on the list.
Each structure on the list shall include values for use with a call to the `socket()` function, and a socket address
for use with the `connect()` function or, if the `AI_PASSIVE` flag was specified, for use with the `bind()` function.
The fields `ai_family`, `ai_socktype`, and `ai_protocol` shall be usable as the arguments to the `socket()` function to
create a socket suitable for use with the returned address. The fields `ai_addr` and `ai_addrlen` are usable as the
arguments to the `connect()` or `bind()` functions with such a socket, according to the `AI_PASSIVE` flag.

If _nodename_ is not `null`, and if requested by the `AI_CANONNAME` flag, the ai_canonname field of the first returned
`addrinfo` structure shall point to a `null`-terminated string containing the canonical name corresponding to the input
_nodename_, if the canonical name is not available, then `ai_canonname` shall refer to the _nodename_ argument or a
string with the same contents. The contents of the ai_flags field of the returned structures are undefined.

All fields in socket address structures returned by `getaddrinfo()` that are not filled in through an explicit argument
(for example, `sin6_flowinfo`) shall be set to zero.

Note:
This makes it easier to compare socket address structures.

## Errors

The `getaddrinfo()` function shall fail and return the corresponding error value if:

* `EAI_AGAIN` - The name could not be resolved at this time. Future attempts may succeed.

* `EAI_BADFLAGS` - The flags parameter had an invalid value.

* `EAI_FAIL` - A non-recoverable error occurred when attempting to resolve the name.

* `EAI_FAMILY` - The address family was not recognized.

* `EAI_MEMORY` - There was a memory allocation failure when trying to allocate storage for the return value.

* `EAI_NONAME` - The name does not resolve for the supplied parameters.

Neither _nodename_ nor _servname_ were supplied. At least one of these shall be supplied.

* `EAI_SERVICE` - The service passed was not recognized for the specified socket type.
`EAI_SOCKTYPE`

The intended socket type was not recognized.

* `EAI_SYSTEM` - A system error occurred, the error code can be found in `errno`.

## Tests

Untested

## Known bugs

None

## See Also

1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
