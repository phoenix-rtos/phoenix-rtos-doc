###Synopsis

`#include <unistd.h>`

`int fdatasync(int fildes);`

###Description

The `fdatasync()` function synchronizes the data of the file. 

Arguments:

<u>fildes</u> - the file descriptor.

The `fdatasync()` function forces all currently queued I/O operations associated with the file indicated by file descriptor <u>fildes</u> to the synchronized I/O completion state.

###Return value

Upon successful completion, the `fdatasync()` function returns `0`, otherwise, `-1` is returned and `errno` set to indicate the error.

If the function fails, outstanding I/O operations are not guaranteed to be completed.

###Errors

[`EBADF`]  The <u>fildes</u> argument is not a valid file descriptor
[`EINVAL`] This implementation does not support synchronized I/O for this file.

###Implementation tasks

 * Implement the `fdatasync()` function.