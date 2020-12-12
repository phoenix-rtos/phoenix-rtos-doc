###Synopsis

`#include <stdio.h>`

`int fsetpos(FILE *stream, const fpos_t *pos);`

###Description

The function sets the file position of the given stream to the given position. The argument pos is a position given by
the function `fgetpos()`.

Arguments:
<u>stream</u> - a pointer to the given stream
<u>pos</u> - the required file position

###Return value

The `fsetpos()` function returns `0` if it succeeds; otherwise, it returns `-1` and sets `errno` to indicate the error.

###Errors

The `fsetpos()` function fails if, either the stream is unbuffered or the stream's buffer needed to be flushed, and the call to `fsetpos()` causes an underlying `lseek()` or `write()` to be invoked, and: 

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor and the thread would be delayed in the write operation. 
[`EBADF`]  The file descriptor underlying the stream file is not open for writing or the stream's buffer needed to be flushed and the file is not open. 
[`EFBIG`]  An attempt was made to write a file that exceeds the maximum file size. or
           An attempt was made to write a file that exceeds the file size limit of the process. or
           The file is a regular file and an attempt was made to write at or beyond the offset maximum associated with the corresponding stream. 
[`EINTR`]  The write operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`]    A physical I/O error has occurred, or the process is a member of a background process group attempting to perform a `write()` to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned.
[`ENOSPC`] There was no free space remaining on the device containing the file. 
[`EOVERFLOW`] For fseek(), the resulting file offset would be a value which cannot be represented correctly in an object of type `long`. 
              For fseeko(), the resulting file offset would be a value which cannot be represented correctly in an object of type `off_t`. 
[`EPIPE`]  An attempt was made to write to a pipe or `FIFO` that is not open for reading by any process; a `SIGPIPE` signal is also sent to the thread. 
[`ESPIPE`] The file descriptor underlying <u>stream</u> is associated with a pipe, `FIFO`, or socket. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device. 

###Implementation tasks

 * Implement `fsetpos()` function.