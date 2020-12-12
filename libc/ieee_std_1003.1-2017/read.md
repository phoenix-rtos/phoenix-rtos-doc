### Synopsis

`#include <unistd.h>`

`int read(int fildes, void *buf, size_t nbyte);`

###Description

`read()` attempts to read `nbyte` bytes of data from the object referenced by the descriptor `fildes` into the buffer pointed to by buf. 

###Return value

If successful, the number of bytes actually read is returned.  Upon reading end-of-file, zero is returned.  Otherwise, a -1 is returned and the global variable `errno` is set to indicate the error.

###Errors

    
