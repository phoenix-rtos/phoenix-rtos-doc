###Synopsis

`#include <unistd.h>`

`int fchdir(int fildes);`

###Description

The function changes the working directory.

Arguments:

<u>fildes</u> - the file descriptor.

The `fchdir()` function is equivalent to `chdir()` except that the directory that is to be the new current working directory is specified by the file descriptor <u>fildes</u>.

An application can obtain a file descriptor for a file of type directory using `open()`, provided that the file status flags and access modes do not contain `O_WRONLY` or `O_RDWR`.

###Return value

Upon successful completion, `fchdir()` returns `0`. Otherwise, `-1` is returned and `errno` set to indicate the error. On failure the current working directory remains unchanged.

###Errors

[`EACCES`] Search permission is denied for a he directory referenced by <u>fildes</u>.
[`EBADF`] The <u>fildes</u> argument is not a valid open file descriptor.
[`ENOTDIR`] The open file descriptor <u>fildes</u> does not refer to a directory.
[`EINTR`] A signal was caught during the execution of `fchdir()`.
[`EIO`] An I/O error occurred while reading from or writing to the file system..

###Implementation tasks

 * Implement `fchdir()` function