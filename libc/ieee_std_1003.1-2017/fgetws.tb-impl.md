###Synopsis

`#include <stdio.h>`

`#include <wchar.h>`

`wchar_t *fgetws(wchar_t *ws, int n,
       FILE *stream);`

###Description

The function gets a wide-character string from a stream.
 
Arguments:

<u>ws</u> - the array saving the read wide character string,
<u>n</u> - the maximum number of wide characters to read +1,
<u>stream</u> - the input stream.

The `fgetws()` function reads characters from the <u>stream</u>, converts these to the corresponding wide-character codes, places them in the `wchar_t` array pointed to by <u>ws</u>, until <u>n</u>-1 characters are read, or a <newline> is read, converted, and transferred to <u>ws</u>, or an end-of-file condition is encountered. The wide-character string, <u>ws</u>, is then terminated with a null wide-character code.

If an error occurs, the resulting value of the file position indicator for the stream is unspecified.

###Return value

Upon successful completion, the `fgetws()` function returns <u>ws</u>. 
If the end-of-file indicator for the stream is set, or if the stream is at end-of-file, the end-of-file indicator for the stream is set and `fgetws()` returns a null pointer and sets `errno` to indicate the error. 

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

* Implement `wchar.h` file. 
* Implement the `fgetws()` function.