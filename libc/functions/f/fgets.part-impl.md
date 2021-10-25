###Synopsis

`#include <stdio.h>`

`char *fgets(char *str, int n, FILE *stream);`

###Description

The function reads a line from the specified stream and stores it into the string pointed to by <u>str</u>. 
It stops when either:

 * (<u>n</u>-1) characters are read,
 * the newline character is read, 
 * the end-of-file is reached,

whichever comes first.

Arguments:
<u>str</u> - the result string,
<u>n</u> - the maximum number of characters to be read,
<u>stream</u> - the input stream.

A null byte is written after the last byte read into the array. If the end-of-file condition is encountered before any bytes are read, the contents of the array pointed to by <u>str</u> not changed.

###Return value

Upon successful completion, `fgets()` returns <u>str</u>. 

If the stream is at end-of-file, the end-of-file indicator for the stream is set and `fgets()` returns a null pointer. If a read error occurs, the error indicator for the stream is set, `fgets()` returns a null pointer and sets `errno` to indicate the error. 

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the `fgetc()` operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for reading. 
[`EINTR`]  The read operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`]    A physical I/O error has occurred, or the process is in a background process group attempting to read from its controlling terminal, and either the calling thread is blocking `SIGTTIN` or the process is ignoring `SIGTTIN` or the process group of the process is orphaned.
[`EOVERFLOW`]  The file is a regular file and an attempt was made to read at or beyond the offset maximum associated with the corresponding stream. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks

* Implement error handling for the function.