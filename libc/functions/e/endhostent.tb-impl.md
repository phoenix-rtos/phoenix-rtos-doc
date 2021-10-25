###Synopsis

`#include <netdb.h>`

`void endhostent(void);`
`struct hostent *gethostent(void);`
`void sethostent(int stayopen);`

###Description

The functions retrieve information about hosts contained in the network host database as `hostent` structures.

The `hostent` structure is defined in <`netdb.h`> as follows:

           struct hostent {
               char  *h_name;            /* official name of host */
               char **h_aliases;         /* alias list */
               int    h_addrtype;        /* host address type */
               int    h_length;          /* length of address */
               char **h_addr_list;       /* list of addresses */
           }

Arguments:

<u>stayopen</u> - if the <u>stayopen</u> argument is non-zero, the connection is not closed by a call to `gethostent()`, and the implementation maintains an open file descriptor.

These functions retrieve information about hosts stored in a specialized database.

The `sethostent()` function opens a connection to the database and sets the next entry for retrieval to the first entry in the database. If the <u>stayopen</u> argument is non-zero, the connection is not closed by a call to `gethostent()`, and the implementation maintains an open file descriptor.

The `gethostent()` function reads the next entry in the database, opening and closing a connection to the database as necessary. Entries are returned in the form of `hostent` structures.

The `endhostent()` function closes the connection to the database, releasing any open file descriptor.


The application does not modify the structure to which the return value points, nor any storage areas pointed to by pointers within the structure. The returned pointer, and pointers within the structure, might be invalidated or the structure or the storage areas might be overwritten by a subsequent call to `gethostent()`. The returned pointer, and pointers within the structure, might also be invalidated if the calling thread is terminated.

These functions are not thread-safe.

###Return value

On success the `gethostent()` function returns a pointer to a `hostent` structure if the requested entry was found, and a null pointer if the end of the database was reached or the requested entry was not found.

###Errors

No errors are defined for these functions.

###Implementation tasks

* Add necessary definition to <`netdb.h`>.
* Implement the `gethostent()` function.
* Implement the `endhostent()` function.
* Implement the `sethostent())` function.
