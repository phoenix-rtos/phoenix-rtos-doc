###Synopsis

`#include <stdio.h>`

`int fputc(int c, FILE *stream);`

###Description

Writes a character (an unsigned char) specified by the argument <u>c</u> to the specified stream and advances the position indicator for the stream.

Arguments:

<u>c</u> - a character,
<u>stream</u> - an output file.

The last data modification and last file status change timestamps of the file are marked for update between the successful execution of `fputc()` and the next successful completion of a call to `fflush()` or `fclose()` on the same stream or a call to `exit()` or `abort()`. 

###Return value

On success the character written to the <u>stream</u> is returned. Otherwise  `EOF`, the error indicator for the stream is set, and `errno` is set to indicate the error.

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
