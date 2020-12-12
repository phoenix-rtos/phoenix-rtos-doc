###Synopsis

`#include <stdio.h>`

`#include <wchar.h>`

`wint_t fgetwc(FILE *stream);`

###Description

The function gets a wide-character code from a stream.
 
Arguments:

<u>stream</u> - the input stream.

The `fgetwc()` function obtains the next character (if present) from the input stream pointed to by <u>stream</u>, converts that to the corresponding wide-character code, and advances the associated file position indicator for the stream (if defined).

If an error occurs, the resulting value of the file position indicator for the stream is unspecified.

###Return value

Upon successful completion, the `fgetwc()` function returns the wide-character code of the character read from the input stream pointed to by <u>stream</u> converted to a type  `wint_t`. 
If the end-of-file indicator for the stream is set, or if the stream is at end-of-file, the end-of-file indicator for the stream is set and `fgetwc()` returns `WEOF`. If a read error occurs, the error indicator for the stream is set, `fgetwc()` returns `WEOF` and sets `errno` to indicate the error. If an encoding error occurs, the error indicator for the stream is set, `fgetwc()` returns `WEOF`, and sets `errno` to indicate the error.

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying <u>stream</u> and the thread would be delayed in the `fgetwc()` operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for reading. 
[`EILSEQ`] The data obtained from the input stream does not form a valid character.
[`EINTR`]  The read operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`]    A physical I/O error has occurred, or the process is in a background process group attempting to read from its controlling terminal, and either the calling thread is blocking `SIGTTIN` or the process is ignoring `SIGTTIN` or the process group of the process is orphaned.
[`EOVERFLOW`]  The file is a regular file and an attempt was made to read at or beyond the offset maximum associated with the corresponding stream. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks

* Implement the `wchar.h` file.
* Implement the `fgetwc()` function.