###Synopsis

`#include <unistd.h>`

`int ftruncate(int fildes, off_t length);`

###Description

The `ftruncate()` function truncates a file to a specified <u>length</u>.

Arguments:
    
<u>fildes</u> - a valid file descriptor open for writing.
<u>length</u> - a resulting length of the file to be truncated.

If <u>fildes</u> is not a valid file descriptor open for writing, the `ftruncate()` function fails.

If <u>fildes</u> refers to a regular file, the `ftruncate()` function causes the size of the file to be truncated to <u>length</u>. If the size of the file previously exceeded <u>length</u>, the extra data is no longer available to reads on the file. If the file previously was smaller than this size, `ftruncate()` shall increase the size of the file. If the file size is increased, the extended area appears as if it were zero-filled. The value of the seek pointer is not modified by a call to `ftruncate()`.

Upon successful completion, if <u>fildes</u> refers to a regular file, `ftruncate()` marks for update the last data modification and last file status change timestamps of the file and the `S_ISUID` and `S_ISGID` bits of the file mode may be cleared. If the `ftruncate()` function is unsuccessful, the file is unaffected.

If the request would cause the file size to exceed the soft file size limit for the process, the request fails and the implementation generates the `SIGXFSZ` signal for the thread.

If <u>fildes</u> refers to a directory, `ftruncate()` fails.

If <u>fildes</u> refers to any other file type, except a shared memory object, the result is unspecified.

If <u>fildes</u> refers to a shared memory object, `ftruncate()` sets the size of the shared memory object to <u>length</u>. 

If the effect of `ftruncate()` is to decrease the size of a memory mapped file or a shared memory object and whole pages beyond the new end were previously mapped, then the whole pages beyond the new end are discarded.

References to discarded pages result in the generation of a `SIGBUS` signal.

If the effect of `ftruncate()` is to increase the size of a memory object, it is unspecified whether the contents of any mapped pages between the old end-of-file and the new are flushed to the underlying object.

###Return value

Upon successful completion, `ftruncate()` returns `0`; otherwise, `-1` is returned and `errno` set to indicate the error.


###Errors

[`EINTR`] A signal was caught during execution.
[`EINVAL`] The <u>length</u> argument was less than `0`.
[`EFBIG`] or [`EINVAL`] The <u>length</u> argument was greater than the maximum file size.
[`EFBIG`] The file is a regular file and <u>length</u> is greater than the offset maximum established in the open file description associated with <u>fildes</u>.
[`EIO`]  An I/O error occurred while reading from or writing to a file system.
[`EBADF`] or [`EINVAL`] The <u>fildes</u> argument is not a file descriptor open for writing. 
        
###Implementation tasks:
    
 * Implement error handling for the `ftruncate()` function.
 