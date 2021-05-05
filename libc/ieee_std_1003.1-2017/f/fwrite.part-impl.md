###Synopsis

`#include <stdio.h>`

`size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);`

###Description

The `fwrite()` function writes data from the array pointed to by <u>ptr</u> to the given <u>stream</u>. It puts down <u>nmemb</u> elements each of size <u>size</u>.

Arguments:
    
<u>ptr</u> - an array containing data,
<u>size</u> - a size of a single element,
<u>nmemb</u> - a number of elements,
<u>stream</u> - a stream to which data is put.

For each object, <u>size</u> calls are made to the `fputc()` function, taking the values (in order) from an array of `unsigned char` exactly overlaying the object. The file-position indicator for the <u>stream</u> (if defined) is advanced by the number of bytes successfully written. If an error occurs, the resulting value of the file-position indicator for the <u>stream</u> is unspecified.

The last data modification and last file status change timestamps of the file are marked for update between the successful execution of `fwrite()` and the next successful completion of a call to `fflush()` or `fclose()` on the same stream, or a call to `exit()` or `abort()`.  
    
###Return value

The `fwrite()` function returns the number of elements successfully written, which may be less than <u>nmemb</u> if a write error is encountered. If <u>size</u> or <u>nmemb</u> is `0`, `fwrite()` return `0` and the state of the stream remains unchanged. Otherwise, if a write error occurs, the error indicator for the stream is set, and `errno` is set to indicate the error. 

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the write operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for writing. 
[`EFBIG`] An attempt was made to write to a file that exceeds the maximum file size. 
[`EFBIG`] An attempt was made to write to a file that exceeds the file size limit of the process. 
[`EFBIG`] The file is a regular file and an attempt was made to write at or beyond the offset maximum. 
[`EINTR`] The write operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`] A physical I/O error has occurred, or the process is a member of a background process group attempting to write to its controlling terminal, `TOSTOP` is set, the calling thread is not blocking `SIGTTOU`, the process is not ignoring `SIGTTOU`, and the process group of the process is orphaned. 
[`ENOSPC`] There was no free space remaining on the device containing the file. 
[`EPIPE`] An attempt is made to write to a pipe or `FIFO` that is not open for reading by any process. A `SIGPIPE` signal is also sent to the thread. 
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`] A request was made of a nonexistent device, or the request was outside the capabilities of the device.

###Implementation tasks

* implement error handling,