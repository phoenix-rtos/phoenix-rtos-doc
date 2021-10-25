###Synopsis

`#include <stdio.h>`

`int fclose(FILE *stream);`

###Description

The function closes the stream.

Arguments:

<u>stream</u> - the stream to be closed.

The `fclose()` function causes the stream pointed to by <u>stream</u> to be flushed and the associated file to be closed. Any unwritten buffered data for the stream is written to the file; any unread buffered data is discarded. Whether or not the call succeeds, the stream is disassociated from the file and any buffer set by the `setbuf()` or `setvbuf()` function are disassociated from the stream. If the associated buffer was automatically allocated, it is deallocated.

If the file is not already at `EOF`, and the file is one capable of seeking, the file offset of the underlying open file description is set to the file position of the stream if the stream is the active handle to the underlying file description.

The `fclose()` function marks for update the last data modification and last file status change timestamps of the underlying file, if the stream was writable, and if buffered data remains that has not yet been written to the file. The `fclose()` function performs the equivalent of a `close()` on the file descriptor that is associated with the stream pointed to by <u>stream</u>.

After the call to `fclose()`, any use of <u>stream</u> results in undefined behavior.

###Return value

Upon successful completion, `fclose()` returns `0`. Otherwise, `EOF` is returned and `errno` set to indicate the error.

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation. 
[`EBADF`] The file descriptor underlying stream is not valid. 
[`EFBIG`] An attempt was made to write a file that exceeds the maximum file size or
          An attempt was made to write a file that exceeds  the file size limit of the process or
          The file is a regular file and an attempt was made to write at or beyond the offset maximum associated with the corresponding stream. 
[`EINTR`] The `fclose()` function was interrupted by a signal. 
[`EIO`] The process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned.
[`ENOMEM`] The underlying stream was created by `open_memstream()` or `open_wmemstream()` and insufficient memory is available. 
[`ENOSPC`] There was no free space remaining on the device containing the file or in the buffer used by the `fmemopen()` function. 
[`EPIPE`] An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal is also sent to the thread. 
[`ENXIO`] A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks

 * Implement error detection for errors described above.