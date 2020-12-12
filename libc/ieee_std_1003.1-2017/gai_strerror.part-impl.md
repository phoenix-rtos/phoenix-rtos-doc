###Synopsis

`#include <netdb.h>`

`const char *gai_strerror(int ecode);`

###Description

The `gai_strerror()` function returns an address and name information error description.

Arguments:
    
<u>ecode</u> - an error numerical value.

The `gai_strerror()` function returns a text string describing an error value for the `getaddrinfo()` and `getnameinfo()` functions listed in the <`netdb.h`> header.

When the <u>ecode</u> argument is one of the following values listed in the <`netdb.h`> header:

 [`EAI_AGAIN`]
 [`EAI_BADFLAGS`]
 [`EAI_FAIL`]
 [`EAI_FAMILY`]
 [`EAI_MEMORY`]
 [`EAI_NONAME`]
 [`EAI_OVERFLOW`]
 [`EAI_SERVICE`]
 [`EAI_SOCKTYPE`]
 [`EAI_SYSTEM`]
     
the function return value points to a string describing the error. If the argument is not one of those values, the function returns a pointer to a string whose contents indicate an unknown error.
    
###Return value

Upon successful completion, gai_strerror() shall return a pointer to an implementation-defined string.

###Errors

No errors are defined.

###Implementation tasks

* implement the `gai_strerror()`,