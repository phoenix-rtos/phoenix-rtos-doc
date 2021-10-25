###Synopsis

`#include <stdio.h>`

`int getc(FILE *stream);`

###Description

Gets the next character (an unsigned char) from the specified stream and advances the position indicator for the stream.

Arguments:

<u>stream</u> - the specified stream,

The function (if it is implemented as a macro) may evaluate <u>stream</u> more than once, so the argument should never be an expression with side-effects.

###Return value

Upon successful completion, `getc()` returns the next byte from the input stream pointed to by <u>stream</u>. If the end-of-file indicator for the stream is set, or if the stream is at end-of-file, the end-of-file indicator for the stream is set and `getc()` returns `EOF`. If a read error occurs, the error indicator for the <u>stream</u> is set, `getc()` returns `EOF`, and sets `errno` to indicate the error.

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the `getc()` operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for reading. 
[`EINTR`]  The read operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`]    A physical I/O error has occurred, or the process is in a background process group attempting to read from its controlling terminal, and either the calling thread is blocking `SIGTTIN` or the process is ignoring `SIGTTIN` or the process group of the process is orphaned.
[`EOVERFLOW`]  The file is a regular file and an attempt was made to read at or beyond the offset maximum associated with the corresponding stream. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks

* Implement error handling for the `getc()` function.