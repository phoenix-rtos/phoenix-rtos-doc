###Synopsis

`#include <stdio.h>`

`int fileno(FILE *stream);`

###Description

The function maps a stream pointer (<u>stream</u>) to a file descriptor.

Arguments:

<u>stream</u> - the pointer to the stream,

###Return value

On success the function returns the integer value of the file descriptor associated with <u>stream</u>. Otherwise, the value `-1` is returned and `errno` set to indicate the error. 

###Errors

[`EBADF`]      The file descriptor underlying <u>stream</u> is not a valid file descriptor or
               The stream is not associated with a file.

###Implementation tasks

 * Implement error handling for the function.