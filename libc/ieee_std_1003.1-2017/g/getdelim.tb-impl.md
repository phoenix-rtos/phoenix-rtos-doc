###Synopsis

`#include <stdio.h>`

`ssize_t getdelim(char **restrict lineptr, size_t *restrict n,
       int delimiter, FILE *restrict stream);`
`ssize_t getline(char **restrict lineptr, size_t *restrict n,
       FILE *restrict stream);`

###Description

The `getdelim()`, `getline()` functions read a delimited record from the stream.

Arguments:

<u>lineptr</u> - a pointer to the space into which the data is put,
<u>n</u> - the maximum number of bytes to be read,
<u>delimiter</u> - a character which terminates the reading process,
<u>stream</u> - an input stream.

The `getdelim()` function reads from <u>stream</u> until it encounters a character matching the <u>delimiter</u> character. The <u>delimiter</u> argument is an `int`, the value of which the application ensures is a character representable as an `unsigned char` of equal value that terminates the read process. If the <u>delimiter</u> argument has any other value, the behavior is undefined.

The application ensures that * <u>lineptr</u> is a valid argument that could be passed to the `free()` function. If * <u>n</u> is non-zero, the application ensures that * <u>lineptr</u> either points to an object of size at least * <u>n</u> bytes, or is a null pointer.

If * <u>lineptr</u> is a null pointer or if the object pointed to by * <u>lineptr</u> is of insufficient size, an object is allocated as if by `malloc()` or the object is reallocated as if by `realloc()`, respectively, such that the object is large enough to hold the characters to be written to it, including the terminating `NULL`, and *<u>n</u> is set to the new size. If the object was allocated, or if the reallocation operation moved the object, * <u>lineptr</u> is updated to point to the new object or new location. The characters read, including any delimiter, are stored in the object, and a terminating `NULL` added when the <u>delimiter</u> or end-of-file is encountered.

The `getline()` function is equivalent to the `getdelim()` function with the <u>delimiter</u> character equal to the `<newline>` character.

The `getdelim()` and `getline()` functions may mark the last data access timestamp of the file associated with stream for update. The last data access timestamp is marked for update by the first successful execution of `fgetc()`, `fgets()`, `fread()`, `fscanf()`, `getc()`, `getchar()`, `getdelim()`, `getline()`, `gets()`, or `scanf()` using stream that returns data not supplied by a prior call to `ungetc()`.

These functions are widely used to solve the problem that the `fgets()` function has with long lines. The functions automatically enlarge the target buffers if needed. These are especially useful since they reduce code needed for applications.

###Return value

Upon successful completion, the `getline()` and `getdelim()` functions return the number of bytes written into the buffer, including the <u>delimiter</u> character if one was encountered before `EOF`, but excluding the terminating `NUL` character. If the end-of-file indicator for the <u>stream</u> is set, or if no characters were read and the <u>stream</u> is at end-of-file, the end-of-file indicator for the <u>stream</u> are set and the function returns `-1`. If an error occurs, the error indicator for the <u>stream</u> is set, and the function returns `-1` and sets `errno` to indicate the error.

###Errors

[`EAGAIN`] The `O_NONBLOCK` flag is set for the file descriptor underlying stream and the thread would be delayed in the `fgetc()` operation. 
[`EBADF`]  The file descriptor underlying stream is not a valid file descriptor open for reading. 
[`EINTR`]  The read operation was terminated due to the receipt of a signal, and no data was transferred. 
[`EIO`]    A physical I/O error has occurred, or the process is in a background process group attempting to read from its controlling terminal, and either the calling thread is blocking `SIGTTIN` or the process is ignoring `SIGTTIN` or the process group of the process is orphaned.
[`EOVERFLOW`]  The file is a regular file and an attempt was made to read at or beyond the offset maximum associated with the corresponding stream or
            The number of bytes to be written into the buffer, including the delimiter character (if encountered), would exceed {`SSIZE_MAX`}.  
[`ENOMEM`] Insufficient storage space is available. 
[`ENXIO`]  A request was made of a nonexistent device, or the request was outside the capabilities of the device.
[`EINVAL`]  <u>lineptr</u> or <u>n</u> is a null pointer.
    
###Implementation tasks

* Implement error handling for `getline()`.
* Implement the `getdelim()` function.
