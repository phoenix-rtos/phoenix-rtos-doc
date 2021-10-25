###Synopsis

`#include <netdb.h>`

`void endnetent(void);`
`struct netent *getnetbyaddr(uint32_t net, int type);`
`struct netent *getnetbyname(const char *name);`
`struct netent *getnetent(void);`
`void setnetent(int stayopen);`

###Description

The functions retrieve information about networks contained in the network database (`netent` structures).

The `netent` structure is defined in <`netdb.h`> as follows:

           struct netent {
               char      *n_name;     /* official network name */
               char     **n_aliases;  /* alias list (`NULL` terminated */
               int        n_addrtype; /* net address type */
               uint32_t   n_net;      /* network number  */
           }

Arguments:
    
<u>net</u> - network number in host byte order,
<u>type</u> - address family,
<u>name</u> - network name,    
<u>stayopen</u> - If the <u>stayopen</u> argument is non-zero, the connection is not closed by a call to `getnetent()`.

These functions retrieve information about networks stored in a specialized database.

The `setnetent()` function opens and rewinds the database. If the <u>stayopen</u> argument is non-zero, the connection to the net database is not closed after each call to `getnetent()` (either directly, or indirectly through one of the other `getnet*()` functions), and maintain an open file descriptor to the database.

The `getnetent()` function reads the next entry of the database, opening and closing a connection to the database as necessary.

The `getnetbyaddr()` function searches the database from the beginning, and finds the first entry for which the address family specified by <u>type</u> matches the `n_addrtype` member and the network number <u>net</u> matches the `n_net` member, opening and closing a connection to the database as necessary. 

The `getnetbyname()` function searches the database from the beginning and finds the first entry for which the network name specified by <u>name</u> matches the `n_name` member, opening and closing a connection to the database as necessary.

The `getnetbyaddr()`, `getnetbyname()`, and `getnetent()` functions return a pointer to a `netent` structure, the members of which  contain the fields of an entry in the network database.

The `endnetent()` function closes the database, releasing any open file descriptor.

These functions are not thread-safe.

###Return value

On success the `getnetbyaddr()`, `getnetbyname()`, and `getnetent()` return a pointer to a `netent` structure if the requested entry was found, and a null pointer otherwise.

The application does not modify the structure to which the return value points, nor any storage areas pointed to by pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the structure or the storage areas might be overwritten by a subsequent call to `getnetbyaddr()`, `getnetbyname()`, or `getnetent()`. The returned pointer, and pointers within the structure, might also be invalidated if the calling thread is terminated.

###Errors

No errors are defined for these functions.

###Implementation tasks

* Add necessary definitions to <`netdb.h`>
* Implement the `getnetbyaddr` function.
* Implement the `setnetent` function.
* Implement the `endnetent()` function.
* Implement the `getnetent()` function.
* Implement the `getnetbyname()` function.
