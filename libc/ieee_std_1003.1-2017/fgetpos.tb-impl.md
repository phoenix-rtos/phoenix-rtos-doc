###Synopsis

`#include <stdio.h>`

`int fgetpos(FILE *stream, fpos_t *pos);`

###Description

The function gets the current file position of the <u>stream</u> and writes it to <u>pos</u>.

Arguments:

<u>stream</u> - the stream to be examined,
<u>pos</u> - a pointer to an object, in which the current file position of the <u>stream</u> is stored.

###Return value

The function returns `0` on success, otherwise it returns `-1` and sets `errno` to indicate the type of error.

###Errors

[`EBADF`]      The file descriptor underlying stream is not valid. 
[`EOVERFLOW`]  The current value of the file position cannot be represented correctly in an object of type `fpos_t`. 
[`ESPIPE`]     The file descriptor underlying stream is associated with a pipe, FIFO, or socket. 

###Implementation tasks

 * Implement the `fgetpos()` function.