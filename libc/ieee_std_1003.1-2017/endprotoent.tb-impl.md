###Synopsis

`#include <netdb.h>`

`void endprotoent(void);`
`struct protoent *getprotobyname(const char *name);`
`struct protoent *getprotobynumber(int proto);`
`struct protoent *getprotoent(void);`
`void setprotoent(int stayopen);`

###Description

The functions retrieve information about network protocols contained in the network protocols database (`protoent` structures).

The `protoent` structure is defined in <`netdb.h`> as follows:

           struct protoent {
               char  *p_name;       /* official protocol name */
               char **p_aliases;    /* alias list, (`NULL` terminated */
               int    p_proto;      /* protocol number */
           }

Arguments:
    
<u>name</u> - network protocol name,
<u>proto</u> - protocol number,
<u>stayopen</u> - If the <u>stayopen</u> argument is non-zero, the connection to the network protocol database is not closed after each call to `getprotoent()` (either directly, or indirectly through one of the other `getproto*()` functions).

These functions retrieve information about network protocols stored in a specialized database.

The `setprotoent()` function opens a connection to the database, and sets the next entry to the first entry.

The `getprotobyname()` function searches the database from the beginning and finds the first entry for which the protocol name specified by <u>name</u> matches the `p_name` member, opening and closing a connection to the database as necessary.

The `getprotobynumber()` function searches the database from the beginning and finds the first entry for which the protocol number specified by <u>proto</u> matches the `p_proto` member, opening and closing a connection to the database as necessary.

The `getprotoent()` function reads the next entry of the database, opening and closing a connection to the database as necessary.

The `getprotobyname()`, `getprotobynumber()`, and `getprotoent()` functions each returns a pointer to a `protoent` structure, the members of which contain the fields of an entry in the network protocol database.

The `endprotoent()` function closes the connection to the database, releasing any open file descriptor.

These functions are not thread-safe.

###Return value

On success the `getprotobyname()`, `getprotobynumber()`, and `getprotoent()` functions return a pointer to a `protoent` structure if the requested entry was found, and a null pointer otherwise.

The application does not modify the structure to which the return value points, nor any storage areas pointed to by pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the structure or the storage areas might be overwritten by a subsequent call to `getprotobyname()`, `getprotobynumber()`, or `getprotoent()`. The returned pointer, and pointers within the structure, might also be invalidated if the calling thread is terminated.

###Errors

No errors are defined for these functions.

###Implementation tasks

* Add necessary definitions to <`netdb.h`>
* Implement the `getprotoent` function.
* Implement the `getprotobyname` function.
* Implement the `endprotoent()` function.
* Implement the `getprotobynumber()` function.
* Implement the `setprotoent()` function.

