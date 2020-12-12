###Synopsis

`#include <stdio.h>`

`int fflush(FILE *stream);`

###Description

Flushes the output buffer of a stream. 

Arguments:

<u>stream</u> - the stream to be flushed

If <u>stream</u> points to an output stream, any unwritten data for that stream is written to the file, and the last data modification and last file status change timestamps of the underlying file are marked for update.

If <u>stream</u> points to an input stream, with an underlying file description, if the file is not already at `EOF`, and the file is one capable of seeking, the file offset of the underlying open file description is set to the file position of the stream, and any characters pushed back onto the stream by `ungetc()` or `ungetwc()` that have not subsequently been read from the stream are discarded (without further changing the file offset).

If <u>stream</u> is a null pointer, `fflush()` performs this flushing action on all streams for which the behavior is defined above.

###Return value
On success `fflush()` returns `0`; otherwise, it  sets the error indicator for the stream and returns `EOF`, and sets `errno` to indicate the error.

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation. 
[`EBADF`]  The file descriptor underlying stream is not valid. 
[`EFBIG`]  An attempt was made to write a file that exceeds the maximum file size. 
[`EFBIG`]  An attempt was made to write a file that exceeds the file size limit of the process. 
[`EFBIG`]  The file is a regular file and an attempt was made to write at or beyond the offset maximum associated with the corresponding stream. 
[`EINTR`]  The `fflush()` function was interrupted by a signal. 
[`EIO`]    The process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. 
[`ENOMEM`] The underlying stream was created by `open_memstream()` or `open_wmemstream()` and insufficient memory is available. 
[`ENOSPC`] There was no free space remaining on the device containing the file or in the buffer used by the `fmemopen()` function. 
[`EPIPE`]  An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal is also sent to the thread. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device

###Implementation tasks

 * Implement error handling as described above.