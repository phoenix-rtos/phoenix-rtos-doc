###Synopsis

`#include <fcntl.h>`

`int fcntl(int fildes, int cmd, ...);`

###Description

The `fcntl()` function performs one of the operations described below on the open file.

Arguments:

<u>fildes</u> - the file descriptor.
<u>cmd</u> - the operation to be performed on the file (from `fcntl.h` file). The operation is one of the following:
    
 * `F_DUPFD`,
 * `F_DUPFD_CLOEXEC`,
 * `F_GETFD`,
 * `F_SETFD`,
 * `F_GETFL`, 
 * `F_SETFL`,
 * `F_GETOWN`, 
 * `F_SETOWN`, 
 * `F_GETLK`, 
 * `F_SETLK`,
 * `F_SETLKW`.

    
###Return value

Upon successful completion, the value returned by depends on <u>cmd</u> as follows:
    
 * `F_DUPFD` A new file descriptor.
 * `F_DUPFD_CLOEXEC` A new file descriptor.
 * `F_GETFD` Value of flags defined in <`fcntl.h`>. The return value is not negative. 
 * `F_SETFD` Value other than `-1`.
 * `F_GETFL` Value of file status flags and access modes. The return value is not negative.
 * `F_SETFL` Value other than `-1`.
 * `F_GETOWN` Value of the socket owner process or process group; this will not be `-1`. 
 * `F_SETOWN` Value other than `-1`. 
 * `F_GETLK` Value other than `-1`. 
 * `F_SETLK` Value other than `-1`.
 * `F_SETLKW` Value other than `-1`.
    
Otherwise, `-1` is returned and `errno` set to indicate the error.

###Errors

[`EACCES`] or [`EAGAIN`] The <u>cmd</u> argument is `F_SETLK`; the type of lock (`l_type`) is a shared (`F_RDLCK`) or exclusive (`F_WRLCK`) lock and the segment of a file to be locked is already exclusive-locked by another process, or the type is an exclusive lock and some portion of the segment of a file to be locked is already shared-locked or exclusive-locked by another process.
[`EBADF`]  The <u>fildes</u> argument is not a valid open file descriptor, or the argument <u>cmd</u> is `F_SETLK` or `F_SETLKW`, the type of lock, `l_type`, is a shared lock (`F_RDLCK`), and <u>fildes</u> is not a valid file descriptor open for reading, or the type of lock, `l_type`, is an exclusive lock (`F_WRLCK`), and <u>fildes</u> is not a valid file descriptor open for writing.
[`EINTR`]  The <u>cmd</u> argument is `F_SETLKW` and the function was interrupted by a signal.
[`EINVAL`] The <u>cmd</u> argument is invalid, or the <u>cmd</u> argument is `F_DUPFD` or `F_DUPFD_CLOEXEC` and <u>arg</u> is negative or greater than or equal to {`OPEN_MAX`}, or the <u>cmd</u> argument is `F_GETLK`, `F_SETLK`, or `F_SETLKW` and the data pointed to by <u>arg</u> is not valid, or <u>fildes</u> refers to a file that does not support locking.
[`EMFILE`] The argument <u>cmd</u> is `F_DUPFD` or `F_DUPFD_CLOEXEC` and all file descriptors available to the process are currently open, or no file descriptors greater than or equal to arg are available.
[`ENOLCK`] The argument <u>cmd</u> is `F_SETLK` or `F_SETLKW` and satisfying the lock or unlock request would result in the number of locked regions in the system exceeding a system-imposed limit.
[`EOVERFLOW`] One of the values to be returned cannot be represented correctly.
[`EOVERFLOW`] The <u>cmd</u> argument is `F_GETLK`, `F_SETLK`, or `F_SETLKW` and the smallest or, if `l_len` is non-zero, the largest offset of any byte in the requested segment cannot be represented correctly in an object of type `off_t`.
[`ESRCH`] The <u>cmd</u> argument is `F_SETOWN` and no process or process group can be found corresponding to that specified by <u>arg</u>.
[`EDEADLK`] The <u>cmd</u> argument is `F_SETLKW`, the lock is blocked by a lock from another process, and putting the calling process to sleep to wait for that lock to become free would cause a deadlock.
[`EINVAL`] The <u>cmd</u> argument is `F_SETOWN` and the value of the argument is not valid as a process or process group identifier.
[`EPERM`]  The <u>cmd</u> argument is `F_SETOWN` and the calling process does not have permission to send a `SIGURG` signal to any process specified by <u>arg</u>. 

###Implementation tasks

 * Implement handling varargs properly
 * Implement error handling for above errors.