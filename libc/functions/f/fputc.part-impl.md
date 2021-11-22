# Synopsis 
`#include <stdio.h>`</br>

` int fputc(int c, FILE *stream);`</br>

## Status
Partially implemented
## Conformance
IEEE Std 1003.1-2017
## Description

The `fputc()` function shall write the byte specified by _c_ (converted to an unsigned char) to the output
stream pointed to by stream, at the position indicated by the associated file-position indicator for the stream (if
defined), and shall advance the indicator appropriately. If the file cannot support positioning requests, or if the stream was
opened with append mode, the byte shall be appended to the output stream.
The
last data modification and last file status change timestamps of the file shall be marked for update between the successful
execution of `fputc()` and the next successful completion of a call to `fflush()`
or `fclose()` on the same stream or a call to `exit()` or `abort()`. 


## Return value


Upon successful completion, `fputc()` shall return the value it has written. Otherwise, it shall return `EOF`, the error indicator for the stream shall be set and `errno` shall be set to indicate the error.


## Errors


The `fputc()` function shall fail if either the stream is unbuffered or the stream's buffer needs to be
flushed, and:


 * `EAGAIN` - The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation.


 * `EBADF` - The file descriptor underlying stream is not a valid file descriptor open for writing. 

 * `EFBIG` - An attempt was made to write to a file that exceeds the maximum file size. 

 * `EFBIG` - An attempt was made to write to a file that exceeds the file size limit of the process. 

 * `EFBIG` - The file is a regular file and an attempt was made to write at or beyond the offset maximum. 

 * `EINTR` - The write operation was terminated due to the receipt of a signal, and no data was transferred. 

 * `EIO` - A physical I/O error has occurred, or the process is a member of a background process group attempting to write to its controlling
terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of
the process is orphaned. This error may also be returned under implementation-defined conditions. 

 * `ENOSPC` - There was no free space remaining on the device containing the file. 

 * `EPIPE` - An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal shall also be sent to the
thread. 


The `fputc()` function may fail if:

 * `ENOMEM` - Insufficient storage space is available. 

 * `ENXIO` - A request was made of a nonexistent device, or the request was outside the capabilities of the device. 

## Tests

Untested

## Known bugs

None

## See Also 
1. [Standard library functions](../README.md)
2. [Table of Contents](../../../README.md)
