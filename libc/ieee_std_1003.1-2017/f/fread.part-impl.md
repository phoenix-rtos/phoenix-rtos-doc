###Synopsis

`#include <stdio.h>`

`size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);`

###Description

The `fread()` function reads data from the given stream into the array pointed to by <u>ptr</u>.

Arguments:

<u>ptr</u> - an array saving the read data,
<u>size</u> - a size of an unique item,
<u>nmemb</u> - a number of items to read,
<u>stream</u> - the input stream. 

The `fread()` function reads into the array pointed to by <u>ptr</u> up to <u>nmemb</u> elements whose size is specified by <u>size</u> in bytes, from the stream pointed to by <u>stream</u>. For each object, <u>size</u> calls are made to the `fgetc()` function and the results stored, in the order read, in an array of unsigned char exactly overlaying the object. The file position indicator for the stream (if defined) is advanced by the number of bytes successfully read. If an error occurs, the resulting value of the file position indicator for the stream is unspecified. If a partial element is read, its value is unspecified.

The `fread()` function may mark the last data access timestamp of the file associated with <u>stream</u> for update. The last data access timestamp is marked for update by the first successful execution of `fgetc()`, `fgets()`, `fread()`, `fscanf()`, `getc()`, `getchar()`, `getdelim()`, `getline()`, `gets()`, or <u>scanf()</u> using <u>stream</u> that returns data not supplied by a prior call to <u>ungetc()</u>.

###Return value

Upon successful completion, `fread()` returns the number of elements successfully read which is less than <u>nmemb</u> only if a read error or end-of-file is encountered. If size or <u>nitems</u> is `0`, `fread()` returns `0` and the contents of the array and the state of the stream remain unchanged. 
Otherwise, if a read error occurs, the error indicator for the stream is set, and `errno` is set to indicate the error. 

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the `fgetc()` operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for reading. 
[`EINTR`]  The read operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`]    A physical I/O error has occurred, or the process is in a background process group attempting to read from its controlling terminal, and either the calling thread is blocking `SIGTTIN` or the process is ignoring `SIGTTIN` or the process group of the process is orphaned.
[`EOVERFLOW`]  The file is a regular file and an attempt was made to read at or beyond the offset maximum associated with the corresponding stream. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks
	
 * Implement error handling for the function

