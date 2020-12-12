###Synopsis

`#include <unistd.h>`

`int fchown(int fildes, uid_t owner, gid_t group);`

###Description

The function changes the owner and the group of the file.

Arguments:

<u>fildes</u> - the file descriptor.
<u>owner</u> - the new owner of a file.
<u>group</u> - the new group of a file.

The `fchown()` function is equivalent to `chown()` except that the file whose owner and group are changed is specified by the file descriptor <u>fildes</u>.

###Return value

Upon successful completion, `fchown()` returns `0`. Otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

[`EBADF`] The <u>fildes</u> argument is not a valid open file descriptor.
[`EPERM`] The effective user ID does not match the owner of the file or the process does not have appropriate privileges and `_POSIX_CHOWN_RESTRICTED` indicates that such privilege is required.
[`EROFS`] The file referred to by <u>fildes</u> resides on a read-only file system.

[`EINTR`] The `fchown()` function was interrupted by a signal.
[`EINVAL`] The owner or group ID is not a value supported by the implementation. The <u>fildes</u> argument refers to a pipe or socket or an fattach()-ed STREAM and the implementation disallows execution of `fchown()` on a pipe.
[`EIO`] A physical I/O error has occurred. 

###Implementation tasks

 * Implement `fchown()` function