###Synopsis

`#include <sys/socket.h>`
`#include <netdb.h>`

`void freeaddrinfo(struct addrinfo *ai);`

`int getaddrinfo(const char *nodename,
       const char *servname,
       const struct addrinfo *hints,
       struct addrinfo **res);`

###Description

The `freeaddrinfo()` function frees one or more `addrinfo` structures returned by `getaddrinfo()`, along with any additional storage associated with those structures. If the `ai_next` field of the structure is not null, the entire list of structures is freed. The `freeaddrinfo()` function supports the freeing of arbitrary sublists of an `addrinfo` list originally returned by `getaddrinfo()`.

The `getaddrinfo()` function translates the name of a service location (for example, a host name) and/or a service name and returns a set of socket addresses and associated information to be used in creating a socket with which to address the specified service.

Arguments:

<u>ai</u> - the `addrinfo` structure to be freed,
<u>nodename</u> - the requested service location; either a null pointer (the requested service location is local to the caller) or a pointer to a null-terminated string,
<u>servname</u> - either a null pointer or a pointer to a null-terminated string, a port name or number
<u>hints</u> - a structure containing input values that directs the operation by providing options and by limiting the returned information to a specific socket type, address family, and/or protocol. 
<u>res</u> - the result - the pointer to a linked list of `addrinfo` structures, each of which specifies a socket address and information for use in creating a socket with which to use that socket address. The list includes at least one `addrinfo` structure. 

All fields in socket address structures returned by `getaddrinfo()` that are not filled in through an explicit argument are set to zero. 

###Return value

The `freeaddrinfo()` function does not return any value.

Upon successful completion, `getaddrinfo()` returns `0`. The corresponding error value is returned on failure.

###Errors

For `getaddrinfo()`:

[`EAI_AGAIN`] The name could not be resolved at this time. Future attempts may succeed.
[`EAI_BADFLAGS`] The <u>flags</u> parameter had an invalid value.
[`EAI_FAIL`] A non-recoverable error occurred when attempting to resolve the name.
[`EAI_FAMILY`] The address family was not recognized.
[`EAI_MEMORY`] There was a memory allocation failure when trying to allocate storage for the return value.
[`EAI_NONAME`] The name does not resolve for the supplied parameters.
               Neither <u>nodename</u> nor <u>servname</u> were supplied. At least one of these should be supplied.
[`EAI_SERVICE`] The service passed was not recognized for the specified socket type.
[`EAI_SOCKTYPE`] The intended socket type was not recognized.
[`EAI_SYSTEM`] A system error occurred; the error code can be found in `errno`. 
    
###Implementation tasks
	
 * Delete manifest constants from the function code.
 * Implement error handling for the functions
