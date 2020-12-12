###Synopsis

`#include <stdio.h>`
`#include <wchar.h>`

`wint_t fputws(const wchar_t *ws, FILE *stream);`

###Description

The `fputws()` function writes the character string corresponding to the (null-terminated) wide-character string <u>ws</u> to the output stream pointed to by <u>stream</u>. No character corresponding to the terminating null wide-character code is written.

Arguments:

<u>ws</u> - a wide character string to be written,
<u>stream</u> - the output stream. 

The last data modification and last file status change timestamps of the file are marked for update between the successful execution of `fputws()` and the next successful completion of a call to `fflush()` or `fclose()` on the same stream or a call to `exit()` or `abort()`.

###Return value

Upon successful completion, `fputws()` returns a non-negative number - the number of bytes written. 
Otherwise, it returns `-1`, sets an error indicator for the stream, and sets `errno` to indicate the error. 

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for writing. 
[`EFBIG`] An attempt was made to write to a file that exceeds the maximum file size. 
[`EFBIG`] An attempt was made to write to a file that exceeds the file size limit of the process. 
[`EFBIG`] The file is a regular file and an attempt was made to write at or beyond the offset maximum. 
[`EILSEQ`] The wide-character code <u>wc</u> does not correspond to a valid character.
[`EINTR`] The write operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`] A physical I/O error has occurred, or the process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. 
[`EPIPE`] An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal is also sent to the thread. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`] A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks
	
 * Implement `wchar.h` file
 * Implement the `fputws()` function
