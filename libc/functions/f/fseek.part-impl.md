###Synopsis

`#include <stdio.h>`

`int fseek(FILE *stream, long int offset, int whence);`
`int fseeko(FILE *stream, off_t offset, int whence);`

###Description

Sets the file position of the stream to the given <u>offset</u>. The argument <u>offset</u> signifies the number of bytes to seek from the given <u>whence</u> position.

Arguments:
<u>stream</u> - the stream to position,    
<u>offset</u> - the number of bytes to seek from the given <u>whence</u> position,
<u>whence</u> - the starting stream position.

The new position, measured in bytes from the beginning of the file, is obtained by adding <u>offset</u> to the position specified by <u>whence</u>. The specified point is the beginning of the file for `SEEK_SET`, the current value of the file-position indicator for `SEEK_CUR`, or end-of-file for `SEEK_END`.

If the stream is to be used with wide-character input/output functions, the application ensures that <u>offset</u> is either `0` or a value returned by an earlier call to `ftell()` on the same stream and <u>whence</u> is `SEEK_SET`.

A successful call to `fseek()` clears the end-of-file indicator for the stream and undo any effects of `ungetc()` and `ungetwc()` on the same stream. After an `fseek()` call, the next operation on an update stream may be either input or output.

If the most recent operation, other than `ftell()`, on a given stream is `fflush()`, the file offset in the underlying open file description is adjusted to reflect the location specified by `fseek()`.

The `fseek()` function allows the file-position indicator to be set beyond the end of existing data in the file. If data is later written at this point, subsequent reads of data in the gap return bytes with the value `0` until data is actually written into the gap.

If the stream is writable and buffered data had not been written to the underlying file, `fseek()` causes the unwritten data to be written to the file and marks the last data modification and last file status change timestamps of the file for update.

The `fseeko()` function is equivalent to the `fseek()` function except that the <u>offset</u> argument is of type `off_t`.

###Return value

The `fseek()` and `fseeko()` functions return `0` if they succeed. Otherwise, they return `-1` and set `errno` to indicate the error. 

###Errors

The `fseek()` and `fseeko()` functions fail if, either the stream is unbuffered or the stream's buffer needed to be flushed, and the call to `fseek()` or `fseeko()` causes an underlying `lseek()` or `write()` to be invoked, and: 

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor and the thread would be delayed in the write operation. 
[`EBADF`]  The file descriptor underlying the stream file is not open for writing or the stream's buffer needed to be flushed and the file is not open. 
[`EFBIG`]  An attempt was made to write a file that exceeds the maximum file size. or
           An attempt was made to write a file that exceeds the file size limit of the process. or
           The file is a regular file and an attempt was made to write at or beyond the offset maximum associated with the corresponding stream. 
[`EINTR`]  The write operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EINVAL`] The <u>whence</u> argument is invalid. The resulting file-position indicator would be set to a negative value. 
[`EIO`]    A physical I/O error has occurred, or the process is a member of a background process group attempting to perform a `write()` to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking SIGTTOU, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. 
[`ENOSPC`] There was no free space remaining on the device containing the file. 
[`EOVERFLOW`] For `fseek()`, the resulting file offset would be a value which cannot be represented correctly in an object of type `long`. 
              For `fseeko()`, the resulting file offset would be a value which cannot be represented correctly in an object of type `off_t`. 
[`EPIPE`]  An attempt was made to write to a pipe or `FIFO` that is not open for reading by any process; a `SIGPIPE` signal is also sent to the thread. 
[`ESPIPE`] The file descriptor underlying stream is associated with a pipe, `FIFO`, or socket. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device. 

###Implementation tasks

 * Implement error handling