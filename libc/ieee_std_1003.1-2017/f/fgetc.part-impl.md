###Synopsis

`#include <stdio.h>`

`int fgetc(FILE *stream);`

###Description

The function gets the next character (an unsigned char) from the specified stream and advances the position indicator for the stream.

Arguments:
<u>stream</u> - the input stream.

If the end-of-file indicator for the input stream pointed to by <u>stream</u> is not set and a next byte is present, the `fgetc()` function obtains the next byte as an `unsigned char` converted to an `int`, from the input stream pointed to by <u>stream</u>, and advances the associated file position indicator for the stream (if defined). Since `fgetc()` operates on bytes, reading a character consisting of multiple bytes (or "a multi-byte character") requires multiple calls to `fgetc()`.

###Return value

Upon successful completion, `fgetc()` returns the next byte from the input stream pointed to by <u>stream</u>. 

If the end-of-file indicator for the stream is set, or if the stream is at end-of-file, the end-of-file indicator for the stream is set and `fgetc()` returns `EOF`. If a read error occurs, the error indicator for the stream is set, `fgetc()` returns `EOF`, and sets `errno` to indicate the error.

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