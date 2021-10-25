###Synopsis

`#include <stdio.h>`

`#include <wchar.h>`

`wint_t fputwc(wchar_t wc, FILE *stream);`

###Description

The `fputwc()` function writes the character corresponding to the wide-character code <u>wc</u> to the output stream pointed to by <u>stream</u>, at the position indicated by the associated file-position indicator for the <u>stream</u> (if defined), and advances the indicator appropriately. If the file cannot support positioning requests, or if the stream was opened with append mode, the character is appended to the output stream. If an error occurs while writing the character, the shift state of the output file is left in an undefined state.

Arguments:

<u>wc</u> - a wide character to be written,
<u>stream</u> - the output stream. 

The last data modification and last file status change timestamps of the file are marked for update between the successful execution of `fputwc()` and the next successful completion of a call to `fflush()` or `fclose()` on the same stream or a call to `exit()` or `abort()`.

###Return value

Upon successful completion, `fputwc()` returns <u>wc</u>. 
Otherwise, it returns `WEOF`, sets an error indicator for the stream, and sets `errno` to indicate the error. 

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for writing. 
[`EFBIG`] An attempt was made to write to a file that exceeds the maximum file size. 
[`EFBIG`] An attempt was made to write to a file that exceeds the file size limit of the process. 
[`EFBIG`] The file is a regular file and an attempt was made to write at or beyond the offset maximum. 
[`EILSEQ`] The wide-character code <u>wc</u> does not correspond to a valid character.
[`EINTR`] The write operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`] A physical I/O error has occurred, or the process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. 
[`ENOSPC`] There was no free space remaining on the device containing the file. 
[`EPIPE`] An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal is also sent to the thread. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`] A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks
	
 * Implement `wchar.h` file
 * Implement the `fputwc()` function
