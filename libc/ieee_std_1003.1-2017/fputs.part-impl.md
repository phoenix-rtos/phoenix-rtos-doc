###Synopsis

`#include <stdio.h>`

`int fputs(const char *str, FILE *stream);`

###Description

Writes a string to the specified stream up to but not including the terminating null character.

###Return value

Upon successful completion, `fputs()` returns the number of bytes written if it is up to {`INT_MAX`} bytes, and returns {`INT_MAX`} for all longer strings. 
Otherwise, it returns `EOF`, sets an error indicator for the stream, and sets `errno` to indicate the error. 

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for writing. 
[`EFBIG`] An attempt was made to write to a file that exceeds the maximum file size. 
[`EFBIG`] An attempt was made to write to a file that exceeds the file size limit of the process. 
[`EFBIG`] The file is a regular file and an attempt was made to write at or beyond the offset maximum. 
[`EINTR`] The write operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`] A physical I/O error has occurred, or the process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. 
[`ENOSPC`] There was no free space remaining on the device containing the file. 
[`EPIPE`] An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal is also sent to the thread. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`] A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks
	
 * Implement error handling for the function

	

