###Synopsis

`#include <sys/stat.h>`

`int fchmod(int fildes, mode_t mode);`

###Description

The function changes the mode of a file.

Arguments:

<u>fildes</u> - the file descriptor.
<u>mode</u> - the new mode of a file.

The `fchmod()` function is equivalent to `chmod()` except that the file whose permissions are changed is specified by the file descriptor <u>fildes</u>.

If <u>fildes</u> references a shared memory object, the `fchmod()` function need only affect the `S_IRUSR`, `S_IWUSR`, `S_IRGRP`, `S_IWGRP`, `S_IROTH`, and `S_IWOTH` file permission bits.

If <u>fildes</u> references a typed memory object or a socket , the behavior of `fchmod()` is unspecified.

If <u>fildes</u> refers to a STREAM (which is fattach()-ed into the file system name space) the call returns successfully, doing nothing. 

###Return value

Upon successful completion, `fchmod()` returns `0`. Otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

[`EBADF`] The <u>fildes</u> argument is not a valid open file descriptor.
[`EPERM`] The effective user ID does not match the owner of the file and the process does not have appropriate privileges.
[`EROFS`] The file referred to by <u>fildes</u> resides on a read-only file system.

The fchmod() function may fail if:

[`EINTR`] The `fchmod()` function was interrupted by a signal.
[`EINVAL`] The value of the <u>mode</u> argument is invalid.
[`EINVAL`] The <u>fildes</u> argument refers to a pipe and the implementation disallows execution of `fchmod()` on a pipe. 

###Implementation tasks

 * Implement `fchmod()` function