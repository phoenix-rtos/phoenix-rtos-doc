###Synopsis

`#include <stdio.h>`

`FILE *fmemopen(void *restrict buf, size_t size, const char *restrict mode); `

###Description

The `fmemopen()` function associates the buffer given by the <u>buf</u> and size arguments with a stream. The <u>buf</u> argument is either a null pointer or points to a buffer that is at least <u>size</u> bytes long.

Arguments:
<u>buf</u> - the pointer to the buffer.
<u>size</u> - the buffer <u>size</u>.
<u>mode</u> - the mode of the file.

The <u>mode</u> argument points to a string. If the string is one of the following, the stream is opened in the indicated mode. Otherwise, the behavior is undefined.

All mode strings allowed by `fopen()` are accepted:

   `r`     Open the stream for reading.
   `w`    Open the stream for writing.
   `a`     Append; open the stream for writing at the first null byte.
   `r+`   Open the stream for update (reading and writing).
   `w+`  Open the stream for update (reading and writing). Truncate the buffer contents.
   `a+`   Append; open the stream for update (reading and writing); the initial position is at the first null byte.

If a null pointer is specified as the <u>buf</u> argument, `fmemopen()` allocates <u>size</u> bytes of memory as if by a call to `malloc()`. This buffer is automatically freed when the stream is closed. Because this feature is only useful when the stream is opened for updating (because there is no way to get a pointer to the buffer) the `fmemopen()` call may fail if the <u>mode</u> argument does not include a '+'.

The stream  maintains a current position in the buffer. This position is initially set to either the beginning of the buffer (for `r` and `w` modes) or to the first null byte in the buffer (for `a` modes). If no null byte is found in append mode, the initial position is set to one byte after the end of the buffer.

If <u>buf</u> is a null pointer, the initial position is always set to the beginning of the buffer.

The stream also maintains the size of the current buffer contents; use of `fseek()` or `fseeko()` on the stream with `SEEK_END` seeks relative to this size. For modes `r` and `r+` the <u>size</u> is set to the value given by the <u>size</u> argument. For modes `w` and `w+` the initial size is zero and for modes `a` and `a+` the initial size  is:

 * Zero, if <u>buf</u> is a null pointer,

 * The position of the first null byte in the buffer, if one is found,

 * The value of the <u>size</u> argument, if <u>buf</u> is not a null pointer and no null byte is found.

A read operation on the stream does not advance the current buffer position beyond the current buffer size. Reaching the buffer size in a read operation  counts as `end-of-file'. Null bytes in the buffer  have no special meaning for reads. The read operation  starts at the current buffer position of the stream.

A write operation starts either at the current position of the stream (if mode has not specified 'a' as the first character) or at the current size of the stream (if mode had 'a' as the first character). If the current position at the end of the write is larger than the current buffer size, the current buffer size is set to the current position. A write operation on the stream  does not advance the current buffer size beyond the size given in the <u>size</u> argument.

When a stream opened for writing is flushed or closed, a null byte is written at the current position or at the end of the buffer, depending on the size of the contents. If a stream opened for update is flushed or closed and the last write has advanced the current buffer size, a null byte is written at the end of the buffer if it fits.

An attempt to seek a memory buffer stream to a negative position or to a position larger than the buffer size given in the <u>size</u> argument fails.

###Return value

Upon successful completion, `fmemopen()` returns a pointer to the object controlling the stream. Otherwise, a null pointer is returned, and `errno` is set to indicate the error.

###Errors

[`EMFILE`] {`STREAM_MAX`} streams are currently opened in the calling process.
[`EINVAL`] The value of the mode argument is not valid <b>or</b>
           The <u>buf</u> argument is a null pointer and the <u>mode</u> argument does not include a '+' character <b>or</b>
           The <u>size</u> argument specifies a buffer size of zero and the implementation does not support this.
[`ENOMEM`] The <u>buf</u> argument is a null pointer and the allocation of a buffer of length <u>size</u> has failed.
[`EMFILE`] {`FOPEN_MAX`} streams are currently opened in the calling process. 
    
###Implementation tasks

 * Implement the `fmemopen()` function.
