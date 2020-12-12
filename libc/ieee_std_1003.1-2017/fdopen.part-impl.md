###Synopsis

`#include <stdio.h>`

`FILE *fdopen(int fildes, const char *mode);`

###Description

The `fdopen()` function associates a stream with a file descriptor.

Arguments:

<u>fildes</u> - the file descriptor.
<u>mode</u> - the mode of opening (read, write, append).

The <u>mode</u> argument is a character string having one of the following values:

`r` or `rb`   Open a file for reading.
`w` or `wb`   Open a file for writing.
`a` or `ab`   Open a file for writing at end-of-file.
`r+` or `rb+` or `r+b`   Open a file for update (reading and writing).
`w+` or `wb+` or `w+b`   Open a file for update (reading and writing).
`a+` or `ab+` or `a+b`   Open a file for update (reading and writing) at end-of-file. 

The application ensures that the mode of the stream as expressed by the <u>mode</u> argument is allowed by the file access mode of the open file description to which <u>fildes</u> refers. The file position indicator associated with the new stream is set to the position indicated by the file offset associated with the file descriptor.

The error and end-of-file indicators for the stream are cleared. The `fdopen()` function causes the last data access timestamp of the underlying file to be marked for update.

If <u>fildes</u> refers to a shared memory object or a typed memory object, the result of the `fdopen()` function is unspecified.

The `fdopen()` function preserve the offset maximum previously set for the open file description corresponding to <u>fildes</u>.
 
###Return value

Upon successful completion, `fdopen()` returns a pointer to a stream; otherwise, a null pointer is returned and `errno` set to indicate the error.

###Errors

[`EMFILE`] {`STREAM_MAX`} streams are currently open in the calling process.
[`EBADF`] The <u>fildes</u> argument is not a valid file descriptor.
[`EINVAL`] The <u>mode</u> argument is not a valid mode.
[`EMFILE`] {`FOPEN_MAX`} streams are currently open in the calling process.
[`ENOMEM`] Insufficient space to allocate a buffer. 
    
###Implementation tasks

 * Implement error detection as described above.
 * Implement the function behavior for shared and typed memory objects.
 