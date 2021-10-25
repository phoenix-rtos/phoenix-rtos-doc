###Synopsis

`#include <netdb.h>`

`void endservent(void);`
`struct servent *getservbyname(const char *name, const char *proto);`
`struct servent *getservbyport(int port, const char *proto);`
`struct servent *getservent(void);`
`void setservent(int stayopen);`

###Description

The functions retrieve information about network services.

The information is stored in the database which is a set of `servent` structures defined in <`netdb.h`>:
    
            struct servent {
               char  *s_name;       /* official service name */
               char **s_aliases;    /* alias list */
               int    s_port;       /* port number */
               char  *s_proto;      /* protocol to use */
           }

Arguments:
    
<u>name</u> - the service name,
<u>proto</u> - the protocol name,
<u>port</u> - the port number,
<u>stayopen</u> -  for non-zero values, the net database is not closed after each call to the `getservent()` function (either directly, or indirectly through one of the other `getserv*()` functions).  


These functions retrieve information about network services stored in the database containing `servent` structures.

The `setservent()` function opens a connection to the database, and sets the next entry to the first entry according to the <u>stayopen</u> argument value.

The `getservent()` function reads the next entry of the database, opening and closing a connection to the database as necessary.

The `getservbyname()` function searches the database from the beginning and finds the first entry for which the service name specified by <u>name</u> matches the `s_name` member and the protocol name specified by <u>proto</u> matches the `s_proto` member, opening and closing a connection to the database as necessary. If <u>proto</u> is a null pointer, any value of the `s_proto` member is matched.

The `getservbyport()` function searches the database from the beginning and finds the first entry for which the port specified by <u>port</u> matches the `s_port` member and the protocol name specified by <u>proto</u> matches the `s_proto` member, opening and closing a connection to the database as necessary. If <u>proto</u> is a null pointer, any value of the `s_proto` member is matched. The <u>port</u> argument is a value obtained by converting a `uint16_t` in network byte order to `int`. It need not be compatible with the port values of all address families.

The `getservbyname()`, `getservbyport()`, and `getservent()` functions return a pointer to a `servent` structure, the members of which contain the fields of an entry in the network services database.

The `endservent()` function shall closes the database, releasing any open file descriptor.

These functions are not thread-safe.

###Return value

On success the `getservbyname()`, `getservbyport()`, and `getservent()` functions return a pointer to a `servent` structure, otherwise a null pointer is returned. 

###Errors

No errors are defined. 

###Implementation tasks

* Implement the `setservent()` function.
* Implement the `getservent()` function.
* Implement the `getservbyname()` function.
* Implement the `getservbyport()` function.
* Implement the `endservent()` function.
