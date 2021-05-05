###Synopsis

`#include <stdio.h>`

`long int ftell(FILE *stream);`
`off_t ftello(FILE *stream);`

###Description

The functions return the current file position of the given stream.

Arguments:
    
<u>stream</u> - a pointer to the stream.

The `ftell()` function obtains the current value of the file-position indicator for the stream pointed to by stream.

The `ftello()` function is equivalent to `ftell()`, except that the return value is of type `off_t`. 

###Return value

Upon successful completion, `ftell()` and `ftello()` return the current value of the file-position indicator for the stream measured in bytes from the beginning of the file.
Otherwise, `ftell()` and `ftello()` return `-1`, and set `errno` to indicate the error.

###Errors

[`EBADF`] The file descriptor underlying stream is not an open file descriptor. 
[`EOVERFLOW`] For `ftell()`, the current file offset cannot be represented correctly in an object of type `long`. 
[`EOVERFLOW`] For `ftello()`, the current file offset cannot be represented correctly in an object of type `off_t`. 
[`ESPIPE`] The file descriptor underlying stream is associated with a pipe, `FIFO`, or socket. 
    
###Implementation tasks:
    
 * Implement error handling for `ftell()` function.
 * Implement error handling for `ftello()` function.
